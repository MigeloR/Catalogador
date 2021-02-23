-- MySQL dump 10.13  Distrib 5.6.49, for Win64 (x86_64)
--
-- Host: localhost    Database: pkmn
-- ------------------------------------------------------
-- Server version	5.6.49-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pkmn_tipos`
--

DROP TABLE IF EXISTS `pkmn_tipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pkmn_tipos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pkmn_id` int(11) DEFAULT NULL,
  `tipos_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pkmn_tipos`
--

LOCK TABLES `pkmn_tipos` WRITE;
/*!40000 ALTER TABLE `pkmn_tipos` DISABLE KEYS */;
INSERT INTO `pkmn_tipos` VALUES (1,1,11),(2,1,16),(3,2,11),(4,2,16),(5,3,11),(6,3,16),(7,4,4),(8,5,4),(9,6,4),(10,6,17),(11,7,1),(12,8,1),(13,9,1),(14,10,3),(15,11,3),(16,12,3),(17,12,17),(18,13,3),(19,13,16),(20,14,3),(21,14,16),(22,15,3),(23,15,16),(24,16,12),(25,16,17),(26,17,12),(27,17,17),(28,18,12),(29,18,17);
/*!40000 ALTER TABLE `pkmn_tipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pokemon`
--

DROP TABLE IF EXISTS `pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pokemon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon`
--

LOCK TABLES `pokemon` WRITE;
/*!40000 ALTER TABLE `pokemon` DISABLE KEYS */;
INSERT INTO `pokemon` VALUES (15,'beedrill'),(9,'blastoise'),(1,'bulbasaur'),(12,'butterfree'),(10,'caterpie'),(6,'charizard'),(4,'charmander'),(5,'charmeleon'),(2,'ivysaur'),(14,'kakuna'),(11,'metapod'),(18,'pidgeot'),(17,'pidgeotto'),(16,'pidgey'),(19,'pikachu'),(20,'raichu'),(21,'ratata'),(7,'squirtle'),(3,'venusaur'),(8,'warturtle'),(13,'weedle');
/*!40000 ALTER TABLE `pokemon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos`
--

DROP TABLE IF EXISTS `tipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipos` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos`
--

LOCK TABLES `tipos` WRITE;
/*!40000 ALTER TABLE `tipos` DISABLE KEYS */;
INSERT INTO `tipos` VALUES (2,'acero'),(1,'agua'),(3,'bicho'),(5,'dragon'),(6,'electrico'),(7,'fantasma'),(4,'fuego'),(8,'hada'),(9,'hielo'),(10,'lucha'),(12,'normal'),(11,'planta'),(18,'psiquico'),(13,'roca'),(14,'siniestro'),(15,'tierra'),(16,'veneno'),(17,'volador');
/*!40000 ALTER TABLE `tipos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-22 13:46:24
