CREATE DATABASE  IF NOT EXISTS `blogspot_erd` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `blogspot_erd`;
-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: localhost    Database: blogspot_erd
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL,
  `blog_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `users_id` int NOT NULL,
  `blogs_id` int NOT NULL,
  PRIMARY KEY (`blog_id`,`user_id`,`id`),
  KEY `fk_admins_users1_idx` (`users_id`),
  KEY `fk_admins_blogs1_idx` (`blogs_id`),
  CONSTRAINT `fk_admins_blogs1` FOREIGN KEY (`blogs_id`) REFERENCES `blogs` (`id`),
  CONSTRAINT `fk_admins_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs`
--

DROP TABLE IF EXISTS `blogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blogs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL,
  `updated_at` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs`
--

LOCK TABLES `blogs` WRITE;
/*!40000 ALTER TABLE `blogs` DISABLE KEYS */;
/*!40000 ALTER TABLE `blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `contents` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `post_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_posts1_idx` (`post_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_posts1` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_path` blob,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `posts_id` int NOT NULL,
  `admin_blog_id` int NOT NULL,
  `admin_user_id` int NOT NULL,
  `admin_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_files_posts1_idx` (`posts_id`),
  KEY `fk_files_admins1_idx` (`admin_blog_id`,`admin_user_id`,`admin_id`),
  CONSTRAINT `fk_files_admins1` FOREIGN KEY (`admin_blog_id`, `admin_user_id`, `admin_id`) REFERENCES `admins` (`blog_id`, `user_id`, `id`),
  CONSTRAINT `fk_files_posts1` FOREIGN KEY (`posts_id`) REFERENCES `posts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `page_views`
--

DROP TABLE IF EXISTS `page_views`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `page_views` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `blog_id` int NOT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `view_length` decimal(10,0) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`,`blog_id`),
  KEY `fk_users_has_blogs_blogs1_idx` (`blog_id`),
  KEY `fk_users_has_blogs_users1_idx` (`user_id`),
  CONSTRAINT `fk_users_has_blogs_blogs1` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`id`),
  CONSTRAINT `fk_users_has_blogs_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `page_views`
--

LOCK TABLES `page_views` WRITE;
/*!40000 ALTER TABLE `page_views` DISABLE KEYS */;
/*!40000 ALTER TABLE `page_views` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `blog_id` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `admin_blog_id` int NOT NULL,
  `admin_user_id` int NOT NULL,
  `admin_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_posts_blogs1_idx` (`blog_id`),
  KEY `fk_posts_admins1_idx` (`admin_blog_id`,`admin_user_id`,`admin_id`),
  CONSTRAINT `fk_posts_admins1` FOREIGN KEY (`admin_blog_id`, `admin_user_id`, `admin_id`) REFERENCES `admins` (`blog_id`, `user_id`, `id`),
  CONSTRAINT `fk_posts_blogs1` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-01  9:16:07
