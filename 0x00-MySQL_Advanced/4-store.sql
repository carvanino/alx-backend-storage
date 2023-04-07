-- Updates the quantity of an item once an order has been placed
-- by decreasing the quantity of the item and updating the number of orders
DELIMITER # ;
CREATE
DEFINER=`root`@`localhost`
TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE NEW.item_name = name;
	END;
#
