from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from history.history import history
from memory.memory import save_memory
from template.buffet_trump import buffet_trump
from operator import itemgetter
from retriever import Retriever
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

def create_chat_text_chain(llm):
    memory = save_memory()
    prompt_bot = buffet_trump()
    
    return RunnableParallel({
        'persona_memory': itemgetter('query') | retriever, # retriever도 연결예정
        'history': RunnableLambda(memory.load_memory_variables) | itemgetter('history'),
        'query': RunnablePassthrough(),
    }) | {
        'answer': prompt_bot | llm | StrOutputParser(),
        'persona_memory': itemgetter('persona_memory'),
        'conversation': prompt_bot | history
    }
