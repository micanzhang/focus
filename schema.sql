-- MySQL dump 10.14  Distrib 5.5.34-MariaDB, for Linux (i686)
--
-- Host: localhost    Database: focus
-- ------------------------------------------------------
-- Server version	5.5.34-MariaDB

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

DROP DATABASE IF EXISTS `focus`;

CREATE DATABASE `focus`;

USE `focus`;

GRANT ALL PRIVILEGES ON `focus`.* TO 'focus'@'%' IDENTIFIED BY 'focus';
GRANT ALL PRIVILEGES ON `focus`.* TO 'focus'@'localhost' IDENTIFIED BY 'focus';

-- ----------------------------
-- Table structure for `follow`
-- ----------------------------
DROP TABLE IF EXISTS `follow`;
CREATE TABLE `follow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `follower` varchar(32) NOT NULL COMMENT 'follow one ',
  `following` varchar(32) NOT NULL DEFAULT '' COMMENT 'followed one',
  `create_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `follower` (`follower`,`following`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of follow
-- ----------------------------
INSERT INTO `follow` VALUES ('4', 'micanzhang', 'user1', '1392195329');

-- ----------------------------
-- Table structure for `mention`
-- ----------------------------
DROP TABLE IF EXISTS `mention`;
CREATE TABLE `mention` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`,`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mention
-- ----------------------------
INSERT INTO `mention` VALUES ('1', 'micanzhang', '7');
INSERT INTO `mention` VALUES ('5', 'micanzhang', '12');
INSERT INTO `mention` VALUES ('6', 'micanzhang', '13');
INSERT INTO `mention` VALUES ('8', 'micanzhang', '14');
INSERT INTO `mention` VALUES ('2', 'user1', '9');
INSERT INTO `mention` VALUES ('3', 'user2', '9');
INSERT INTO `mention` VALUES ('4', 'user2', '10');
INSERT INTO `mention` VALUES ('7', 'user2', '13');

-- ----------------------------
-- Table structure for `post`
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `author` varchar(32) NOT NULL,
  `content` varchar(255) NOT NULL,
  `create_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `content` (`content`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('1', 'micanzhang', 'micanzhang', '#无耻之徒 加油菲利普', '1392086198');
INSERT INTO `post` VALUES ('2', 'micanzhang', 'micanzhang', '#无耻之徒 菲奥娜sucks！', '1392086767');
INSERT INTO `post` VALUES ('3', 'micanzhang', 'micanzhang', '#nba# #crossover# @allen @skip @micanzhang you guys rocks!and #and1tour# is a wonderful game', '1392112847');
INSERT INTO `post` VALUES ('4', 'micanzhang', 'micanzhang', '#nba# #crossover# @allen @skip @micanzhang you guys rocks!and #and1tour# is a wonderful game', '1392112948');
INSERT INTO `post` VALUES ('5', 'micanzhang', 'micanzhang', '#nba# #crossover# @allen @skip @micanzhang you guys rocks!and #and1tour# is a wonderful game', '1392113044');
INSERT INTO `post` VALUES ('6', 'micanzhang', 'micanzhang', '#nba# #crossover# @allen @skip @micanzhang you guys rocks!and #and1tour# is a wonderful game', '1392113074');
INSERT INTO `post` VALUES ('7', 'micanzhang', 'micanzhang', '#nba# #crossover# @allen @skip @micanzhang you guys rocks!and #and1tour# is a wonderful game', '1392113130');
INSERT INTO `post` VALUES ('8', 'user1', 'user1', '#无耻之徒# 快点出吧', '1392181938');
INSERT INTO `post` VALUES ('9', 'micanzhang', 'micanzhang', '#雷霆vs开拓者# @user1 @user2 利拉德和阿尔德里奇最后面有点独啊', '1392196513');
INSERT INTO `post` VALUES ('10', 'micanzhang', 'micanzhang', '#雷霆vs开拓者# @user2 估计季后赛会遇上。。。', '1392198253');
INSERT INTO `post` VALUES ('11', 'micanzhang', 'micanzhang', '#无耻之徒#  karen不出来了吗？', '1392198442');
INSERT INTO `post` VALUES ('12', 'user1', 'user1', '#无耻之徒# @micanzhang kind of peaty.', '1392198590');
INSERT INTO `post` VALUES ('13', 'user1', 'user1', '#happy张江# @micanzhang @user2 上次的照片真不错...', '1392198680');
INSERT INTO `post` VALUES ('14', 'user1', 'user1', '#阿森纳vs曼联# @micanzhang 阿森纳状态起来的太慢了，上半场没有进入状态啊', '1392249128');
INSERT INTO `post` VALUES ('15', 'user1', 'micanzhang', '#无耻之徒 加油菲利普', '1392249881');

-- ----------------------------
-- Table structure for `post_geo`
-- ----------------------------
DROP TABLE IF EXISTS `post_geo`;
CREATE TABLE `post_geo` (
  `post_id` int(11) NOT NULL,
  `lat` float(10,6) NOT NULL,
  `lng` float(10,6) NOT NULL,
  `address` varchar(95) NOT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post_geo
-- ----------------------------
INSERT INTO `post_geo` VALUES ('10', '31.235041', '121.506599', '');
INSERT INTO `post_geo` VALUES ('11', '31.235252', '121.505814', '');
INSERT INTO `post_geo` VALUES ('12', '31.231178', '121.511467', '');
INSERT INTO `post_geo` VALUES ('13', '31.201258', '121.591743', '');

-- ----------------------------
-- Table structure for `post_topic`
-- ----------------------------
DROP TABLE IF EXISTS `post_topic`;
CREATE TABLE `post_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(32) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `topic` (`topic`,`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post_topic
-- ----------------------------
INSERT INTO `post_topic` VALUES ('3', 'and1tour', '6');
INSERT INTO `post_topic` VALUES ('6', 'and1tour', '7');
INSERT INTO `post_topic` VALUES ('2', 'crossover', '6');
INSERT INTO `post_topic` VALUES ('5', 'crossover', '7');
INSERT INTO `post_topic` VALUES ('12', 'happy张江', '13');
INSERT INTO `post_topic` VALUES ('1', 'nba', '6');
INSERT INTO `post_topic` VALUES ('4', 'nba', '7');
INSERT INTO `post_topic` VALUES ('7', '无耻之徒', '8');
INSERT INTO `post_topic` VALUES ('10', '无耻之徒', '11');
INSERT INTO `post_topic` VALUES ('11', '无耻之徒', '12');
INSERT INTO `post_topic` VALUES ('13', '阿森纳vs曼联', '14');
INSERT INTO `post_topic` VALUES ('8', '雷霆vs开拓者', '9');
INSERT INTO `post_topic` VALUES ('9', '雷霆vs开拓者', '10');

-- ----------------------------
-- Table structure for `session`
-- ----------------------------
DROP TABLE IF EXISTS `session`;
CREATE TABLE `session` (
  `session_id` char(128) NOT NULL,
  `atime` datetime NOT NULL,
  `data` text,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of session
-- ----------------------------
INSERT INTO `session` VALUES ('69bb705419a0590806b636cf54a24dda86b2cec9', '2014-02-12 15:06:55', 'KGRwMQpTJ2lwJwpwMgpWMTI3LjAuMC4xCnAzCnNTJ2xvZ2luJwpwNApJMQpzUyd1c2VyJwpwNQpj\nY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDYKKGNhcHAubW9kZWwudXNlcgpVc2VyCnA3CmNfX2J1\naWx0aW5fXwpvYmplY3QKcDgKTnRScDkKKGRwMTAKUyd1c2VybmFtZScKcDExClZkaWFuZQpwMTIK\nc1Mnc3RhdHVzJwpwMTMKSTAKc1MndXBkYXRlX3RpbWUnCnAxNApMMTM5MjE4NDgwMkwKc1MnX3Nh\nX2luc3RhbmNlX3N0YXRlJwpwMTUKZzYKKGNzcWxhbGNoZW15Lm9ybS5zdGF0ZQpJbnN0YW5jZVN0\nYXRlCnAxNgpnOApOdFJwMTcKKGRwMTgKUydjbGFzc18nCnAxOQpnNwpzUydtb2RpZmllZCcKcDIw\nCkkwMApzUydjb21taXR0ZWRfc3RhdGUnCnAyMQooZHAyMgpzUydpbnN0YW5jZScKcDIzCmc5CnNT\nJ2NhbGxhYmxlcycKcDI0CihkcDI1CnNTJ3BhcmVudHMnCnAyNgooZHAyNwpzUydrZXknCnAyOAoo\nZzcKKEw0TAp0dHAyOQpzUydleHBpcmVkJwpwMzAKSTAwCnNTJ19wZW5kaW5nX211dGF0aW9ucycK\ncDMxCihkcDMyCnNic1MnZW1haWwnCnAzMwpWZGlhbmVAZ21haWwuY29tCnAzNApzUydjcmVhdGVf\ndGltZScKcDM1CkwxMzkyMTg0ODAyTApzUydfcGFzc3dvcmQnCnAzNgpWYzY0YTk3ZjRhNjAyM2Yz\nZWIzMjk2MTA4MjYwN2ZjNTUKcDM3CnNTJ2lkJwpwMzgKTDRMCnNic1Mnc2Vzc2lvbl9pZCcKcDM5\nClMnNjliYjcwNTQxOWEwNTkwODA2YjYzNmNmNTRhMjRkZGE4NmIyY2VjOScKcDQwCnMu\n');
INSERT INTO `session` VALUES ('b0a7ee90d1e2d02ae4778a0bf10ce33e2fc8530b', '2014-02-13 14:12:34', 'KGRwMQpTJ2lwJwpwMgpWMTI3LjAuMC4xCnAzCnNTJ2xvZ2luJwpwNApJMQpzUyd1c2VyJwpwNQpj\nY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDYKKGNhcHAubW9kZWwudXNlcgpVc2VyCnA3CmNfX2J1\naWx0aW5fXwpvYmplY3QKcDgKTnRScDkKKGRwMTAKUyd1c2VybmFtZScKcDExClZ1c2VyMQpwMTIK\nc1Mnc3RhdHVzJwpwMTMKSTAKc1MndXBkYXRlX3RpbWUnCnAxNApMMTM5MjE4MTUyMUwKc1MnX3Nh\nX2luc3RhbmNlX3N0YXRlJwpwMTUKZzYKKGNzcWxhbGNoZW15Lm9ybS5zdGF0ZQpJbnN0YW5jZVN0\nYXRlCnAxNgpnOApOdFJwMTcKKGRwMTgKUydjbGFzc18nCnAxOQpnNwpzUydtb2RpZmllZCcKcDIw\nCkkwMApzUydjb21taXR0ZWRfc3RhdGUnCnAyMQooZHAyMgpzUydpbnN0YW5jZScKcDIzCmc5CnNT\nJ2NhbGxhYmxlcycKcDI0CihkcDI1CnNTJ3BhcmVudHMnCnAyNgooZHAyNwpzUydrZXknCnAyOAoo\nZzcKKEwyTAp0dHAyOQpzUydleHBpcmVkJwpwMzAKSTAwCnNTJ19wZW5kaW5nX211dGF0aW9ucycK\ncDMxCihkcDMyCnNic1MnZW1haWwnCnAzMwpWdXNlcjFAZ21haWwuY29tCnAzNApzUydjcmVhdGVf\ndGltZScKcDM1CkwxMzkyMTgxNTIxTApzUydfcGFzc3dvcmQnCnAzNgpWN2NkMmUxNmMzOTBjM2Zl\nNTMyMGZkMGM5NmFiMjg2YWIKcDM3CnNTJ2lkJwpwMzgKTDJMCnNic1Mnc2Vzc2lvbl9pZCcKcDM5\nClMnYjBhN2VlOTBkMWUyZDAyYWU0Nzc4YTBiZjEwY2UzM2UyZmM4NTMwYicKcDQwCnMu\n');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(64) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'micanzhang', '2770296fe4b10de796846b7e71c50b5f', 'ice3wtt@gmail.com', '0', '1392030091', '1392030091');
INSERT INTO `user` VALUES ('2', 'user1', '7cd2e16c390c3fe5320fd0c96ab286ab', 'user1@gmail.com', '0', '1392181521', '1392181521');
INSERT INTO `user` VALUES ('3', 'user2', '24c117ef7286f382b41b98638bb19151', 'user2@gmail.com', '0', '1392181836', '1392181836');
INSERT INTO `user` VALUES ('4', 'diane', 'c64a97f4a6023f3eb32961082607fc55', 'diane@gmail.com', '0', '1392184802', '1392184802');
