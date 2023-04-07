-- Creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER # 
CREATE DEFINER=`root`@`localhost`
TRIGGER update_vemail 
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF OLD.email != NEW.email THEN
			SET NEW.valid_email = NEW.valid_email - 1;
		END IF;
	END;
#
