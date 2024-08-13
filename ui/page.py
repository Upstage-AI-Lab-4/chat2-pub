import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def launch():
    demo = gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
    )

    demo.launch()
