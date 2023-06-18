create database bdbigbreadsa;

use  bdbigbreadsa;

create table if not exists productos(
id_producto int primary key not null,
codigo_producto int,
criollitos varchar (45) not null,
pan_frences varchar (45) not null,
medialunas varchar (45) not null,
alfajores_de_maicena varchar(45) not null,
stock int,
precio double not null,
id_receta int not null,
FOREIGN KEY (id_recetas) REFERENCES recetas(id_recetas)
);

create table if not exists recetas(
id_recetas int primary key not null,
codigo_receta int,
nombre_producto varchar (45) not null,
cantidad_insumo int not null,
id_criollitos int not null,
harina int,
agua int,
sal int,
azucar int,
levadura int,
grasa int,
id_pan_frances int not null,
harina int,
agua int,
levadura int,
sal int,
aceite int,
id_medialunas int not null,
levadura int,
leche int,
harina int,
sal int,
azucar int,
huevo int,
manteca int,
esencia_de_vainilla int,
id_alfajor_de_maicena int not null,
manteca int,
azucar int,
huevo int,
harina int,
maicena int,
polvo_de_hornear int,
limon int,
coco_rayado int,
dulce_de_leche int,
id_insumos int not null
FOREIGN KEY (id_insumos) REFERENCES insumos(id_insumos)
);

create table if not exists insumos(
id_insumos int primary key not null,
codigo_insumo int,
harina int,
agua int,
levadura int,
sal int,
aceite int,
azucar int,
grasa int,
manteca int,
leche int,
huevo int,
esencia_de_vainilla int,
maicena int,
polvo_de_hornear int,
limon int,
coco_rayado int,
dulce_de_leche int,
stock int not null
);

create table if not exists produccion_diaria(
id_produccion_diaria int primary key not null,
codigo_del_producto_a_elaborar int,
nombre_del_producto_a_elaborar varchar (45) not null,
cantidad_a_elaborar_en_kg int not null,
id_receta int not null,
id_producto int not null
FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
