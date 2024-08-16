import os
from indexing.vector_store import VectorStore


class Retriever:
    def __init__(self):
        # Get the directory of the current file (retriever.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the absolute path to the index directory
        vector_store_path = os.path.join(current_dir, '..', 'indexing')
        
        # Load the vector store using the constructed path
        self.vector_store = VectorStore().load_vector_store(
            vector_store_path=vector_store_path
        )
        

    def retriever(self, query):
        '''
        ### 트러블 슈팅 해결법
        기존 : get_relevant_documents(query)
        수정 : invoke(query)
        '''
        retriever = self.vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})
        retriever_result = retriever.invoke(query) 
        new_result=[]

        for d in retriever_result:
            new_result.append(d.page_content)
        return '\n'.join(new_result)
        

       
    
    