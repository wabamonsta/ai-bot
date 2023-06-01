import gradio as gr
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
preload_models()

os.environ["SUNO_OFFLOAD_CPU"] = True
os.environ["SUNO_USE_SMALL_MODELS"] = True

output = "The quick brown fox - Jump over the moon [clear throat]"
audio_array = generate_audio(output)
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
with gr.Blocks() as demo:
    with gr.Row():
        text1 = gr.Textbox(label="t1")


demo.launch(share=True)