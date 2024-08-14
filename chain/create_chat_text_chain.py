from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from history.history import history
from memory.memory import save_memory
from template.buffet_trump import buffet_trump
from operator import itemgetter
from retriever.retriever import Retriever
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

def create_chat_text_chain(llm):
    memory = save_memory()
    prompt_bot = buffet_trump()

    def retrieve_(query):
        print(f"Retrieve Persona Memory Query: {query}")
        retriever = Retriever()
        result = retriever.retriever(query=query)
        print(f"Retrieved Persona Memory: {result}")
        return result
    
    class ChatTextChain:
        def __init__(self, llm, memory, prompt_bot):
            self.llm = llm
            self.memory = memory
            self.prompt_bot = prompt_bot

        def stream(self, params):
            chain = RunnableParallel({
                'persona_memory': itemgetter('query') | RunnableLambda(retrieve_),  # retriever도 연결예정
                'history': RunnableLambda(self.memory.load_memory_variables) | itemgetter('history'),
                'query': itemgetter('query'),
            }) | {
                        'answer': self.prompt_bot | self.llm | StrOutputParser(),
                    }

            result = chain.invoke(params)
            self.memory.save_context({'query': params['query']}, {"answer": result["answer"]})
            yield result

    return ChatTextChain(llm, memory, prompt_bot)
