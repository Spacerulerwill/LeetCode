-- https://leetcode.com/problems/employee-bonus/
SELECT name, bonus
FROM Employee
FULL OUTER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus IS NULL or bonus < 1000