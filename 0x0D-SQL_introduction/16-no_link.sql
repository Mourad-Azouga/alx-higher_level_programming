-- SAY LY NAME
SELECT `score`, IF EXISTS `name`
FROM `second_table`
ORDER BY `score`