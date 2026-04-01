import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from pandasql import sqldf

"""
Dataframes para cada una de las tablas
"""

#Dataframe para facturacion.csv
df_facturacion= pd.read_csv(r'Data\Facturacion.csv', sep=';')

#Dataframe para pedidos.csv
df_pedidos = pd.read_csv(r'Data\Pedidos.csv', sep=';')

#Dataframe para proveedor.csv
df_proveedor = pd.read_csv(r'Data\Proveedor.csv', sep=';')

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

