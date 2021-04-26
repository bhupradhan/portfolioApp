-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 26, 2021 at 11:54 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `acadamics`
--

CREATE TABLE `acadamics` (
  `constantKey` int(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `board` varchar(100) NOT NULL,
  `college` varchar(100) NOT NULL,
  `marks` int(100) NOT NULL,
  `hboards` varchar(50) NOT NULL,
  `hcollege` varchar(100) NOT NULL,
  `hmarks` int(100) NOT NULL,
  `skills` varchar(200) NOT NULL,
  `level` varchar(50) NOT NULL,
  `category` varchar(200) NOT NULL,
  `ptitle` longtext NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `acadamics`
--

INSERT INTO `acadamics` (`constantKey`, `email`, `board`, `college`, `marks`, `hboards`, `hcollege`, `hmarks`, `skills`, `level`, `category`, `ptitle`, `description`) VALUES
(123, 'bhupradhan20@gmail.com', 'CBSE', 'DAV Public school', 95, 'CBSE', 'DAV Public School', 89, 'Python', 'Basic', 'technical', 'Web application for construction company', 'Web application for construction company using flask and reactjs for front end');

-- --------------------------------------------------------

--
-- Table structure for table `achieve`
--

CREATE TABLE `achieve` (
  `constantKey` int(50) NOT NULL,
  `sem` int(50) NOT NULL,
  `activity` longtext NOT NULL,
  `email` varchar(100) NOT NULL,
  `time` int(100) NOT NULL,
  `course` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `achieve`
--

INSERT INTO `achieve` (`constantKey`, `sem`, `activity`, `email`, `time`, `course`) VALUES
(123, 3, 'PHP', 'bhupradhan20@gmail.com', 50, 'Technical'),
(123, 4, 'Advance Python', 'bhupradhan20@gmail.com', 120, 'Technical');

-- --------------------------------------------------------

--
-- Table structure for table `coact`
--

CREATE TABLE `coact` (
  `constantKey` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `activity` longtext NOT NULL,
  `sem` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coact`
--

INSERT INTO `coact` (`constantKey`, `email`, `activity`, `sem`) VALUES
('123', 'bhupradhan20@gmail.com', 'Php workshop', '3'),
('123', 'bhupradhan20@gmail.com', 'flask workshop(February 20)', '4');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `constantKey` int(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `address` longtext NOT NULL,
  `cname` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `year` varchar(200) NOT NULL,
  `links` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`constantKey`, `fname`, `lname`, `email`, `city`, `dob`, `address`, `cname`, `branch`, `year`, `links`) VALUES
(123, 'Bhushan', 'Pradhan', 'bhupradhan20@gmail.com', 'panvel', '1999-09-20', 'panvel', 'Pillai College Of Engineering, New Panvel', 'computer engineering', 'Second Year', 'blog site: https://intospirituality.blogspot.com/2020/06/about   linkedin: www.linkedin.com/in/bhushan   github: https://github.com/bhupradhan'),
(123, 'Ameya', 'Joshi', 'ameyajoshi20@gmail.com', 'panvel', '2000-06-23', 'panvel', 'Pillai College Of Engineering, New Panvel', 'computer engineering', 'Second Year', 'https://intospirituality.blogspot.com/2020/06/about www.linkedin.com/in/bhushan https://github.com/bhupradhan'),
(123, 'Ameya', 'Joshi', 'pradhanbhuvi18ce@student.mes.ac.in', 'panvel', '2000-11-07', 'panvel', 'Pillai College Of Engineering, New Panvel', 'computer engineering', 'Second Year', 'no links');

-- --------------------------------------------------------

--
-- Table structure for table `goals`
--

CREATE TABLE `goals` (
  `email` varchar(200) NOT NULL,
  `sgoals` varchar(200) NOT NULL,
  `lgoals` varchar(200) NOT NULL,
  `constantKey` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `goals`
--

INSERT INTO `goals` (`email`, `sgoals`, `lgoals`, `constantKey`) VALUES
('bhupradhan20@gmail.com', 'Be Happy', 'Become Entreprenuar', '123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
