# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Salaries AS s ON s.employee_id = e.employee_id 
WHERE s.salary IS NULL
UNION
SELECT s.employee_id
FROM Employees AS e
RIGHT JOIN Salaries AS s ON s.employee_id = e.employee_id 
WHERE e.name IS NULL
ORDER BY employee_id ASC;