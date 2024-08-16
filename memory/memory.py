from langchain.memory import ConversationBufferWindowMemory

class Memory:
    
    def __init__(self):
        pass
    
    def save_memory(self):
        """
        prompt 에 주입될 persona_memory 생성
        """
        return ConversationBufferWindowMemory(
            k=20, 
            ai_prefix='Smart Investor', 
            human_prefix='human'
        )
