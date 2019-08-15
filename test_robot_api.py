#!/usr/bin/python3
import unittest
from robot_api.request_robot_api import exec_stop, get_robot_id_from_file


class TestRobotAPI(unittest.TestCase):

    def setUp(self):
        pass

    def test_robot_stop_01(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[0]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    def test_robot_stop_02(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[1]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_03(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[2]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_04(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[3]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_05(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[4]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_06(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[5]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_07(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[6]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_08(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[7]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_09(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[8]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skip("No need")
    def test_robot_stop_10(self):

        id = get_robot_id_from_file("..\\robot_api\\text.tfvars")[9]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
