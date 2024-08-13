import gradio as gr
from typing import Callable, Any


def launch(handler: Callable[[Any, Any, Any, Any], str]) -> None:
    with gr.ChatInterface(handler, additional_inputs=[]) as demo:
        pass

    demo.launch()
