from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from tools.classifier import ClassifierTool
from models.schemas import Query
import spacy
from spacy.matcher import Matcher



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
    

@router.post("/clean_text")
async def clean_text(
    query: Query
    ):
    """
    Clean Text:
        Input: query
        Output: JSON "text": "response"

        Description:
            This input transforms the input by converting each non-stop and non-punct token to lowercase.
            It then gets the lemma of each of these tokens and joins them as a string in the output.
    """

    # load spacy for nlp
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    doc = nlp(query.text)

    # lowercasing, removing stopwords, and punction.
    doc_processed = ' '.join([token.text.lower() for token in doc if not token.is_stop and not token.is_punct])
    doc = nlp(doc_processed)
    
    lemma_text = [token.lemma_ for token in doc]

    output = []
    for word in lemma_text:
        output.append(word)
    

    return JSONResponse(status_code=200, content={"cleaned_text": ' '.join(output)}, media_type="application/json")
    





    