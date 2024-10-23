CREATE TABLE N_RollCall (
RollNumber INT PRIMARY KEY, Name VARCHAR(25)
);
CREATE TABLE O_RollCall (
RollNumber INT PRIMARY KEY, Name VARCHAR(25)
);
INSERT INTO N_RollCall (RollNumber, Name) VALUES (1, 'ganesh'), (2, 'adi'), (3, 'om');
INSERT INTO O_RollCall (RollNumber, Name) VALUES (1, 'ganesh'), (4, 'pawan'), (5, 'harshal');
DELIMITER //
CREATE PROCEDURE MergeData()
BEGIN
DECLARE rln INT;
DECLARE nm VARCHAR(25);
-- Declare a cursor for N_RollCall
DECLARE cur CURSOR FOR SELECT RollNumber, Name FROM N_RollCall;
-- Open the cursor OPEN cur;
-- Loop through the cursor read_loop: LOOP
FETCH cur INTO rln, nm;
-- Check if the data already exists in O_RollCall
IF NOT EXISTS (SELECT 1 FROM O_RollCall WHERE RollNumber = rln AND Name = nm) THEN
-- Insert the data into O_RollCall
INSERT INTO O_RollCall (RollNumber, Name) VALUES (rln, nm); END IF;
END LOOP;
-- Close the cursor CLOSE cur;
END //
Call procedure CALL MergeData();
Select data from O_RollCall to verify the merge SELECT * FROM O_RollCall;
-- GANESH