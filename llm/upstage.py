from os import environ
from langchain_upstage import ChatUpstage
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatUpstage()

def chat(message: str):
    try:
        messages = [
            HumanMessage(message)
        ]
        response = llm.invoke(messages)
        print(response)

        return response
    except Exception as e:
        print('error:', print(e))
        print('upstage_api_key:', environ.get('UPSTAGE_API_KEY')[:5])

        raise

name = 'upstage solar'
