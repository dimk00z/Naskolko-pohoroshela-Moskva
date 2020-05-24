/*
Create table
*/
CREATE TABLE "Hospital_services" (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"patient"	TEXT,
	"place"	TEXT,
	"service_date"	TEXT,
	"service_name"	TEXT
)
/*
SQLLite
*/
SELECT service_name AS "Популярные услуги", COUNT(service_name) as 'Количество'
from Hospital_services
GROUP BY service_name
ORDER BY COUNT(service_name) DESC
LIMIT 10
/*
With TOP 10
*/
SELECT TOP 10 service_name
AS "Популярные услуги", COUNT
(service_name) as 'Количество'
from Hospital_services
GROUP BY service_name
ORDER BY COUNT
(service_name) DESC
