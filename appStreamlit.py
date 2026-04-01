import streamlit as st
import pandas as pd
import plotly.express as px
from pandasql import sqldf

"""
Dataframes para cada una de las tablas
"""

#Dataframe para facturacion.csv
df_facturacion= pd.read_csv("Data/Facturacion.csv", sep=';', encoding='latin1')

#Dataframe para pedidos.csv
df_pedidos = pd.read_csv("Data/Pedidos.csv", sep=';', encoding='latin1')

#Dataframe para proveedor.csv
df_proveedor = pd.read_csv("Data/Proveedor.csv", sep=';', encoding='latin1')

# Convertir fechas a datetime
df_facturacion['fecha_factura'] = pd.to_datetime(df_facturacion['fecha_factura'])

#Ejecutamos sql
pysqldf = lambda q: sqldf(q, globals())

# Nuevos DataFrames basados en las consultas SQL proporcionadas

# Top 5 de productos más pedidos según la cantidad total
df_top5_productos_mas_pedidos_cantidad = (
    df_pedidos.groupby('Producto')['cantidad']
    .sum()
    .reset_index()
    .rename(columns={'cantidad': 'total_cantidad'})
    .sort_values('total_cantidad', ascending=False)
    .head(5)
)

# Top 5 productos menos pedidos según cantidad
df_top5_productos_menos_pedidos_cantidad = (
    df_pedidos.groupby('Producto')['cantidad']
    .sum()
    .reset_index()
    .rename(columns={'cantidad': 'total_cantidad'})
    .sort_values('total_cantidad', ascending=True)
    .head(5)
)

# Top 5 productos más pedidos según valor total facturado
df_top5_productos_mas_pedidos_valor = (
    df_pedidos.groupby('Producto')['Total pedido']
    .sum()
    .reset_index()
    .rename(columns={'Total pedido': 'total_facturado'})
    .sort_values('total_facturado', ascending=False)
    .head(3)
)

# Top 5 productos menos pedidos según valor total facturado
df_top5_productos_menos_pedidos_valor = (
    df_pedidos.groupby('Producto')['Total pedido']
    .sum()
    .reset_index()
    .rename(columns={'Total pedido': 'total_facturado'})
    .sort_values('total_facturado', ascending=True)
    .head(3)
)

# Top 5 proveedores con más facturaciones
df_top5_proveedores_mas_facturaciones = (
    df_facturacion.groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturaciones'})
    .sort_values('total_facturaciones', ascending=False)
    .head(5)
)

# Proveedores con menos facturaciones
df_top5_proveedores_menos_facturaciones = (
    df_facturacion.groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturaciones'})
    .sort_values('total_facturaciones', ascending=True)
    .head(3)
)

# Top 5 proveedores con más valor total facturado
df_top5_proveedores_mas_valor_facturado = (
    df_facturacion.groupby('nombre_proveedor')['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_facturado'})
    .sort_values('total_facturado', ascending=False)
    .head(5)
)

# Top 5 proveedores con menos valor total facturado
df_top5_proveedores_menos_valor_facturado = (
    df_facturacion.groupby('nombre_proveedor')['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_facturado'})
    .sort_values('total_facturado', ascending=True)
    .head(3)
)

# Facturas pendientes de pago en cada año
df_facturas_pendientes_por_anio = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby(df_facturacion['fecha_factura'].dt.year)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'facturas_pendientes', 'fecha_factura': 'anio'})
    .sort_values('anio')
)

# Total a pagar en cada año por facturas no pagadas
df_total_pendiente_por_anio = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby(df_facturacion['fecha_factura'].dt.year)['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_pendiente', 'fecha_factura': 'anio'})
    .sort_values('anio')
)

# Frecuencia de tipo de facturas
df_frecuencia_tipo_factura = (
    df_facturacion.groupby('tipo_factura')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'cantidad'})
)

