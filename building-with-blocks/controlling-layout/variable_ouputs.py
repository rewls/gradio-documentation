"""
variable_outputs.py (Guides, Building With Blocks, Controlling Layout)
The number of output textboxes is controlled by an input slider
"""

import gradio as gr


max_textboxes = 10


def variable_outputs(k, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10):
    k = int(k)
    return [gr.Textbox(visible = True)] * k + \
            [gr.Textbox(visible = False)] * (max_textboxes - k)


with gr.Blocks() as demo:
    s = gr.Slider(1, max_textboxes, value = max_textboxes, step = 1,
                  label = "How many textboxes to show:")
    textboxes = []
    for i in range(max_textboxes):
        t = gr.Textbox(f"Textbox {i}", label = "test")
        textboxes.append(t)

    s.change(variable_outputs, [s, *textboxes], textboxes)


if __name__ == "__main__":
    demo.launch()
