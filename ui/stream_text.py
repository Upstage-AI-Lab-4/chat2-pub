def stream_text(iter):
    yield '...'
    output = ''

    for o in iter:
        if 'answer' in o:
            output += o['answer']
            yield output
