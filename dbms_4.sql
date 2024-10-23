-- Declare variables
DECLARE
  emp_id NUMBER := 101;
  emp_name VARCHAR2(50) := 'John Doe';
  emp_salary NUMBER := 50000;
BEGIN
  -- Check if the employee's salary is above a certain threshold
  IF emp_salary > 60000 THEN
    -- If the salary is above the threshold, raise an exception
    RAISE_APPLICATION_ERROR(-20001, 'Salary is too high for employee ' || emp_name);
  ELSE
    -- If the salary is within an acceptable range, display a message
    DBMS_OUTPUT.PUT_LINE('Employee ' || emp_name || ' with ID ' || emp_id || ' has an acceptable salary.');
  END IF;

EXCEPTION
  -- Handle exceptions
  WHEN OTHERS THEN
    -- If any other exception occurs, display an error message
    DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;
/