# Mes en el año 2022 donde más se efectúan facturas
df_mes_mas_facturas_2022 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2022]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2023 donde más se efectúan facturas
df_mes_mas_facturas_2023 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2023]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2024 donde más se efectúan facturas
df_mes_mas_facturas_2024 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2024]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2025 donde más se efectúan facturas
df_mes_mas_facturas_2025 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2025]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Responsable con más facturas pendientes de pago
df_responsable_mas_pendientes = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby('responsable')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_pendientes'})
    .sort_values('total_pendientes', ascending=False)
)

# Facturas pendientes por proveedor
df_facturas_pendientes_por_proveedor = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'facturas_pendientes'})
    .sort_values('facturas_pendientes', ascending=False)
)

# Consultas adicionales: totales únicos y generales

# Total de proveedores únicos
total_proveedores_unicos = df_facturacion['nombre_proveedor'].nunique()

# Total de facturaciones
total_facturaciones = len(df_facturacion)

# Total de valor facturado
total_valor_facturado = df_facturacion['valor_total $'].sum()

# Total de productos únicos
total_productos_unicos = df_pedidos['Producto'].nunique()

# Para consistencia, crear DataFrames con estos totales
df_totales_generales = pd.DataFrame({
    'metrica': ['Total Proveedores Únicos', 'Total Facturaciones', 'Total Valor Facturado', 'Total Productos Únicos'],
    'valor': [total_proveedores_unicos, total_facturaciones, total_valor_facturado, total_productos_unicos]
})

# Estilo de la pagina
st.set_page_config(
    page_title="Dashboard Facturación",
    layout="wide"
)

# CSS personalizado con colores púrpura, azul y naranja
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<style>
.metric-card {
    background-color: #f0f0f0;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    font-family: 'Inter', sans-serif;
    border-left: 5px solid #6a0dad; /* Púrpura */
}

.metric-title {
    color: #333;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    color: #1f77b4; /* Azul */
    font-size: 32px;
    font-weight: 700;
}

.sidebar-button {
    background-color: #6a0dad; /* Púrpura */
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    margin: 5px;
    width: 100%;
}

.sub-button {
    background-color: #ff7f0e; /* Naranja */
    color: white;
    border: none;
    padding: 8px;
    border-radius: 5px;
    margin: 5px;
}

.chart-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Navegación con sidebar
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Productos", "Proveedores", "Facturas pendientes", "Facturas", "Copiloto"])

