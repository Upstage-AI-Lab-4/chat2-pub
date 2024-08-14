from indexing.vector_store import VectorStore


class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        

    def retriever(self, query):
        retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})
        retriever_result = retriever.get_relevant_documents(query)

        # for d in retriever_result:
        #     print(d.page_content)
        #     print("===") 
        return retriever_result
        

       
    
    