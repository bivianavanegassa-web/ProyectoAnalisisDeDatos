
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
