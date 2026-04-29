import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# Configuración de la pestaña del navegador
st.set_page_config(
    page_title="Turno TV",
    page_icon="https://raw.githubusercontent.com/madob-maker/Turno-TV/main/logo.png",
    layout="centered"
)

# Inyección para forzar el icono en el escritorio del móvil
components.html(
    """
    <script>
        const link = parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = './manifest.json?v=7';
        parent.document.head.appendChild(link);
        
        const icon = parent.document.createElement('link');
        icon.rel = 'icon';
        icon.href = 'https://raw.githubusercontent.com/madob-maker/Turno-TV/main/logo.png';
        parent.document.head.appendChild(icon);
    </script>
    """,
    height=0,
)

# Estilos visuales
st.markdown("""
    <style>
    .stApp { background-color: #fffaf5; }
    .stButton>button {
        background-color: #ff9d42;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
    }
    .caja-resultado {
        background-color: #ffe0b2;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #ff9d42;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo y Título
st.image("https://raw.githubusercontent.com/madob-maker/Turno-TV/main/logo.png", width=120)
st.title("Turno TV")

# Lógica de participantes
participantes = ["Adri", "Nata", "Papá", "Mamá"]
fecha_base = date(2026, 4, 29)
fecha_consulta = st.date_input("Consultar fecha:", date.today())

if st.button("VER QUIÉN MANDA HOY"):
    delta = fecha_consulta - fecha_base
    dias = delta.days
    
    if dias < 0:
        st.warning("El ciclo comienza el 29/04/2026.")
    else:
        ganador = participantes[dias % 4]
        st.markdown(f"""
            <div class="caja-resultado">
                <p style="color: #8d5524; margin-bottom: 0;">Hoy le toca a:</p>
                <h1 style="color: #5d3a1a; font-size: 50px; margin-top: 0;">{ganador}</h1>
            </div>
        """, unsafe_allow_html=True)

st.info("Orden: Adri ➔ Nata ➔ Papá ➔ Mamá")
