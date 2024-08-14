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

    class ChatTextChain:
        def __init__(self, llm, memory, prompt_bot):
            self.llm = llm
            self.memory = memory
            self.prompt_bot = prompt_bot

        def stream(self, params):
            chain = RunnableParallel({
                'persona_memory': itemgetter('query'), # retriever도 연결예정
                'history': RunnableLambda(self.memory.load_memory_variables) | itemgetter('history'),
                'query': itemgetter('query'),
            }) | {
                        'answer': self.prompt_bot | self.llm | StrOutputParser(),
                        'persona_memory': itemgetter('persona_memory'),
                        'prompt': self.prompt_bot,
                        'conversation': self.prompt_bot | history
                    }

            result = chain.invoke(params)
            self.memory.save_context({'query': params['query']}, {"answer": result["answer"]})
            yield result

    return ChatTextChain(llm, memory, prompt_bot)