# Función para mostrar métricas generales
def mostrar_metricas_generales():
    st.header("Dashboards Informacionales")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Proveedores Únicos</div>
            <div class="metric-value">{total_proveedores_unicos}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Facturaciones</div>
            <div class="metric-value">{total_facturaciones}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Valor Facturado</div>
            <div class="metric-value">${total_valor_facturado:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Productos Únicos</div>
            <div class="metric-value">{total_productos_unicos}</div>
        </div>
        """, unsafe_allow_html=True)

# Escala de salud de la empresa
def mostrar_escala_salud():
    total_pendiente = df_total_pendiente_por_anio['total_pendiente'].sum()
    salud_porcentaje = max(0, (total_valor_facturado - total_pendiente) / total_valor_facturado * 100)
    st.subheader("Escala de Salud de la Empresa")
    fig = px.bar(x=['Salud Financiera'], y=[salud_porcentaje], color_discrete_sequence=['#1f77b4'])
    fig.update_layout(yaxis_range=[0, 100], title="Porcentaje de Salud (Valor Facturado - Pendiente)")
    st.plotly_chart(fig)

# Mostrar métricas y salud en todas las páginas
mostrar_metricas_generales()
mostrar_escala_salud()

# Contenido basado en la opción seleccionada
if opcion == "Productos":
    st.header("Análisis de Productos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 5 Productos Más Pedidos (Cantidad)")
        fig = px.bar(df_top5_productos_mas_pedidos_cantidad, x='Producto', y='total_cantidad', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Top 5 Productos Menos Pedidos (Cantidad)")
        fig = px.bar(df_top5_productos_menos_pedidos_cantidad, x='Producto', y='total_cantidad', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top 5 Productos Más Pedidos (Valor)")
        fig = px.bar(df_top5_productos_mas_pedidos_valor, x='Producto', y='total_facturado', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with col4:
        st.subheader("Top 5 Productos Menos Pedidos (Valor)")
        fig = px.bar(df_top5_productos_menos_pedidos_valor, x='Producto', y='total_facturado', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)

elif opcion == "Proveedores":
    st.header("Análisis de Proveedores")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 5 Proveedores con Más Facturaciones")
        fig = px.bar(df_top5_proveedores_mas_facturaciones, x='nombre_proveedor', y='total_facturaciones', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Top 5 Proveedores con Menos Facturaciones")
        fig = px.bar(df_top5_proveedores_menos_facturaciones, x='nombre_proveedor', y='total_facturaciones', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top 5 Proveedores con Más Valor Facturado")
        fig = px.bar(df_top5_proveedores_mas_valor_facturado, x='nombre_proveedor', y='total_facturado', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with col4:
        st.subheader("Top 5 Proveedores con Menos Valor Facturado")
        fig = px.bar(df_top5_proveedores_menos_valor_facturado, x='nombre_proveedor', y='total_facturado', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)

elif opcion == "Facturas pendientes":
    st.header("Análisis de Facturas Pendientes")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Facturas Pendientes por Año")
        fig = px.bar(df_facturas_pendientes_por_anio, x='anio', y='facturas_pendientes', color='anio', color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Total Pendiente por Año")
        st.dataframe(df_total_pendiente_por_anio)
    st.subheader("Responsables con Más Facturas Pendientes")
    fig = px.bar(df_responsable_mas_pendientes, x='responsable', y='total_pendientes', color='responsable', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig)
    st.subheader("Proveedores con Más Facturas Pendientes")
    fig = px.bar(df_facturas_pendientes_por_proveedor, x='nombre_proveedor', y='facturas_pendientes', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig)

elif opcion == "Facturas":
    st.header("Análisis de Facturas por Año")
    anio_seleccionado = st.selectbox("Selecciona un año:", [2022, 2023, 2024, 2025])
    if anio_seleccionado == 2022:
        df_mes = df_mes_mas_facturas_2022
    elif anio_seleccionado == 2023:
        df_mes = df_mes_mas_facturas_2023
    elif anio_seleccionado == 2024:
        df_mes = df_mes_mas_facturas_2024
    elif anio_seleccionado == 2025:
        df_mes = df_mes_mas_facturas_2025
    st.subheader(f"Facturas por Mes en {anio_seleccionado}")
    fig = px.bar(df_mes, x='mes', y='total_facturas', color='mes', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig)

elif opcion == "Copiloto":
    st.header("Copiloto - Próximamente")

else:
    st.header("🏢 Bienvenido al Dashboard de Facturación Interactivo")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #6a0dad, #1f77b4); color: white; padding: 30px; border-radius: 15px; text-align: center; font-family: 'Inter', sans-serif; box-shadow: 0px 4px 15px rgba(0,0,0,0.3);">
        <h2 style="color: #ff7f0e; margin-bottom: 20px;">Descubre Insights Poderosos para tu Empresa</h2>
        <p style="font-size: 18px; line-height: 1.6;">
            Explora análisis detallados de <strong>productos</strong>, <strong>proveedores</strong> y <strong>facturaciones</strong> con gráficos interactivos que te permiten identificar tendencias, optimizar procesos y tomar decisiones estratégicas. 
            Monitorea facturas pendientes, evalúa la salud financiera de tu empresa y accede a métricas clave en tiempo real. 
            ¡Transforma datos en oportunidades de crecimiento!
        </p>
        <p style="font-size: 16px; margin-top: 20px;">
            <em>Desarrollado por: Maria Alejandra Florez, Biviana Andrea Vanegas Salazar, Jose Andres Diaz Gutierrez, Paula Andrea Fernandez Castaño</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("Selecciona una opción del menú lateral para explorar los datos.")

