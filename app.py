import streamlit as st
from PIL import Image
import numpy as np

st.title('SomeliApp')

st.markdown(
    """
    O someliapp é uma ferramenta que vai te ajudar a 
    escolher o vinho perfeito para combinar com sua refeição!
    """
)

st.markdown("## Adicione uma foto")

st.markdown("Para começar, escolha a imagem da sua refeição:")

uploaded_file = st.file_uploader(
    # "Escolha a imagem da sua refeição...", 
    "",
    type=["jpg", "png"], 
    accept_multiple_files=False, 
    help="A imagem será utilizada para encontrar o vinho que combina com sua refeição."
)

if uploaded_file is not None:
    st.markdown("Essa é a imagem que você adicionou: ")
    # model = load_model()
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    st.markdown("## Resultado")
    st.markdown(
        """
        Esse é o resultado que o nosso modelo sugere para combinar com sua receita!
        """
    )
    array_image = np.array(image)
    # prediction = model.predict(image)
    prediction = "Vinho tinto!"
    st.markdown(f'*{prediction}*')
