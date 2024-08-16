from chain.create_chat_text_chain import ChatTextChain
from ui import page
from llm.upstage import llm, name
from ui.stream_text import stream_text
<<<<<<< HEAD
from logger.logger import Logger
=======
import logging
from indexing.vector_store import VectorStore
from retriever.retriever import Retriever
>>>>>>> 6a02f76 (종료)

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

def main():
    # VectorStore 인스턴스 생성
    vector_store = VectorStore()

    # Retriever 인스턴스 생성
    retriever = Retriever(vector_store)

    # 각 모듈 실행
    vector_store.run()
    retriever.run()

if __name__ == '__main__':
    page.launch(on_user_input)
    main()