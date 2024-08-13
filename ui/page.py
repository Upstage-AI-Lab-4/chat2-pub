import gradio as gr
import time
from typing import Callable, Any

def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.05)
        yield response[: i + 1]

def launch(handler: Callable[[Any, Any, Any, Any], str]) -> None:
    demo = gr.ChatInterface(
        handler,
        additional_inputs=[
        ],
    )

    demo.launch()
