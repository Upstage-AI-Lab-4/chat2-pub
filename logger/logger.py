import logging

class Logger:
    
    def __init__(self):
        pass
    
    def setLogger(self):
        """
        setLogger 함수 설명
        로그 출력을 ERROR보다 상위레벨만 출력되도록 설정하였습니다.
        """
        logging.basicConfig()
        logging.getLogger('Langchain.retrievers.multi_query').setLevel(logging.ERROR)