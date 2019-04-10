-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 10, 2019 at 07:27 AM
-- Server version: 5.7.25-0ubuntu0.16.04.2
-- PHP Version: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205CDE`
--

-- --------------------------------------------------------

--
-- Table structure for table `CommentTable`
--

CREATE TABLE `CommentTable` (
  `CommentID` int(200) NOT NULL,
  `MusicID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `Comment` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CommentTable`
--

INSERT INTO `CommentTable` (`CommentID`, `MusicID`, `UserID`, `Comment`) VALUES
(1, 2, 2, 'Excellent!'),
(2, 2, 2, 'It sounds good'),
(3, 2, 2, 'Unbelievable! '),
(4, 3, 2, 'Not bad');

-- --------------------------------------------------------

--
-- Table structure for table `CustomerInformation`
--

CREATE TABLE `CustomerInformation` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `Phone` int(11) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Balance` int(6) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CustomerInformation`
--

INSERT INTO `CustomerInformation` (`id`, `username`, `pwd`, `Phone`, `Email`, `Balance`) VALUES
(2, 'Wong', 'Wong', 12345685, 'chriswong@gmail.com', 20),
(3, 'MayLee', 'abc', 28971238, 'Maylee@gmail.com', 0),
(4, 'BenLee', 'Lee', 89732123, 'benLee@gmail.com', 0),
(5, 'MaryTo', 'Lam', 15624362, 'maryto@gmail.com', 0),
(7, 'Mary', 'Little', NULL, 'had@gmail', 0),
(8, 'Mac', 'local', NULL, 'maclovers@gmail', 0),
(9, 'Window', 'www', NULL, 'wind@gmail.com', 0),
(10, 'Window', 'www', NULL, 'wind@gmail.com', 0),
(11, 'apple', 'abc', NULL, 'juice@gmail.com', 0),
(12, 'orange', 'aabb', NULL, 'juicy@gmail.com', 0),
(15, 'Kitty', 'pwd', 12345678, 'Kitty@gmail.com', 0),
(16, '123', '123', 12345678, '123@123.com', 0),
(17, 'Wasser', '123', 12345678, '123@123.com', 100),
(18, '123', '123', 12345678, '123@123.com', 0),
(19, 'abc', 'abc', 12345678, 'abc@123.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `MusicInformation`
--

CREATE TABLE `MusicInformation` (
  `MusicID` int(10) NOT NULL,
  `MusicName` text NOT NULL,
  `Musicimage` varbinary(1000) DEFAULT NULL,
  `ImgName` varchar(300) DEFAULT NULL,
  `TypeOfMusic` set('Pop Music','Rock','Dance Music','Jazz','Hip-Hop','Blues','Classical Music','Others') NOT NULL,
  `Price` int(10) DEFAULT NULL,
  `Share` set('Public','Friends','Myself','') NOT NULL DEFAULT 'Public',
  `Description` text,
  `UserID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MusicInformation`
--

INSERT INTO `MusicInformation` (`MusicID`, `MusicName`, `Musicimage`, `ImgName`, `TypeOfMusic`, `Price`, `Share`, `Description`, `UserID`) VALUES
(1, 'Song', '', '', 'Jazz', NULL, 'Friends', 'Hello, it is my first song', 2),
(2, 'Music2', '', '', 'Rock', 13, 'Public', 'Hello, it is my second song', 2),
(3, 'Music3', '', '', 'Rock', NULL, 'Public', 'Hello, it is my third song', 2),
(4, 'POP', NULL, NULL, 'Pop Music', NULL, 'Public', 'POP is my song', 17),
(5, 'Song2', NULL, NULL, 'Hip-Hop', NULL, 'Public', 'A song for friends', 17),
(6, 'Dance', NULL, NULL, 'Dance Music', 10, 'Public', 'Creative', 2);

-- --------------------------------------------------------

--
-- Table structure for table `Purchase`
--

CREATE TABLE `Purchase` (
  `PurchaseID` int(200) NOT NULL,
  `UserID` int(11) NOT NULL,
  `MusicID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Purchase`
--

INSERT INTO `Purchase` (`PurchaseID`, `UserID`, `MusicID`) VALUES
(1, 2, 2),
(5, 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `SaleMusic`
--

CREATE TABLE `SaleMusic` (
  `SaleID` int(11) NOT NULL,
  `MusicID` int(11) NOT NULL,
  `Number` int(11) NOT NULL DEFAULT '0',
  `UserID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `SaleMusic`
--

INSERT INTO `SaleMusic` (`SaleID`, `MusicID`, `Number`, `UserID`) VALUES
(1, 4, 1, 2),
(2, 4, 1, 17),
(3, 6, 0, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CommentTable`
--
ALTER TABLE `CommentTable`
  ADD PRIMARY KEY (`CommentID`),
  ADD KEY `MusicID` (`MusicID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `CustomerInformation`
--
ALTER TABLE `CustomerInformation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `MusicInformation`
--
ALTER TABLE `MusicInformation`
  ADD PRIMARY KEY (`MusicID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `Purchase`
--
ALTER TABLE `Purchase`
  ADD PRIMARY KEY (`PurchaseID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `MusicID` (`MusicID`);

--
-- Indexes for table `SaleMusic`
--
ALTER TABLE `SaleMusic`
  ADD PRIMARY KEY (`SaleID`),
  ADD KEY `MusicID` (`MusicID`),
  ADD KEY `UserID` (`UserID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CommentTable`
--
ALTER TABLE `CommentTable`
  MODIFY `CommentID` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `CustomerInformation`
--
ALTER TABLE `CustomerInformation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `MusicInformation`
--
ALTER TABLE `MusicInformation`
  MODIFY `MusicID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `Purchase`
--
ALTER TABLE `Purchase`
  MODIFY `PurchaseID` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `SaleMusic`
--
ALTER TABLE `SaleMusic`
  MODIFY `SaleID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `CommentTable`
--
ALTER TABLE `CommentTable`
  ADD CONSTRAINT `CommentTable_ibfk_1` FOREIGN KEY (`MusicID`) REFERENCES `MusicInformation` (`MusicID`),
  ADD CONSTRAINT `CommentTable_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `CustomerInformation` (`id`);

--
-- Constraints for table `MusicInformation`
--
ALTER TABLE `MusicInformation`
  ADD CONSTRAINT `MusicInformation_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `CustomerInformation` (`id`);

--
-- Constraints for table `Purchase`
--
ALTER TABLE `Purchase`
  ADD CONSTRAINT `Purchase_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `CustomerInformation` (`id`),
  ADD CONSTRAINT `Purchase_ibfk_2` FOREIGN KEY (`MusicID`) REFERENCES `MusicInformation` (`MusicID`);

--
-- Constraints for table `SaleMusic`
--
ALTER TABLE `SaleMusic`
  ADD CONSTRAINT `SaleMusic_ibfk_1` FOREIGN KEY (`MusicID`) REFERENCES `MusicInformation` (`MusicID`),
  ADD CONSTRAINT `SaleMusic_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `CustomerInformation` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
