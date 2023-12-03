use booking;

DROP TRIGGER IF EXISTS block_modification;
DELIMITER //
CREATE TRIGGER block_modification
BEFORE UPDATE
ON room FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Modification data in table is prohibited';
END //
DELIMITER ;

DROP TRIGGER IF EXISTS block_deletion;
DELIMITER //
CREATE TRIGGER block_deletion
BEFORE DELETE
ON user FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Delete data in table is prohibited';
END //
DELIMITER ;

DROP TRIGGER IF EXISTS minimal_cardinality;
DELIMITER //
CREATE TRIGGER minimal_cardinality
BEFORE INSERT
ON hotel FOR EACH ROW
BEGIN
  DECLARE counter INT;
  SELECT COUNT(*) INTO counter FROM hotel;
  IF counter <= 6 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot insert less than 6 rows';
  END IF;
END //
DELIMITER ;