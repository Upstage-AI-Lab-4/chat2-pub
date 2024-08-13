import gradio as gr
from typing import Callable, Any


def launch(handler: Callable[[Any, Any, Any, Any], str]) -> None:
    demo = gr.ChatInterface(
        handler,
        additional_inputs=[
        ],
    )

    demo.launch()
