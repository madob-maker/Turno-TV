import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# URL directa de tu logo en GitHub
URL_LOGO = "https://raw.githubusercontent.com/madob-maker/Turno-TV/main/logo.png"

# Configuración de la página
st.set_page_config(
    page_title="Turno TV",
    page_icon=URL_LOGO,
    layout="centered"
)

# --- INYECCIÓN PARA FORZAR EL ICONO Y EL MANIFEST ---
# Subimos a v=10 para asegurar que el móvil detecte el cambio de estilo
components.html(
    f"""
    <script>
        const link = parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = './manifest.json?v=10';
        parent.document.head.appendChild(link);
        
        const icon = parent.document.createElement('link');
        icon.rel = 'icon';
        icon.href = '{URL_LOGO}';
        parent.document.head.appendChild(icon);
    </script>
    """,
    height=0,
)

# --- ESTILO VISUAL MODO OSCURO ---
st.markdown("""
    <style>
    /* Fondo principal oscuro */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Textos principales en blanco/gris claro */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }

    /* Botón naranja vibrante */
    .stButton>button {
        background-color: #ff9d42;
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0px 4px 10px rgba(255, 157, 66, 0.3);
    }
    
    .stButton>button:hover {
        background-color: #ffb36b;
        color: white !important;
    }

    /* Caja de resultado en tono oscuro contrastado */
    .resultado-caja {
        background-color: #1d2129;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #ff9d42;
        margin: 20px 0px;
    }

    /* Nombre del ganador en naranja para que resalte mucho */
    .nombre-ganador {
        font-size: 50px;
        color: #ff9d42;
        font-weight: bold;
        display: block;
        text-shadow: 0px 0px 15px rgba(255, 157, 66, 0.2);
    }

    /* Estilo para el selector de fecha */
    div[data-baseweb="input"] {
        background-color: #262730;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
st.image(URL_LOGO, width=120)
st.title("Turno TV")
st.write("Gestiona quién manda hoy en el salón")

# Configuración de los participantes
# A = Adri, N = Nata, M = Papá, MB = Mamá
participantes = ["Adri", "Nata", "Papá", "Mamá"]
fecha_base = date(2026, 4, 29)

# Selector de fecha (con color adaptado por el CSS)
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
                <span style="color: #cccccc; font-size: 20px;">Hoy el mando es de:</span><br>
                <span class="nombre-ganador">{ganador}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Información del orden
        st.info("Orden de turnos: Adri ➔ Nata ➔ Papá ➔ Mamá")

st.caption(f"Ciclo iniciado el {fecha_base.strftime('%d/%m/%Y')} con Adri.")
