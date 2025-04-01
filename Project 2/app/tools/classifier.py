from langchain.chains import LLMChain

from models.schemas import ClassificationResult
from prompts.classification import CLASSIFICATION_PROMPT
from prompts.model_prompts import PROMPTS


class ClassifierTool:
    def __init__(self, llm):
        self.chain = LLMChain(
            llm=llm,
            prompt=CLASSIFICATION_PROMPT,
            verbose=True
        )
        self.valid_agents = {"ai", "admissions", "general"}
    async def classify_query(self, text: str) -> ClassificationResult:
        try:
            result = await self.chain.arun(query=text)
            best_agent = result.strip().lower()

            if best_agent not in self.valid_agents:
                raise RuntimeError(f"invalid agent type returned: {best_agent}")
            return ClassificationResult(
                agent=best_agent,
                debug_info={
                    "method": "llm",
                    "raw_response": result
                }
            )
        except Exception as e:
            raise ValueError(f"Classification failed {str(e)}") from e
    
    async def route_query(self, classification_result: dict, query_text: str) -> str:

        agent = classification_result["agent"]
        prompt = PROMPTS[agent]

        chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True
        )
        
        return await chain.arun(query=query_text)
        