-- phpMyAdmin SQL Dump
-- version 3.3.1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Фев 11 2011 г., 13:02
-- Версия сервера: 5.0.51
-- Версия PHP: 5.2.6-1+lenny9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- База данных: `immotrade`
--

-- --------------------------------------------------------

--
-- Структура таблицы `pages_news`
--

CREATE TABLE IF NOT EXISTS `pages_news` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(500) NOT NULL,
  `title_ru` varchar(500) default NULL,
  `title_en` varchar(500) default NULL,
  `title_de` varchar(500) default NULL,
  `content` longtext NOT NULL,
  `content_ru` longtext,
  `content_en` longtext,
  `content_de` longtext,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `pages_news`
--

INSERT INTO `pages_news` (`id`, `title`, `title_ru`, `title_en`, `title_de`, `content`, `content_ru`, `content_en`, `content_de`, `created`, `updated`) VALUES
(1, 'Тестовая новость', 'Тестовая новость', NULL, NULL, 'Содержание тестовой новости', 'Содержание тестовой новости', NULL, NULL, '2011-02-08 13:20:21', '2011-02-08 13:20:27'),
(2, 'Тестовая новость 2', 'Тестовая новость 2', NULL, NULL, ' Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости ', ' Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости  Содержание тестовой новости ', NULL, NULL, '2011-02-08 13:22:17', '2011-02-08 14:06:40');

-- --------------------------------------------------------

--
-- Структура таблицы `pages_staticpage`
--

CREATE TABLE IF NOT EXISTS `pages_staticpage` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(500) NOT NULL,
  `title_ru` varchar(500) default NULL,
  `title_en` varchar(500) default NULL,
  `title_de` varchar(500) default NULL,
  `url` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `content_ru` longtext,
  `content_en` longtext,
  `content_de` longtext,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `pages_staticpage_a4b49ab` (`url`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `pages_staticpage`
--

INSERT INTO `pages_staticpage` (`id`, `title`, `title_ru`, `title_en`, `title_de`, `url`, `content`, `content_ru`, `content_en`, `content_de`, `created`, `updated`) VALUES
(1, 'О нас', 'О нас', NULL, NULL, 'about-us', 'Содержание страницы на русском языке', 'Содержание страницы на русском языке', NULL, NULL, '2011-02-08 13:19:25', '2011-02-08 13:19:25'),
(2, 'Акции', 'Акции', NULL, NULL, 'shares', 'Содержимое страницы акции', 'Содержимое страницы акции', NULL, NULL, '2011-02-08 13:54:42', '2011-02-08 13:54:42'),
(3, 'Услуги и цены', 'Услуги и цены', NULL, NULL, 'services-and-prices', 'Сожержимое страницы услуги и цены', 'Сожержимое страницы услуги и цены', NULL, NULL, '2011-02-08 13:55:24', '2011-02-08 13:55:24'),
(4, 'Сотрудничество', 'Сотрудничество', NULL, NULL, 'cooperation', 'Содержимое страницы сотрудничество', 'Содержимое страницы сотрудничество', NULL, NULL, '2011-02-08 13:55:57', '2011-02-08 13:55:57');
