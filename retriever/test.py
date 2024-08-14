#create retriever - persona
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


embed_model = OpenAIEmbeddings(api_key=api_key,
                                  model='text-embedding-3-small')

vector_index = FAISS.from_documents(documents, embed_model)
retriever = vector_index.as_retriever(search_type="mmr", search_kwargs={"k": 3})
result = retriever.get_relevant_documents(query)
for d in result:
    print(d.page_content)
    print("===")

vector_index.save_local("../models/holmes_faiss.json")


#VectorStore
from langchain_community.vectorstores import FAISS

vector_index = FAISS.from_documents(documents, embed_model)

retrieved = vector_index.similarity_search("What is MistralAI?")
retrieved[0].page_content

#Retriever
# search_type
# mmr: maximal marginal relevance retrieval
query = 'OpenAI의 sora모델에 대해 알려줘'
retriever = vector_index.as_retriever(search_type="mmr")
retriever.get_relevant_documents(query)

# similarity_score_threshold
retriever = vector_index.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.3} #score_threshold": 0.3 값을 조정해서
)
retriever.get_relevant_documents(query)

# top_k
retriever = vector_index.as_retriever(search_kwargs={"k": 3})
retriever.get_relevant_documents(query)

#Multi Query etriever
import logging

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0)

from langchain.retrievers.multi_query import MultiQueryRetriever
retriever_multi = MultiQueryRetriever.from_llm(
    retriever=vector_index.as_retriever(), llm=llm
)

retriever_multi.get_relevant_documents(query="OpenAI의 sora모델에 대해 알려줘")

#Parent Document Retriever
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore

store = InMemoryStore()

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)

vector_index = Chroma(collection_name='split_parents', embedding_function=embed_model)

retriever = ParentDocumentRetriever(
    vectorstore=vector_index,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)
retriever.docstore
retriever.get_relevant_documents(query="OpenAI의 sora모델에 대해 알려줘")
retriever.add_documents(docs)
retriever.get_relevant_documents(query="OpenAI의 sora모델에 대해 알려줘")

