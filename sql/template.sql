-- --------------------------------------------------------
-- Host:                         192.168.24.100
-- Server version:               10.6.16-MariaDB-0ubuntu0.22.04.1 - Ubuntu 22.04
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for Remote_Access
CREATE DATABASE IF NOT EXISTS `Remote_Access` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `Remote_Access`;

-- Dumping structure for table Remote_Access.remote_access
CREATE TABLE IF NOT EXISTS `remote_access` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) NOT NULL,
  `cel_phone` varchar(20) DEFAULT NULL,
  `e_mail` varchar(40) NOT NULL,
  `ext` smallint(6) NOT NULL,
  `login` varchar(20) DEFAULT NULL,
  `destination_pc` varchar(20) NOT NULL,
  `hours_in` varchar(10) DEFAULT NULL,
  `hours_out` varchar(10) DEFAULT NULL,
  `week_days` varchar(10) DEFAULT NULL,
  `service_name` varchar(10) NOT NULL,
  `access_granted` int(1) NOT NULL DEFAULT 0,
  `comments` varchar(110) DEFAULT NULL,
  KEY `PRIMARY KEY` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table Remote_Access.remote_access: ~56 rows (approximately)
INSERT INTO `remote_access` (`id`, `user_name`, `cel_phone`, `e_mail`, `ext`, `login`, `destination_pc`, `hours_in`, `hours_out`, `week_days`, `service_name`, `access_granted`, `comments`) VALUES
	(1, 'Adrian Onilov', '916-398-7903', 'adrian@uskoexpedite.com', 2023, '', 'USKO-2023', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Citrus Heights'),
	(2, 'Alex Lebedchik', '916-517-0592', 'alebedchik@uskologistics.com', 1106, 'alebedchik', 'USKO-1224', '', '', '', 'RDP', 0, 'hap'),
	(3, 'Alex PrimeHardware', '717-793-8456', 'alex@primehardware.com', 1200, 'alex', 'USKO-1200', '', '', '', 'RDP', 1, ''),
	(4, 'Alice Dutova', '916-952-2115', 'aliced@uskoinc.com', 1005, 'aliced', 'USKO-1209', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Sacramento'),
	(5, 'Art Luilkovich', '916-747-5166', 'art@uskoinc.com', 2017, 'artur', 'USKO-2017', '', '', '', 'RDP', 1, 'ISP: '),
	(6, 'Carina Garbuzova', '916-546-0080', 'carinag@uskoexpedite.com', 2035, 'carinag', 'USKO-2054', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Antelope'),
	(7, 'Darya Veprzhytskaya', '', 'veprzhytskayad@uskologistics.com', 1208, 'veprzhytskayad', 'USKO-1208', '', '', '', 'RDP', 1, ''),
	(8, 'David Shilo', '916-547-6911', 'davids@uskoinc.com', 1206, 'davids', 'USKO-1206', '', '', '', 'RDP', 0, 'hap'),
	(9, 'Diana Kalmykov', '916-993-0159', 'dianak@uskoinc.com', 1008, 'dianak', 'USKO-1092', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Folsom'),
	(10, 'DJ Atakeev', '916-346-7337', 'dj@uskoexpedite.com', 2073, 'djatakeev', 'USKO-2073', '', '', '', 'RDP', 0, 'hap'),
	(11, 'Ela Karpenko', '916-915-7375', 'ela@uskoinc.com', 1071, 'ela', 'USKO-1005', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Olivehust'),
	(12, 'Elena Grigorian', '916-895-4922', 'grigoriane@uskologistics.com', 1235, 'grigoriane', 'USKO-1235', '', '', '', 'RDP', 1, 'hap'),
	(13, 'Emil Atakeev', '916-969-3710', 'emil@uskoexpedite.com', 2071, 'emil', 'USKO-2071', '', '', '', 'RDP', 0, 'hap'),
	(14, 'Inna Manachynska', '', 'imanachynska@uskoexpedite.com', 2062, 'imanachynska', 'USKO-2062', '', '', '', 'RDP', 1, ''),
	(15, 'Inna Razumovsky', '916-949-9090', 'inna@uskoinc.com', 2044, 'Inna', 'usko-2044', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Citrus Heights'),
	(16, 'Inna Razumovsky', '916-949-9090', 'inna@uskoinc.com', 2044, 'Inna', 'accounting', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Citrus Heights'),
	(17, 'Ivan Kushnir', '660-281-3810', 'ivan@uskoexpedite.com', 2034, 'Ink', 'USKO-2034', '', '', '', 'RDP', 0, 'hap'),
	(18, 'Ivan Tarasiuk', '', 'itarasiuk@uskoinc.com', 1193, 'itarasiuk', 'USKO-1193', '', '', '', 'RDP', 1, 'ui/ux designer'),
	(19, 'James Oleksyuk', '916-307-2132', 'james@uskoinc.com', 1034, 'James', 'USKO-1034', '', '', '', 'RDP', 0, 'hap Only turn on when Chris Felkin says to; on a day by day basis'),
	(20, 'Jeppe Lisdorf', '916-555-1212', 'jeppe@lisdorfandco.com', 7655, 'jeppe', 'BOOKS', '', '', '', 'RDP', 1, 'ISP: Verizon Wireless; Location: Irvine'),
	(21, 'Jessica Kambur', '916-996-8892', 'jessica@uskoexpedite.com', 2043, 'jessica', 'USKO-2043', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Sacramento'),
	(22, 'Jessica Podgayetskaya', '', 'jpodgayetskaya@uskoinc.com', 24000, 'jpodgayetskaya', 'USKO-1071', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Sacramento'),
	(23, 'John Borish', '916-792-1324', 'chris@uskoinc.com', 1032, 'cfelkin', 'USKO-1032', '', '', '', 'RDP', 0, 'hap Chris Felkin'),
	(24, 'Karina Tkachenko', '916-717-5791', 'karina@uskoinc.com', 1002, 'Karina', 'USKO-1002', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Folsom'),
	(25, 'Kate Kulman', '', 'kkulman@uskoinc.com', 1112, 'kkulman', 'USKO-1112', '', '', '', 'RDP', 1, 'hap'),
	(26, 'Kate Taistra', '', 'ktaistra@uskoinc.com', 2401, 'ktaistra', 'USKO-2401', '', '', '', 'RDP', 1, 'ISP: Zain Jordan; Location: Amman Jordan'),
	(27, 'Kate Vishnivetskaya', '', 'kvishnivetskaya@uskoinc.com', 2402, 'kvishnivetskaya', 'USKO-2402', '', '', '', 'RDP', 1, 'ISP: Spd Chernega Aleksandr Anatolevich; Location: Odesa'),
	(28, 'Leo Ciobanu', '916-585-2422', 'leo@uskoexpedite.com', 2021, 'leo', 'USKO-2021', '', '', '', 'RDP', 1, 'hap'),
	(29, 'Luby Skots', '916-730-6470', 'luby@uskoinc.com', 1093, 'luby', 'USKO-1093', '', '', '', 'RDP', 1, 'hap'),
	(30, 'Mariia K', '', 'mariiak@primehardware.com', 2405, 'mariiak', 'USKO-2405', '', '', '', 'RDP', 1, 'Primehardware'),
	(31, 'Mary Myronova', '', 'mmyronova@uskoinc.com', 2400, 'mmyronova', 'USKO-2400', '', '', '', 'RDP', 1, 'ISP: Limanet Ltd; Location: Odesa'),
	(32, 'Max Chuvilin', '916-350-0815', 'maxc@uskoexpedite.com', 2033, 'mchuvillin', 'USKO-2033', '', '', '', 'RDP', 0, 'hap'),
	(33, 'Mike Borish', '916-335-7786', 'mike@uskoinc.com', 1031, 'mike', 'USKO-1031', '', '', '', 'RDP', 0, 'hap'),
	(34, 'Miki Nguen', '', 'nguenm@uskologistics.com', 2403, 'nguenm', 'USKO-2403', '', '', '', 'RDP', 1, 'ISP: Tenet Scientific Production Enterprise Llc; Location: Odesa. Uses multiple networks; different ISPs'),
	(35, 'Milen Mananov', '916-605-9294', 'milen@uskoexpedite.com', 2085, 'mmananov', 'USKO-2085', '', '', '', 'RDP', 0, 'hap'),
	(36, 'Mirbek Tepshibaev', '347-570-8965', 'mirbek@uskoexpedite.com', 2072, 'mtepshibaev', 'USKO-2072', '', '', '', 'RDP', 0, 'hap'),
	(37, 'Nelli Piluyeva', '', 'nelli@uahouse.org', 2406, 'npiluyeva', 'USKO-1191', '', '', '', 'RDP', 1, 'part-time uahouse'),
	(38, 'Nikolay Skots', '916-969-7870', 'nikolay@uskoinc.com', 1040, 'nikolay', 'USKO-1040', '', '', '', 'RDP', 1, 'hap'),
	(39, 'Oleg Khomits', '916-532-9911', 'olegk@uskoinc.com', 1036, 'olegk', 'USKO-1036', '', '', '', 'RDP', 0, 'hap'),
	(40, 'Oleks Kuznetsov', '', 'oleks.kuznetsov@gmail.com', 24001, 'oleks', 'USKO-2404', '', '', '', 'RDP', 1, 'devops contractor?'),
	(41, 'Peter Chuk', '916-718-8451', 'cpeter@uskoinc.com', 1191, 'cpeter', 'USKO-1191', '', '', '', 'RDP', 1, 'ISP: Mediacom Cable; Location: Chariton'),
	(42, 'Peter Chuk', '916-718-8451', 'cpeter@uskoinc.com', 9922, 'cpeter', 'WEB01A', '', '', '', 'SSH', 1, 'Serverâ€™s Access (extension 9922 was made up. Not a real extension - only use for remote login)'),
	(43, 'Peter Zuza', '916-270-7076', 'peter@uskoexpedite.com', 2024, 'peter', 'USKO-2024', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Roseville'),
	(44, 'Phil Murza', '916-896-4897', 'phil@uskoinc.com', 1012, 'phil', 'USKO-1012', '', '', '', 'RDP', 0, 'hap'),
	(45, 'Roman Terushkov', '916-202-5096', 'roman@uskoexpedite.com', 2045, 'romant', 'USKO-2045', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Roseville'),
	(46, 'Said Khashimi', '916-367-9435', 'skhashimi@uskoinc.com', 1192, 'skhashimi', 'USKO-1192', '', '', '', 'RDP', 1, 'ISP: Comcast Cable; Location: Citrus Heights'),
	(47, 'Sergey Oleksyuk', '916-241-5753', 'serge@uskoinc.com', 1035, 'soleksyuk', 'USKO-1035', '', '', '', 'RDP', 0, 'hap'),
	(48, 'Sergey Skots', '916-256-7676', 'serges@uskoinc.com', 1091, 'sergeys', 'USKO-1116', '', '', '', 'RDP', 1, 'ISP: Verizon Wireless; Location: Sacramento'),
	(49, 'Snizhana Samiylenko', '916-969-9679', 'snizhana@uskoinc.com', 1114, 'snizhana', 'USKO-1114', '', '', '', 'RDP', 1, 'ISP: Wave Broadband; Location: Lincoln'),
	(50, 'Tanya Kravchuk', '', 'tanyak@uahouse.org', 24001, 'tanyak', 'USKO-2404', '', '', '', 'RDP', 0, 'needed for qb?'),
	(51, 'Vasily Borovsky', '954-512-3629', 'vas@uskoinc.com', 131, '', 'USKO-LOG-1215', '', '', '', 'RDP', 1, 'He wanted short ext'),
	(52, 'Viktoria Balueva', '', 'viktoriia@uskoexpedite.com', 2063, '', 'USKO-2063', '', '', '', 'RDP', 1, 'Odessa. Ext. 2411?'),
	(53, 'Vladee Chilocci', '916-207-1212', 'vladee@uskoinc.com', 1013, 'vladee', 'USKO-1013', '', '', '', 'RDP', 0, 'hap'),
	(54, 'Yana Yaroshuk', '916-591-5752', 'yyaroshuk@uskoinc.com', 1141, 'yyaroshuk', 'USKO-1122', '', '', '', 'RDP', 1, 'hap'),
	(55, 'Yaro Naumchuk', '916-517-0609', 'yaro@uskoinc.com', 1026, 'yaro', 'USKO-1026', '', '', '', 'RDP', 1, 'hap'),
	(56, 'Yuriy Mudrik ', '916-477-1087', 'yuriym@uskoinc.com', 1042, 'yuriym', 'USKO-1042', '', '', '', 'RDP', 1, 'hap');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
