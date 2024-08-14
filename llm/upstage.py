from dotenv import load_dotenv
import os
from langchain_upstage import ChatUpstage
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
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
        print('upstage_api_key:', os.getenv('UPSTAGE_API_KEY')[:5])

        raise

name = 'upstage solar'
