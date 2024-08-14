import os
#from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_upstage import UpstageEmbeddings


class Retriever:
    def __init__(self):
        self.api_key = "-"
        os.environ["OPENAI_API_KEY"] = self.api_key
        os.environ.get("OPENAI_API_KEY")
        #self.embedding_model = OpenAIEmbeddings(api_key=self.api_key, model="text-embedding-3-small") 
        self.embedding_model = UpstageEmbeddings(api_key=self.api_key, model="solar-embedding-1-large")
        

    def retriever(self, vector_store, query):
        retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})
        result = retriever.get_relevant_documents(query)

        # for d in result:
        #     print(d.page_content)
        #     print("===") 
        return result
        

       
    
    