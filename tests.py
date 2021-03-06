import unittest
import client.arguments_validation as validation
import server.handler.server_handler as handler


class TestArgumentsValidation(unittest.TestCase):
    def test_wrong_ip_format_fails(self):
        wrong_ip_format = '192.168.56.5.1'
        result = validation.is_valid_ipv4_address(wrong_ip_format)
        self.assertEqual(result, False)

    def test_not_existing_ip_address_fails(self):
        not_existing_ip = "192.168.56.500"
        result = validation.is_valid_ipv4_address(not_existing_ip)
        self.assertEqual(result, False)

    def test_valid_ip_ok(self):
        not_existing_ip = '192.168.56.5'
        result = validation.is_valid_ipv4_address(not_existing_ip)
        self.assertEqual(result, True)

    def test_valid_port_ok(self):
        port = validation.BIGGEST_AVAILABLE_PORT
        result = validation.is_valid_port(port)
        self.assertEqual(result, True)

    def test_out_of_range_port_fails(self):
        port = validation.BIGGEST_AVAILABLE_PORT + 1
        result = validation.is_valid_port(port)
        self.assertEqual(result, False)

    def test_wrong_type_of_port_fails(self):
        port = "125"
        result = validation.is_valid_port(port)
        self.assertEqual(result, False)


class TestServerHandler(unittest.TestCase):
    def test_password_is_hashed_to_bytes(self):
        password = "12345"
        hashed_password = handler.Server.hash_password(password)
        self.assertIsInstance(hashed_password, bytes)


if __name__ == '__main__':
    unittest.main()
