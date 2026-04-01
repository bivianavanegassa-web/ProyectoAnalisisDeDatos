
-- Limpieza de valores en los atributos de la tabla facturacion, para la correcta lectura de las tildes
UPDATE facturacion set categoria = REPLACE(categoria,'EnergÃ­a','Energia') WHERE numero_radicado LIKE 'NT%';
UPDATE facturacion set categoria = REPLACE(categoria,'AlimentaciÃ³n','Alimentacion') WHERE numero_radicado LIKE 'NT%';
UPDATE facturacion set categoria = REPLACE(categoria,'ConsultorÃ­a','Consultoria') WHERE numero_radicado LIKE 'NT%';
UPDATE facturacion set categoria = REPLACE(categoria,'Servicios PÃºblicos','Servicios Publicos') WHERE numero_radicado LIKE 'NT%';

-- Limpieza de valores en los atributos de la tabla proveedores, para la correcta lectura de las tildes
UPDATE proveedores set categoria = REPLACE(categoria,'Energía','Energia') WHERE nit_proveedor LIKE 'NIT%';
UPDATE proveedores set categoria = REPLACE(categoria,'Alimentación','Alimentacion') WHERE nit_proveedor LIKE 'NIT%';
UPDATE proveedores set categoria = REPLACE(categoria,'ConsultorÃ­a','Consultoria') WHERE nit_proveedor LIKE 'NIT%';

-- Limpieza de valores en los atributos de la tabla pedidos, para la correcta lectura de las tildes
UPDATE pedidos set categoria = REPLACE(categoria,'Energï¿½a','Energia') WHERE numero_pedido LIKE 'PED%';
UPDATE pedidos set categoria = REPLACE(categoria,'Alimentaciï¿½n','Alimentacion') WHERE numero_pedido LIKE 'PED%';
UPDATE pedidos set categoria = REPLACE(categoria,'Consultorï¿½a','Consultoria') WHERE numero_pedido LIKE 'PED%';
UPDATE pedidos set categoria = REPLACE(categoria,'Servicios Pï¿½blicos','Servicios Publicos') WHERE numero_pedido LIKE 'PED%';

UPDATE pedidos set producto = REPLACE(producto,'ï¿½a','ia') WHERE numero_pedido LIKE 'PED%';
UPDATE pedidos set producto = REPLACE(producto,'ï¿½n','on') WHERE numero_pedido LIKE 'PED%';
UPDATE pedidos set producto = REPLACE(producto,'ï¿½','e') WHERE numero_pedido LIKE 'PED%';



-- Realizamos consultas

-- Para ver solo aquellos datos en los que aparece informacion de la categoria: Servicios Publicos
SELECT * from proveedores WHERE categoria = "Servicios Publicos";
-- Para ver al mismo tiempo la tabla de facturacion y de proveedores
SELECT * from facturacion inner JOIN proveedores on facturacion.nit_proveedor  = proveedores.nit_proveedor WHERE proveedores.nombre_proveedor = "ABM";
-- Para ver la tabla de pedidos
select * from pedidos;

-- Para consultar los tipos de categorias sin repetir en la tabla de pedidos
SELECT DISTINCT categoria FROM pedidos;
-- Para consultar los tipos de producto sin repetir en la tabla de pedidos
SELECT DISTINCT producto FROM pedidos;


-- Consultas tipo GROUP BY
SELECT categoria, producto, COUNT(*) FROM pedidos GROUP BY categoria, producto;
SELECT categoria, SUM(valor_total) FROM facturacion GROUP BY categoria;
SELECT producto, SUM(cantidad) FROM pedidos GROUP BY producto;
SELECT nombre_proveedor, COUNT(*) FROM pedidos GROUP BY nombre_proveedor;

-- Top 5 de productos más pedidos segun la cantidad total
-- Tener en cuenta solo uno y poder hacer análisis para esto 
SELECT producto, SUM(cantidad) AS total_cantidad
FROM pedidos
GROUP BY producto
ORDER BY total_cantidad DESC
LIMIT 5;

-- Top 5 productos menos pedidos
-- Tener en cuenta solo uno y poder hacer análisis para esto 
SELECT producto, SUM(cantidad) AS total_cantidad
FROM pedidos
GROUP BY producto
ORDER BY total_cantidad ASC
LIMIT 5;

-- Consulta para obtener el top 5 de productos más pedidos segun el valor total facturado
SELECT producto, SUM(total_pedido) AS total_facturado
FROM pedidos
GROUP BY producto
ORDER BY total_facturado DESC
LIMIT 3;

