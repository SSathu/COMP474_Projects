from fastapi import APIRouter, HTTPException, Request, Depends
from tools.classifier import ClassifierTool
from models.schemas import Query

router = APIRouter(prefix="/api/v1")

def get_classifier(request: Request) -> ClassifierTool:
    return request.app.state.classifier

@router.post("/classify")
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