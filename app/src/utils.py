import base64
import os

import pandas as pd
import streamlit as st

from .constants import BASE_DIR


@st.cache_data
def load_data():
    return pd.read_csv(BASE_DIR / "resources" / "resources.csv").fillna("")


def load_logos():
    def get_image_base64(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()

    return {
        "hf": get_image_base64(BASE_DIR / "resources" / "logos/hf.png"),
        "web": get_image_base64(BASE_DIR / "resources" / "logos/web.png"),
        "arxiv": get_image_base64(BASE_DIR / "resources" / "logos/arxiv.png"),
        "github": get_image_base64(BASE_DIR / "resources" / "logos/github.png"),
        "text": get_image_base64(BASE_DIR / "resources" / "logos/text.png"),
        "vision": get_image_base64(BASE_DIR / "resources" / "logos/vision.png"),
        "speech": get_image_base64(BASE_DIR / "resources" / "logos/speech.png"),
    }


def create_markdown_img(base64_string, link_url=None, dim=15):
    img_tag = f'<img src="data:image/png;base64,{base64_string}" width="{dim}px" height="{dim}px" alt="Image">'
    if link_url:
        return f'<a href="{link_url}" target="_blank">{img_tag}</a>'
    else:
        return img_tag


def get_environment():
    return os.getenv("STREAMLIT_ENV", "dev")