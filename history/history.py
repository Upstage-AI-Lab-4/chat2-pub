def history(prompt):
    """
    prompt 에 주입될 history chat 생성
    """
    return prompt.messages[0].content.split('###\n')[-1]
