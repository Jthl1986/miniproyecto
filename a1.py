import pandas as pd
import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="¿Qué rinde uso?",page_icon="🌱",layout="wide") 
st.title("Calculadora de rinde")

#rendimientos estimados por region de soja
esojarbsas = 2.41
esojarcor = 2.50
esojarsta = 2.13
esojarer = 1.70
esojarlapam = 2.15

#rendimientos estimados por region de maiz
emaizrbsas = 6.72
emaizrcor = 7.49
emaizrsta = 5.51
emaizrer = 3.0
emaizrlapam = 6.98

#https://www.bcr.com.ar/es/mercados/gea/estimaciones-nacionales-de-produccion/estimaciones

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

#https://datosestimaciones.magyp.gob.ar/reportes.php?reporte=Estimaciones

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
region = st.radio('Ingrese provincia: ',["Buenos Aires", "Cordoba", "Santa Fe", "Entre Rios", "La Pampa"])
cultivo = st.radio('Ingrese tipo de cultivo: ', ["Soja", "Maiz"])
rinde = st.number_input("Ingrese rinde ultima campaña (Tn/ha) ", step=1)
if st.button("Ingresar"):
    rinde_historico = rendimientos2.get((region, cultivo), 0)
    rindeestimado = rendimientos.get((region, cultivo), 0)
    dif = (rinde - rinde_historico)/rinde_historico
    ratio = 1 + dif
    resultado = rindeestimado * ratio
    st.success("Rinde para cargar en excel", round(resultado, 2))
    
rend_soja = {
    "Buenos Aires": esojarbsas,
    "Cordoba": esojarcor,
    "Santa Fe": esojarsta,
    "Entre Rios": esojarer,
    "La Pampa": esojarlapam,
}

rend_maiz = {
    "Buenos Aires": emaizrbsas,
    "Cordoba": emaizrcor,
    "Santa Fe": emaizrsta,
    "Entre Rios": emaizrer,
    "La Pampa": emaizrlapam,
}

st.write("En caso de no informar el rinde en F8819 utilizar para el planteo productivo (excel) los que figuran en las tablas inferiores")

st.header("Rendimientos estimados de Soja por Región")
df = pd.DataFrame.from_dict(rend_soja, orient='index', columns=['Rendimiento (Ton/Ha)'])
st.dataframe(df, width=800)

st.header("Rendimientos estimados de Maíz por Región")
df = pd.DataFrame.from_dict(rend_maiz, orient='index', columns=['Rendimiento (Ton/Ha)'])
st.dataframe(df, width=800)
