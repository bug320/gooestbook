
CREATE TABLE IF NOT EXISTS `guestbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `reply` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `date` datetime NOT NULL,
  `ip` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

CREATE TABLE User(
    id int(11) not null AUTO_INCREMENT,
    name     CHAR(10),
    passwd   CHAR(10),
    email    CHAR(225),
    sex      CHAR(10),
    PRIMARY KEY (id)
);

