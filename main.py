from ui import page
from llm.upstage import chat, name


def model(input):
    return f'''
    TODO: model output string
    input: {input}
    model: {name}
    output: {chat(input).content}
    '''

def load_template():
    """
    load_template 함수 설명
    아래의 template은 Warren Buffet와 Donald Trump의 소개 및 톤앤매너 설정 부분,
    persona_memory에 Warren Buffet의 명언을 담은 docs를 반영하도록 설정하고,
    history에 기존 대화 전부를 저장하도록 설정하였습니다.
    """
    template="""
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

    yield model(message)


if __name__ == '__main__':
    page.launch(on_user_input)
