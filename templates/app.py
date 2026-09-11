# The sample thingy. Replace this file with your own Gradio app.
#
# The same file runs in two places: in the browser (Gradio-Lite, the
# free route) and on a Hugging Face server (the hosted route). Keep it
# working in both by following python-thingy-guide.md: Gradio 5.45
# features only, no threads, no sockets, no exception may escape an
# event handler, and matplotlib uses the Agg backend with PNG plots.

import sys

import matplotlib
matplotlib.use("Agg")  # must precede any pyplot import
import matplotlib.pyplot as plt
import numpy as np
import gradio as gr

TITLE = "The Wiggler"
AUTHOR = "Your Name Here"


def draw(freq, damping):
    t = np.linspace(0, 10, 1000)
    y = np.exp(-damping * t) * np.sin(2 * np.pi * freq * t)
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, y, color="#c28e0e", linewidth=2)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("time (s)")
    ax.set_title(f"A damped oscillation: freq {freq:.1f} Hz, damping {damping:.2f}")
    fig.tight_layout()
    plt.close(fig)
    return fig


with gr.Blocks(title=TITLE) as demo:
    gr.Markdown(f"# {TITLE}\nBy **{AUTHOR}**")
    with gr.Row():
        freq = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Frequency (Hz)")
        damping = gr.Slider(0.0, 1.0, value=0.2, step=0.05, label="Damping")
    plot = gr.Plot(format="png")
    freq.change(draw, [freq, damping], plot)
    damping.change(draw, [freq, damping], plot)
    demo.load(draw, [freq, damping], plot)


def running_in_pyodide():
    return sys.platform == "emscripten" or "pyodide" in sys.modules


if __name__ == "__main__" or running_in_pyodide():
    demo.launch()
