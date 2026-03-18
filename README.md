# Proyecto Análisis De Datos Integrador 
## Descripción

Este proyecto consiste en aplicar los conocimientos adquiridos durante el bootcamp de Talento Tech centrado en el análisis de datos aplicado en la recepción y radicación de facturas de proveedores.

## Justificación

Las empresas día a día reciben grandes volúmenes de facturas provenientes de diversos proveedores, esto limita la toma de decisiones oportunas basadas en la información de este volumen masivo de datos. En consecuencia, estos datos se tornan subutilizados y olvidados en el tiempo.

En este contexto, surge la necesidad de aplicar técnicas de análisis de datos que permitan transformar la información en conocimiento útil. Para ello, se emplean herramientas como MySQL para la gestión y consulta estructurada de los datos, Python para su procesamiento y análisis, y Streamlit para la visualización e interpretación interactiva de los resultados.

De esta manera, el proyecto busca facilitar la comprensión del comportamiento de la facturación en la empresa, aportando insumos clave para la optimización de recursos y la toma de decisiones estratégicas.

## Objetivo General

Analizar el comportamiento de las facturas en una empresa en los últimos 4 años

## Objetivos Específicos

* Depurar y estandarizar la información contenida en las tablas de facturación, proveedores y pedidos, corrigiendo inconsistencias de codificación y formato en variables como categoría y producto, con el fin de garantizar la calidad de los datos para su posterior análisis.

* Describir el comportamiento de las facturas de la empresa durante los últimos 3 años, mediante consultas de selección, agrupación y agregación sobre variables como categoría, valor total, cantidad de productos y proveedores, para identificar tendencias, frecuencias y distribución de los registros.

* Comparar los valores de facturación y precios registrados con sus respectivos promedios generales, utilizando subconsultas y funciones en SQL, con el propósito de detectar facturas y productos que presenten comportamientos superiores al promedio dentro del periodo analizado.

![Diagrama entidad-relación que muestra el proceso de recepción de facturación y pago a proveedores. En la parte superior, la entidad Proveedores se conecta a los atributos NIT_Proveedor, Nombre_proveedor, Ubicación y Categoría. Desde Proveedores fluye hacia el proceso Radicar, que se conecta a la entidad Facturación. La entidad Facturación contiene los atributos ID_Registro, NIT_Proveedor, Número_pedido, Fecha_ingresa en el lado izquierdo, y Categoría, Sociedad, Estado_factura, Tipo_factura en el lado derecho. Desde Facturación se continúa al proceso Detallar, que se conecta a la entidad Pedidos. La entidad Pedidos presenta los atributos Número_pedido, Producto, Cantidad y Valor. El diagrama utiliza símbolos de entidades en óvalos azules, procesos en rectángulos azules y conectores de líneas. La estructura general muestra el flujo de datos desde proveedores hasta los detalles de pedidos.](Data/Diagrama_MER.jpg)