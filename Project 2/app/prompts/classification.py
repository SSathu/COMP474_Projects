from langchain.prompts import PromptTemplate

CLASSIFICATION_PROMPT = PromptTemplate(
    input_variables=["query"],
    template = """
    Your task is to categorize this query:
    
    **Query:** {query}

    **Categories:**
    - ai ( Questions about artificial intelligence, machine learning, LLMs )
    - admissions (Questions about admissions, requirements, or applications for Computer Science)
    - general (everything else)

    **Examples:**
    - "what is a neural network?" -> ai
    - "what is the program deadline for CS?" -> admissions
    - "why is the sky blue?" -> general

    Respond with ONLY one of the category names.
    """
)