import streamlit as st
from datetime import date
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Turno TV", page_icon="logo.png")

# --- LÓGICA PARA SERVIR EL MANIFEST ---
# Este bloque permite que el navegador encuentre el manifest.json
def inject_pwa_meta():
    st.markdown(
        f"""
        <link rel="manifest" href="./manifest.json?v=10">
        <link rel="icon" href="./logo.png">
        """,
        unsafe_allow_html=True,
    )

# --- ESTILOS ---
st.markdown("""
    <style>
    .stApp { background-color: #fffaf5; }
    .resultado {
        background-color: #ffe0b2;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #ff9d42;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
if os.path.exists("logo.png"):
    st.image("logo.png", width=120)

st.title("Turno TV")

participantes = ["Adri", "Nata", "Papá", "Mamá"]
fecha_base = date(2026, 4, 29)
fecha_consulta = st.date_input("Selecciona fecha:", date.today())

if st.button("¿A QUIÉN LE TOCA?"):
    delta = fecha_consulta - fecha_base
    dias = delta.days
    if dias < 0:
        st.warning("El ciclo aún no ha comenzado.")
    else:
        ganador = participantes[dias % 4]
        st.markdown(f'<div class="resultado"><h1 style="color:#5d3a1a;">{ganador}</h1></div>', unsafe_allow_html=True)

# Inyectar metadatos al final
inject_pwa_meta()
