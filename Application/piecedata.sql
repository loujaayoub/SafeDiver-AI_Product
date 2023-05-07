-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Mer 26 Janvier 2022 à 10:35
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `piecedata`
--


-- --------------------------------------------------------

--
-- Structure de la table `devis_piece`
--

CREATE TABLE IF NOT EXISTS `devis_piece` (
  `marque` varchar(5) DEFAULT NULL,
  `modele` varchar(5) DEFAULT NULL,
  `piece` varchar(20) DEFAULT NULL,
  `DMC` varchar(9) DEFAULT NULL,
  `prix_original` decimal(6,2) NOT NULL,
  `prix_recuperable` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `devis_piece`
--

INSERT INTO `devis_piece` (`marque`, `modele`, `piece`, `DMC`, `prix_original`, `prix_recuperable`) VALUES
('DACIA', 'LOGAN', 'Aile/Fender', '2010-2014', '0.00', '600.00'),
('DACIA', 'LOGAN', 'Aile/Fender', '2005-2009', '0.00', '1500.00'),
('DACIA', 'LOGAN', 'Aile/Fender', '2015-2019', '0.00', '800.00'),
('DACIA', 'LOGAN', 'Aile/Fender', '2020-2024', '139.00', '0.00'),
('DACIA', 'LOGAN', 'Calendre', '2010-2014', '0.00', '233.00'),
('DACIA', 'LOGAN', 'Calendre', '2015-2019', '970.00', '566.00'),
('DACIA', 'LOGAN', 'Calandre', '2020-2024', '739.00', '1050.00'),
('DACIA', 'LOGAN', 'Calandre', '2010-2014', '0.00', '500.00'),
('DACIA', 'LOGAN', 'Calandre', '2015-2019', '0.00', '600.00'),
('DACIA', 'LOGAN', 'Calandre', '2010-2014', '0.00', '400.00'),
('DACIA', 'LOGAN', 'Capot', '2010-2014', '0.00', '1266.00'),
('DACIA', 'LOGAN', 'Capot', '2015-2019', '1500.00', '1766.00'),
('DACIA', 'LOGAN', 'Capot', '2020-2024', '0.00', '3047.00'),
('DACIA', 'LOGAN', 'Capot', '2020-2024', '3047.00', '0.00'),
('DACIA', 'LOGAN', 'Capot', '2010-2014', '0.00', '1200.00'),
('DACIA', 'LOGAN', 'Capot', '2015-2019', '0.00', '1333.00'),
('DACIA', 'LOGAN', 'Capot', '2020-2024', '251.00', '0.00'),
('DACIA', 'LOGAN', 'Coffre', '2005-2009', '0.00', '1133.00'),
('DACIA', 'LOGAN', 'Coffre', '2010-2014', '0.00', '1200.00'),
('DACIA', 'LOGAN', 'Coffre', '2015-2019', '0.00', '1366.00'),
('DACIA', 'LOGAN', 'Lampe Avant', '2015-2019', '0.00', '700.00'),
('DACIA', 'LOGAN', 'Lampe Avant', '2020-2024', '210.00', '0.00'),
('DACIA', 'LOGAN', 'Lampe Avant', '2005-2009', '0.00', '300.00'),
('DACIA', 'LOGAN', 'Lampe Avant', '2010-2014', '0.00', '300.00'),
('DACIA', 'LOGAN', 'Lampe Arriere', '2010-2014', '0.00', '400.00'),
('DACIA', 'LOGAN', 'Lampe Arriere', '2015-2019', '714.00', '400.00'),
('DACIA', 'LOGAN', 'Lampe Arriere', '2020-2024', '800.00', '500.00'),
('DACIA', 'LOGAN', 'Pare-chocs arrière', '2005-2009', '0.00', '800.00'),
('DACIA', 'LOGAN', 'Pare-chocs arrière', '2010-2014', '0.00', '866.00'),
('DACIA', 'LOGAN', 'Pare-chocs arrière', '2015-2019', '0.00', '933.00'),
('DACIA', 'LOGAN', 'Pare-chocs arrière', '2020-2024', '2291.00', '0.00'),
('DACIA', 'LOGAN', 'Pare-chocs Avant', '2010-2014', '0.00', '1200.00'),
('DACIA', 'LOGAN', 'Pare-chocs Avant', '2015-2019', '1673.00', '1466.00'),
('DACIA', 'LOGAN', 'Pare-chocs Avant', '2020-2024', '2656.00', '1828.00'),
('DACIA', 'LOGAN', 'Porte Arriere', '2005-2009', '0.00', '1000.00'),
('DACIA', 'LOGAN', 'Porte Arriere', '2010-2014', '0.00', '3000.00'),
('DACIA', 'LOGAN', 'Porte Arriere', '2015-2019', '3764.00', '0.00'),
('DACIA', 'LOGAN', 'Porte Avant', '2005-2009', '0.00', '1500.00'),
('DACIA', 'LOGAN', 'Porte Avant', '2010-2014', '0.00', '1575.00'),
('DACIA', 'LOGAN', 'Porte Avant', '2015-2019', '0.00', '1500.00'),
('DACIA', 'LOGAN', 'Porte Avant', '2015-2019', '2902.00', '0.00'),
('DACIA', 'LOGAN', 'Rétroviseur', '2010-2014', '0.00', '450.00'),
('DACIA', 'LOGAN', 'Rétroviseur', '2015-2019', '859.00', '700.00'),
('DACIA', 'LOGAN', 'Roue', '2015-2019', '100.00', '150.00'),
('DACIA', 'LOGAN', 'Roue', '2020-2024', '150.00', '200.00'),
('DACIA', 'LOGAN', 'Fenetre Laterale', '2015-2019', '500.00', '600.00'),
('DACIA', 'LOGAN', 'Fenetre Laterale', '2020-2024', '600.00', '700.00'),
('DACIA', 'LOGAN', 'Fenetre Avant', '2015-2019', '100.00', '150.00'),
('DACIA', 'LOGAN', 'Fenetre Avant', '2020-2024', '150.00', '200.00'),
('DACIA', 'LOGAN', 'Fenetre Arriere', '2015-2019', '100.00', '150.00'),
('DACIA', 'LOGAN', 'Fenetre Arriere', '2020-2024', '150.00', '200.00');

-- --------------------------------------------------------

--
-- Structure de la table `mot_mop`
--

CREATE TABLE IF NOT EXISTS `mot_mop` (
  `Operation_E` varchar(20) NOT NULL DEFAULT '',
  `C1_MOT` decimal(4,2) NOT NULL,
  `C2_MOT` decimal(4,2) NOT NULL,
  `C3_MOT` decimal(4,2) NOT NULL,
  `C4_MOT` decimal(4,2) NOT NULL,
  `C1_MOP` decimal(4,2) NOT NULL,
  `C2_MOP` decimal(4,2) NOT NULL,
  `C3_MOP` decimal(4,2) NOT NULL,
  `C4_MOP` decimal(4,2) NOT NULL,
  PRIMARY KEY (`Operation_E`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `mot_mop`
--

INSERT INTO `mot_mop` (`Operation_E`, `C1_MOT`, `C2_MOT`, `C3_MOT`, `C4_MOT`, `C1_MOP`, `C2_MOP`, `C3_MOP`, `C4_MOP`) VALUES
('Aile/Fender', '3.00', '4.00', '4.00', '4.00', '3.00', '3.00', '3.00', '4.00'),
('Calandre', '0.70', '0.70', '0.70', '0.70', '1.00', '1.00', '1.00', '1.00'),
('Calendre', '0.70', '0.70', '0.70', '0.70', '1.00', '1.00', '1.00', '1.00'),
('Capot', '4.00', '4.00', '5.00', '5.00', '4.00', '4.00', '4.00', '5.00'),
('Coffre', '5.00', '5.00', '5.00', '5.00', '4.00', '5.00', '5.00', '5.00'),
('Lampe Arriere', '0.70', '0.70', '0.70', '0.80', '0.00', '0.00', '0.00', '0.00'),
('Lampe Avant', '0.70', '0.70', '0.70', '0.80', '0.00', '0.00', '0.00', '0.00'),
('Pare-chocs Avant', '3.00', '4.00', '4.00', '5.00', '3.00', '3.00', '3.00', '4.00'),
('Pare-chocs arrière', '3.00', '3.00', '4.00', '4.00', '3.00', '3.00', '3.00', '3.00'),
('Porte Arriere', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '6.00'),
('Porte Avant', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '6.00'),
('Fenetre Avant ', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '6.00'),
('Fenetre Laterale', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '6.00'),
('Fenetre Arriere', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '5.00', '6.00'),
('Rétroviseur', '1.00', '1.00', '1.00', '1.00', '0.20', '0.20', '0.20', '0.20');

-- --------------------------------------------------------

--
-- Structure de la table `peinture`
--

CREATE TABLE IF NOT EXISTS `peinture` (
  `Operation` varchar(20) NOT NULL DEFAULT '',
  `C1_UN` int(3) DEFAULT NULL,
  `C1_MET` int(3) DEFAULT NULL,
  `C1_NAC` int(3) DEFAULT NULL,
  `C2_UN` int(3) DEFAULT NULL,
  `C2_MET` int(3) DEFAULT NULL,
  `C2_NAC` int(3) DEFAULT NULL,
  `C3_UN` int(3) DEFAULT NULL,
  `C3_MET` int(3) DEFAULT NULL,
  `C3_NAC` int(3) DEFAULT NULL,
  `C4_UN` int(3) DEFAULT NULL,
  `C4_MET` int(3) DEFAULT NULL,
  `C4_NAC` int(3) DEFAULT NULL,
  PRIMARY KEY (`Operation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `peinture`
--

INSERT INTO `peinture` (`Operation`, `C1_UN`, `C1_MET`, `C1_NAC`, `C2_UN`, `C2_MET`, `C2_NAC`, `C3_UN`, `C3_MET`, `C3_NAC`, `C4_UN`, `C4_MET`, `C4_NAC`) VALUES
('Aile/Fender', 210, 268, 342, 222, 300, 384, 226, 304, 388, 246, 330, 418),
('Capot', 230, 290, 374, 242, 322, 418, 246, 326, 422, 266, 354, 456),
('Coffre', 230, 290, 374, 242, 322, 418, 246, 326, 422, 266, 350, 456),
('Pare-chocs Avant', 198, 258, 342, 210, 290, 390, 214, 294, 394, 234, 322, 420),
('Pare-chocs arrière', 198, 258, 342, 210, 290, 390, 214, 294, 394, 234, 322, 420),
('Porte Arriere', 218, 278, 374, 230, 310, 418, 234, 314, 422, 254, 342, 456),
('Porte Avant', 218, 278, 374, 230, 310, 418, 234, 314, 422, 254, 342, 456),
('PorteAVD', 218, 278, 374, 230, 310, 418, 234, 314, 422, 254, 342, 456),
('PorteAVG', 218, 278, 374, 230, 310, 418, 234, 314, 422, 254, 342, 456);

-- --------------------------------------------------------

--
-- Structure de la table `reparation`
--

CREATE TABLE IF NOT EXISTS `reparation` (
  `Operation_D` varchar(20) NOT NULL DEFAULT '',
  `C1_Endom_Leger` decimal(4,2) NOT NULL,
  `C1_Endom_Moyen` decimal(4,2) NOT NULL,
  `C1_Endom_Fort` decimal(4,2) NOT NULL,
  `C2_Endom_Leger` decimal(4,2) NOT NULL,
  `C2_Endom_Moyen` decimal(4,2) NOT NULL,
  `C2_Endom_Fort` decimal(4,2) NOT NULL,
  `C4_Endom_Leger` decimal(4,2) NOT NULL,
  `C4_Endom_Moyen` decimal(4,2) NOT NULL,
  `C4_Endom_Fort` decimal(4,2) NOT NULL,
  `PROPOSITION%` int(2) NOT NULL,
  PRIMARY KEY (`Operation_D`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `reparation`
--

INSERT INTO `reparation` (`Operation_D`, `C1_Endom_Leger`, `C1_Endom_Moyen`, `C1_Endom_Fort`, `C2_Endom_Leger`, `C2_Endom_Moyen`, `C2_Endom_Fort`, `C4_Endom_Leger`, `C4_Endom_Moyen`, `C4_Endom_Fort`, `PROPOSITION%`) VALUES
('Aile/Fender', '1.00', '3.00', '4.00', '2.00', '3.00', '5.00', '2.00', '4.00', '7.00', 21),
('Calandre', '1.00', '1.00', '3.00', '1.00', '2.00', '4.00', '1.00', '3.00', '5.00', 18),
('Calendre', '1.00', '1.00', '3.00', '1.00', '2.00', '4.00', '1.00', '3.00', '5.00', 18),
('Capot', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', '3.00', '6.00', '10.00', 21),
('Coffre', '2.00', '4.00', '7.00', '3.00', '5.00', '8.00', '3.00', '6.00', '9.00', 22),
('Lampe Arriere', '1.00', '2.00', '2.00', '1.00', '2.00', '2.00', '1.00', '2.00', '2.00', 16),
('Lampe Avant', '1.00', '2.00', '2.00', '1.00', '2.00', '2.00', '1.00', '2.00', '2.00', 16),
('Pare-chocs Avant', '2.00', '3.00', '4.00', '2.00', '3.00', '6.00', '2.00', '4.00', '7.00', 21),
('Pare-chocs arrière', '2.00', '3.00', '4.00', '2.00', '3.00', '6.00', '2.00', '4.00', '7.00', 21),
('Porte Arriere', '2.00', '4.00', '6.00', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', 21),
('Porte Avant', '2.00', '4.00', '6.00', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', 21),
('Fenetre Laterale', '2.00', '4.00', '6.00', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', 21),
('Fenetre Avant', '2.00', '4.00', '6.00', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', 21),
('Fenetre Arriere', '2.00', '4.00', '6.00', '2.00', '4.00', '7.00', '3.00', '5.00', '9.00', 21),
('Rétroviseur', '1.00', '2.00', '3.00', '1.00', '2.00', '4.00', '1.00', '3.00', '6.00', 17);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
