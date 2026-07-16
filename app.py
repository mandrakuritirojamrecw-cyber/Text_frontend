import gradio as gr
import requests

API_URL = "https://text-backend-mr70.onrender.com/translate"

languages = [
    "auto",
    "english",
    "telugu",
    "hindi",
    "tamil",
    "kannada",
    "malayalam",
    "french",
    "german",
    "spanish",
    "japanese",
    "korean",
    "chinese"
]

def translate(text, source, target):
    data = {
        "text": text,
        "source_language": source,
        "target_language": target
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        return response.json()["translated"]
    else:
        return f"Error {response.status_code}: {response.text}"

demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(lines=6, label="Enter Text"),
        gr.Dropdown(languages, value="auto", label="Source Language"),
        gr.Dropdown(languages, value="telugu", label="Target Language")
    ],
    outputs=gr.Textbox(lines=6, label="Translated Text"),
    title="🌍 AI Text Translator"
)

demo.launch()
