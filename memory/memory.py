from langchain.memory import ConversationBufferWindowMemory

def save_memory():
    """
    prompt 에 주입될 persona_memory 생성
    """
    return ConversationBufferWindowMemory(
        k=20, 
        ai_prefix='Smart Investor', 
        human_prefix='human'
    )