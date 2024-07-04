-- задание 1
SELECT c.login, COUNT(o."courierId")
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;


-- задание 2
SELECT track,
   CASE
      WHEN finished = true THEN 2
      WHEN canсelled = true THEN -1
      WHEN "inDelivery" = true THEN 1
      ELSE 0
   END
FROM "Orders";
