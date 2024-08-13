from langchain_upstage import ChatUpstage
from os import environ

llm = ChatUpstage()

def chat(message: str):
    try:
        print(llm)
        response = llm.invoke(message)
        print(response)

        return response
    except Exception as e:
        print('error:', print(e))
        print('upstage_api_key:', environ.get('UPSTAGE_API_KEY')[:5])

        raise

name = 'upstage solar'
