CREATE DATABASE  IF NOT EXISTS `new_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `new_db`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: new_db
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
  `image` varchar(100) NOT NULL,
  `date_of_review` date DEFAULT NULL,
  `date_of_delete` date DEFAULT NULL,
  `author_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_article_visibility_0ceb05a7` (`visibility`),
  KEY `article_article_date_of_delete_63cd03f4` (`date_of_delete`),
  KEY `article_article_author_id_e6b479f8_fk_user_customuser_id` (`author_id`),
  CONSTRAINT `article_article_author_id_e6b479f8_fk_user_customuser_id` FOREIGN KEY (`author_id`) REFERENCES `user_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_article`
--

LOCK TABLES `article_article` WRITE;
/*!40000 ALTER TABLE `article_article` DISABLE KEYS */;
INSERT INTO `article_article` VALUES (1,'ЛУЧШИЕ ОНЛАЙН-УНИВЕРСИТЕТЫ МИРА С БЕСПЛАТНЫМ ОБУЧЕНИЕМ','Мы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\\r\\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\\r\\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\\r\\n\\r\\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\\r\\n\\r\\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\\r\\n\\r\\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\\r\\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\\r\\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\\r\\n\\r\\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\\r\\n\\r\\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.\\r\\n\\r\\nМы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\\r\\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\\r\\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\\r\\n\\r\\nГлавный исполнительный директор Курт Торнтон рассказывает, что HoloVision отличается от голограмм, что создаются лазером, тем, что для получения голографического изображения в человеческий рост Provision 3D Media будет использовать новейший «фирменный источник света».\\r\\n\\r\\nПолноразмерные голограммы найдут широкое применение в розничной торговле в игровой индустрии, рекламе, бизнесе и других сферах. Также голограммы в полный рост в скором времени появятся и в обычных домах. Если ранее ученым было не известно, как это сделать, то теперь новый, современный, автоматический дом с голограммами, станет реальностью в ближайшие 10-20 лет.',1,'article/цели.jpg','2020-05-23',NULL,NULL),(2,'Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации','Мы видели голограммы в кино. Теперь настало время их увидеть в своем доме!\\r\\nКомпания Provision 3D Media собирает 950 000 долл. на реализацию современного проекта HoloVision, который связан с полноразмерными голографическими изображениями. Новая технология позволит создать голографические дисплеи размером до 52 дюймов.\\r\\nВ компании решили искать деньги на уникальную разработку - прототип системы, которая создает голограмму в натуральную величину.\\r\\n\\r\\n',1,'article/s1200.jpg','2020-04-07',NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add Заказ звонка',1,'add_feedback'),(2,'Can change Заказ звонка',1,'change_feedback'),(3,'Can delete Заказ звонка',1,'delete_feedback'),(4,'Can view Заказ звонка',1,'view_feedback'),(5,'Can add Отзыв',2,'add_review'),(6,'Can change Отзыв',2,'change_review'),(7,'Can delete Отзыв',2,'delete_review'),(8,'Can view Отзыв',2,'view_review'),(9,'Can add Приложение',3,'add_review_addition'),(10,'Can change Приложение',3,'change_review_addition'),(11,'Can delete Приложение',3,'delete_review_addition'),(12,'Can view Приложение',3,'view_review_addition'),(13,'Can add Пользователь',4,'add_customuser'),(14,'Can change Пользователь',4,'change_customuser'),(15,'Can delete Пользователь',4,'delete_customuser'),(16,'Can view Пользователь',4,'view_customuser'),(17,'Can add Статья',5,'add_article'),(18,'Can change Статья',5,'change_article'),(19,'Can delete Статья',5,'delete_article'),(20,'Can view Статья',5,'view_article'),(21,'Can add Классификация',6,'add_classification'),(22,'Can change Классификация',6,'change_classification'),(23,'Can delete Классификация',6,'delete_classification'),(24,'Can view Классификация',6,'view_classification'),(25,'Can add ПО',7,'add_software'),(26,'Can change ПО',7,'change_software'),(27,'Can delete ПО',7,'delete_software'),(28,'Can view ПО',7,'view_software'),(29,'Can add Тег',8,'add_tag'),(30,'Can change Тег',8,'change_tag'),(31,'Can delete Тег',8,'delete_tag'),(32,'Can view Тег',8,'view_tag'),(33,'Can add Классификация_значение',9,'add_classification_value'),(34,'Can change Классификация_значение',9,'change_classification_value'),(35,'Can delete Классификация_значение',9,'delete_classification_value'),(36,'Can view Классификация_значение',9,'view_classification_value'),(37,'Can add Приложение',10,'add_addition'),(38,'Can change Приложение',10,'change_addition'),(39,'Can delete Приложение',10,'delete_addition'),(40,'Can view Приложение',10,'view_addition'),(41,'Can add log entry',11,'add_logentry'),(42,'Can change log entry',11,'change_logentry'),(43,'Can delete log entry',11,'delete_logentry'),(44,'Can view log entry',11,'view_logentry'),(45,'Can add permission',12,'add_permission'),(46,'Can change permission',12,'change_permission'),(47,'Can delete permission',12,'delete_permission'),(48,'Can view permission',12,'view_permission'),(49,'Can add group',13,'add_group'),(50,'Can change group',13,'change_group'),(51,'Can delete group',13,'delete_group'),(52,'Can view group',13,'view_group'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session'),(61,'Can add Избранное',16,'add_favourite'),(62,'Can change Избранное',16,'change_favourite'),(63,'Can delete Избранное',16,'delete_favourite'),(64,'Can view Избранное',16,'view_favourite'),(65,'Can add Комментарий',17,'add_comment'),(66,'Can change Комментарий',17,'change_comment'),(67,'Can delete Комментарий',17,'delete_comment'),(68,'Can view Комментарий',17,'view_comment'),(69,'Can add Обсуждение',18,'add_discussion'),(70,'Can change Обсуждение',18,'change_discussion'),(71,'Can delete Обсуждение',18,'delete_discussion'),(72,'Can view Обсуждение',18,'view_discussion'),(73,'Can add Заказ',19,'add_order'),(74,'Can change Заказ',19,'change_order'),(75,'Can delete Заказ',19,'delete_order'),(76,'Can view Заказ',19,'view_order');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussion_comment`
--

DROP TABLE IF EXISTS `discussion_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discussion_comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email_phone` varchar(60) DEFAULT NULL,
  `content` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `client_id` int DEFAULT NULL,
  `discussion_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `discussion_comment_discussion_id_458a5179_fk_discussio` (`discussion_id`),
  KEY `discussion_comment_date_of_delete_2d965785` (`date_of_delete`),
  KEY `discussion_comment_visibility_04985e96` (`visibility`),
  KEY `discussion_comment_client_id_9a2844f9_fk_user_customuser_id` (`client_id`),
  CONSTRAINT `discussion_comment_client_id_9a2844f9_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `discussion_comment_discussion_id_458a5179_fk_discussio` FOREIGN KEY (`discussion_id`) REFERENCES `discussion_discussion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_comment`
--

