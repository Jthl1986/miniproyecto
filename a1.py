import pandas as pd
import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="¿Qué rinde uso?",page_icon="🌱",layout="wide") 
st.title("Calculadora de rinde")

#rendimientos por cultivo por region
esojarbsas = 2.41
esojarcor = 2.50
esojarsta = 2.13
esojarer = 1.70
esojarlapam = 2.15

emaizrbsas = 6.72
emaizrcor = 7.49
emaizrsta = 5.51
emaizrer = 3.0
emaizrlapam = 6.98

hsojarbsas = 3.30
hsojarcor = 2.97
hsojarsta = 3.13
hsojarer = 2.54
hsojarlapam = 3.45

hmaizrbsas = 7.08
hmaizrcor = 7.50
hmaizrsta = 6.17
hmaizrer = 3.76
hmaizrlapam = 7.15

rendimientos = {
    ("Buenos Aires", "Soja"): esojarbsas,
    ("Cordoba", "Soja"): esojarcor,
    ("Santa Fe", "Soja"): esojarsta,
    ("Entre Rios", "Soja"): esojarer,
    ("La Pampa", "Soja"): esojarlapam,
    ("Buenos Aires", "Maiz"): emaizrbsas,
    ("Cordoba", "Maiz"): emaizrcor,
    ("Santa Fe", "Maiz"): emaizrsta,
    ("Entre Rios", "Maiz"): emaizrer,
    ("La Pampa", "Maiz"): emaizrlapam,
}

rendimientos2 = {
    ("Buenos Aires", "Soja"): hsojarbsas,
    ("Cordoba", "Soja"): hsojarcor,
    ("Santa Fe", "Soja"): hsojarsta,
    ("Entre Rios", "Soja"): hsojarer,
    ("La Pampa", "Soja"): hsojarlapam,
    ("Buenos Aires", "Maiz"): hmaizrbsas,
    ("Cordoba", "Maiz"): hmaizrcor,
    ("Santa Fe", "Maiz"): hmaizrsta,
    ("Entre Rios", "Maiz"): hmaizrer,
    ("La Pampa", "Maiz"): hmaizrlapam,
}

#Ingresos usuario
region = st.selectbox('Ingrese provincia: ',["Buenos Aires", "Cordoba", "Santa Fe", "Entre Rios", "La Pampa"])
cultivo = st.selectbox('Ingrese tipo de cultivo: ', ["Soja", "Maiz"])
rinde = st.number_input("Ingrese rinde ultima campaña ", step=1)
if st.button("Ingresar"):
    rinde_historico = rendimientos.get((region, cultivo), 0)
    dif = (rinde - rinde_historico)/rinde
    rindeestimado = rendimientos2.get((region, cultivo), 0)
    resultado = rindeestimado * dif
    st.success(resultado)
    
