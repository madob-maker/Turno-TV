import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# Configuración de la página e icono de la pestaña
st.set_page_config(
    page_title="Turno TV",
    page_icon="logo.png",
    layout="centered"
)

# --- INYECCIÓN DEL MANIFEST PARA EL MÓVIL ---
components.html(
    """
    <script>
        const link = parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = './manifest.json';
        parent.document.head.appendChild(link);
    </script>
    """,
    height=0,
)

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main {
        background-color: #fffaf5;
    }
    .stButton>button {
        background-color: #ff9d42;
        color: white;
        border-radius: 10px;
        border: none;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .resultado {
        font-size: 40px;
        color: #5d3a1a;
        text-align: center;
        font-weight: bold;
        background: #ffe0b2;
        padding: 20px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA APP ---
# Mostrar el logo centrado
st.image("logo.png", width=150)

st.title("Turno TV")
st.subheader("Tu día de TV")

# Configuración de la lógica
participantes = ["A", "N", "M", "MB"]
fecha_base = date(2026, 4, 29)

# Selector de fecha
fecha_consulta = st.date_input("¿Qué día quieres consultar?", date.today())

if st.button("CALCULAR TURNO"):
    delta = fecha_consulta - fecha_base
    dias = delta.days
    
    if dias < 0:
        st.warning(f"El ciclo comienza el {fecha_base.strftime('%d/%m/%Y')}. Elige una fecha igual o posterior.")
    else:
        indice = dias % 4
        ganador = participantes[indice]
        
        st.markdown(f'<div class="resultado">Hoy le toca a: {ganador}</div>', unsafe_allow_html=True)
        
        # Guía visual del orden
        st.write("")
        st.info(f"Orden de rotación: A ➔ N ➔ M ➔ MB")

st.caption("La rotación comenzó el 29/04/2026 con el participante A.")
