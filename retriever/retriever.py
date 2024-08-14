#from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_upstage import UpstageEmbeddings
from langchain_community.vectorstores import FAISS
import os

class Retriever:
    def __init__(self, api_key):
        self.api_key = api_key
        self.embed_model = None
        self.vector_index = None
        self.retriever = None

    def retriever(self, documents, query, vector_index_path):
        #self.embed_model = OpenAIEmbeddings(api_key=self.api_key, model='text-embedding-3-small')
        
        self.embed_model = UpstageEmbeddings(
            api_key=self.api_key,
            model="solar-embedding-1-large"
        )
        
        self.vector_index = FAISS.from_documents(documents, self.embed_model)
        self.retriever = self.vector_index.as_retriever(search_type="mmr", search_kwargs={"k": 3})

        result = self.retriever.get_relevant_documents(query)
        for doc in result:
            print(doc.page_content)
            print("===")

        if vector_index_path:
            self.vector_index.save_local(vector_index_path)

    def run(self):
        # retriever 함수를 호출
        pass