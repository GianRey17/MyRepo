import streamlit as st
from PIL import Image
import time

Lady = { "c1": 'Modest', 'c2': 'Gorgeous', 'c3': 'Smart' }
Chelcee = {"c1": 'Cute', 'c2': 'Chubby', 'c3': 'Pretty'}

st.header("characteristics")
options = st.multiselect("Ano type mo sa bayi?", ("Gorgeous", "Modest", "Smart", "Pretty", "Chubby", "Friendly", "Cute"))
st.write(f"You selected: {options}")
if any(option in Lady.values() for option in options):
    st.write('Type mo si Lady? back off akon nasa')
    loading = st.empty()
    with loading:
     st.spinner('Loading...')
     time.sleep(5)
     st.write('Complete.')
     image = Image.open('/Users/marycrispineda/Downloads/chad.jpg')
     st.image(image, width=300, caption='akig ko')