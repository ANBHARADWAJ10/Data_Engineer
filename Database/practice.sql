SELECT * FROM employees;
SELECT dept, COUNT(emp_id) FROM employees
GROUP BY dept;