
-- Проверяем, что заказ с ID=101 существует и оплачен
SELECT * FROM orders WHERE order_id = 101 AND status = 'PAID';
