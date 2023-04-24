import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Armário')
option = st.selectbox(
    "O que deseja fazer:",
    ("Adicionar", "Atualizar", "Deletar")
)
if option == "Adicionar":
    Nome = st.text_input("Nome do componente")
    Quantidade = st.text_input("Quantidade:")
    desc = st.text_input("Descrição do objeto")
    cadastro = st.button("CADASTRAR")
    if cadastro:
        dados = dict(nome=Nome, dec=desc, quant=Quantidade)
        enviar = requests.post("http://127.0.0.1:5000/api/", json=dados)

elif option == "Atualizar":
    st.write("atualize")
else:
    delete = st.text_input("Digite o id do componente")
    deletar = st.button("DELETAR")
    if deletar:
        d = dict(id=str(delete))
        enviar = requests.delete("http://127.0.0.1:5000/api/", json=d)
        #st.warning(enviar['status'])

r = requests.get('http://127.0.0.1:5000/api/')
st.table(r.json())