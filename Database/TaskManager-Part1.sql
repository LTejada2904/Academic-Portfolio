##Parte 1- Comandos DDL
##Parte a, Crear base de datos
CREATE SCHEMA task_manager;

##Parte b, crear las 9 tablas de las 8 entidades y tabla dummy
CREATE TABLE `task_manager`.`departamento` (
  `id_dept` VARCHAR(9) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(250) NULL,
  PRIMARY KEY (`id_dept`));
  
CREATE TABLE `task_manager`.`equipo` (
  `id_equipo` VARCHAR(9) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripción` VARCHAR(250) NULL,
  `id_dept` VARCHAR(9) NULL,
  PRIMARY KEY (`id_equipo`),
  INDEX `id_dept_idx` (`id_dept` ASC) VISIBLE,
  CONSTRAINT `id_dept`
    FOREIGN KEY (`id_dept`)
    REFERENCES `task_manager`.`departamento` (`id_dept`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
    
CREATE TABLE `task_manager`.`usuario` (
  `id_usuario` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(320) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  `teléfono` double NOT NULL,
  `rol` VARCHAR(45) NULL,
  `id_equipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `id_usuario_UNIQUE` (`id_usuario` ASC) VISIBLE,
  INDEX `id_equipo_idx` (`id_equipo` ASC) VISIBLE,
  CONSTRAINT `id_equipo`
    FOREIGN KEY (`id_equipo`)
    REFERENCES `task_manager`.`equipo` (`id_equipo`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
    
CREATE TABLE `task_manager`.`tarea` (
  `id_tarea` VARCHAR(9) NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `hora_vencimiento` TIME NOT NULL,
  `prioridad` BINARY NULL,
  `estado` VARCHAR(45) NULL,
  `descripción` VARCHAR(250) NULL,
  `id_usuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_tarea`),
  INDEX `id_usuario_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `task_manager`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

CREATE TABLE `task_manager`.`proyecto` (
  `id_proyecto` VARCHAR(9) NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(250) NULL,
  PRIMARY KEY (`id_proyecto`),
  UNIQUE INDEX `id_proyecto_UNIQUE` (`id_proyecto` ASC) VISIBLE);

CREATE TABLE `task_manager`.`documento` (
  `id_documento` VARCHAR(9) NOT NULL,
  `titulo` VARCHAR(45) NULL,
  `contenido` BLOB NULL,
  `fecha_creada` DATE NULL,
  `tipo` VARCHAR(5) NULL,
  `id_usuario_fk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_documento`),
  INDEX `id_usuario_idx` (`id_usuario_fk` ASC) VISIBLE,
  CONSTRAINT `id_usuario_fk`
    FOREIGN KEY (`id_usuario_fk`)
    REFERENCES `task_manager`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
    
CREATE TABLE `task_manager`.`comentario` (
  `id_comentario` VARCHAR(9) NOT NULL,
  `contenido` VARCHAR(500) NOT NULL,
  `fecha_creado` TIMESTAMP NOT NULL,
  `id_usuariofk` VARCHAR(45) NOT NULL,
  `id_tarea_fk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_comentario`),
  UNIQUE INDEX `id_comentario_UNIQUE` (`id_comentario` ASC) VISIBLE,
  INDEX `id_usuario_idx` (`id_usuariofk` ASC) VISIBLE,
  INDEX `id_tarea_idx` (`id_tarea_fk` ASC) VISIBLE,
  CONSTRAINT `id_usuariofk`
    FOREIGN KEY (`id_usuariofk`)
    REFERENCES `task_manager`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `id_tarea_fk`
    FOREIGN KEY (`id_tarea_fk`)
    REFERENCES `task_manager`.`tarea` (`id_tarea`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
    
CREATE TABLE `task_manager`.`notificacion` (
  `id_notificacion` VARCHAR(9) NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `contenido` VARCHAR(250) NOT NULL,
  `timestamp` TIMESTAMP NOT NULL,
  `estado` VARCHAR(45) NULL,
  `idusuario_fk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_notificacion`),
  UNIQUE INDEX `id_notificacion_UNIQUE` (`id_notificacion` ASC) VISIBLE,
  INDEX `idusuario_fk_idx` (`idusuario_fk` ASC) VISIBLE,
  CONSTRAINT `idusuario_fk`
    FOREIGN KEY (`idusuario_fk`)
    REFERENCES `task_manager`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

CREATE TABLE `task_manager`.`dummy` (
  `iddummy` INT NOT NULL,
  `dummycol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddummy`));
  
##Parte c, alterar 2 estructuras de tablas
ALTER TABLE `task_manager`.`dummy` 
ADD COLUMN `id_proyecto2` VARCHAR(9) NOT NULL AFTER `dummycol`,
ADD UNIQUE INDEX `id_proyecto2_UNIQUE` (`id_proyecto2` ASC) VISIBLE;

ALTER TABLE `task_manager`.`documento` 
CHANGE COLUMN `fecha_creada` `fecha_creada` TIMESTAMP NOT NULL ,
CHANGE COLUMN `tipo` `tipo` VARCHAR(5) NOT NULL ;

#Parte d, eliminar entidad dummy
DROP TABLE `task_manager`.`dummy`;

##Parte e, añadir 3 indeces
CREATE INDEX `estado_idx` ON `task_manager`.`tarea` (`estado` ASC) VISIBLE;

CREATE INDEX `titulo_documento_idx` ON `task_manager`.`documento` (`titulo` ASC) VISIBLE;

CREATE INDEX `fecha_creado_idx` ON `task_manager`.`comentario` (`fecha_creado` ASC) VISIBLE;

##Parte f, alterar 2 indeces
ALTER TABLE `task_manager`.`tarea` 
ALTER INDEX `estado_idx` VISIBLE;

ALTER TABLE `task_manager`.`comentario` 
ALTER INDEX `fecha_creado_idx` VISIBLE;

##Parte g, eliminar indice
ALTER TABLE `task_manager`.`comentario` 
DROP INDEX `fecha_creado_idx` ;

##Parte h, creacion de view
CREATE VIEW vista_usuario_tarea AS
SELECT 
    u.id_usuario,
    u.nombre AS nombre_usuario,
    u.apellido AS apellido_usuario,
    u.email,
    t.id_tarea,
    t.titulo AS titulo_tarea,
    t.fecha_vencimiento,
    t.hora_vencimiento,
    t.prioridad,
    t.estado AS estado_tarea,
    t.descripción AS descripción_tarea
FROM 
    task_manager.usuario u
JOIN 
    task_manager.tarea t ON u.id_usuario = t.id_usuario;
    
SELECT * FROM vista_usuario_tarea;


CREATE VIEW vista_departamento_equipo AS
SELECT 
    d.id_dept,
    d.nombre AS nombre_departamento,
    d.descripcion AS descripcion_departamento,
    e.id_equipo,
    e.nombre AS nombre_equipo,
    e.descripción AS descripción_equipo
FROM 
    task_manager.departamento d
JOIN 
    task_manager.equipo e ON d.id_dept = e.id_dept;

SELECT * FROM vista_departamento_equipo;

##Parte i, alterar vistas
ALTER VIEW vista_usuario_tarea AS
SELECT 
    u.id_usuario,
    u.nombre AS nombre_usuario,
    u.apellido AS apellido_usuario,
    t.id_tarea,
    t.titulo AS titulo_tarea,
    t.fecha_vencimiento,
    t.hora_vencimiento,
    t.prioridad,
    t.estado AS estado_tarea,
    t.descripción AS descripción_tarea
FROM 
    task_manager.usuario u
JOIN 
    task_manager.tarea t ON u.id_usuario = t.id_usuario;
    
    
ALTER VIEW vista_departamento_equipo AS
SELECT 
    d.id_dept,
    d.nombre AS nombre_departamento,
    e.id_equipo,
    e.nombre AS nombre_equipo
FROM 
    task_manager.departamento d
JOIN 
    task_manager.equipo e ON d.id_dept = e.id_dept;

##Parte j, eliminar una vista
DROP VIEW vista_departamento_equipo;

##Parte 2- Comandos DML
##Parte a, Insertar 5 records por cada tabla
INSERT INTO `task_manager`.`departamento` (`id_dept`, `nombre`, `descripcion`)
VALUES
	('D00000001', 'Recursos Humanos', 'El Departamento de Recursos Humanos es el corazón de nuestra organización, dedicado a nutrir el talento.'),
	('D00000002', 'Contabilidad', 'El Departamento de Contabilidad es el pilar financiero de nuestra organización.'),
	('D00000003', 'IT', 'El Departamento de Tecnología de la Información (IT) es el núcleo tecnológico de nuestra empresa, liderando la innovación y la excelencia digital.'),
	('D00000004', 'Mercadeo', 'El Departamento de Mercadeo es el motor creativo y estratégico de nuestra empresa.'),
	('D00000005', 'Mantenimiento', 'El Departamento de Mantenimiento es el guardián de la funcionalidad y seguridad de nuestra empresa.');

INSERT INTO task_manager.equipo (id_equipo, nombre, descripción, id_dept)
VALUES
('E00100001', 'Reclutamiento', 'El equipo de reclutamiento es un grupo dedicado de profesionales que se especializa en identificar y seleccionar talentos para la organización.', 'D00000001'),
('E00100002', 'Servicio al Empleado', 'El equipo de servicio del empleado, liderado por Recursos Humanos, se enfoca en proporcionar asistencia y apoyo integral a los empleados de la organización.', 'D00000001'),
('E00200001', 'Cobros', 'Encargados de gestionar eficientemente los pagos pendientes y asegurar la recuperación oportuna de los fondos adeudados', 'D00000002'),
('E00200002', 'Nomina', 'Nos dedicamos a garantizar la precisión y puntualidad en el procesamiento de salarios y beneficios para los empleados de la organización. ', 'D00000002'),
('E00300001', 'Desarrolladores', 'Colaboramos para crear soluciones tecnológicas innovadoras y robustas.', 'D00000003');

INSERT INTO task_manager.usuario (id_usuario, nombre, apellido, email, contraseña, teléfono, rol, id_equipo)
VALUES
('maria.rivera', 'Maria', 'Rivera', 'maria.rivera@hotmail.com', 'abc123', 7877504125, 'Supervisora de Reclutamiento', 'E00100001'),
('felipe50', 'Felipe', 'Robles', 'felipe50@gmail.com', 'sAnFelip0#', 7878856245, 'Oficial de Nomina', 'E00200002'),
('rosa_resto2005', 'Rosa', 'Resto', 'rosa_resto2005@icloud.com', 'roJaR3st01', 7506521452, 'Programadora Bases de Datos', 'E00300001'),
('luiss@martinez', 'Luis', 'Martinez', 'luis@martinez@gmail.com', 'mart.50!lUi', 7875203012, 'Desarrollador de Aplicaciones', 'E00300001'),
('luisito_vargas', 'Luis', 'Vargas', 'luisito_vargas@yahoo.com', 'xyz987', 7879512034, 'Ingeniero de Sistemas', 'E00300001');

INSERT INTO task_manager.tarea (id_tarea, titulo, fecha_vencimiento, hora_vencimiento, prioridad, estado, descripción, id_usuario)
VALUES
('T00000001', 'Desarrollar Base de Datos', '2023-10-20', '14:00:00', 1, 'En progreso', 'Desarrollar base de datos para sistema de contabilidad', 'maria.rivera'),
('T00000002', 'Desarrollar Aplicacion Contabilidad', '2023-10-21', '15:00:00', 2, 'Pendiente', 'Desarrollar la aplicacion de contabilidad de la empresa.', 'luiss@martinez'),
('T00000003', 'Creacion de nominas', '2023-10-22', '16:00:00', 3, 'Completada', 'Crear, firmar y completar nominas de empleados de la empresa', 'felipe50'),
('T00000004', 'Migracion de redes', '2023-10-23', '17:00:00', 4, 'Pendiente', 'Migrar redes de edificio A a B', 'luisito_vargas'),
('T00000005', 'Desarrollar informe de aplicacion', '2023-10-24', '18:00:00', 5, 'En progreso', 'Desarrollar un informe de ingenieria de software de los pasos a seguir para desarrollar aplicacion de contabilidad', 'luiss@martinez');

INSERT INTO task_manager.proyecto (id_proyecto, titulo, descripcion)
VALUES
('P00030001', 'Aplicacion Contabilidad', 'Desarrollar aplicacion para el dept de contabilidad completamente funcional.'),
('P00010001', 'Aumento de Nomina Salarial', 'Desarrollar informes de empleados y presupuestos para aumento de nomina salariral a empleados.'),
('P00030002', 'Migracion de Redes', 'Migrar las redes del antiguo edificio al nuevo edificio y desarrollar una red robusta'),
('P00050001', 'Reclutamiento de Mantenimiento', 'Reclutar empleados para amntenimiento de las oficinas'),
('P00040001', 'Desarrollo de material promocional', 'Desarrollar material promocional para eventos de reclutamiento y de marketing para la empresa.');

INSERT INTO task_manager.documento (id_documento, titulo, contenido, fecha_creada, tipo, id_usuario_fk)
VALUES
('D00000001', 'Empleados Dept de IT', 'Contenido del documento 1', '2023-10-20', '.pdf', 'maria.rivera'),
('D00000002', 'Informe de desarrollo', 'Contenido del documento 2', '2023-10-21', '.doc', 'luiss@martinez'),
('D00000003', 'Informe nóminas septiembre', 'Contenido del documento 3', '2023-10-22', '.xlsx', 'felipe50'),
('D00000004', 'Modelo Entidad Relación', 'Contenido del documento 4', '2023-10-23', '.pdf', 'rosa_resto2005'),
('D00000005', 'Desarrollo de Redes', 'Contenido del documento 5', '2023-10-24', '.docx', 'luiss@martinez');

INSERT INTO task_manager.comentario (id_comentario, contenido, fecha_creado, id_usuariofk, id_tarea_fk)
VALUES
('C00000001', 'Comentario 1', '2023-10-20 14:30:00', 'maria.rivera', 'T00000001'),
('C00000002', 'Comentario 2', '2023-10-21 15:30:00', 'luiss@martinez', 'T00000002'),
('C00000003', 'Comentario 3', '2023-10-22 16:30:00', 'felipe50', 'T00000003'),
('C00000004', 'Comentario 4', '2023-10-22 17:00:50', 'maria.rivera', 'T00000001'),
('C00000005', 'Comentario 4', '2023-10-25 18:30:47', 'luisito_vargas', 'T00000005');

##Parte b- Actualizar dos datos de cada tabla
UPDATE task_manager.departamento
SET nombre = 'Recursos Humanos y Talento'
WHERE id_dept = 'D00000001';

UPDATE task_manager.departamento
SET descripcion = 'Departamento encargado de gestionar las finanzas y garantizar el cumplimiento normativo.'
WHERE id_dept = 'D00000002';

UPDATE task_manager.equipo
SET nombre = 'Equipo de Atracción de Talento'
WHERE id_equipo = 'E00100001';

UPDATE task_manager.equipo
SET descripción = 'Equipo dedicado a proporcionar soporte y asistencia a los empleados en temas laborales y de recursos humanos.'
WHERE id_equipo = 'E00100002';

UPDATE task_manager.usuario
SET rol = 'Especialista en Reclutamiento'
WHERE id_usuario = 'maria.rivera';

UPDATE task_manager.usuario
SET email = 'felipe.robles@empresa.com'
WHERE id_usuario = 'felipe50';

UPDATE task_manager.tarea
SET estado = 'En revisión por el supervisor'
WHERE id_tarea = 'T00000001';

UPDATE task_manager.tarea
SET fecha_vencimiento = '2023-10-28'
WHERE id_tarea = 'T00000002';

UPDATE task_manager.proyecto
SET titulo = 'Proyecto de Expansión de Mercado'
WHERE id_proyecto = 'P00010001';

UPDATE task_manager.proyecto
SET descripcion = 'Proyecto estratégico para ingresar a nuevos mercados y aumentar la presencia de la empresa.'
WHERE id_proyecto = 'P00010001';

UPDATE task_manager.documento
SET contenido = 'Nuevo informe financiero para el tercer trimestre.'
WHERE id_documento = 'D00000001';

UPDATE task_manager.documento
SET tipo = '.pdf'
WHERE id_documento = 'D00000002';

UPDATE task_manager.comentario
SET contenido = 'Actualización: Se han completado las primeras.'
WHERE id_comentario = 'C00000001';

UPDATE task_manager.comentario
SET fecha_creado = '2023-10-27 10:30:00'
WHERE id_comentario = 'C00000002';

##Parte C eliminar 1 record por tabla
DELETE FROM task_manager.departamento
WHERE id_dept = 'D00000001'
LIMIT 1;

DELETE FROM task_manager.equipo
WHERE id_equipo = 'E00100001'
LIMIT 1;

DELETE FROM task_manager.usuario
WHERE id_usuario = 'maria.rivera'
LIMIT 1;

DELETE FROM task_manager.tarea
WHERE id_tarea = 'T00000001'
LIMIT 1;

DELETE FROM task_manager.proyecto
WHERE id_proyecto = 'P00030001'
LIMIT 1;

DELETE FROM task_manager.documento
WHERE id_documento = 'D00000001'
LIMIT 1;

DELETE FROM task_manager.comentario
WHERE id_comentario = 'C00000001'
LIMIT 1;

DELETE FROM task_manager.notificacion
WHERE id_notificacion = 'N00000001'
LIMIT 1;

##Parte d, Truncar la tabla proyecto
TRUNCATE `task_manager`.`proyecto`;

##Seleccionar cada tabla
SELECT * FROM task_manager.departamento;

SELECT * FROM task_manager.equipo;

SELECT * FROM task_manager.usuario;

SELECT * FROM task_manager.tarea;

SELECT * FROM task_manager.proyecto;

SELECT * FROM task_manager.documento;

SELECT * FROM task_manager.comentario;

SELECT * FROM task_manager.notificacion;