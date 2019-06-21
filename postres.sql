-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-06-2019 a las 06:07:49
-- Versión del servidor: 10.1.32-MariaDB
-- Versión de PHP: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tutoriales`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `postres`
--

CREATE TABLE `postres` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` varchar(20) NOT NULL,
  `stock` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `postres`
--

INSERT INTO `postres` (`id`, `nombre`, `precio`, `stock`, `img`, `created_at`, `updated_at`) VALUES
(1, 'Gelatina de Fresa', '4.50', '46', 'gf_xSeTO3I.jpg', '2019-06-20 08:27:15.877932', '2019-06-20 08:27:49.101833'),
(2, 'Torta de Chocolate', '5.50', '30', 'tc_eZFc4sh.jpg', '2019-06-20 08:27:35.583059', '2019-06-20 11:04:36.835346'),
(3, 'Suspiro a la Limeña', '3.80', '35', 'sl_jCFHSpr.jpg', '2019-06-20 08:28:14.497285', '2019-06-20 08:28:14.497285'),
(4, 'Arroz con Leche', '3.60', '38', 'al_3a7jXQt.jpg', '2019-06-20 08:28:52.368451', '2019-06-20 08:28:52.368451');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `postres`
--
ALTER TABLE `postres`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `postres`
--
ALTER TABLE `postres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
