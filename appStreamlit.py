import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import conexionMYSQL as cx

# conexión a MySQL
conexion =cx.conectar_mysql()

cursor = conexion.cursor()

#Estilo de la pagina
st.set_page_config(
    page_title="Dashboard Facturación",
    layout="wide"
)

# CSS personalizado 
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<style>
.metric-card {
    background-color: #161b22;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    font-family: 'Inter', sans-serif;
}

.metric-title {
    color: #8b949e;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    color: #58a6ff;
    font-size: 32px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

#Nos cercioramos de que la conexión se haya establecido correctamente
if conexion.is_connected():
    print("Conexión exitosa a MySQL")
else:
    print("No se pudo conectar")

#Ejecutamos consultas SQL para obtener los datos necesarios

# Consulta para proveedores de categoría Servicios Públicos
consulta_proveedores_servicios_publicos = "SELECT * FROM proveedores WHERE categoria = 'Servicios Publicos'"
df_proveedores_servicios = pd.read_sql(consulta_proveedores_servicios_publicos, conexion)

# Consulta para facturación unida con proveedores donde nombre_proveedor es ABM
consulta_facturacion_join_proveedores_abm = """
SELECT * FROM facturacion 
INNER JOIN proveedores ON facturacion.nit_proveedor = proveedores.nit_proveedor 
WHERE proveedores.nombre_proveedor = 'ABM'
"""
df_facturacion_abm = pd.read_sql(consulta_facturacion_join_proveedores_abm, conexion)

# Consulta para todos los pedidos
consulta_todos_pedidos = "SELECT * FROM pedidos"
df_todos_pedidos = pd.read_sql(consulta_todos_pedidos, conexion)

# Consulta para categorías distintas en pedidos
consulta_categorias_distintas_pedidos = "SELECT DISTINCT categoria FROM pedidos"
df_categorias_distintas = pd.read_sql(consulta_categorias_distintas_pedidos, conexion)

# Consulta para productos distintos en pedidos
consulta_productos_distintos_pedidos = "SELECT DISTINCT producto FROM pedidos"
df_productos_distintos = pd.read_sql(consulta_productos_distintos_pedidos, conexion)

# Consulta GROUP BY: conteo por categoría 
consulta_conteo_categoria = "SELECT categoria, COUNT(*) AS conteo_categoria FROM pedidos GROUP BY categoria"
df_conteo_categoria = pd.read_sql(consulta_conteo_categoria, conexion)

# Consulta GROUP BY: conteo por producto
consulta_conteo_producto = "SELECT producto, COUNT(*) AS conteo_producto FROM pedidos GROUP BY producto"
df_conteo_producto = pd.read_sql(consulta_conteo_producto, conexion)

# Consulta GROUP BY: suma valor_total por categoría en facturación
consulta_suma_valor_categoria_facturacion = "SELECT categoria, SUM(valor_total) AS suma_valor FROM facturacion GROUP BY categoria"
df_suma_valor_categoria = pd.read_sql(consulta_suma_valor_categoria_facturacion, conexion)

# Consulta GROUP BY: suma cantidad por producto en pedidos
consulta_suma_cantidad_producto = "SELECT producto, SUM(cantidad) AS suma_cantidad FROM pedidos GROUP BY producto"
df_suma_cantidad_producto = pd.read_sql(consulta_suma_cantidad_producto, conexion)

# Consulta GROUP BY: conteo por nombre_proveedor en pedidos
consulta_conteo_por_proveedor = "SELECT nombre_proveedor, COUNT(*) AS conteo FROM pedidos GROUP BY nombre_proveedor"
df_conteo_proveedor = pd.read_sql(consulta_conteo_por_proveedor, conexion)

# Subconsulta: Facturas por encima del valor promedio
consulta_facturas_sobre_promedio = """
SELECT numero_radicado, valor_total
FROM facturacion
WHERE valor_total > (SELECT AVG(valor_total) FROM facturacion)
"""
df_facturas_sobre_promedio = pd.read_sql(consulta_facturas_sobre_promedio, conexion)

# Subconsulta: Productos por encima del precio promedio
consulta_productos_sobre_promedio_precio = """
SELECT producto, precio
FROM pedidos
WHERE precio > (SELECT AVG(precio) FROM pedidos)
"""
df_productos_sobre_promedio = pd.read_sql(consulta_productos_sobre_promedio_precio, conexion)

# Consulta para total facturación usando función
consulta_total_facturacion = "SELECT total_facturacion() AS total_facturacion"
df_total_facturacion = pd.read_sql(consulta_total_facturacion, conexion)

# Consulta para promedio precios usando función
consulta_promedio_precios = "SELECT promedio_precios() AS promedio_precios"
df_promedio_precios = pd.read_sql(consulta_promedio_precios, conexion)

#Mostramos los datos en Streamlit
st.title("Facturación de la empresa en los últimos 4 años")

#Resumen de facturacion total y promedio de precios
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Total Facturación</div>
        <div class="metric-value">${df_total_facturacion['total_facturacion'][0]:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈 Promedio de Precios</div>
        <div class="metric-value">${df_promedio_precios['promedio_precios'][0]:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)


fig_categoria = px.pie(
    df_conteo_categoria,
    names="categoria",
    values="conteo_categoria",
    title="Distribución de pedidos por categoría",
    color_discrete_sequence=px.colors.sequential.Blues
)


fig_producto = px.bar(
    df_conteo_producto,
    x="producto",
    y="conteo_producto",
    title="Frecuencia de pedidos por producto",
    color="conteo_producto",
    color_continuous_scale="Blues"
)


#Valor total por categoría en facturación
fig_valor_categoria = px.bar(
    df_suma_valor_categoria,
    x="categoria",
    y="suma_valor",
    title="Valor total por categoría",
    color="suma_valor",
    color_continuous_scale="Teal"
)
#cantidad en los productos
st.plotly_chart(fig_valor_categoria, use_container_width=True)

fig_cantidad = px.bar(
    df_suma_cantidad_producto,
    x="producto",
    y="suma_cantidad",
    title="Cantidad total por producto",
    color="suma_cantidad",
    color_continuous_scale="IceFire"
)
#conteo por proveedor
st.plotly_chart(fig_cantidad, use_container_width=True)

fig_proveedor = px.bar(
    df_conteo_proveedor,
    x="nombre_proveedor",
    y="conteo",
    title="Pedidos por proveedor",
    color="conteo",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_proveedor, use_container_width=True)

#Organizacion tipo Dashboard
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_categoria, use_container_width=True)

with col2:
    st.plotly_chart(fig_producto, use_container_width=True)