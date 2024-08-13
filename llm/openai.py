from os import environ

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)

def chat(message: str):
    try:
        print(llm)
        messages = [
            (
                "system",
                "You are a helpful assistant that translates English to French. Translate the user sentence.",
            ),
            ("human", "I love programming."),
        ]

        response = llm.invoke(messages)
        print(response)

        return response
    except Exception as e:
        print('error:', print(e))
        print('openai_api_key:', environ.get('OPENAI_API_KEY')[:5])

        raise

name = 'openai chat-gpt'
