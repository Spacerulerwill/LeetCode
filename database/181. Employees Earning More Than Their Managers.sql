-- https://leetcode.com/problems/employees-earning-more-than-their-managers
SELECT name as Employee
FROM Employee
WHERE salary > (
    SELECT salary
    FROM Employee
    AS E2
    WHERE id = Employee.managerId
)