LOCK TABLES `discussion_comment` WRITE;
/*!40000 ALTER TABLE `discussion_comment` DISABLE KEYS */;
INSERT INTO `discussion_comment` VALUES (3,NULL,NULL,'Огромное спасмбо за отзыв! Огромное спасмбо за отзыв! Огромное спасмбо за отзыв! Мы стараемся радовать вас с каждым выходом нового ПО!','2020-05-31 13:43:15.688988',NULL,1,2,1),(4,NULL,'fdddd@mal.ff','Огромное спасмбо за отзыв! Огромное спасмбо за отзыв!','2020-05-03 13:43:31.127200',NULL,1,NULL,1),(5,NULL,NULL,'Огромное спасмбо за отзыв!','2020-05-31 13:43:41.769178',NULL,1,2,3),(6,'Иван','89555555550','Привет, согласна с вами!','2020-05-20 14:05:23.483935',NULL,1,NULL,2),(34,'Анастасия','fdddd@mal.ff','<div class=\"container\">\n    <h2>Greetings</h2>\n    <div class=\"inner\">Hello</div>\n    <div class=\"inner\">Goodbye</div>\n</div>','2020-06-05 09:44:57.654735',NULL,1,NULL,34),(35,'Иван','89555555555','ddd','2020-06-05 10:33:04.216554',NULL,1,NULL,34),(36,'Платно','89555555555','ddddd','2020-06-05 10:33:19.327980',NULL,1,NULL,32),(37,'Иван','fdddd@mal.ff','dddd','2020-06-05 10:34:48.134298',NULL,1,NULL,31),(38,'Анастасия','89555555555','дадаададдадада','2020-06-05 10:37:51.849752',NULL,1,NULL,29),(51,'Анастасия','89555555555','иимим','2020-06-05 11:37:12.954339',NULL,1,NULL,30),(52,'Иван','fdddd@mal.ff','вввв','2020-06-05 11:37:30.535022',NULL,1,NULL,30),(53,'Кирилл','89555555550','ввввввцццццццц','2020-06-05 11:37:48.952747',NULL,1,NULL,30),(54,'Анастасия','fdddd@mal.ff','eeeeee','2020-06-05 11:42:51.719258',NULL,1,NULL,22),(55,'Иван','fdddd@mal.ff','eeee','2020-06-05 11:43:09.026437',NULL,1,NULL,22),(56,'Иван','89555555555','qqqqqqqqqqqq','2020-06-06 10:07:34.093438',NULL,1,NULL,23),(57,'Кирилл','89555555555','йййййй','2020-06-06 10:42:09.210208',NULL,1,NULL,34),(58,'Анастасия','fdddd@mal.ff','qqqqqqq','2020-06-08 07:20:28.175785',NULL,1,NULL,35),(59,'Анастасия','89555555555d@fffffff.dddd','йййй','2020-06-08 07:31:02.688824',NULL,1,NULL,24),(60,'Платон','89555555555','ыыыы','2020-06-08 11:14:27.341650',NULL,1,NULL,45),(61,'Иван','89555555555','уууквуауыв','2020-06-08 11:14:50.758118',NULL,1,NULL,46),(62,'Кирилл','89555555555d@fffffff.dddd','уууууу','2020-06-08 11:15:45.757721',NULL,1,NULL,47),(63,'Кирилл','fdddd@mal.ff','hghbhhh','2020-06-08 11:28:06.522558',NULL,1,NULL,48),(64,'Анастасия','89555555555','wwww','2020-06-08 11:32:25.823139',NULL,1,NULL,49),(65,'Анастасия','fdddd@mal.ff','eeeee','2020-06-08 11:34:22.276540',NULL,1,NULL,50),(66,'Анастасия','89555555555','qqqq','2020-06-08 11:37:49.490174',NULL,1,NULL,51),(67,'Анастасия','ndmitrievnaa@mail.ru','qwqwqwqwqw','2020-06-08 11:54:56.551254',NULL,1,NULL,52),(68,'Анастасия','ndmitrievnaa@mail.ru','1212122121212121','2020-06-08 11:57:51.493362',NULL,1,NULL,53),(69,'Иван','fdddd@mal.ff','dsddsdsdsds','2020-06-08 11:59:19.323690',NULL,1,NULL,54),(70,'Анастасия','fdddd@mal.ff','qqqqq','2020-06-08 12:04:35.589746',NULL,1,NULL,55),(71,'Анастасия','89555555555','gggggg','2020-06-08 12:04:48.496906',NULL,1,NULL,55),(72,'Анастасия','89555555555','fffff','2020-06-08 12:05:16.090935',NULL,1,NULL,54),(73,'Анастасия','89555555555','44444','2020-06-08 12:08:28.087664',NULL,1,NULL,56),(74,'Кирилл','fdddd@mal.ff','77777','2020-06-08 12:19:34.070507',NULL,1,NULL,57),(75,'Анастасия','89555555555d@fffffff.dddd','3333','2020-06-08 12:21:24.746910',NULL,1,NULL,58),(76,'Анастасия','89555555555','77777','2020-06-08 12:22:59.156760',NULL,1,NULL,59),(77,'Анастасия','89555555555','yhththt','2020-06-08 12:23:18.858149',NULL,1,NULL,59),(78,'Анастасия','fdddd@mal.ff','7777','2020-06-08 12:24:46.561275',NULL,1,NULL,60),(79,'Анастасия','fdddd@mal.ff','222222','2020-06-08 12:29:06.607376',NULL,1,NULL,61),(80,'Анастасия','89555555555','hnnhh','2020-06-08 12:29:19.682631',NULL,1,NULL,61),(81,'Анастасия','fdddd@mal.ff','dddddd','2020-06-08 12:30:33.111176',NULL,1,NULL,62),(82,'Анастасия','fdddd@mal.ff','tttt','2020-06-08 12:32:29.876036',NULL,1,NULL,63),(83,'Анастасия','fdddd@mal.ff','rrrrrrr','2020-06-08 12:32:42.936893',NULL,1,NULL,63),(84,'Анастасия','fdddd@mal.ff','праппаа','2020-06-08 12:32:54.631992',NULL,1,NULL,63),(85,'Анастасия','fdddd@mal.ff','аааа','2020-06-08 12:35:41.530848',NULL,1,NULL,62),(86,'Анастасия','fdddd@mal.ff','ллллл','2020-06-08 13:08:01.387971',NULL,1,NULL,64),(87,'Анастасия','fdddd@mal.ff','ававав','2020-06-08 13:08:54.888752',NULL,1,NULL,64),(88,'Анастасия','89555555555','нгнгнгнгн','2020-06-08 13:10:54.548104',NULL,1,NULL,65),(89,'Анастасия','fdddd@mal.ff','6666','2020-06-08 13:11:45.065990',NULL,1,NULL,66),(90,'Анастасия','fdddd@mal.ff','55555','2020-06-08 13:11:56.728334',NULL,1,NULL,66),(91,'Анастасия','89555555555d@fffffff.dddd','онноно','2020-06-08 13:12:13.589441',NULL,1,NULL,66);
/*!40000 ALTER TABLE `discussion_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussion_discussion`
--

DROP TABLE IF EXISTS `discussion_discussion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discussion_discussion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email_phone` varchar(60) DEFAULT NULL,
  `content` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `client_id` int DEFAULT NULL,
  `software_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `discussion_discussion_client_id_a9c05a76_fk_user_customuser_id` (`client_id`),
  KEY `discussion_discussio_software_id_91db9453_fk_software_` (`software_id`),
  KEY `discussion_discussion_date_of_delete_6f163ab1` (`date_of_delete`),
  KEY `discussion_discussion_visibility_65c28825` (`visibility`),
  CONSTRAINT `discussion_discussio_software_id_91db9453_fk_software_` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`),
  CONSTRAINT `discussion_discussion_client_id_a9c05a76_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_discussion`
--

LOCK TABLES `discussion_discussion` WRITE;
/*!40000 ALTER TABLE `discussion_discussion` DISABLE KEYS */;
INSERT INTO `discussion_discussion` VALUES (1,NULL,NULL,'Замечательная программа! Не могу нарадоваться! Приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Приложение станет совершенно идеальным для меня! Спасибо вам!','2020-05-31 10:34:26.107778',NULL,1,2,1),(2,'Светлана','89555555555','Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня!','2020-05-31 11:23:28.847014',NULL,1,NULL,1),(3,'Антон','89555555555','Огромное спасмбо за отзыв! Мы стараемся радовать вас с каждым выходом нового ПО!Огромное спасмбо за отзыв! Мы стараемся радовать вас с каждым выходом нового ПО!Огромное спасмбо за отзыв! Мы стараемся радовать вас с каждым выходом нового ПО!','2020-05-31 13:00:49.615141',NULL,1,NULL,2),(22,'Петр','89555555555','Спасибо, классно!','2020-06-04 13:54:58.303379',NULL,1,NULL,1),(23,'Иван','fdddd@mal.ff','Круто!','2020-06-04 13:56:26.278879',NULL,1,NULL,1),(24,'Иван','89555555555','Привет, круто!','2020-06-04 14:01:44.946440',NULL,1,NULL,1),(29,'Кирилл','89555555555d@fffffff.dddd','Спасибо !','2020-06-05 09:30:16.175418',NULL,1,NULL,1),(30,'Филипп','89555555555','сли вы указали название события \"click\", то все события данного типа будут устранены. Если вы пишите jQuery плагин или просто работаете над большим проектом, то советуем использовать пространства имён. Все события из специфического пространства имён могут быть удалены после указания названия. К примеру, \".myPlugin\".\nДля удаления обработчиков, необходимо указывать параметр selector, в точности совпадающий с таким же параметром, использованным в методе .on(). Если нужно удалить с элементов все обработчики, следует в параметре selector указать значение — \'**\'.','2020-06-05 09:31:49.548382',NULL,1,NULL,1),(31,'Артемий','89555555555d@fffffff.dddd','функция\nТип: Function ( Integer elementOfArray, String html) => htmlString или Element или Text или jQuery\nФункция, которая возвращает строку HTML, элемент (ы) DOM, текстовый узел (ы) или объект jQuery для вставки в начале каждого элемента в наборе соответствующих элементов. Получает позицию индекса элемента в наборе и старое значение HTML элемента в качестве аргументов. Внутри функции thisотносится к текущему элементу в наборе.','2020-06-05 09:35:19.111401',NULL,1,NULL,1),(32,'Иван','89555555555','<h2>Greetings</h2>\n<div class=\"container\">\n  <div class=\"inner\">Hello</div>\n  <div class=\"inner\">Goodbye</div>\n</div>','2020-06-05 09:37:30.515376',NULL,1,NULL,1),(34,'Иван','fdddd@mal.ff','аааа','2020-06-05 09:41:07.480493',NULL,1,NULL,1),(35,'Анастасия','89555555555','йййййй','2020-06-06 11:47:32.561296',NULL,1,NULL,1),(36,'Анастасия','fdddd@mal.ff','11111','2020-06-08 07:20:05.153732',NULL,1,NULL,1),(37,'Анастасия','fdddd@mal.ff','11111','2020-06-08 07:21:33.748361',NULL,1,NULL,1),(38,'Анастасия','fdddd@mal.ff','ййййй','2020-06-08 07:37:52.791612',NULL,1,NULL,1),(39,'Кирилл','89555555550','Привет всем!','2020-06-08 07:56:59.895630',NULL,1,NULL,1),(40,'Иван','fdddd@mal.ff','Приветики!','2020-06-08 07:57:26.156363',NULL,1,NULL,1),(41,'Кирилл','fdddd@mal.ff','урааа','2020-06-08 07:58:39.968756',NULL,1,NULL,1),(42,'Анастасия','fdddd@mal.ff','111','2020-06-08 11:05:43.614020',NULL,1,NULL,1),(43,'Анастасия','fdddd@mal.ff','111','2020-06-08 11:06:28.536316',NULL,1,NULL,1),(44,'Анастасия','fdddd@mal.ff','ннннннннннннннн','2020-06-08 11:07:23.511311',NULL,1,NULL,1),(45,'Виктор','fdddd@mal.ff','Приветики!','2020-06-08 11:12:05.254708',NULL,1,NULL,1),(46,'Анастасия','fdddd@mal.ff','11йй','2020-06-08 11:14:39.438345',NULL,1,NULL,1),(47,'Кирилл','89555555555','авивимвпвпавмвпксе','2020-06-08 11:15:23.276263',NULL,1,NULL,1),(48,'Анастасия','89555555550','пппп','2020-06-08 11:27:57.664933',NULL,1,NULL,1),(49,'Анастасия','fdddd@mal.ff','bbbbbb','2020-06-08 11:32:19.161451',NULL,1,NULL,1),(50,'Анастасия','89555555550','fffff','2020-06-08 11:34:16.117298',NULL,1,NULL,1),(51,'Анастасия','fdddd@mal.ff','gggggg','2020-06-08 11:37:41.065773',NULL,1,NULL,1),(52,'Анастасия','fdddd@mal.ff','11111','2020-06-08 11:54:26.099830',NULL,1,NULL,1),(53,'Анастасия','fdddd@mal.ff','eeee','2020-06-08 11:57:41.404653',NULL,1,NULL,1),(54,'Кирилл','89555555550','ffffff','2020-06-08 11:59:11.026330',NULL,1,NULL,1),(55,'Платно','89555555550','wwwwwwww','2020-06-08 12:04:27.900435',NULL,1,NULL,1),(56,'Анастасия','fdddd@mal.ff','22222','2020-06-08 12:08:20.022047',NULL,1,NULL,1),(57,'Анастасия','fdddd@mal.ff','111111121212121','2020-06-08 12:19:25.698192',NULL,1,NULL,1),(58,'Платно','89555555550','5555','2020-06-08 12:21:17.897359',NULL,1,NULL,1),(59,'Анастасия','fdddd@mal.ff','77777','2020-06-08 12:22:51.855167',NULL,1,NULL,1),(60,'Анастасия','fdddd@mal.ff','000000','2020-06-08 12:24:39.839309',NULL,1,NULL,1),(61,'Анастасия','fdddd@mal.ff','eeee','2020-06-08 12:28:57.888169',NULL,1,NULL,1),(62,'Анастасия','fdddd@mal.ff','555','2020-06-08 12:30:25.204612',NULL,1,NULL,1),(63,'Кирилл','fdddd@mal.ff','3333','2020-06-08 12:32:21.853713',NULL,1,NULL,1),(64,'Анастасия','fdddd@mal.ff','вавававав','2020-06-08 13:07:48.511883',NULL,1,NULL,1),(65,'Анастасия','fdddd@mal.ff','ккк','2020-06-08 13:10:47.395196',NULL,1,NULL,1),(66,'Анастасия','fdddd@mal.ff','77777','2020-06-08 13:11:38.085042',NULL,1,NULL,1);
/*!40000 ALTER TABLE `discussion_discussion` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_user_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-05-23 05:40:44.269432','1','ЛУЧШИЕ ОНЛАЙН-УНИВЕРСИТЕТЫ МИРА С БЕСПЛАТНЫМ ОБУЧЕНИЕМ',1,'[{\"added\": {}}]',5,2),(2,'2020-05-23 05:41:35.995672','2','Автоматизированное кафе для доставки кофе на дом и в офис? а также способы автоматизации',1,'[{\"added\": {}}]',5,2),(3,'2020-05-23 05:41:56.659114','1','Feedback object (1)',1,'[{\"added\": {}}]',1,2),(4,'2020-05-23 05:42:04.284365','2','Feedback object (2)',1,'[{\"added\": {}}]',1,2),(5,'2020-05-23 05:42:27.214003','3','Feedback object (3)',1,'[{\"added\": {}}]',1,2),(6,'2020-05-23 05:44:40.437965','1','Review object (1)',1,'[{\"added\": {}}]',2,2),(7,'2020-05-23 05:45:29.668680','2','Review object (2)',1,'[{\"added\": {}}]',2,2),(8,'2020-05-23 05:45:39.261825','3','Review object (3)',1,'[{\"added\": {}}]',2,2),(9,'2020-05-23 05:46:32.045505','1','Платно',1,'[{\"added\": {}}]',3,2),(10,'2020-05-23 05:49:14.626831','1','Грузоперевозки',1,'[{\"added\": {}}]',7,2),(11,'2020-05-23 05:49:50.610187','2','Кафе',1,'[{\"added\": {}}]',7,2),(12,'2020-05-30 17:22:01.799531','1','Грузоперевозки',1,'[{\"added\": {}}]',10,2),(13,'2020-05-30 17:22:25.688628','2','Компьютер',1,'[{\"added\": {}}]',10,2),(14,'2020-05-30 17:22:38.039465','3','Кафе',1,'[{\"added\": {}}]',10,2),(15,'2020-05-30 17:37:18.127142','1','Платно',1,'[{\"added\": {}}]',8,2),(16,'2020-05-30 17:37:30.771818','2','Кафе',1,'[{\"added\": {}}]',8,2),(17,'2020-05-30 17:39:33.510295','3','Перевозки',1,'[{\"added\": {}}]',8,2),(18,'2020-05-30 17:39:47.635036','4','Бизнес',1,'[{\"added\": {}}]',8,2),(19,'2020-05-31 10:34:26.108775','1','Discussion object (1)',1,'[{\"added\": {}}]',18,2),(20,'2020-05-31 11:23:28.848012','2','Discussion object (2)',1,'[{\"added\": {}}]',18,2),(21,'2020-05-31 13:00:49.657393','3','Discussion object (3)',1,'[{\"added\": {}}]',18,2),(22,'2020-05-31 13:43:15.695971','3','Comment object (3)',1,'[{\"added\": {}}]',17,2),(23,'2020-05-31 13:43:31.129231','4','Comment object (4)',1,'[{\"added\": {}}]',17,2),(24,'2020-05-31 13:43:41.770139','5','Comment object (5)',1,'[{\"added\": {}}]',17,2),(25,'2020-05-31 14:05:23.485942','6','Comment object (6)',1,'[{\"added\": {}}]',17,2),(26,'2020-06-05 14:43:10.595190','3','Образование',1,'[{\"added\": {}}]',7,2),(27,'2020-06-05 15:39:51.768684','3','Образование',2,'[{\"changed\": {\"fields\": [\"\\u041c\\u0438\\u043d\\u0438-\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435 \\u041f\\u041e\"]}}]',7,2),(28,'2020-06-05 15:40:08.522327','2','Кафе',2,'[{\"changed\": {\"fields\": [\"\\u041c\\u0438\\u043d\\u0438-\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435 \\u041f\\u041e\"]}}]',7,2),(29,'2020-06-05 15:40:20.603951','1','Грузоперевозки',2,'[{\"changed\": {\"fields\": [\"\\u041c\\u0438\\u043d\\u0438-\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435 \\u041f\\u041e\"]}}]',7,2),(30,'2020-06-05 18:40:39.258331','4','Поликлиника',1,'[{\"added\": {}}]',7,2),(31,'2020-06-05 18:43:07.987260','4','Больница',1,'[{\"added\": {}}]',10,2),(32,'2020-06-05 18:49:38.403000','5','Цветочная лавка',1,'[{\"added\": {}}]',7,2),(33,'2020-06-05 18:50:05.332985','5','Цветы дружбы',1,'[{\"added\": {}}]',10,2),(34,'2020-06-06 07:27:38.767746','5','Wdtns',1,'[{\"added\": {}}]',8,2),(35,'2020-06-06 07:27:55.536118','5','Цветы',2,'[{\"changed\": {\"fields\": [\"\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435\", \"Softwares\"]}}]',8,2),(36,'2020-06-06 07:28:11.695123','1','Платно',2,'[{\"changed\": {\"fields\": [\"Softwares\"]}}]',8,2),(37,'2020-06-06 14:43:29.310409','1','Order object (1)',1,'[{\"added\": {}}]',19,2),(38,'2020-06-06 14:43:44.887439','1','Order object (1)',2,'[]',19,2),(39,'2020-06-06 14:57:56.071411','1','Order object (1)',2,'[]',19,2),(40,'2020-06-07 16:17:33.523975','50','ivan.dmitriev.2000@yandex.ru',1,'[{\"added\": {}}]',4,2),(41,'2020-06-07 16:23:50.177720','2','Order object (2)',1,'[{\"added\": {}}]',19,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'admin','logentry'),(5,'article','article'),(13,'auth','group'),(12,'auth','permission'),(14,'contenttypes','contenttype'),(17,'discussion','comment'),(18,'discussion','discussion'),(1,'feedback','feedback'),(19,'order','order'),(2,'review','review'),(3,'review','review_addition'),(15,'sessions','session'),(10,'software','addition'),(6,'software','classification'),(9,'software','classification_value'),(16,'software','favourite'),(7,'software','software'),(8,'software','tag'),(4,'user','customuser');
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
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-05-23 05:05:25.742880'),(2,'contenttypes','0002_remove_content_type_name','2020-05-23 05:05:25.954253'),(3,'auth','0001_initial','2020-05-23 05:05:26.131553'),(4,'auth','0002_alter_permission_name_max_length','2020-05-23 05:05:26.580509'),(5,'auth','0003_alter_user_email_max_length','2020-05-23 05:05:26.588487'),(6,'auth','0004_alter_user_username_opts','2020-05-23 05:05:26.597018'),(7,'auth','0005_alter_user_last_login_null','2020-05-23 05:05:26.606030'),(8,'auth','0006_require_contenttypes_0002','2020-05-23 05:05:26.610983'),(9,'auth','0007_alter_validators_add_error_messages','2020-05-23 05:05:26.618995'),(10,'auth','0008_alter_user_username_max_length','2020-05-23 05:05:26.628205'),(11,'auth','0009_alter_user_last_name_max_length','2020-05-23 05:05:26.636180'),(12,'auth','0010_alter_group_name_max_length','2020-05-23 05:05:26.655923'),(13,'auth','0011_update_proxy_permissions','2020-05-23 05:05:26.664898'),(14,'user','0001_initial','2020-05-23 05:05:26.862573'),(15,'admin','0001_initial','2020-05-23 05:05:27.464638'),(16,'admin','0002_logentry_remove_auto_add','2020-05-23 05:05:27.681022'),(17,'admin','0003_logentry_add_action_flag_choices','2020-05-23 05:05:27.691963'),(18,'article','0001_initial','2020-05-23 05:05:27.761233'),(19,'article','0002_article_author','2020-05-23 05:05:27.914272'),(20,'feedback','0001_initial','2020-05-23 05:05:27.987130'),(21,'feedback','0002_feedback_client','2020-05-23 05:05:28.097950'),(22,'software','0001_initial','2020-05-23 05:05:28.635986'),(23,'review','0001_initial','2020-05-23 05:05:30.110436'),(24,'review','0002_auto_20200520_2347','2020-05-23 05:05:30.598796'),(25,'sessions','0001_initial','2020-05-23 05:05:30.659309'),(26,'user','0002_auto_20200523_1322','2020-05-23 05:22:06.281987'),(27,'user','0003_auto_20200523_1326','2020-05-23 05:26:36.345901'),(28,'user','0004_customuser_is_staff','2020-05-23 05:36:25.358274'),(29,'user','0005_auto_20200523_1339','2020-05-23 05:39:22.141532'),(30,'user','0006_auto_20200523_2300','2020-05-23 15:01:41.552097'),(31,'user','0007_auto_20200523_2301','2020-05-23 15:01:41.666250'),(32,'user','0008_auto_20200525_1707','2020-05-25 09:07:59.475005'),(33,'user','0009_auto_20200525_1744','2020-05-25 09:44:12.401655'),(34,'software','0002_favourite','2020-05-26 09:47:02.096189'),(35,'software','0003_auto_20200526_1754','2020-05-26 09:55:03.572899'),(36,'user','0010_auto_20200529_2345','2020-05-29 15:45:56.922889'),(37,'user','0011_customuser_mailing','2020-05-30 09:50:50.596236'),(38,'software','0004_auto_20200531_0137','2020-05-30 17:37:09.074321'),(39,'software','0005_auto_20200531_0138','2020-05-30 17:38:28.775547'),(40,'software','0006_auto_20200531_0139','2020-05-30 17:39:24.957845'),(41,'software','0007_auto_20200531_0421','2020-05-30 20:21:18.333749'),(42,'discussion','0001_initial','2020-05-31 10:32:08.994487'),(43,'software','0008_software_name_small','2020-06-05 15:38:12.369843'),(44,'software','0009_auto_20200606_0230','2020-06-05 18:30:56.905366'),(45,'discussion','0002_auto_20200606_2232','2020-06-06 14:32:56.942162'),(46,'order','0001_initial','2020-06-06 14:32:57.021979'),(47,'order','0002_order_name','2020-06-06 14:57:38.430007'),(48,'order','0003_order_type_soft','2020-06-07 08:59:31.215913'),(49,'user','0012_auto_20200609_0115','2020-06-08 17:15:08.768273');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
INSERT INTO `django_session` VALUES ('57i76a484e3dq57epsfpq72eze2rz8xq','N2FiNDEzNDcxZmQ2ZDA0YzBmNDM0NjYxMWVmODAyOGQ1YjkxNzFlMzp7fQ==','2020-06-08 09:31:01.538653'),('hacsgi2dppb5ve1euhfuzm77s3j4oad9','N2FiNDEzNDcxZmQ2ZDA0YzBmNDM0NjYxMWVmODAyOGQ1YjkxNzFlMzp7fQ==','2020-06-08 09:30:12.056962'),('u4or84lrmxklii66lw2v2a2fywp35zvf','N2FiNDEzNDcxZmQ2ZDA0YzBmNDM0NjYxMWVmODAyOGQ1YjkxNzFlMzp7fQ==','2020-06-08 09:36:48.333232');
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
  `phone` varchar(25) NOT NULL,
  `comment` longtext,
  `date` datetime(6) NOT NULL,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_feedback_client_id_16534924_fk_user_customuser_id` (`client_id`),
  CONSTRAINT `feedback_feedback_client_id_16534924_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_feedback`
--

LOCK TABLES `feedback_feedback` WRITE;
/*!40000 ALTER TABLE `feedback_feedback` DISABLE KEYS */;
INSERT INTO `feedback_feedback` VALUES (1,'Анастасия','+7 (790) 166-8607','','2020-05-23 05:41:56.658135',NULL),(2,'Анастасия','+ 7 901 668-60-77','FFFFFFFFF','2020-05-23 05:42:04.283421',NULL),(3,NULL,'89043435565','Перезвоните мнеееее','2020-05-23 05:42:27.213066',NULL);
/*!40000 ALTER TABLE `feedback_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order`
--

DROP TABLE IF EXISTS `order_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kind` varchar(3) NOT NULL,
  `cost` double NOT NULL,
  `note` longtext,
  `date` datetime(6) NOT NULL,
  `starting_date` datetime(6) DEFAULT NULL,
  `ending_date` datetime(6) DEFAULT NULL,
  `discount` double DEFAULT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `client_id` int NOT NULL,
  `manager_id` int DEFAULT NULL,
  `software_id` int DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `type_soft` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_order_client_id_8dc70a8e_fk_user_customuser_id` (`client_id`),
  KEY `order_order_manager_id_501ebc55_fk_user_customuser_id` (`manager_id`),
  KEY `order_order_software_id_6cccd8ee_fk_software_software_id` (`software_id`),
  KEY `order_order_kind_4637dc96` (`kind`),
  KEY `order_order_date_of_delete_9b7aa63e` (`date_of_delete`),
  KEY `order_order_visibility_6841e7d2` (`visibility`),
  CONSTRAINT `order_order_client_id_8dc70a8e_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `order_order_manager_id_501ebc55_fk_user_customuser_id` FOREIGN KEY (`manager_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `order_order_software_id_6cccd8ee_fk_software_software_id` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
INSERT INTO `order_order` VALUES (1,'buy',5000,'','2020-06-06 14:43:29.309411','2020-06-06 14:42:12.000000','2021-06-06 12:00:00.000000',50,NULL,1,2,31,1,'Грузоперевозки','Настольное приложение'),(2,'org',100000,'Как указано выше, по умолчанию квантификаторы жадные. Этот подход решает очень важную проблему — проблему границы шаблона. Скажем, шаблон \\d+ захватывает максимально возможное количество цифр. Поэтому можно быть уверенным, что перед найденным шаблоном идёт не цифра, и после идёт не цифра. Однако если в шаблоне есть не жадные части (например, явный текст), то подстрока может быть найдена неудачно. Например, если мы хотим найти «слова», начинающиеся на СУ, после которой идут цифры, при помощи регулярки СУ\\d*, то мы найдём и неправильные шаблоны:\r\nПересечение подстрок\r\n\r\nВ обычной ситуации регулярки позволяют найти только непересекающиеся шаблоны. Вместе с проблемой границы слова это делает их использование в некоторых случаях более сложным. Например, если мы решим искать e-mail адреса при помощи неправильной регулярки \\w+@\\w+ (или даже лучше, [\\w\'._+-]+@[\\w\'._+-]+), то в неудачном случае найдём вот что:\r\n\r\nЭксперименты в песочнице\r\n\r\nЕсли вы впервые сталкиваетесь с регулярными выражениями, то лучше всего сначала попробовать песочницу. Посмотрите, как работают простые шаблоны и квантификаторы. Решите следующие задачи для этого текста (возможно, к части придётся вернуться после следующей теории):\r\nНайдите все натуральные числа (возможно, окружённые буквами);\r\nНайдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);\r\nНайдите слова, в которых есть русская буква, а когда-нибудь за ней цифра;\r\nНайдите все слова, начинающиеся с русской или латинской большой буквы (\\b — граница слова);\r\nНайдите слова, которые начинаются на гласную (\\b — граница слова);;\r\nНайдите все натуральные числа, не находящиеся внутри или на границе слова;\r\nНайдите строчки, в которых есть символ * (. — это точно не конец строки!);\r\nНайдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки;\r\nВыделите одним махом весь кусок оглавления (в конце примера, вместе с тегами);\r\nВыделите одним махом только текстовую часть оглавления, без тегов;\r\nНайдите пустые строчки;','2020-06-07 16:23:50.176723','2020-06-07 16:23:12.000000','2021-09-09 16:23:21.000000',10,NULL,1,52,2,NULL,'Кроссплатформенное приложение по добыче нефти','Сайт');
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_review`
--

DROP TABLE IF EXISTS `review_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kind` varchar(3) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email_phone` varchar(60) DEFAULT NULL,
  `content` longtext,
  `comment` longtext,
  `date` datetime(6) NOT NULL,
  `star` int NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `client_id` int DEFAULT NULL,
  `software_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `review_review_kind_8448a21c` (`kind`),
  KEY `review_review_date_of_delete_eb4575fe` (`date_of_delete`),
  KEY `review_review_visibility_f311a70b` (`visibility`),
  KEY `review_review_client_id_4f1ce3b8_fk_user_customuser_id` (`client_id`),
  KEY `review_review_software_id_bd39c353_fk_software_software_id` (`software_id`),
  CONSTRAINT `review_review_client_id_4f1ce3b8_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `review_review_software_id_bd39c353_fk_software_software_id` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_review`
--

LOCK TABLES `review_review` WRITE;
/*!40000 ALTER TABLE `review_review` DISABLE KEYS */;
INSERT INTO `review_review` VALUES (1,'com','Анастасия','89555555555','Замечательная программа!Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки','','2020-05-23 05:44:40.436007',5,NULL,1,NULL,NULL),(2,'com',NULL,'89555555555d@fffffff.dddd','Замечательная программа!Спасибо вам! Замечательная программа! Не могу нарадоваться! Замечательная программа!Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа!Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа!Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам! Замечательная программа! Не могу нарадоваться! Жду доработки, которую предложила, и тогда приложение станет совершенно идеальным для меня! Спасибо вам!\',\'Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!','Огромное спасмбо за отзыв! Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!Огромное спасмбо за отзыв! Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!Огромное спасмбо за отзыв!','2020-05-23 05:45:29.666727',1,NULL,1,NULL,NULL),(3,'com',NULL,'89555555555','','','2020-05-23 05:45:39.259873',3,NULL,1,NULL,NULL),(4,'com','Анастасия','89555555555','',NULL,'2020-05-31 10:13:45.289050',5,NULL,1,NULL,2);
/*!40000 ALTER TABLE `review_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_review_addition`
--

DROP TABLE IF EXISTS `review_review_addition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_review_addition` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `size` tinyint(1) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `review_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_review_addition_review_id_e61e7301_fk_review_review_id` (`review_id`),
  KEY `review_review_addition_date_of_delete_c3d05256` (`date_of_delete`),
  CONSTRAINT `review_review_addition_review_id_e61e7301_fk_review_review_id` FOREIGN KEY (`review_id`) REFERENCES `review_review` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_review_addition`
--

LOCK TABLES `review_review_addition` WRITE;
/*!40000 ALTER TABLE `review_review_addition` DISABLE KEYS */;
INSERT INTO `review_review_addition` VALUES (1,'Платно',1,'review/image_2020-05-05_22-36-12.png',NULL,1);
/*!40000 ALTER TABLE `review_review_addition` ENABLE KEYS */;
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
  `is_main` tinyint(1) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  `software_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_addition_software_id_c60543b6_fk_software_software_id` (`software_id`),
  KEY `software_addition_date_of_delete_38c55ff3` (`date_of_delete`),
  CONSTRAINT `software_addition_software_id_c60543b6_fk_software_software_id` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_addition`
--

LOCK TABLES `software_addition` WRITE;
/*!40000 ALTER TABLE `software_addition` DISABLE KEYS */;
INSERT INTO `software_addition` VALUES (1,'Грузоперевозки',1,1,'soft/business_C9S0ITJ.jpg',1,NULL,1),(2,'Компьютер',1,1,'soft/computer_KfHsbSl.jpg',0,NULL,1),(3,'Кафе',1,1,'soft/pizza_QKyW2jU.jpg',0,NULL,2),(4,'Больница',1,1,'soft/45D05B5E-3677-448F-A788-F0E7BCFB7939.webp',1,NULL,4),(5,'Цветы дружбы',1,1,'soft/winny.jpg',0,NULL,5);
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
  `name` varchar(50) NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification`
