CREATE DATABASE  IF NOT EXISTS `test_soft_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `test_soft_db`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: test_soft_db
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `article_article`
--

DROP TABLE IF EXISTS `article_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article_article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `text` longtext NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `date_of_review` date DEFAULT NULL,
  `date_of_delete` date DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `author_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_article_author_id_e6b479f8_fk_user_user_id` (`author_id`),
  KEY `article_article_date_of_delete_63cd03f4` (`date_of_delete`),
  KEY `article_article_visibility_0ceb05a7` (`visibility`),
  CONSTRAINT `article_article_author_id_e6b479f8_fk_user_user_id` FOREIGN KEY (`author_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_article`
--

LOCK TABLES `article_article` WRITE;
/*!40000 ALTER TABLE `article_article` DISABLE KEYS */;
INSERT INTO `article_article` VALUES (1,'ЛУЧШИЕ ОНЛАЙН-УНИВЕРСИТЕТЫ МИРА С БЕСПЛАТНЫМ ОБУЧЕНИЕМ','Мы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.',1,'2020-05-05',NULL,'article/цветы-птица.jpg',1),(2,'Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации','Мы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\r\n\r\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\r\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\r\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\r\n\r\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\r\n\r\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.',1,'2020-04-08',NULL,'',2);
/*!40000 ALTER TABLE `article_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add ПО',1,'add_software'),(2,'Can change ПО',1,'change_software'),(3,'Can delete ПО',1,'delete_software'),(4,'Can view ПО',1,'view_software'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add Приложение',8,'add_addition'),(30,'Can change Приложение',8,'change_addition'),(31,'Can delete Приложение',8,'delete_addition'),(32,'Can view Приложение',8,'view_addition'),(33,'Can add Классификация',9,'add_classification'),(34,'Can change Классификация',9,'change_classification'),(35,'Can delete Классификация',9,'delete_classification'),(36,'Can view Классификация',9,'view_classification'),(37,'Can add Приложение_классификация',10,'add_software_classification'),(38,'Can change Приложение_классификация',10,'change_software_classification'),(39,'Can delete Приложение_классификация',10,'delete_software_classification'),(40,'Can view Приложение_классификация',10,'view_software_classification'),(41,'Can add Классификация_значение',11,'add_classification_value'),(42,'Can change Классификация_значение',11,'change_classification_value'),(43,'Can delete Классификация_значение',11,'delete_classification_value'),(44,'Can view Классификация_значение',11,'view_classification_value'),(45,'Can add Приложение_классификация',12,'add_software_classification_value'),(46,'Can change Приложение_классификация',12,'change_software_classification_value'),(47,'Can delete Приложение_классификация',12,'delete_software_classification_value'),(48,'Can view Приложение_классификация',12,'view_software_classification_value'),(49,'Can add Статья',13,'add_article'),(50,'Can change Статья',13,'change_article'),(51,'Can delete Статья',13,'delete_article'),(52,'Can view Статья',13,'view_article'),(53,'Can add Пользователь',14,'add_user'),(54,'Can change Пользователь',14,'change_user'),(55,'Can delete Пользователь',14,'delete_user'),(56,'Can view Пользователь',14,'view_user'),(57,'Can add Scheduled task',15,'add_schedule'),(58,'Can change Scheduled task',15,'change_schedule'),(59,'Can delete Scheduled task',15,'delete_schedule'),(60,'Can view Scheduled task',15,'view_schedule'),(61,'Can add task',16,'add_task'),(62,'Can change task',16,'change_task'),(63,'Can delete task',16,'delete_task'),(64,'Can view task',16,'view_task'),(65,'Can add Failed task',17,'add_failure'),(66,'Can change Failed task',17,'change_failure'),(67,'Can delete Failed task',17,'delete_failure'),(68,'Can view Failed task',17,'view_failure'),(69,'Can add Successful task',18,'add_success'),(70,'Can change Successful task',18,'change_success'),(71,'Can delete Successful task',18,'delete_success'),(72,'Can view Successful task',18,'view_success'),(73,'Can add Queued task',19,'add_ormq'),(74,'Can change Queued task',19,'change_ormq'),(75,'Can delete Queued task',19,'delete_ormq'),(76,'Can view Queued task',19,'view_ormq'),(77,'Can add Тег',20,'add_tag'),(78,'Can change Тег',20,'change_tag'),(79,'Can delete Тег',20,'delete_tag'),(80,'Can view Тег',20,'view_tag'),(81,'Can add Приложение_тег',21,'add_software_tag'),(82,'Can change Приложение_тег',21,'change_software_tag'),(83,'Can delete Приложение_тег',21,'delete_software_tag'),(84,'Can view Приложение_тег',21,'view_software_tag'),(85,'Can add Заказ звонка',22,'add_feedback'),(86,'Can change Заказ звонка',22,'change_feedback'),(87,'Can delete Заказ звонка',22,'delete_feedback'),(88,'Can view Заказ звонка',22,'view_feedback'),(89,'Can add ПО',23,'add_software'),(90,'Can change ПО',23,'change_software'),(91,'Can delete ПО',23,'delete_software'),(92,'Can view ПО',23,'view_software'),(93,'Can add Приложение_классификация',24,'add_software_classification_value'),(94,'Can change Приложение_классификация',24,'change_software_classification_value'),(95,'Can delete Приложение_классификация',24,'delete_software_classification_value'),(96,'Can view Приложение_классификация',24,'view_software_classification_value'),(97,'Can add Тег',25,'add_tag'),(98,'Can change Тег',25,'change_tag'),(99,'Can delete Тег',25,'delete_tag'),(100,'Can view Тег',25,'view_tag'),(101,'Can add Классификация',26,'add_classification'),(102,'Can change Классификация',26,'change_classification'),(103,'Can delete Классификация',26,'delete_classification'),(104,'Can view Классификация',26,'view_classification'),(105,'Can add Классификация_значение',27,'add_classification_value'),(106,'Can change Классификация_значение',27,'change_classification_value'),(107,'Can delete Классификация_значение',27,'delete_classification_value'),(108,'Can view Классификация_значение',27,'view_classification_value'),(109,'Can add Приложение',28,'add_addition'),(110,'Can change Приложение',28,'change_addition'),(111,'Can delete Приложение',28,'delete_addition'),(112,'Can view Приложение',28,'view_addition');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$CH3eqVMoVskq$D+WWrN/kDzjoBtplV5hVg+62J5CxgjauimWshOc31Ao=','2020-05-06 14:41:07.666761',1,'admin','','','ndmitrievnaa@mail.ru',1,1,'2020-04-23 17:07:03.886827');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-23 17:08:30.412689','1','Главная картинка',1,'[{\"added\": {}}]',8,1),(2,'2020-04-24 14:11:06.374834','2','Применение',1,'[{\"added\": {}}]',8,1),(3,'2020-05-02 16:26:04.024577','1','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',1,'[{\"added\": {}}]',13,1),(4,'2020-05-02 16:28:15.005881','1','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',2,'[{\"changed\": {\"fields\": [\"\\u0414\\u0430\\u0442\\u0430 \\u043f\\u0443\\u0431\\u043b\\u0438\\u043a\\u0430\\u0446\\u0438\\u0438\"]}}]',13,1),(5,'2020-05-02 17:39:19.502091','1','Анастасия',1,'[{\"added\": {}}]',14,1),(6,'2020-05-02 18:31:39.756612','1','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',2,'[{\"changed\": {\"fields\": [\"\\u0410\\u0432\\u0442\\u043e\\u0440\"]}}]',13,1),(7,'2020-05-03 05:33:25.066907','1','Анастасия',2,'[]',14,1),(8,'2020-05-03 06:55:14.910184','1','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',2,'[{\"changed\": {\"fields\": [\"\\u0424\\u043e\\u0442\\u043e\"]}}]',13,1),(9,'2020-05-03 07:04:24.468530','1','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',2,'[]',13,1),(10,'2020-05-03 07:05:17.484928','2','Автоматизированное образование',1,'[{\"added\": {}}]',13,1),(11,'2020-05-03 07:05:32.869256','2','Автоматизированное образование',2,'[{\"changed\": {\"fields\": [\"\\u0410\\u0432\\u0442\\u043e\\u0440\"]}}]',13,1),(12,'2020-05-03 14:23:25.813996','2','Артем',1,'[{\"added\": {}}]',14,1),(13,'2020-05-03 16:16:32.813846','3','Вид',1,'[{\"added\": {}}]',9,1),(14,'2020-05-03 16:16:40.067222','1','Вид',3,'',9,1),(15,'2020-05-03 16:17:05.852125','3','Настольное приложение',1,'[{\"added\": {}}]',11,1),(16,'2020-05-03 16:17:11.028123','4','Сайт',1,'[{\"added\": {}}]',11,1),(17,'2020-05-03 16:17:18.800197','5','Мобильное приложение',1,'[{\"added\": {}}]',11,1),(18,'2020-05-03 16:17:57.917907','6','Грузоперевозки',1,'[{\"added\": {}}]',11,1),(19,'2020-05-03 16:19:05.800262','2','Software_Classification_Value object (2)',1,'[{\"added\": {}}]',12,1),(20,'2020-05-03 16:19:11.153408','3','Software_Classification_Value object (3)',1,'[{\"added\": {}}]',12,1),(21,'2020-05-03 16:20:36.470537','7','Перевозки',1,'[{\"added\": {}}]',11,1),(22,'2020-05-03 16:56:30.125250','4','Тип использования',1,'[{\"added\": {}}]',9,1),(23,'2020-05-03 16:57:02.878535','8','Групповой доступ',1,'[{\"added\": {}}]',11,1),(24,'2020-05-03 16:57:12.906369','4','Software_Classification_Value object (4)',1,'[{\"added\": {}}]',12,1),(25,'2020-05-03 18:19:30.832583','5','Software_Classification_Value object (5)',1,'[{\"added\": {}}]',12,1),(26,'2020-05-03 19:21:02.146107','6','Software_Classification_Value object (6)',1,'[{\"added\": {}}]',12,1),(27,'2020-05-03 19:21:07.612999','7','Software_Classification_Value object (7)',1,'[{\"added\": {}}]',12,1),(28,'2020-05-03 19:21:13.604381','8','Software_Classification_Value object (8)',1,'[{\"added\": {}}]',12,1),(29,'2020-05-04 07:36:13.445226','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\", \"\\u041a\\u043e\\u0440\\u043e\\u0442\\u043a\\u043e\\u0435 \\u043e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(30,'2020-05-04 07:37:07.754672','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(31,'2020-05-04 07:37:33.599573','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(32,'2020-05-04 08:03:11.883147','2','Кафе',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\", \"\\u041a\\u043e\\u0440\\u043e\\u0442\\u043a\\u043e\\u0435 \\u043e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(33,'2020-05-04 08:03:56.613444','2','Кафе',2,'[]',1,1),(34,'2020-05-04 08:24:24.225896','5','Ограничение доступа',1,'[{\"added\": {}}]',9,1),(35,'2020-05-04 08:24:40.155109','9','Без разделения ролей',1,'[{\"added\": {}}]',11,1),(36,'2020-05-04 08:24:54.115277','10','Разделение ролей',1,'[{\"added\": {}}]',11,1),(37,'2020-05-04 08:25:09.903483','9','Software_Classification_Value object (9)',1,'[{\"added\": {}}]',12,1),(38,'2020-05-04 08:25:15.294260','10','Software_Classification_Value object (10)',1,'[{\"added\": {}}]',12,1),(39,'2020-05-04 08:25:37.184294','6','Дополнительные установки',1,'[{\"added\": {}}]',9,1),(40,'2020-05-04 08:25:42.354815','7','Установка',1,'[{\"added\": {}}]',9,1),(41,'2020-05-04 08:25:59.484013','11','Не требуются',1,'[{\"added\": {}}]',11,1),(42,'2020-05-04 08:26:07.114853','12','Не требуется',1,'[{\"added\": {}}]',11,1),(43,'2020-05-04 08:26:13.887633','13','Требуется',1,'[{\"added\": {}}]',11,1),(44,'2020-05-04 08:26:21.396953','14','Требуются',1,'[{\"added\": {}}]',11,1),(45,'2020-05-04 08:26:36.558809','11','Software_Classification_Value object (11)',1,'[{\"added\": {}}]',12,1),(46,'2020-05-04 08:26:43.235108','12','Software_Classification_Value object (12)',1,'[{\"added\": {}}]',12,1),(47,'2020-05-04 08:26:47.699832','13','Software_Classification_Value object (13)',1,'[{\"added\": {}}]',12,1),(48,'2020-05-04 08:26:52.996676','14','Software_Classification_Value object (14)',1,'[{\"added\": {}}]',12,1),(49,'2020-05-04 08:50:42.060594','2','Кафе',2,'[{\"changed\": {\"fields\": [\"\\u0412\\u043e\\u0437\\u043c\\u043e\\u0436\\u043d\\u043e\\u0441\\u0442\\u044c \\u0434\\u043e\\u0440\\u0430\\u0431\\u043e\\u0442\\u043a\\u0438\"]}}]',1,1),(50,'2020-05-04 09:12:54.820344','1','Платно',1,'[{\"added\": {}}]',20,1),(51,'2020-05-04 09:13:03.890192','2','Бесплатно',1,'[{\"added\": {}}]',20,1),(52,'2020-05-04 09:13:11.878709','3','Перевозки',1,'[{\"added\": {}}]',20,1),(53,'2020-05-04 09:13:16.536654','4','Доставка',1,'[{\"added\": {}}]',20,1),(54,'2020-05-04 09:13:25.880808','1','Software_Tag object (1)',1,'[{\"added\": {}}]',21,1),(55,'2020-05-04 09:13:29.327827','2','Software_Tag object (2)',1,'[{\"added\": {}}]',21,1),(56,'2020-05-04 09:13:29.694644','3','Software_Tag object (3)',1,'[{\"added\": {}}]',21,1),(57,'2020-05-04 09:13:32.770816','4','Software_Tag object (4)',1,'[{\"added\": {}}]',21,1),(58,'2020-05-04 09:13:39.154980','5','Software_Tag object (5)',1,'[{\"added\": {}}]',21,1),(59,'2020-05-04 09:13:43.614021','6','Software_Tag object (6)',1,'[{\"added\": {}}]',21,1),(60,'2020-05-04 11:07:22.792352','6','Software_Tag object (6)',2,'[{\"changed\": {\"fields\": [\"\\u0422\\u0435\\u0433\"]}}]',21,1),(61,'2020-05-04 11:07:39.940735','5','Software_Tag object (5)',2,'[{\"changed\": {\"fields\": [\"\\u0422\\u0435\\u0433\"]}}]',21,1),(62,'2020-05-04 11:07:44.687336','4','Software_Tag object (4)',2,'[{\"changed\": {\"fields\": [\"\\u0422\\u0435\\u0433\"]}}]',21,1),(63,'2020-05-04 11:07:50.013341','3','Software_Tag object (3)',3,'',21,1),(64,'2020-05-04 11:07:55.206563','2','Software_Tag object (2)',2,'[{\"changed\": {\"fields\": [\"\\u0422\\u0435\\u0433\"]}}]',21,1),(65,'2020-05-04 11:08:00.897158','1','Software_Tag object (1)',2,'[{\"changed\": {\"fields\": [\"\\u0422\\u0435\\u0433\"]}}]',21,1),(66,'2020-05-04 13:40:50.073497','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(67,'2020-05-04 13:42:09.727946','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(68,'2020-05-04 13:45:36.426209','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(69,'2020-05-04 13:46:01.198994','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435\"]}}]',1,1),(70,'2020-05-05 09:04:15.702014','3','ЛУЧШИЕ ОНЛАЙН-УНИВЕРСИТЕТЫ МИРА С БЕСПЛАТНЫМ ОБУЧЕНИЕМ',1,'[{\"added\": {}}]',13,1),(71,'2020-05-05 09:04:41.815322','4','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',1,'[{\"added\": {}}]',13,1),(72,'2020-05-06 14:42:53.711166','2','Артем',2,'[{\"changed\": {\"fields\": [\"Kind\"]}}]',14,1),(73,'2020-05-06 14:43:02.135371','2','Артем',2,'[{\"changed\": {\"fields\": [\"Kind\"]}}]',14,1),(74,'2020-05-06 14:43:05.372990','2','Артем',2,'[]',14,1),(75,'2020-05-06 14:43:10.463623','1','Анастасия',2,'[{\"changed\": {\"fields\": [\"Kind\"]}}]',14,1),(76,'2020-05-07 15:40:27.250467','3','Автодоставка',1,'[{\"added\": {}}]',23,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(13,'article','article'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(17,'django_q','failure'),(19,'django_q','ormq'),(15,'django_q','schedule'),(18,'django_q','success'),(16,'django_q','task'),(22,'feedback','feedback'),(7,'sessions','session'),(8,'soft','addition'),(9,'soft','classification'),(11,'soft','classification_value'),(1,'soft','software'),(10,'soft','software_classification'),(12,'soft','software_classification_value'),(21,'soft','software_tag'),(20,'soft','tag'),(28,'software','addition'),(26,'software','classification'),(27,'software','classification_value'),(23,'software','software'),(24,'software','software_classification_value'),(25,'software','tag'),(14,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-23 13:48:32.425243'),(2,'auth','0001_initial','2020-04-23 13:48:32.696666'),(3,'admin','0001_initial','2020-04-23 13:48:34.065257'),(4,'admin','0002_logentry_remove_auto_add','2020-04-23 13:48:34.364422'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-23 13:48:34.374395'),(6,'contenttypes','0002_remove_content_type_name','2020-04-23 13:48:34.583166'),(7,'auth','0002_alter_permission_name_max_length','2020-04-23 13:48:34.689897'),(8,'auth','0003_alter_user_email_max_length','2020-04-23 13:48:34.732787'),(9,'auth','0004_alter_user_username_opts','2020-04-23 13:48:34.742760'),(10,'auth','0005_alter_user_last_login_null','2020-04-23 13:48:34.848477'),(11,'auth','0006_require_contenttypes_0002','2020-04-23 13:48:34.854460'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-23 13:48:34.864433'),(13,'auth','0008_alter_user_username_max_length','2020-04-23 13:48:34.986761'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-23 13:48:35.097464'),(15,'auth','0010_alter_group_name_max_length','2020-04-23 13:48:35.129379'),(16,'auth','0011_update_proxy_permissions','2020-04-23 13:48:35.143342'),(17,'sessions','0001_initial','2020-04-23 13:48:35.198195'),(18,'soft','0001_initial','2020-04-23 13:48:35.272995'),(19,'soft','0002_auto_20200424_0102','2020-04-23 17:03:04.410594'),(20,'soft','0003_auto_20200424_2210','2020-04-24 14:10:53.580319'),(21,'soft','0004_auto_20200424_2241','2020-04-24 14:41:29.871242'),(22,'soft','0005_auto_20200424_2244','2020-04-24 14:44:43.246504'),(23,'soft','0006_classification_software_classification','2020-04-26 13:48:32.343225'),(24,'soft','0007_auto_20200426_2153','2020-04-26 13:53:57.312338'),(25,'article','0001_initial','2020-05-02 15:35:42.961096'),(26,'article','0002_article_photo','2020-05-02 15:50:18.987453'),(27,'article','0003_auto_20200503_0032','2020-05-02 16:32:20.069301'),(28,'user','0001_initial','2020-05-02 17:34:41.487136'),(29,'article','0004_article_author','2020-05-02 18:30:42.675320'),(30,'article','0005_auto_20200503_0230','2020-05-02 18:30:43.042727'),(31,'django_q','0001_initial','2020-05-03 06:08:22.048521'),(32,'django_q','0002_auto_20150630_1624','2020-05-03 06:08:22.285831'),(33,'django_q','0003_auto_20150708_1326','2020-05-03 06:08:22.467160'),(34,'django_q','0004_auto_20150710_1043','2020-05-03 06:08:22.476815'),(35,'django_q','0005_auto_20150718_1506','2020-05-03 06:08:22.516119'),(36,'django_q','0006_auto_20150805_1817','2020-05-03 06:08:22.615356'),(37,'django_q','0007_ormq','2020-05-03 06:08:22.674847'),(38,'django_q','0008_auto_20160224_1026','2020-05-03 06:08:22.680832'),(39,'django_q','0009_auto_20171009_0915','2020-05-03 06:08:22.769035'),(40,'article','0006_auto_20200503_1441','2020-05-03 06:41:28.684695'),(41,'soft','0008_software_modification','2020-05-04 08:42:41.164328'),(42,'soft','0009_software_tag_tag','2020-05-04 09:10:02.943131'),(43,'soft','0010_auto_20200504_1712','2020-05-04 09:12:32.811088'),(44,'soft','0011_auto_20200504_1720','2020-05-04 09:20:49.597880'),(45,'soft','0012_auto_20200504_1800','2020-05-04 10:00:33.381536'),(46,'soft','0013_auto_20200504_1904','2020-05-04 11:08:24.525175'),(47,'article','0007_remove_article_author','2020-05-04 11:36:53.139905'),(48,'soft','0014_auto_20200504_1936','2020-05-04 11:47:24.636502'),(49,'user','0002_auto_20200504_1936','2020-05-04 11:48:13.676089'),(50,'feedback','0001_initial','2020-05-04 16:00:57.648116'),(51,'feedback','0002_auto_20200505_0210','2020-05-04 18:10:32.625888'),(52,'feedback','0003_auto_20200505_0212','2020-05-04 18:12:36.907285'),(53,'article','0002_article_author','2020-05-05 08:21:59.019539'),(54,'feedback','0004_auto_20200505_2128','2020-05-05 13:28:18.948134'),(55,'soft','0002_classification_value_visibility','2020-05-05 13:28:19.019944'),(56,'soft','0003_delete_software_tag','2020-05-05 17:04:32.478688'),(57,'soft','0004_tag_softwares','2020-05-05 17:07:47.532687'),(58,'soft','0005_tag_articles','2020-05-05 17:34:16.369060'),(59,'soft','0006_software_size','2020-05-06 10:17:28.837357'),(60,'software','0001_initial','2020-05-06 11:55:53.845597'),(61,'article','0002_auto_20200506_2109','2020-05-06 13:09:55.845550'),(62,'software','0002_auto_20200506_2108','2020-05-06 13:10:39.407519'),(63,'software','0003_auto_20200506_2109','2020-05-06 14:42:28.895467'),(64,'user','0002_auto_20200506_2237','2020-05-06 14:42:28.993524'),(65,'article','0003_auto_20200507_1809','2020-05-07 10:09:41.512459'),(66,'software','0004_auto_20200507_1809','2020-05-07 10:09:41.803131'),(67,'user','0003_auto_20200507_1809','2020-05-07 10:09:41.922988'),(68,'software','0005_delete_software_classification_value','2020-05-07 16:29:12.984535'),(69,'software','0006_classification_value_softwares','2020-05-07 16:29:49.178760'),(70,'software','0007_remove_classification_value_softwares','2020-05-07 16:48:44.857110'),(71,'software','0008_classification_value_softwares','2020-05-07 16:48:44.919942');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_q_ormq`
--

DROP TABLE IF EXISTS `django_q_ormq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_q_ormq` (
  `id` int NOT NULL AUTO_INCREMENT,
  `key` varchar(100) NOT NULL,
  `payload` longtext NOT NULL,
  `lock` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_q_ormq`
--

LOCK TABLES `django_q_ormq` WRITE;
/*!40000 ALTER TABLE `django_q_ormq` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_q_ormq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_q_schedule`
--

DROP TABLE IF EXISTS `django_q_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_q_schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `func` varchar(256) NOT NULL,
  `hook` varchar(256) DEFAULT NULL,
  `args` longtext,
  `kwargs` longtext,
  `schedule_type` varchar(1) NOT NULL,
  `repeats` int NOT NULL,
  `next_run` datetime(6) DEFAULT NULL,
  `task` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `minutes` smallint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `django_q_schedule_chk_1` CHECK ((`minutes` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_q_schedule`
--

LOCK TABLES `django_q_schedule` WRITE;
/*!40000 ALTER TABLE `django_q_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_q_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_q_task`
--

DROP TABLE IF EXISTS `django_q_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_q_task` (
  `name` varchar(100) NOT NULL,
  `func` varchar(256) NOT NULL,
  `hook` varchar(256) DEFAULT NULL,
  `args` longtext,
  `kwargs` longtext,
  `result` longtext,
  `started` datetime(6) NOT NULL,
  `stopped` datetime(6) NOT NULL,
  `success` tinyint(1) NOT NULL,
  `id` varchar(32) NOT NULL,
  `group` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_q_task`
--

LOCK TABLES `django_q_task` WRITE;
/*!40000 ALTER TABLE `django_q_task` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_q_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5uhe4xv32rl9c5x4bbpodnp94zouh9kz','NWMxZTgxYjZkN2ZkNzc5YmJiZWViNDA4OWViYmY4ZjkyZTIzNDljMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmMmI1Y2VkYzc0YzgxNDc0YjQ2NGRkNTczZGE0NGU0YTY2M2UxMTljIn0=','2020-05-20 14:41:07.670710');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_feedback`
--

DROP TABLE IF EXISTS `feedback_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback_feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `comment` longtext,
  `date` datetime(6) NOT NULL,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_feedback_client_id_16534924_fk_user_user_id` (`client_id`),
  CONSTRAINT `feedback_feedback_client_id_16534924_fk_user_user_id` FOREIGN KEY (`client_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_feedback`
--

LOCK TABLES `feedback_feedback` WRITE;
/*!40000 ALTER TABLE `feedback_feedback` DISABLE KEYS */;
INSERT INTO `feedback_feedback` VALUES (1,'Анастасия','+ 7 901 668-60-77','bbbb','2020-05-04 18:12:47.071595',NULL);
/*!40000 ALTER TABLE `feedback_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soft_software`
--

DROP TABLE IF EXISTS `soft_software`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soft_software` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `description` longtext NOT NULL,
  `description_medium` longtext NOT NULL,
  `description_small` longtext NOT NULL,
  `date_of_delete` varchar(20) DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `modification` tinyint(1) NOT NULL,
  `size` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soft_software`
--

LOCK TABLES `soft_software` WRITE;
/*!40000 ALTER TABLE `soft_software` DISABLE KEYS */;
INSERT INTO `soft_software` VALUES (1,'Грузоперевозки',10000,'Это приложение позволяет управлять заказами грузоперевозок. \r\nЭффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\n Это приложение позволяет управлять заказами грузоперевозок.\r\nЭффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\nвозможность аналитической работы с бизнесом: количество о заказов и многое другое.\r\n\r\nЭффективное управление бизнесом при помощи этого приложения. \r\n Выполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\nЭто приложение позволяет управлять заказами грузоперевозок.\r\n Эффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.\r\n\r\n\r\nЭффективное управление бизнесом при помощи этого приложения. \r\n Выполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\nЭто приложение позволяет управлять заказами грузоперевозок.\r\n Эффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.','Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.','Направление справа налево (в rtl слева направо).',NULL,1,1,NULL),(2,'Кафе',0,'Для описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.','Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налевои, сверху вниз или снизу вверх.','Flex-элементы выкладываются в строку',NULL,1,0,100000);
/*!40000 ALTER TABLE `soft_software` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software!_classification`
--

DROP TABLE IF EXISTS `software!_classification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software!_classification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `date_of_delete` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software!_classification`
--

LOCK TABLES `software!_classification` WRITE;
/*!40000 ALTER TABLE `software!_classification` DISABLE KEYS */;
/*!40000 ALTER TABLE `software!_classification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software!_classification_value`
--

DROP TABLE IF EXISTS `software!_classification_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software!_classification_value` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(200) NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `classification_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_classificat_classification_id_9fa77065_fk_software_` (`classification_id`),
  CONSTRAINT `software_classificat_classification_id_9fa77065_fk_software_` FOREIGN KEY (`classification_id`) REFERENCES `software!_classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software!_classification_value`
--

LOCK TABLES `software!_classification_value` WRITE;
/*!40000 ALTER TABLE `software!_classification_value` DISABLE KEYS */;
/*!40000 ALTER TABLE `software!_classification_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software!_software_classification_value`
--

DROP TABLE IF EXISTS `software!_software_classification_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software!_software_classification_value` (
  `id` int NOT NULL AUTO_INCREMENT,
  `classification_value_id` int NOT NULL,
  `software_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_software_cl_classification_value_a4c86c62_fk_software_` (`classification_value_id`),
  KEY `software_software_cl_software_id_bb5d3ebb_fk_software_` (`software_id`),
  CONSTRAINT `software_software_cl_classification_value_a4c86c62_fk_software_` FOREIGN KEY (`classification_value_id`) REFERENCES `software!_classification_value` (`id`),
  CONSTRAINT `software_software_cl_software_id_bb5d3ebb_fk_software_` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software!_software_classification_value`
--

LOCK TABLES `software!_software_classification_value` WRITE;
/*!40000 ALTER TABLE `software!_software_classification_value` DISABLE KEYS */;
/*!40000 ALTER TABLE `software!_software_classification_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software!_tag`
--

DROP TABLE IF EXISTS `software!_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software!_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` longtext NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `date_of_delete` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software!_tag`
--

LOCK TABLES `software!_tag` WRITE;
/*!40000 ALTER TABLE `software!_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `software!_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software!_tag_articles`
--

DROP TABLE IF EXISTS `software!_tag_articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software!_tag_articles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tag_id` int NOT NULL,
  `article_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `software_tag_articles_tag_id_article_id_f44f692d_uniq` (`tag_id`,`article_id`),
  KEY `software_tag_articles_article_id_b235881a_fk_article_article_id` (`article_id`),
  CONSTRAINT `software_tag_articles_article_id_b235881a_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`),
  CONSTRAINT `software_tag_articles_tag_id_c6cae2d2_fk_software_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `software!_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software!_tag_articles`
--

LOCK TABLES `software!_tag_articles` WRITE;
/*!40000 ALTER TABLE `software!_tag_articles` DISABLE KEYS */;
/*!40000 ALTER TABLE `software!_tag_articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_addition`
--

DROP TABLE IF EXISTS `software_addition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_addition` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `kind` tinyint(1) NOT NULL,
  `size` tinyint(1) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `software_id` int DEFAULT NULL,
  `is_main` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_addition_software_id_c60543b6_fk_software_software_id` (`software_id`),
  KEY `software_addition_date_of_delete_38c55ff3` (`date_of_delete`),
  CONSTRAINT `software_addition_software_id_c60543b6_fk_software_software_id` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_addition`
--

LOCK TABLES `software_addition` WRITE;
/*!40000 ALTER TABLE `software_addition` DISABLE KEYS */;
INSERT INTO `software_addition` VALUES (1,'Главная картинка',1,1,'soft/pizza.jpg',NULL,1,0),(2,'Применение',1,1,'soft/цветы-птица_6YvpoHP.jpg',NULL,1,1);
/*!40000 ALTER TABLE `software_addition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_classification`
--

DROP TABLE IF EXISTS `software_classification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_classification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification`
--

LOCK TABLES `software_classification` WRITE;
/*!40000 ALTER TABLE `software_classification` DISABLE KEYS */;
INSERT INTO `software_classification` VALUES (2,'Область применения',NULL,1),(3,'Вид',NULL,1),(4,'Тип использования',NULL,1),(5,'Ограничение доступа',NULL,1),(6,'Дополнительные установки',NULL,1),(7,'Установка',NULL,1);
/*!40000 ALTER TABLE `software_classification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_classification_value`
--

DROP TABLE IF EXISTS `software_classification_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_classification_value` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(200) DEFAULT NULL,
  `classification_id` int DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soft_classification__classification_id_1eb7dd81_fk_soft_clas` (`classification_id`),
  KEY `software_classification_value_visibility_62c1ea04` (`visibility`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification_value`
--

LOCK TABLES `software_classification_value` WRITE;
/*!40000 ALTER TABLE `software_classification_value` DISABLE KEYS */;
INSERT INTO `software_classification_value` VALUES (3,'Настольное приложение',3,1),(4,'Сайт',3,1),(5,'Мобильное приложение',3,1),(6,'Грузоперевозки',2,1),(7,'Перевозки',2,1),(8,'Групповой доступ',4,1),(9,'Без разделения ролей',5,1),(10,'Разделение ролей',5,1),(11,'Не требуются',6,1),(12,'Не требуется',7,1),(13,'Требуется',7,1),(14,'Требуются',6,1);
/*!40000 ALTER TABLE `software_classification_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_classification_value_softwares`
--

DROP TABLE IF EXISTS `software_classification_value_softwares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_classification_value_softwares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `classification_value_id` int NOT NULL,
  `software_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `software_classification__classification_value_id__334be279_uniq` (`classification_value_id`,`software_id`),
  KEY `software_classificat_software_id_32821c6e_fk_software_` (`software_id`),
  CONSTRAINT `software_classificat_classification_value_97ba4229_fk_software_` FOREIGN KEY (`classification_value_id`) REFERENCES `software_classification_value` (`id`),
  CONSTRAINT `software_classificat_software_id_32821c6e_fk_software_` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification_value_softwares`
--

LOCK TABLES `software_classification_value_softwares` WRITE;
/*!40000 ALTER TABLE `software_classification_value_softwares` DISABLE KEYS */;
INSERT INTO `software_classification_value_softwares` VALUES (1,3,1),(5,3,2),(6,4,2),(2,6,1),(4,7,1),(3,8,1),(7,8,2),(8,9,1),(9,10,2),(12,11,2),(10,12,1),(13,12,2),(11,14,1);
/*!40000 ALTER TABLE `software_classification_value_softwares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_software`
--

DROP TABLE IF EXISTS `software_software`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_software` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `is_free` tinyint(1) NOT NULL,
  `price` double NOT NULL,
  `description` longtext NOT NULL,
  `description_medium` longtext NOT NULL,
  `description_small` longtext NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `modification` tinyint(1) NOT NULL,
  `size` double DEFAULT NULL,
  `date_of_delete` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `software_software_date_of_delete_5fecbd2a` (`date_of_delete`),
  KEY `software_software_visibility_d0b118f5` (`visibility`),
  KEY `software_software_is_free_a5a171c5` (`is_free`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_software`
--

LOCK TABLES `software_software` WRITE;
/*!40000 ALTER TABLE `software_software` DISABLE KEYS */;
INSERT INTO `software_software` VALUES (1,'Грузоперевозки',0,10000,'Это приложение позволяет управлять заказами грузоперевозок. \r\nЭффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\n Это приложение позволяет управлять заказами грузоперевозок.\r\nЭффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\nвозможность аналитической работы с бизнесом: количество о заказов и многое другое.\r\n\r\nЭффективное управление бизнесом при помощи этого приложения. \r\n Выполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\nЭто приложение позволяет управлять заказами грузоперевозок.\r\n Эффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.\r\n\r\n\r\nЭффективное управление бизнесом при помощи этого приложения. \r\n Выполнение соновной работы по работника: грузчикам, водителям),\r\n автомобилям, заказам. Также в этом приложении осуществяется\r\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\r\nЭто приложение позволяет управлять заказами грузоперевозок.\r\n Эффективное управление бизнесом при помощи этого приложения. \r\nВыполнение соновной работы по работника: грузчикам, водителям),\r\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.','Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.','Направление справа налево (в rtl слева направо).',1,1,1,NULL),(2,'Кафе',1,0,'Для описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\r\n\r\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.','Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налевои, сверху вниз или снизу вверх.','Flex-элементы выкладываются в строку',1,0,10000,NULL),(3,'Автодоставка',0,20000,'Если some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:\r\nЕсли some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\n\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:\r\nЕсли some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\n\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:\r\nЕсли some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\n\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:\r\nЕсли some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\n\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:Если some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.\r\n\r\nupdate\r\nupdate(**kwargs)\r\nВыполняет SQL запрос обновляющий данные указанных полей и возвращает количество измененных записей(которое может быть не равно количеству обновленных записей, если некоторые из них уже содержали новое значение).\r\n\r\nНапример, чтобы отключить комментарии для всех записей опубликованных в 2010 годы, нужно выполнить такой запрос:\r\n\r\n>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)\r\n(Пример подразумевает что модель Entry содержит поля pub_date и comments_on.)\r\n\r\nВы можете изменить несколько полей — нет ограничения на количество полей. Например, изменим поля comments_on и headline:','Если some_queryset не был еще вычислен, но вы точно знаете что будет вычислен в любом случае, тогда вызов some_query_set.exists() выполнит больше работы (один запрос для проверки наличия данных и один для получения данных) чем просто bool(some_queryset), который получит результат и проверит не пустой ли он.','Если some_queryset не был еще вычислен, но вы точн',1,1,NULL,NULL);
/*!40000 ALTER TABLE `software_software` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_tag`
--

DROP TABLE IF EXISTS `software_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` longtext NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_tag_visibility_bf251d73` (`visibility`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag`
--

LOCK TABLES `software_tag` WRITE;
/*!40000 ALTER TABLE `software_tag` DISABLE KEYS */;
INSERT INTO `software_tag` VALUES (1,'Платно','',NULL,1),(2,'Бесплатно','',NULL,1),(3,'Перевозки','',NULL,1),(4,'Доставка','',NULL,1);
/*!40000 ALTER TABLE `software_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_tag_articles`
--

DROP TABLE IF EXISTS `software_tag_articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_tag_articles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tag_id` int NOT NULL,
  `article_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `soft_tag_articles_tag_id_article_id_e09bc410_uniq` (`tag_id`,`article_id`),
  KEY `soft_tag_articles_article_id_5fd29c29_fk_article_article_id` (`article_id`),
  CONSTRAINT `soft_tag_articles_article_id_5fd29c29_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`),
  CONSTRAINT `soft_tag_articles_tag_id_2be17424_fk_soft_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `software_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag_articles`
--

LOCK TABLES `software_tag_articles` WRITE;
/*!40000 ALTER TABLE `software_tag_articles` DISABLE KEYS */;
INSERT INTO `software_tag_articles` VALUES (1,3,1),(2,3,2),(3,4,2);
/*!40000 ALTER TABLE `software_tag_articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_tag_softwares`
--

DROP TABLE IF EXISTS `software_tag_softwares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_tag_softwares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tag_id` int NOT NULL,
  `software_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `soft_tag_softwares_tag_id_software_id_4ec3c2eb_uniq` (`tag_id`,`software_id`),
  KEY `soft_tag_softwares_software_id_cbd47422_fk_soft_software_id` (`software_id`),
  CONSTRAINT `soft_tag_softwares_software_id_cbd47422_fk_soft_software_id` FOREIGN KEY (`software_id`) REFERENCES `soft_software` (`id`),
  CONSTRAINT `soft_tag_softwares_tag_id_0538fc1f_fk_soft_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `software_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag_softwares`
--

LOCK TABLES `software_tag_softwares` WRITE;
/*!40000 ALTER TABLE `software_tag_softwares` DISABLE KEYS */;
INSERT INTO `software_tag_softwares` VALUES (1,1,1),(2,2,2),(3,3,1),(4,4,1);
/*!40000 ALTER TABLE `software_tag_softwares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kind` varchar(3) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `patronymic` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `phone_second` varchar(20) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_user_date_of_delete_9e91f2ce` (`date_of_delete`),
  KEY `user_user_kind_443daf06` (`kind`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES (1,'AUT','Иванова','Анастасия','Максимовна','+ 7 933 666-66-77','+ 7 933 666-66-00','nnnnnnnn@mail.ru','2016-11-02',NULL),(2,'AUT','Мужиков','Артем','Олегович','+ 7 901 668-60-11','+ 7 933 666-66-11','aaaaaaaaaaa@mail.ru','1995-03-07',NULL);
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-09 14:40:03
