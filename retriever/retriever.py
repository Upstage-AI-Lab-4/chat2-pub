#import os
#from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_upstage import UpstageEmbeddings


class Retriever:
    def __init__(self):
        
        

    def retriever(self, vector_store, query):
        retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})
        retriever_result = retriever.get_relevant_documents(query)

        # for d in retriever_result:
        #     print(d.page_content)
        #     print("===") 
        return retriever_result
        

       
    
    