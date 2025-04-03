from app.memory.vector_store import VectorStore
from app.tools.wikipedia_api import WikipediaAPI
from app.llm.ollama_client import OllamaClient


class GeneralAgent:
    def __init__(self):
        self.model = "ollama-general"
        self.ollama_client = OllamaClient(model=self.model)
        self.memory = VectorStore()
        self.wikipedia = WikipediaAPI()

    def respond(self, user_id: str, query: str):
        # Retrieve conversation history
        history = self.memory.retrieve_memory(user_id)

        # Search Wikipedia for general knowledge
        wiki_result = self.wikipedia.search_wikipedia(query)

        # Generate response
        prompt = f"User Query: {query}\n\nPrevious Context:\n{history}\n\nWikipedia Info:\n{wiki_result}"
        response = self.ollama_client.get_response(prompt)

        # Store interaction in memory
        self.memory.store_memory(user_id, query, response)

        return response
