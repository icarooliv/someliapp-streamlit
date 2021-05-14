import streamlit as st
from PIL import Image
import numpy as np
from fastai.basics import load_learner
import numpy as np

learn = load_learner('classificador1.pkl')

CATEGORIES = {
    "molhos_cremes_aperitivos": 1,
    "aperitivos": 2,
    "queijos_suaves": 3,
    "queijos_fortes": 4,
    "sanduiches": 5,
    "comida_asiatica": 6,
    "carnes_churrasco": 7,
    "porco_vitela": 8,
    "ovelha": 9,
    "massas_molhos_suaves": 10,
    "massas_molhos_encorpados": 11,
    "aves": 12,
    "salmão_atum": 13,
    "frutos_mar": 14,
    "mariscos": 15,
    "frutas_sobremesas": 16,
}


FOODS_BY_CATEGORY = {
    "beet_salad": "molhos_cremes_aperitivos",
    "caesar_salad": "molhos_cremes_aperitivos",
    "caprese_salad": "molhos_cremes_aperitivos",
    "apple_pie": "frutas_sobremesas",
    "baklava": "frutas_sobremesas",
    "beignets": "frutas_sobremesas",
    "bread_pudding": "frutas_sobremesas",
    "cannoli": "frutas_sobremesas",
    "carrot_cake": "frutas_sobremesas",
    "cheesecake": "frutas_sobremesas",
    "chocolate_cake": "frutas_sobremesas",
    "chocolate_mousse": "frutas_sobremesas",
    "churros": "frutas_sobremesas",
    "ceviche": "frutos_mar",
    "baby_back_ribs": "porco_vitela",
    "beef_carpaccio": "carnes_churrasco",
    "beef_tartare": "carnes_churrasco",
    "bibimbap": "comida_asiatica",
    "cheese_plate": "queijos_suaves",
    "bruschetta": "aperitivos",
    "breakfast_burrito": "aperitivos",
    "chicken_wings": "aves",
    "chicken_quesadilla": "aves",
    "chicken_curry": "aves",
}

WINES_BY_CATEGORY = {
    "Pouilly Fumé": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Chablis": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Sauvignon Blanc": [1, 2, 3, 4, 6, 8, 10, 12, 13, 14, 15],
    "Riesling": [1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15],
    "Chenin Blanc": [1, 2, 3, 4, 6, 8, 10, 12, 14, 15],
    "Gewürztraminer": [1, 2, 3, 4, 6, 7, 8, 12, 13, 14],
    "Pinos Gris/Grigio": [3, 4, 6, 8, 10, 12, 14],
    "Pouilly-Fuissé": [3, 6, 8, 10, 12, 13, 14, 15],
    "Chadornnay": [3, 4, 8, 11, 12, 13, 14, 15, 16],
    "White Zinfandel": [1, 2, 3, 5, 6, 8, 10, 12, 13, 14, 15, 16],
    "Beaujolais": [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 16],
    "Chianti": [1, 2, 3, 5, 7, 8, 10, 11, 12, 13, 14],
    "Pinot Noir": [1, 3, 5, 7, 8, 9, 11, 12, 13, 14],
    "Merlot ": [1, 3, 4, 5, 7, 9, 11, 12],
    "Zinfandel ": [1, 4, 5, 6, 7, 8, 9, 11, 12],
    "Cabernet Sauvignon ": [1, 4, 5, 7, 8, 9],
    "Blanc de Blancs ": [1, 2, 6, 10, 14, 15],
    "Extra Dry ": [1, 2, 3, 6, 8, 10, 14, 15],
    "Brut": [1, 2, 6, 8, 10, 14, 15],
    "Rosé": [1, 2, 3, 7, 11, 15],
    "Sec ": [16],
    "Doux": [16],
}


def get_wines_by_food(food):
    if not food in FOODS_BY_CATEGORY:
        return []

    category = CATEGORIES[FOODS_BY_CATEGORY[food]]

    wines = []
    for wine in WINES_BY_CATEGORY:
        if category in WINES_BY_CATEGORY[wine]:
            wines.append(wine)
    return wines


st.title("SomeliApp")

st.markdown(
    """
    O someliapp é uma ferramenta que vai te ajudar a 
    escolher o vinho perfeito para combinar com sua refeição!
    """
)

st.markdown("## Adicione uma foto")

st.markdown("Para começar,escolha a imagem da sua refeição:")

uploaded_file = st.file_uploader(
    # "Escolha a imagem da sua refeição...",
    "",
    type=["jpg", "png"],
    accept_multiple_files=False,
    help="A imagem será utilizada para encontrar o vinho que combina com sua refeição.",
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    res = learn.predict(np.array(image))[0]
    wines = get_wines_by_food(res)

    st.markdown("Essa é a imagem que você adicionou: ")
    st.image(image, width=300, caption=res)

    st.markdown("## Resultado")
    st.markdown(
        """
        Esses são os vinhos que nosso modelo sugere para combinar com sua receita!
        """
    )
    if len(wines) > 0:
        st.markdown(f"*{', '.join([str(elem) for elem in wines])}*")
    else:
        st.markdown(f"*Comida não encontrada!*")

