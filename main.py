from chain.create_chat_text_chain import ChatTextChain
from ui import page
from llm.upstage import llm, name
from ui.stream_text import stream_text
from logger.logger import Logger

chain = ChatTextChain(llm)

def on_user_input(message, history):
    print(f'''
        message: {message}
        history: {history}
    ''')

    Logger().setLogger()

    yield from stream_text(chain.stream({
        'query': message,
        'history': history,
    }))

if __name__ == '__main__':
    page.launch(on_user_input)
