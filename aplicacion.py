<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Medallón Espiritual Sello de Salomón — Botánica USA</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<!-- Importación de SweetAlert2 para la alerta estética de error -->
<script src="jsdelivr.net"></script>
<style>
  :root {
    --black: #0f0f0f;
    --gray: #6b6b6b;
    --gray-light: #c8c8c8;
    --border: #e8e8e8;
    --bg: #ffffff;
    --bg2: #f9f8f6;
    --bg3: #f3f1ee;
    --accent: #8b6914;
    --accent-light: #c4963a;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { background: var(--bg); color: var(--black); font-family: 'Montserrat', sans-serif; overflow-x: hidden; }

  /* NAV */
  nav {
    position: fixed; top: 0; width: 100%; z-index: 999;
    background: rgba(255,255,255,0.97); backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    padding: 0 60px; height: 64px;
    display: flex; align-items: center; justify-content: space-between;
  }
  .nav-logo { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-weight: 600; color: var(--black); letter-spacing: 2px; text-transform: uppercase; text-decoration: none; }
  .nav-logo span { color: var(--accent); }
  .nav-back { font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: var(--gray); text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 6px; transition: color 0.2s; }
  .nav-back:hover { color: var(--black); }

  /* BREADCRUMB */
  .breadcrumb { padding: 88px 60px 0; display: flex; gap: 8px; align-items: center; }
  .breadcrumb span { font-size: 0.65rem; letter-spacing: 1px; color: var(--gray); text-transform: uppercase; }
  .breadcrumb .sep { color: var(--gray-light); }
  .breadcrumb .current { color: var(--black); font-weight: 500; }

  /* PRODUCT LAYOUT */
  .product-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    padding: 32px 60px 80px;
    max-width: 1200px;
    margin: 0 auto;
  }
  @media (max-width: 768px) {
    .product-layout { grid-template-columns: 1fr; gap: 40px; padding: 20px; }
    nav { padding: 0 20px; }
    .breadcrumb { padding: 88px 20px 0; }
  }

  /* GALLERY */
  .gallery { position: sticky; top: 80px; }
  .main-img-wrap {
    width: 100%;
    aspect-ratio: 1/1;
    overflow: hidden;
    background: var(--bg3);
    border: 1px solid var(--border);
    position: relative;
    cursor: zoom-in;
  }
  .main-img-wrap img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
    display: block;
  }
  .main-img-wrap:hover img { transform: scale(1.08); }
  .img-badge {
    position: absolute; top: 16px; left: 16px;
    background: var(--black); color: white;
    padding: 5px 14px;
    font-size: 0.6rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 600;
  }
  .thumbnails {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-top: 12px;
  }
  .thumb {
    aspect-ratio: 1/1;
    overflow: hidden;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: border-color 0.2s;
    background: var(--bg3);
  }
  .thumb.active { border-color: var(--black); }
  .thumb:hover { border-color: var(--gray); }
  .thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }

  /* PRODUCT INFO */
  .product-info { padding-top: 8px; }
  .product-brand {
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--accent); font-weight: 600; margin-bottom: 10px;
  }
  .product-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.8rem, 3vw, 2.6rem);
    font-weight: 400; line-height: 1.1;
    color: var(--black); margin-bottom: 6px;
  }
  .product-subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem; font-style: italic;
    color: var(--gray); margin-bottom: 20px; font-weight: 300;
  }
  .rating-row {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 24px; padding-bottom: 24px;
    border-bottom: 1px solid var(--border);
  }
  .stars { color: var(--accent); font-size: 0.75rem; letter-spacing: 2px; }
  .rating-count { font-size: 0.75rem; color: var(--gray); }
  .price-row { display: flex; align-items: baseline; gap: 12px; margin-bottom: 8px; }
  .price-main { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 600; color: var(--black); }
  .price-old { font-size: 1rem; color: var(--gray-light); text-decoration: line-through; }
  .price-save { font-size: 0.7rem; font-weight: 600; color: #2d7a2d; letter-spacing: 1px; text-transform: uppercase; }
  .shipping-note { font-size: 0.75rem; color: var(--gray); margin-bottom: 28px; font-weight: 300; }
  .shipping-note strong { color: var(--black); font-weight: 600; }

  /* SPECS */
  .specs-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 28px; }
  .spec-item { background: var(--bg2); border: 1px solid var(--border); padding: 14px 16px; }
  .spec-label { font-size: 0.6rem; letter-spacing: 2px; text-transform: uppercase; color: var(--gray); font-weight: 600; margin-bottom: 4px; }
  .spec-value { font-size: 0.85rem; font-weight: 500; color: var(--black); }

  /* QUANTITY */
  .section-mini-label { font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: var(--black); font-weight: 600; margin-bottom: 10px; }
  .qty-row { display: flex; align-items: center; gap: 0; margin-bottom: 16px; width: fit-content; border: 1px solid var(--border); }
  .qty-btn { width: 44px; height: 44px; background: none; border: none; font-size: 1.2rem; cursor: pointer; color: var(--black); display: flex; align-items: center; justify-content: center; }
  .qty-btn:hover { background: var(--bg2); }
  .qty-num { width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 600; border-left: 1px solid var(--border); border-right: 1px solid var(--border); }

  /* BUTTONS */
  .btn-add { width: 100%; padding: 18px; background: var(--black); color: white; border: none; font-family: 'Montserrat', 
