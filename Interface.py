import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
import time 
from PIL import Image

def afficher_texte_GPT(texte):
    container = st.empty()
    texte_affiche = ""
    for lettre in texte:
        texte_affiche += str(lettre)
        container.write(texte_affiche)
        time.sleep(0.05)


# Configuration de l'API Azure
api_endpoint = "https://openaihackathonefrei.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2025-01-01-preview"
api_key = "FBLDChmxiGhW9gQlXoX3hiLC6Wlc7qezmTKPDbn5eHGrHdLtGKJYJQQJ99BDACYeBjFXJ3w3AAABACOGpaTC"

# Fonction pour interroger le modèle GPT
def get_gpt_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": "Vous êtes un assistant utile."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
    try:
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {e}"

# Interface Streamlit
st.title("🗺️ Les Collectivités Locales (2024)")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(Image.open("Coll.jpeg"),width= 300)

st.markdown(
    """
    <style>
    body { background-color: white; color: black; }
    </style>
    """,
    unsafe_allow_html=True
)


user_input = st.text_area("Entrez votre question :", "")

# Bouton pour envoyer
if st.button("Envoyer"):
    if user_input.strip():
        response = get_gpt_response(user_input)
        st.write("GPT-4 🤖:")
        afficher_texte_GPT(response)
        #st.write(response)
    else:
        st.warning("Veuillez entrer votre question.")