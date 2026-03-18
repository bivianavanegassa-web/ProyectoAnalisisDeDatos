import streamlit as st
import mysql.connector
import pandas as pd

# conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseñaDeMYSQL",
    database="proyectoanalisisdedatos"
)

cursor = conexion.cursor()

#Nos cercioramos de que la conexión se haya establecido correctamente
if conexion.is_connected():
    print("Conexión exitosa a MySQL")
else:
    print("No se pudo conectar")

# Crear funciones si no existen
cursor.execute("""
DROP FUNCTION IF EXISTS total_facturacion;
CREATE FUNCTION total_facturacion()
RETURNS DECIMAL(15,2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(15,2);
    SELECT SUM(valor_total)
    INTO total
    FROM facturacion;
    RETURN total;
END
""")

cursor.execute("""
DROP FUNCTION IF EXISTS promedio_precios;
CREATE FUNCTION promedio_precios()
RETURNS DECIMAL(15,2)
DETERMINISTIC
BEGIN
    DECLARE promedio_de_precios DECIMAL(15,2);
    SELECT AVG(precio)
    INTO promedio_de_precios
    FROM pedidos;
    RETURN promedio_de_precios;
END
""")

"""
Ejecutamos las consultas SQL
"""

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

# Consulta GROUP BY: conteo por categoría y producto
consulta_conteo_categoria_producto = "SELECT categoria, producto, COUNT(*) AS conteo FROM pedidos GROUP BY categoria, producto"
df_conteo_categoria_producto = pd.read_sql(consulta_conteo_categoria_producto, conexion)

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
st.title("Dashboard de Análisis de Datos")

st.subheader("Proveedores de Categoría Servicios Públicos")
st.dataframe(df_proveedores_servicios)

st.subheader("Facturación Unida con Proveedores (ABM)")
st.dataframe(df_facturacion_abm)

st.subheader("Todos los Pedidos")
st.dataframe(df_todos_pedidos)

st.subheader("Categorías Distintas en Pedidos")
st.dataframe(df_categorias_distintas)

st.subheader("Productos Distintos en Pedidos")
st.dataframe(df_productos_distintos)

st.subheader("Conteo por Categoría y Producto")
st.dataframe(df_conteo_categoria_producto)

st.subheader("Suma Valor Total por Categoría en Facturación")
st.dataframe(df_suma_valor_categoria)

st.subheader("Suma Cantidad por Producto en Pedidos")
st.dataframe(df_suma_cantidad_producto)

st.subheader("Conteo por Proveedor en Pedidos")
st.dataframe(df_conteo_proveedor)

st.subheader("Facturas por Encima del Valor Promedio")
st.dataframe(df_facturas_sobre_promedio)

st.subheader("Productos por Encima del Precio Promedio")
st.dataframe(df_productos_sobre_promedio)

st.subheader("Total Facturación")
st.write(f"Total: {df_total_facturacion.iloc[0,0]}")

st.subheader("Promedio de Precios")
st.write(f"Promedio: {df_promedio_precios.iloc[0,0]}")


