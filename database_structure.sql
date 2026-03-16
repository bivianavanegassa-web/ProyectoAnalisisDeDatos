-- Script de creación de base de datos y tablas (a partir de los CSV de Proveedor/Pedidos/Facturación)

-- 1) Crear la base de datos
CREATE DATABASE IF NOT EXISTS ProyectoAnalisisDeDatos;

-- 2) Usar la base de datos
USE ProyectoAnalisisDeDatos;

-- 3) Crear tablas con llaves primarias y foráneas

-- Tabla de proveedores (se usa nit_proveedor como PK)
CREATE TABLE IF NOT EXISTS Proveedores (
  nit_proveedor VARCHAR(50) PRIMARY KEY,
  nombre_proveedor VARCHAR(150) NOT NULL,
  categoria VARCHAR(100) NOT NULL,
  ubicacion VARCHAR(150) NOT NULL
);

-- Tabla de pedidos (cada pedido apunta a un proveedor)
CREATE TABLE IF NOT EXISTS Pedidos (
  Numero_pedido VARCHAR(50) PRIMARY KEY,
  nit_proveedor VARCHAR(50) NOT NULL,
  nombre_proveedor VARCHAR(150) NOT NULL,
  categoria VARCHAR(100) NOT NULL,
  producto VARCHAR(150) NOT NULL,
  cantidad INT NOT NULL,
  precio DECIMAL(14,2) NOT NULL,
  total_pedido DECIMAL(16,2) NOT NULL,
  FOREIGN KEY (nit_proveedor) REFERENCES Proveedores(nit_proveedor)
);

-- Tabla de facturación (cada factura apunta a un proveedor y a un pedido)
CREATE TABLE IF NOT EXISTS Facturacion (
  fecha_de_registro DATE,
  numero_radicado VARCHAR(50) PRIMARY KEY,
  nit_proveedor VARCHAR(50) NOT NULL,
  nombre_proveedor VARCHAR(150) NOT NULL,
  moneda VARCHAR(10),
  fecha_factura DATE,
  numero_factura VARCHAR(50),
  pedido VARCHAR(50),
  valor_total DECIMAL(18,2),
  estado_factura VARCHAR(50),
  categoria VARCHAR(100),
  tipo_factura VARCHAR(50),
  responsable VARCHAR(100),
  FOREIGN KEY (nit_proveedor) REFERENCES Proveedores(nit_proveedor),
  FOREIGN KEY (pedido) REFERENCES Pedidos(Numero_pedido)
);

