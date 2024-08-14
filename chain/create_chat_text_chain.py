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

    def inner(params):
        chain = RunnableParallel({
            'persona_memory': itemgetter('query'), # retriever도 연결예정
            'history': RunnableLambda(memory.load_memory_variables) | itemgetter('history'),
            'query': itemgetter('query'),
        }) | {
                    'answer': prompt_bot | llm | StrOutputParser(),
                    'persona_memory': itemgetter('persona_memory'),
                    'prompt': prompt_bot,
                    'conversation': prompt_bot | history
                }

        result = chain.invoke(params)
        memory.save_context({'query': params['query']}, {"answer": result["answer"]})

        return result

    return inner
