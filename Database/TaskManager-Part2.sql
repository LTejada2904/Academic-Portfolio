##Parte 1- Comandos DDL para creación de usuarios
##Parte a, crear usuario
CREATE USER 'rosa_resto2005'@'localhost' IDENTIFIED BY 'roJaR3st01';
CREATE USER 'luiss@martinez'@'localhost' IDENTIFIED BY 'mart.50!lUi';
CREATE USER 'luisito_vargas'@'localhost' IDENTIFIED BY 'xyz987';

##Parte b, alterar usuario
ALTER USER 'rosa_resto2005'@'localhost' IDENTIFIED BY 'roSaR3st02';

##Parte c, eliminar usuario
DROP USER 'rosa_resto2005'@'localhost';
DROP USER 'luiss@martinez'@'localhost';
DROP USER 'luisito_vargas'@'localhost';

##Parte d, añadir privilegios al usuaio
GRANT ALL privileges ON task_manager.comentario TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.departamento TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.documento TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.equipo TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.notificacion TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.proyecto TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.tarea TO 'rosa_resto2005'@'localhost';
GRANT ALL privileges ON task_manager.usuario TO 'rosa_resto2005'@'localhost';
GRANT INSERT, UPDATE ON task_manager.comentario TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.departamento TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.documento TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.equipo TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.notificacion TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.proyecto TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.tarea TO 'luiss@martinez'@'localhost';
GRANT INSERT, UPDATE ON task_manager.usuario TO 'luiss@martinez'@'localhost';

##Parte e, revocar privilegios al usuario
REVOKE INSERT, UPDATE ON task_manager.comentario FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.departamento FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.documento FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.equipo FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.notificacion FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.proyecto FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.tarea FROM 'luiss@martinez'@'localhost';
REVOKE INSERT, UPDATE ON task_manager.usuario FROM 'luiss@martinez'@'localhost';

##Parte f, crear rol
CREATE ROLE 'Admin';
CREATE ROLE 'App Dev';
CREATE ROLE 'Sys Eng';

##Parte g, añadir rol al usuario
GRANT 'Admin' TO 'rosa_resto2005'@'localhost';
GRANT 'App Dev' TO 'luiss@martinez'@'localhost';
GRANT 'Sys Eng' TO 'luisito_vargas'@'localhost';

##Parte h, revocar rol al usuario
REVOKE 'Sys Eng' FROM 'luisito_vargas'@'localhost';

##Parte 2- Comandos DDL para stored procedures
##Parte a, crear proceso
DELIMITER //

CREATE PROCEDURE CountTasks()
BEGIN
    DECLARE taskCount INT;

    SELECT COUNT(*) INTO taskCount
    FROM task_manager.tarea;

    SELECT taskCount AS 'Total Tasks';
END//

DELIMITER ;

##Parte b, alterar proceso
USE `ltejada`;
DROP procedure IF EXISTS `CountTasks`;

USE `ltejada`;
DROP procedure IF EXISTS `ltejada`.`CountTasks`;
;

DELIMITER $$
USE `ltejada`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `CountTasks`()
BEGIN
    DECLARE pendingTaskCount INT;

    SELECT COUNT(*) INTO pendingTaskCount
    FROM task_manager.tarea
    WHERE estado = 'Pendiente';

    SELECT pendingTaskCount AS 'Pending Tasks';
END$$

DELIMITER ;
;

##Parte c, eliminar proceso
DROP PROCEDURE CountTasks;

##Parte d, crear función
DELIMITER //

CREATE FUNCTION CalculatePriority(prioridad INT, estado VARCHAR(45)) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE priorityValue INT;
    
    IF estado = 'Completada' THEN
        SET priorityValue = prioridad + 1;
    ELSE
        SET priorityValue = prioridad;
    END IF;
    
    RETURN priorityValue;
END;

//

DELIMITER ;

##Parte e, alterar función
USE `task_manager`;
DROP function IF EXISTS `CalculatePriority`;

USE `task_manager`;
DROP function IF EXISTS `task_manager`.`CalculatePriority`;
;

DELIMITER $$
USE `task_manager`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `CalculatePriority`(prioridad INT, estado VARCHAR(45)) RETURNS int
    DETERMINISTIC
BEGIN
    DECLARE priorityValue INT;
    
    IF estado = 'Completada' OR estado = 'En Progreso' THEN
        SET priorityValue = prioridad + 1;
    ELSE
        SET priorityValue = prioridad;
    END IF;
    
    RETURN priorityValue;
END$$

DELIMITER ;
;

##Parte f, eliminar función
DROP FUNCTION `task_manager`.`CalculatePriority`;