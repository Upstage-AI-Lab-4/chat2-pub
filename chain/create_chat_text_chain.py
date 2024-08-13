from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from history import history
from memory import memory
from template.buffet_trump import buffet_trump
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def create_chat_text_chain(llm):
    return RunnableParallel({
        'persona_memory': memory,
        'history': history,
        'query': RunnablePassthrough(),
    }) \
        | ChatPromptTemplate.from_template(buffet_trump()) \
        | llm \
        | StrOutputParser()
