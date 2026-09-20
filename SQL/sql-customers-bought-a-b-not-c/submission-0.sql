-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders p
    ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT CASE WHEN p.product_name IN ('A', 'B') THEN p.product_name END) = 2
   AND COUNT(CASE WHEN p.product_name = 'C' THEN 1 END) = 0
ORDER BY c.customer_name;