-- Consulta para obtener el top 5 de productos menos pedidos segun el valor total facturado
SELECT producto, SUM(total_pedido) AS total_facturado
FROM pedidos
GROUP BY producto
ORDER BY total_facturado ASC
LIMIT 3;

-- Top 5 de proveedores con más facturaciones
-- Conclusion imortante sobre el mejor proveedor, y mejorar relaciones comerciales con él
SELECT nombre_proveedor, COUNT(*) AS total_facturaciones
FROM facturacion
GROUP BY nombre_proveedor
ORDER BY total_facturaciones DESC
LIMIT 5;

-- Consulta para saber cuáles son los proveedores con menos facturaciones
SELECT nombre_proveedor, COUNT(*) AS total_facturaciones
FROM facturacion
GROUP BY nombre_proveedor
ORDER BY total_facturaciones ASC
LIMIT 3;

-- Top 5 de proveedores con más valor total facturado
SELECT nombre_proveedor, SUM(valor_total) AS total_facturado
FROM facturacion
GROUP BY nombre_proveedor
ORDER BY total_facturado DESC
LIMIT 5;

-- Top 5 de proveedores con menos valor total facturado
SELECT nombre_proveedor, SUM(valor_total) AS total_facturado
FROM facturacion
GROUP BY nombre_proveedor
ORDER BY total_facturado ASC
LIMIT 3;

-- Facturas pendientes de pago en cada año
SELECT 
    EXTRACT(YEAR FROM fecha_factura) AS anio,
    COUNT(*) AS facturas_pendientes
FROM facturacion
WHERE estado_factura = 'Pendiente'
GROUP BY anio
ORDER BY anio;

-- Total a pagar en cada año por facturas que no se han pagado
-- Analizar si la empresa esta en riesgo tributario, demandas por el proveedor, etc.
SELECT 
    EXTRACT(YEAR FROM fecha_factura) AS anio,
    SUM(valor_total) AS total_pendiente
FROM facturacion
WHERE estado_factura = 'Pendiente'
GROUP BY anio
ORDER BY anio;

-- Frecuencia de tipo de facturas electronica/fisica
SELECT 
    tipo_factura,
    COUNT(*) AS cantidad
FROM facturacion
GROUP BY tipo_factura;

-- Mes en el año 2022 donde mas se efectuan facturas
SELECT MONTH(fecha_factura) AS mes, COUNT(*) AS total_facturas
FROM facturacion
WHERE YEAR(fecha_factura) = 2022
GROUP BY mes
ORDER BY total_facturas DESC;

-- Mes en el año 2023 donde mas se efectuan facturas
SELECT MONTH(fecha_factura) AS mes, COUNT(*) AS total_facturas
FROM facturacion
WHERE YEAR(fecha_factura) = 2023
GROUP BY mes
ORDER BY total_facturas DESC;

-- Mes en el año 2024 donde mas se efectuan facturas
SELECT MONTH(fecha_factura) AS mes, COUNT(*) AS total_facturas
FROM facturacion
WHERE YEAR(fecha_factura) = 2024
GROUP BY mes
ORDER BY total_facturas DESC;

-- Mes en el año 2025 donde mas se efectuan facturas
SELECT MONTH(fecha_factura) AS mes, COUNT(*) AS total_facturas
FROM facturacion
WHERE YEAR(fecha_factura) = 2025
GROUP BY mes
ORDER BY total_facturas DESC;

-- Responsable que quedo con mas facturas pendientes de pago
-- Sensibilizar, capacitar y mejorar procesos con el responsable que tiene mas facturas pendientes de pago, para evitar riesgos financieros, tributarios, etc.
-- A tener en cuenta en el cierre del año

SELECT responsable, COUNT(*) AS total_pendientes
FROM facturacion
WHERE estado_factura = 'Pendiente'
GROUP BY responsable
ORDER BY total_pendientes DESC;    





-- Subconsultas

-- Facturas que están por encima del valor promedio
SELECT numero_radicado, valor_total
FROM facturacion
WHERE valor_total >
      (SELECT AVG(valor_total) FROM facturacion);
	
-- Productos que estan por encima del valor promedio
SELECT producto, precio
FROM pedidos
WHERE precio >
      (SELECT AVG(precio) FROM pedidos);

-- Consultas para informacion general

-- Funciones
-- Funcion para calcular el valor total que se pago por todas las facturaciones
DELIMITER //
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

END //
-- Funcion para calcular el promedio de los precios de los productos
DELIMITER //
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

END //

-- Ejecutamos las funciones
select total_facturacion ();
select promedio_precios ();
