import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# --- ENLACE DIRECTO AL LOGO ---
# Usamos el enlace "raw" para que el móvil lo encuentre siempre
URL_LOGO = "https://raw.githubusercontent.com/madob-maker/Turno-TV/main/logo.png"

# Configuración de la página
st.set_page_config(
    page_title="Turno TV",
    page_icon=URL_LOGO,
    layout="centered"
)

# --- INYECCIÓN PARA FORZAR EL ICONO Y EL MANIFEST ---
# Hemos subido la versión a v=8 para obligar al móvil a refrescar el icono
components.html(
    f"""
    <script>
        const link = parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = './manifest.json?v=8';
        parent.document.head.appendChild(link);
        
        const icon = parent.document.createElement('link');
        icon.rel = 'icon';
        icon.href = '{URL_LOGO}';
        parent.document.head.appendChild(icon);
    </script>
    """,
    height=0,
)

# --- ESTILO VISUAL (Colores del logo) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fffaf5;
    }
    .stButton>button {
        background-color: #ff9d42;
        color: white;
        border-radius: 12px;
        border: none;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 18px;
    }
    .resultado-caja {
        background-color: #ffe0b2;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #ff9d42;
        margin: 20px 0px;
    }
    .nombre-ganador {
        font-size: 45px;
        color: #5d3a1a;
        font-weight: bold;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
st.image(URL_LOGO, width=120)
st.title("Turno TV")
st.write("Gestiona quién manda hoy en el salón")

# Configuración de los participantes
participantes = ["Adri", "Nata", "Papá", "Mamá"]
fecha_base = date(2026, 4, 29)

# Selector de fecha (por defecto hoy)
fecha_consulta = st.date_input("Selecciona una fecha para consultar:", date.today())

if st.button("¿A QUIÉN LE TOCA?"):
    delta = fecha_consulta - fecha_base
    dias = delta.days
    
    if dias < 0:
        st.warning(f"El ciclo comenzó el {fecha_base.strftime('%d/%m/%Y')}. Por favor, elige una fecha posterior.")
    else:
        # Lógica de rotación (Módulo 4)
        indice = dias % 4
        ganador = participantes[indice]
        
        st.markdown(f"""
            <div class="resultado-caja">
                <span style="color: #8d5524; font-size: 20px;">Hoy el mando es de:</span><br>
                <span class="nombre-ganador">{ganador}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Información del orden
        st.info("Orden de turnos: Adri ➔ Nata ➔ Papá ➔ Mamá")

st.caption(f"Ciclo iniciado el {fecha_base.strftime('%d/%m/%Y')} con Adri.")
