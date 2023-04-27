import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

def main():
    st.title('Armário', anchor=False)
    total, crud, maior_quant = st.columns(3)
    r = requests.get('http://127.0.0.1:5000/api/')
    data = json.loads(r.text)
    with total:
        st.title("Total", anchor=False)
        total = r.json()
        st.markdown(f"Existem **{len(total)}** itens na tabela")
    with crud:
        option = st.selectbox(
            "O que deseja fazer:",
            ("Adicionar", "Atualizar", "Deletar")
        )
        if option == "Adicionar":
            adicionar()
        elif option == "Atualizar":
            atualizar()
        else:
            deletar()
    with maior_quant:
        st.title("Item", anchor=False)
        if data == []:
            st.write("Tabela vazia")
        else:
            sorted_data = sorted(data, key=lambda x: int(x['quantidade']), reverse=True)  
            item_maior_quantidade = sorted_data[0]  
            st.write("Item com maior quantidade no armario!")
            st.write(f"Nome: {item_maior_quantidade['name']}")
            st.write(f"Quantidade: {item_maior_quantidade['quantidade']}")

    st.table(data)

def adicionar():
    Nome = st.text_input("Nome do componente")
    desc = st.text_input("Descrição do objeto")
    Quantidade = st.text_input("Quantidade:")
    cadastro = st.button("CADASTRAR")
    if cadastro:
        dados = dict(nome=Nome, dec=desc, quant=Quantidade)
        enviar = requests.post("http://127.0.0.1:5000/api/", json=dados)

def atualizar():
    id_rec = st.text_input("Digite o id do componente")
    Nome = st.text_input("Nome do componente")
    desc = st.text_input("Descrição do objeto")
    Quantidade = st.text_input("Quantidade:")
    atualizar = st.button("ATUALIZAR")
    if atualizar:
        dados = dict(id=id_rec, nome=Nome, dec=desc, quant=Quantidade)
        enviar = requests.put("http://127.0.0.1:5000/api/", json=dados)

def deletar():
    delete = st.text_input("Digite o id do componente")
    deletar = st.button("DELETAR")
    if deletar:
        d = dict(id=str(delete))
        enviar = requests.delete("http://127.0.0.1:5000/api/", json=d)

if __name__ == "__main__":
    main()