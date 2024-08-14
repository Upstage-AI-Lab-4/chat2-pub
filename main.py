from chain.create_chat_text_chain import create_chat_text_chain
from ui import page
from llm.upstage import llm, name
from ui.stream_text import stream_text
import logging
from indexing.vector_store import VectorStore
from retriever.retriever import Retriever

chain = create_chat_text_chain(llm)

def setLogger():
    """
    setLogger 함수 설명
    로그 출력을 ERROR보다 상위레벨만 출력되도록 설정하였습니다.
    """
    logging.basicConfig()
    logging.getLogger('Langchain.retrievers.multi_query').setLevel(logging.ERROR)

def on_user_input(message, history, system_prompt, tokens):
    print(f'''
        message: {message}
        history: {history}
        system_prompt: {system_prompt}
        tokens: {tokens}
    ''')

    setLogger()

    yield from stream_text(chain.stream({'query': message}))

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