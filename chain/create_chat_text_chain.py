from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from history.history import History
from memory.memory import Memory
from template.buffet_trump import Template
from operator import itemgetter
from retriever.retriever import Retriever
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

class ChatTextChain:
    def __init__(self, llm):
        self.llm = llm
        self.memory = Memory().save_memory()
        self.prompt_bot = Template().buffet_trump()

    def retrieve_(self, query):
        print(f"Retrieve Persona Memory Query: {query}")
        retriever = Retriever()
        result = retriever.retriever(query=query)
        print(f"Retrieved Persona Memory: {result}")
        return result

    def stream(self, params):
        chain = RunnableParallel({
            'persona_memory': itemgetter('query') | RunnableLambda(self.retrieve_),  # retriever도 연결예정
            'history': RunnableLambda(self.memory.load_memory_variables) | itemgetter('history'),
            'query': itemgetter('query'),
            }) | {
                'answer': self.prompt_bot | self.llm | StrOutputParser(),
            }

        result = chain.invoke(params)
        self.memory.save_context({'query': params['query']}, {"answer": result["answer"]})
        yield result
