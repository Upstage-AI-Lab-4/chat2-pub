from ui import page
from llm.upstage import chat, name


def model(input):
    return f'''
    TODO: model output string
    input: {input}
    model: {name}
    output: {chat(input).content}
    '''


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
