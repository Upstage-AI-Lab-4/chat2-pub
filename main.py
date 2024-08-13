from chain.create_chat_text_chain import create_chat_text_chain
from ui import page
from llm.upstage import llm, name
import logging

chain = create_chat_text_chain(llm)

def setLogger():
    """
    setLogger 함수 설명
    로그 출력을 ERROR보다 상위레벨만 출력되도록 설정하였습니다.
    """
    logging.basicConfig()
    logging.getLogger('Langchain.retrievers.multi_query').setLevel(logging.ERROR)


def load_template():
    """
    load_template 함수 설명
    아래의 template은 Warren Buffet와 Donald Trump의 소개 및 톤앤매너 설정 부분,
    persona_memory에 Warren Buffet의 명언을 담은 docs를 반영하도록 설정하고,
    history에 기존 대화 전부를 저장하도록 설정하였습니다.
    """
    template = """
        I want you to act like Warren Buffett, a famous American businessman and investor.
        I want you to make tone, manner, and the vocabulary
        of Donald Trump who is 45th American President would use.
        I want you respond and answer like Warren Buffett and using the tone, manner, and the vocabulary
        of Donald Trump would use.
        
        You must know all of the knowledge to Warren Buffett and Donald Trump.

        Extraction for Warren Buffett's interviews are as follows:
        ###
        {persona_memory}

        ###
        {history}
        human: {query}
        Smart Investor:
        """
    yield template


def on_user_input(message, history, system_prompt, tokens):
    print(f'''
        message: {message}
        history: {history}
        system_prompt: {system_prompt}
        tokens: {tokens}
    ''')

    output = chain.invoke({'query': message, 'history': history})

    return f'''
    TODO: model output string
    input: {message}
    model: {name}
    output: {output}
    '''

if __name__ == '__main__':
    page.launch(on_user_input)
