-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: taller
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `appUsers`
--

LOCK TABLES `appUsers` WRITE;
/*!40000 ALTER TABLE `appUsers` DISABLE KEYS */;
INSERT INTO `appUsers` VALUES ('Aingeru','abellido','taller');
/*!40000 ALTER TABLE `appUsers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES ('Cliente 1',111222334,'cliente1@ikasle.ehu.eus'),('Cliente 2',222111333,'cliente2@ikasle.ehu.eus'),('Cliente 3',333222111,'cliente3@ikasle.ehu.eus'),('Cliente 4',111333222,'cliente4@ikasle.ehu.eus'),('Cliente 5',222333111,'cliente5@ikasle.ehu.eus'),('Cliente 6',333111222,'cliente6@ikasle.ehu.eus'),('Cliente 7',123456789,'cliente6@ikasle.ehu.eus');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES ('05/05/2024','1239ABC','Se ha sustituido la batería del vehículo, asegurando el arranque del mismo y el correcto funcionamiento de los sistemas eléctricos.'),('12/01/2023','1237ABC','Se ha sustituido la correa de distribución, un componente vital para el correcto funcionamiento del motor. Se recomienda su cambio cada 100.000 km o 5 años, lo que antes llegue.'),('12/02/2024','1237ABC','Revisiones pre-viaje: revisión de niveles, estado de los elementos básicos, sistema de iluminación y batería, con recomendaciones para viajes largos.'),('13/03/2024','1234ABC','Reparaciones mecánicas: reparación de motor, caja de cambios, embrague, suspensión, frenos, diagnosis electrónica, reparación de averías y sustitución de piezas.'),('13/03/2024','1235ABC','Revisión y mantenimiento: cambio de aceite y filtro, revisión de niveles, neumáticos, luces y sistema eléctrico.'),('14/03/2024','1234ABC','Chapa y pintura: reparación de golpes, abolladuras, pintado completo o parcial, pulido y limpieza de la pintura, y restauración de faros.'),('14/04/2024','1238ABC','Se ha realizado una limpieza de los inyectores, mejorando la atomización del combustible y optimizando el rendimiento del motor.'),('14/05/2024','1240ABC','Se ha realizado una revisión completa de la suspensión, verificando el estado de los amortiguadores, muelles y demás componentes. Se recomienda su revisión periódica para garantizar la estabilidad y seguridad del vehículo.'),('15/03/2024','1234ABC','Neumáticos: cambio, equilibrado, alineación de la dirección, reparación de pinchazos y rotación.'),('15/03/2024','1235ABC','ITV: revisión pre-ITV, gestión de la cita y reparación de averías.'),('15/03/2024','1237ABC','Se ha detectado una fuga en el sistema de escape, lo que podía ocasionar problemas de rendimiento y emisiones contaminantes. Se ha reparado la fuga y se ha verificado el correcto funcionamiento del sistema.'),('16/03/2024','1236ABC','Otros servicios: limpieza integral del vehículo, carga de aire acondicionado, instalación de accesorios y vehículo de sustitución.'),('16/03/2024','1238ABC','Se ha realizado una carga completa del sistema de aire acondicionado, garantizando un flujo de aire fresco y confortable en el habitáculo.'),('18/03/2024','1238ABC','Se ha realizado un pulido de los faros, eliminando la opacidad y mejorando la visibilidad nocturna.'),('18/04/2042','1238ABC','Se ha realizado un diagnosis completa del sistema electrónico del vehículo, detectando y reparando la avería que afectaba a su funcionamiento.'),('18/05/2024','1240ABC','Se ha instalado un kit de manos libres Bluetooth, permitiendo una conducción más segura y cómoda al poder realizar llamadas sin necesidad de usar el teléfono móvil.'),('29/04/2024','1239ABC','Se han sustituido las pastillas de freno delanteras/traseras, garantizando una frenada segura y eficiente. Se recomienda revisarlas periódicamente para asegurar su correcto estado.');
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `userClientes`
--

LOCK TABLES `userClientes` WRITE;
/*!40000 ALTER TABLE `userClientes` DISABLE KEYS */;
INSERT INTO `userClientes` VALUES ('Aingeru','Cliente 1'),('Aingeru','Cliente 2'),('Aingeru','Cliente 3'),('Aingeru','Cliente 4'),('Aingeru','Cliente 5'),('Aingeru','Cliente 6'),('Aingeru','Cliente 7');
/*!40000 ALTER TABLE `userClientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vehiculos`
--

LOCK TABLES `vehiculos` WRITE;
/*!40000 ALTER TABLE `vehiculos` DISABLE KEYS */;
INSERT INTO `vehiculos` VALUES ('1234ABC','Mercedes','A45S AMG','Cliente 1'),('1235ABC','Toyota','Corolla','Cliente 1'),('1236ABC','Honda','Civic','Cliente 1'),('1237ABC','Ford','F-150','Cliente 1'),('1238ABC','Chevrolet','Silverado','Cliente 2'),('1239ABC','Ram','1500','Cliente 2'),('1240ABC','Honda','CR-V','Cliente 3'),('1241ABC','BMW','E35 M3','Cliente 1');
/*!40000 ALTER TABLE `vehiculos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-09 22:34:14
