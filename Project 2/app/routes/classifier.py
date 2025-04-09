from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from tools.classifier import ClassifierTool
from tools.syntax_tree import SyntaxTreeTool
from models.schemas import Query
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from IPython.core.display import JSON



router = APIRouter(prefix="/api/v1")

def get_classifier(request: Request) -> ClassifierTool:
    return request.app.state.classifier

@router.post("/llm_classify")
async def classify_text(
    query: Query,
    classifier: ClassifierTool = Depends(get_classifier)
):
    try:
        result = await classifier.classify_query(query)
        return { "agent": result.agent }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Classification Error")
    

@router.post("/preprocessing")
async def clean_text(
    query: Query
    ):
    """
    Preprocessing:
        This is endpoint is responsible for the POS tagging and breakdown of the input text from ther user.
    
        Description:
            This input transforms the input by converting each non-stop and non-punct token to lowercase.
            It then gets the lemma of each of these tokens and joins them as a string in the output.
    """

    # load spacy for nlp
    nlp = spacy.load("en_core_web_sm")

    # generate our syntax tree
    doc = nlp(query.text)
    syntaxTool = SyntaxTreeTool(doc)

    # lowercasing, removing stopwords, and punction.
    doc_processed = ' '.join([token.text.lower() for token in doc if not token.is_stop and not token.is_punct])
    doc_processed_obj = nlp(doc_processed)


    tokens_info = []
    for token in doc_processed_obj:
        tokens_info.append({
            "token.text": token.text,
            "token.tag": token.tag_,
            "token.dep": token.dep_,
            "token.pos": token.pos_
        })

    return JSONResponse(
        status_code=200,
        content={
            "input": query.text,
            "response": tokens_info,
            "tree": syntaxTool.get_syntax_tree()
        }, 
        media_type="application/json")
    


""" @router.post("/")
async def 

 """
    