--

LOCK TABLES `software_classification` WRITE;
/*!40000 ALTER TABLE `software_classification` DISABLE KEYS */;
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
  `value` varchar(200) NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `classification_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_classificat_classification_id_9fa77065_fk_software_` (`classification_id`),
  KEY `software_classification_value_visibility_62c1ea04` (`visibility`),
  CONSTRAINT `software_classificat_classification_id_9fa77065_fk_software_` FOREIGN KEY (`classification_id`) REFERENCES `software_classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification_value`
--

LOCK TABLES `software_classification_value` WRITE;
/*!40000 ALTER TABLE `software_classification_value` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_classification_value_softwares`
--

LOCK TABLES `software_classification_value_softwares` WRITE;
/*!40000 ALTER TABLE `software_classification_value_softwares` DISABLE KEYS */;
/*!40000 ALTER TABLE `software_classification_value_softwares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_favourite`
--

DROP TABLE IF EXISTS `software_favourite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_favourite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_joined` datetime(6) NOT NULL,
  `client_id` int NOT NULL,
  `software_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `software_favourite_client_id_583cf634_fk_user_customuser_id` (`client_id`),
  KEY `software_favourite_software_id_40a58a24_fk_software_software_id` (`software_id`),
  CONSTRAINT `software_favourite_client_id_583cf634_fk_user_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `software_favourite_software_id_40a58a24_fk_software_software_id` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_favourite`
--

LOCK TABLES `software_favourite` WRITE;
/*!40000 ALTER TABLE `software_favourite` DISABLE KEYS */;
INSERT INTO `software_favourite` VALUES (15,'2020-06-04 20:03:20.364066',2,1);
/*!40000 ALTER TABLE `software_favourite` ENABLE KEYS */;
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
  `price` double NOT NULL,
  `is_free` tinyint(1) NOT NULL,
  `description` longtext NOT NULL,
  `description_medium` longtext NOT NULL,
  `description_small` longtext NOT NULL,
  `visibility` tinyint(1) NOT NULL,
  `modification` tinyint(1) NOT NULL,
  `size` double DEFAULT NULL,
  `date_of_delete` varchar(20) DEFAULT NULL,
  `name_small` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `software_software_is_free_a5a171c5` (`is_free`),
  KEY `software_software_visibility_d0b118f5` (`visibility`),
  KEY `software_software_date_of_delete_5fecbd2a` (`date_of_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_software`
--

LOCK TABLES `software_software` WRITE;
/*!40000 ALTER TABLE `software_software` DISABLE KEYS */;
INSERT INTO `software_software` VALUES (1,'Грузоперевозки',10000,0,'Это приложение позволяет управлять заказами грузоперевозок. \\r\\nЭффективное управление бизнесом при помощи этого приложения. \\r\\nВыполнение соновной работы по работника: грузчикам, водителям),\\r\\n автомобилям, заказам. Также в этом приложении осуществяется\\r\\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\\r\\n Это приложение позволяет управлять заказами грузоперевозок.\\r\\nЭффективное управление бизнесом при помощи этого приложения. \\r\\nВыполнение соновной работы по работника: грузчикам, водителям),\\r\\n автомобилям, заказам. Также в этом приложении осуществяется\\r\\nвозможность аналитической работы с бизнесом: количество о заказов и многое другое.\\r\\n\\r\\nЭффективное управление бизнесом при помощи этого приложения. \\r\\n Выполнение соновной работы по работника: грузчикам, водителям),\\r\\n автомобилям, заказам. Также в этом приложении осуществяется\\r\\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\\r\\nЭто приложение позволяет управлять заказами грузоперевозок.\\r\\n Эффективное управление бизнесом при помощи этого приложения. \\r\\nВыполнение соновной работы по работника: грузчикам, водителям),\\r\\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.\\r\\n\\r\\n\\r\\nЭффективное управление бизнесом при помощи этого приложения. \\r\\n Выполнение соновной работы по работника: грузчикам, водителям),\\r\\n автомобилям, заказам. Также в этом приложении осуществяется\\r\\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\\r\\nЭто приложение позволяет управлять заказами грузоперевозок.\\r\\n Эффективное управление бизнесом при помощи этого приложения. \\r\\nВыполнение соновной работы по работника: грузчикам, водителям),\\r\\nавтомобилям, заказам. Также в этом приложении осуществяется возможность аналитической работы с бизнесом: количество о заказов и многое другое.\',\'Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.\',\'Направление справа налево (в rtl слева направо).','Это приложение позволяет управлять заказами грузоперевозок. \\r\\nЭффективное управление бизнесом при помощи этого приложения. \\r\\nВыполнение соновной работы по работника: грузчикам, водителям),\\r\\n автомобилям, заказам. Также в этом приложении осуществяется\\r\\n возможность аналитической работы с бизнесом: количество заказов и многое другое.\\r\\n Это приложение позволяет управлять заказами','Контроль доходов и расходов',1,1,NULL,NULL,'Грузоперевозки'),(2,'Кафе',10000,1,'Для описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\\r\\n\\r\\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\\r\\n\\r\\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\\r\\n\\r\\nДля описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому для дочерних элементов не работают такие CSS-свойства, как float, clear, vertical-align. Также, на flex-контейнер не оказывают влияние свойства column-*, создающие колонки в тексте и псевдоэлементы ::first-line и ::first-letter.Если родительский блок содержит текст или изображения без оберток, они становятся анонимными flex-элементами. Текст выравнивается по верхнему краю блока-контейнера, а высота изображения становится равной высоте блока, т.е. оно деформируеииится.\',\'Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налево, сверху вниз или снизу вверх.Располагать элементы в одном из четырех направлений: слева направо, справа налевои, сверху вниз или снизу вверх.\',\'Flex-элементы выкладываются в строку','Для описания модуля Flexbox используется определенный набор терминов. Значение flex-flow и режим записи определяют соответствие этих терминов физическим направлениям: верх / право / низ / лево, осям: вертикальная / горизонтальная и размерам: ширина / высота.Flex-контейнер устанавливает новый гибкий контекст форматирования для его содержимого. Flex-контейнер не является блочным контейнером, поэтому','Крутое автоматизированное кафе!',1,1,NULL,NULL,'Кафе и кофе всегда с собой'),(3,'Образование',0,1,'Названия таблиц для моделей\r\n\r\nОткуда берется название таблицы для модели Person?\r\n\r\nПо умолчанию Django создает название таблицы объединив название приложения(название которое вы использовали при вызове manage.py startapp), в котором находиться модель, и название модели с нижним подчеркиванием между ними. В нашем примере модель Person предположительно находится в приложение myapp, поэтому название таблицы в базе данных будет myapp_person.\r\n\r\nПодробности смотрите в описании настройки модели db_table, которая также позволяет явно указать название таблицы.','Названия таблиц для моделей\r\n\r\nОткуда берется название таблицы для модели Person?\r\n\r\nПо умолчанию Django создает название таблицы объединив название приложения(название которое вы использовали при вызове manage.py startapp), в котором находиться модель, и название модели с нижним подчеркиванием между ними. В нашем примере модель Person предположительно находится в приложение myapp, поэтому назван','Контроль доходов и расходов! Контроль доходов и расходов!Мониторинг деятельности компании',1,1,NULL,NULL,'Автоматизируй Образование!'),(4,'Поликлиника',15000,0,'Благодаря мобильному приложению вы можете иметь своего «доктора» в своем мобильном телефоне и его ответ в любое время. Мобильное приложение, доступное для всех типов устройств на базе Android и iOS. Через него люди связываются с крупнейшей онлайн-консультацией в области медицины, которая работает уже более 10 лет. В клинике много врачей общей практики и других специалистов готовых ответить на вопросы пациентов 24 часа в сутки, 7 дней в неделю. В каждой стране это приложение разное конечно же. Более подробную информацию можно найти по поисковому запросу в Google или Yandex.\r\n\r\nРанее Центр консультирования работал только через компьютер, но с недавних пор они также сделали запуск тестовой версии для мобильных телефонов (бесплатно в Google Play и AppStore) и в настоящее время предлагает полный набор услуг. В нынешней ситуации, вызванной пандемией COVID-19, когда медицинские учреждения перегружены, кабинеты врачей общей практики обычно остаются закрытыми из-за нехватки защитного оборудования. Врачи, например медцентра в Днепре, только дистанционно обращаются к ним, возможность удаленной консультации по проблемам со здоровьем является огромной пользой для пациентов. В настоящее время наблюдается увеличение использования услуг на 120%. Это около 150-200 консультаций в день.','Благодаря мобильному приложению вы можете иметь своего «доктора» в своем мобильном телефоне и его ответ в любое время. Мобильное приложение, доступное для всех типов устройств на базе Android и iOS. Через него люди связываются с крупнейшей онлайн-консультацией в области медицины, которая работает уже более 10 лет.','Благодаря мобильному приложению вы можете иметь своего «доктора» в своем мобильном телефоне и его ответ в любое время.',1,1,NULL,NULL,'Автоматизируй Медицину - это просто!'),(5,'Цветочная лавка',0,1,'Доставка цветов в Москве Статьи о цветах\r\nСтатьи о цветах\r\nИстория цветка \"Герберы\"\r\nВозможно, вы будете удивлены, но популярная ныне гербера появилась на цветочной мировой палитре только в конце XIX века. Впрочем, одного столетия оказалось вполне достаточно, чтобы цветок из гадкого утенка превратился в прекрасного лебедя, заняв весьма высокое положение, на достижение которого у многих цветков уходит по несколько столетий.  Подробнее\r\n \r\nСорта и виды гербер, используемых во флористике\r\nГерберы – очень красивые и яркие цветы, отличающиеся разнообразием форм и размеров. Благодаря этому различные сорта гербер широко используются в современной флористике. Описание гербер Гербера – многолетнее травянистое растение из семейства сложноцветных (астровых). Оно растет в тропическом климате Южной Африке и Азии. Стебель растения укороченный, а цветонос длинный (до 70 см), полностью свободный от листьев. Диаметр соцветия, которое по виду напоминает ромашку с желтой или коричневой сердцевиной, составляет от 4 до 15 см. Окраска цветов включает в себя практически все оттенки желтого, оранжевого, красного, а также розовые и белые тона.  Подробнее\r\n \r\nТюльпаны на все случаи жизни\r\nОдними из первых ранней весной появляются тюльпаны: желтые, красные, с махровой каемкой на кончиках лепестков. Буйство красок и великолепие форм цветков вызывает удивление и восхищение. По мнению языковедов, слово тюльпан пришло к нам из персидского языка от слова toliban, означающего тюрбан. Сходство формы цветка и восточного головного убора и дало название этому прекрасному цветку. Немного истории.  Подробнее\r\n \r\nПокупаем розы: правила выбора\r\nСамым распространенным подарком на любом празднике является букет из свежих цветов, в композиции которого достаточно часто используются розы. Букет из роз – достаточно универсальный подарок, который можно преподнести и любимой женщине, и коллеге по работе, и по любому другому торжественному поводу. Стоит лишь правильно выбрать оттенок цветов, чтобы подарок был уместен и не был двусмысленно истолкован. Подробнее\r\n \r\nУход за растениями в вашем доме\r\nО таком богатстве растений в наших квартирах в прежние времена приходилось только мечтать. Наш дом украшают декоративные растения-новинки, как правило произрастающие в тропических и субтропических странах, но есть и «старые знакомые», например, комнатные пальмы и папоротники. Правильный уход за комнатными растениями не требует профессиональных знаний, этому не надо учиться специально, как, скажем, иностранному языку.  Подробнее\r\n \r\nОрхидея: легенды, мифы и исторические факты\r\nСегодня, если верить источникам, в мире насчитывается более 25 тысяч видов орхидеи и более 100 тысяч ее гибридов! Этот цветок растет практически в любом климатическом поясе, он распространился по Земному шару и любим многими цветоводами. Несмотря на сложившееся мнение, уход за этим растением не требует каких-то сложных действий, на самом деле растение неприхотливо, хотя здесь многое зависит от каждого конкретного типа. Подробнее\r\n \r\nОрхидея - цветочная аристократка\r\nОрхидея поистине парадоксальный цветок. В свое время это был самый дорогой цветок, и чтобы добыть его снаряжались целые экспедиции, тем не менее, мире существует около 50 000 видов орхидей, распространенных по всему миру, кроме Антарктиды.','Доставка цветов в Москве Статьи о цветах\r\nСтатьи о цветах\r\nИстория цветка \"Герберы\"\r\nВозможно, вы будете удивлены, но популярная ныне гербера появилась на цветочной мировой палитре только в конце XIX века. Впрочем, одного столетия оказалось вполне достаточно, чтобы цветок из гадкого утенка превратился в прекрасного лебедя,','Орхидея - цветочная аристократка\r\nОрхидея: легенды, мифы и исторические факты\r\nУход за растениями в вашем доме',1,0,NULL,NULL,'Цветочная лавка может стать твоей! Хватай!');
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
  `description` longtext,
  `visibility` tinyint(1) NOT NULL,
  `date_of_delete` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `software_tag_visibility_bf251d73` (`visibility`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag`
--

LOCK TABLES `software_tag` WRITE;
/*!40000 ALTER TABLE `software_tag` DISABLE KEYS */;
INSERT INTO `software_tag` VALUES (1,'Платно','',1,NULL),(2,'Кафе','',1,NULL),(3,'Перевозки','',1,NULL),(4,'Бизнес','',1,NULL),(5,'Цветы','',1,NULL);
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
  UNIQUE KEY `software_tag_articles_tag_id_article_id_f44f692d_uniq` (`tag_id`,`article_id`),
  KEY `software_tag_articles_article_id_b235881a_fk_article_article_id` (`article_id`),
  CONSTRAINT `software_tag_articles_article_id_b235881a_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`),
  CONSTRAINT `software_tag_articles_tag_id_c6cae2d2_fk_software_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `software_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag_articles`
--

LOCK TABLES `software_tag_articles` WRITE;
/*!40000 ALTER TABLE `software_tag_articles` DISABLE KEYS */;
INSERT INTO `software_tag_articles` VALUES (1,1,1),(2,2,2),(3,4,1);
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
  UNIQUE KEY `software_tag_softwares_tag_id_software_id_5e72fad1_uniq` (`tag_id`,`software_id`),
  KEY `software_tag_softwar_software_id_580b4c3b_fk_software_` (`software_id`),
  CONSTRAINT `software_tag_softwar_software_id_580b4c3b_fk_software_` FOREIGN KEY (`software_id`) REFERENCES `software_software` (`id`),
  CONSTRAINT `software_tag_softwares_tag_id_d0a291df_fk_software_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `software_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_tag_softwares`
--

LOCK TABLES `software_tag_softwares` WRITE;
/*!40000 ALTER TABLE `software_tag_softwares` DISABLE KEYS */;
INSERT INTO `software_tag_softwares` VALUES (1,1,1),(4,1,2),(9,1,4),(5,2,1),(2,2,2),(3,3,1),(6,4,1),(7,4,3),(8,4,4),(11,5,5);
/*!40000 ALTER TABLE `software_tag_softwares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_customuser`
--

DROP TABLE IF EXISTS `user_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_customuser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `kind` varchar(3) NOT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `patronymic` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `phone_second` varchar(20) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `date_of_delete` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `comment` varchar(900) DEFAULT NULL,
  `social` varchar(400) DEFAULT NULL,
  `mailing` tinyint(1) NOT NULL,
  `guest_session` varchar(80) DEFAULT NULL,
  `max_age` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_customuser_phone_51b3d716_uniq` (`phone`),
  UNIQUE KEY `user_customuser_email_2292cf6d_uniq` (`email`),
  UNIQUE KEY `guest_session` (`guest_session`),
  KEY `user_customuser_kind_d6e0a11c` (`kind`),
  KEY `user_customuser_date_of_delete_a4b62e3f` (`date_of_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_customuser`
--

LOCK TABLES `user_customuser` WRITE;
/*!40000 ALTER TABLE `user_customuser` DISABLE KEYS */;
INSERT INTO `user_customuser` VALUES (2,'pbkdf2_sha256$180000$1jMonB4lNae7$tBZ4579tqLljNJ+fyskVzeSVjOuKXXahiydumfAdk1s=','2020-06-07 16:21:07.621316',1,'ndmitrievnaa@mail.ru','ADM','Дмитриенко','Анастасия','','89016686070','','2020-05-23 05:33:41.953781','2000-08-23',NULL,1,1,NULL,'https://vk.com/musicalprincezzz, https://vk.com/musicalprincezzz',0,NULL,NULL),(31,'pbkdf2_sha256$180000$kafuGuWGkKBJ$OnLRo9XtUFHz9JOaKVfJwKQtnMTHsvU6Bkh6U4shygk=','2020-05-25 16:59:34.411188',0,'fdddd@mal.ff','CL',NULL,'',NULL,NULL,NULL,'2020-05-25 16:59:34.396229',NULL,NULL,1,0,NULL,NULL,0,NULL,NULL),(52,'pbkdf2_sha256$180000$dpcBrLsj9PSX$lxfZH5OqVj2S0WjFPHs+sbqgr8M0X1YoGU94UmU4K34=','2020-06-07 16:20:49.705388',0,NULL,'CL',NULL,'',NULL,'89000000000',NULL,'2020-06-07 16:20:49.673470',NULL,NULL,1,0,NULL,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `user_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_customuser_groups`
--

DROP TABLE IF EXISTS `user_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_customuser_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customuser_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_customuser_groups_customuser_id_group_id_e0a2f621_uniq` (`customuser_id`,`group_id`),
  KEY `user_customuser_groups_group_id_bcbc9e48_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_customuser_grou_customuser_id_192632a7_fk_user_cust` FOREIGN KEY (`customuser_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `user_customuser_groups_group_id_bcbc9e48_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_customuser_groups`
--

LOCK TABLES `user_customuser_groups` WRITE;
/*!40000 ALTER TABLE `user_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_customuser_user_permissions`
--

DROP TABLE IF EXISTS `user_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_customuser_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customuser_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_customuser_user_per_customuser_id_permission_a5da865d_uniq` (`customuser_id`,`permission_id`),
  KEY `user_customuser_user_permission_id_e57e8b9a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_customuser_user_customuser_id_4552d9cc_fk_user_cust` FOREIGN KEY (`customuser_id`) REFERENCES `user_customuser` (`id`),
  CONSTRAINT `user_customuser_user_permission_id_e57e8b9a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_customuser_user_permissions`
--

LOCK TABLES `user_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 18:16:07
