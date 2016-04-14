-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: creditcardmessage
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.1

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
-- Table structure for table `BillGenerator`
--

DROP TABLE IF EXISTS `BillGenerator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BillGenerator` (
  `bankName` varchar(50) DEFAULT NULL,
  `creditCardNumberLastFour` varchar(50) DEFAULT NULL,
  `billAmount` varchar(50) DEFAULT NULL,
  `dueDate` varchar(50) DEFAULT NULL,
  `billGenerationDate` varchar(50) DEFAULT NULL,
  `bankid` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BillGenerator`
--

LOCK TABLES `BillGenerator` WRITE;
/*!40000 ALTER TABLE `BillGenerator` DISABLE KEYS */;
/*!40000 ALTER TABLE `BillGenerator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DueDatePayment`
--

DROP TABLE IF EXISTS `DueDatePayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DueDatePayment` (
  `creditCardNumberLastFour` varchar(50) DEFAULT NULL,
  `billAmount` varchar(50) DEFAULT NULL,
  `billingMonth` varchar(50) DEFAULT NULL,
  `dueDate` varchar(50) DEFAULT NULL,
  `paymentDate` varchar(50) DEFAULT NULL,
  `latePaymentCharges` varchar(50) DEFAULT NULL,
  `bankid` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DueDatePayment`
--

LOCK TABLES `DueDatePayment` WRITE;
/*!40000 ALTER TABLE `DueDatePayment` DISABLE KEYS */;
/*!40000 ALTER TABLE `DueDatePayment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PaymentCreditCard`
--

DROP TABLE IF EXISTS `PaymentCreditCard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PaymentCreditCard` (
  `creditCardNumberLastFour` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `spentDate` varchar(50) DEFAULT NULL,
  `bankid` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PaymentCreditCard`
--

LOCK TABLES `PaymentCreditCard` WRITE;
/*!40000 ALTER TABLE `PaymentCreditCard` DISABLE KEYS */;
/*!40000 ALTER TABLE `PaymentCreditCard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RegisterCreditCard`
--

DROP TABLE IF EXISTS `RegisterCreditCard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RegisterCreditCard` (
  `bankName` varchar(50) DEFAULT NULL,
  `creditCardType` varchar(50) DEFAULT NULL,
  `creditCardNumber` varchar(50) DEFAULT NULL,
  `validityDate` varchar(50) DEFAULT NULL,
  `bankid` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RegisterCreditCard`
--

LOCK TABLES `RegisterCreditCard` WRITE;
/*!40000 ALTER TABLE `RegisterCreditCard` DISABLE KEYS */;
/*!40000 ALTER TABLE `RegisterCreditCard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-14  4:38:07
