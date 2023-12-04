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
AFTER DELETE
ON hotel FOR EACH ROW
BEGIN
  IF(SELECT COUNT(*) FROM hotel)<6
  THEN SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Delete error minimal cardinality';
  END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS block_deletion;
DELIMITER //
CREATE TRIGGER wifi_id_connect
BEFORE INSERT
ON Room FOR EACH ROW
BEGIN
    IF NEW.Wifi_id NOT IN (SELECT id FROM Wifi)
    THEN SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid Wifi_id';
    END IF;
END //
DELIMITER ;

