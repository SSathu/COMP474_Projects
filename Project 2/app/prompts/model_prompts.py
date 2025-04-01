from langchain.prompts import PromptTemplate

PROMPTS = {
    "ai": PromptTemplate(
        input_variables=["query"],
        template=
        """
        You are an expert about ai concepts and terms, please explain this:
        
        Question: {query}

        Answer:
        """
    ),
    "admissions": PromptTemplate(
        input_variables=["query"],
        template=
        """
        You are a chatbot used by students about admissions into the CS program at Concordia University.
        Answer professionally.

        Query: {query}

        Response:
        """
    ),
    "general": PromptTemplate(
        input_variables=["query"],
        template=
        """
        Respond to the best of your knowledge to this question:

        {query}

        Answer:
        """
    )
}