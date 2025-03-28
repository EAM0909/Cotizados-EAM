
import streamlit as st

st.set_page_config(page_title="Cotizador de Etiquetas", layout="centered")
st.title("Cotizador de Etiquetas Flexográficas")

st.markdown("Ingresa los datos de la etiqueta para obtener el precio estimado.")

# Entradas del usuario
ancho = st.number_input("Ancho (cm)", min_value=1.0, value=10.0)
alto = st.number_input("Alto (cm)", min_value=1.0, value=10.0)
material = st.selectbox("Material", ["papel couché", "bopp blanco", "poliéster plata", "papel termal transfer"])
impresion = st.selectbox("Impresión", ["1x0", "2x0", "3x0", "4x0"])
acabado = st.selectbox("Acabado", ["laminado brillante", "laminado mate", "laminado", "sin acabado"])
cantidad = st.number_input("Cantidad de etiquetas", min_value=1, value=5000, step=100)

# Datos base
precio_arranque = 3000
margen = 0.30
costo_tinta_por_tinta = 0.00001785

# Costos por cm2
costo_material_cm2 = {
    "papel couché": 0.0013,
    "bopp blanco": 0.0018,
    "poliéster plata": 0.040,
    "papel termal transfer": 0.0015
}

costo_acabado_cm2 = {
    "laminado brillante": 0.0010,
    "laminado mate": 0.0020,
    "laminado": 0.0010,
    "sin acabado": 0.0
}

# Cálculo
num_tintas = int(impresion[0])
desperdicio_factor = 1.3 + (0.075 * num_tintas)
area_cm2 = ancho * alto * desperdicio_factor

costo_material = area_cm2 * costo_material_cm2[material]
costo_acabado = area_cm2 * costo_acabado_cm2[acabado]
costo_tinta = costo_tinta_por_tinta * num_tintas

costo_unitario_sin_margen = costo_material + costo_acabado + costo_tinta

if cantidad < 5000:
    costo_total = (costo_unitario_sin_margen * cantidad) + precio_arranque
else:
    costo_total = costo_unitario_sin_margen * cantidad

costo_total_con_margen = costo_total * (1 + margen)
precio_unitario_final = costo_total_con_margen / cantidad

# Resultados
st.markdown("---")
st.subheader(f"Precio unitario estimado: ${precio_unitario_final:.4f} MXN")
st.subheader(f"Precio total estimado: ${costo_total_con_margen:,.2f} MXN")
