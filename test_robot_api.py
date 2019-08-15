#!/usr/bin/python3
import unittest

from robot_api.request_robot_api import exec_stop, get_robot_id_from_file


class TestRobotAPI(unittest.TestCase):

    robot_id_list = get_robot_id_from_file("..\\robot_api\\text.tfvars")

    def setUp(self):
        pass

    def test_robot_stop_01(self, robot_id_list=robot_id_list):
        id = robot_id_list[0]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<2, "Not Test")
    def test_robot_stop_02(self, robot_id_list=robot_id_list):
        id = robot_id_list[1]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_03(self, robot_id_list=robot_id_list):
        id = robot_id_list[2]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_04(self, robot_id_list=robot_id_list):
        id = robot_id_list[3]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_05(self, robot_id_list=robot_id_list):
        id = robot_id_list[4]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_06(self, robot_id_list=robot_id_list):
        id = robot_id_list[5]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_07(self, robot_id_list=robot_id_list):
        id = robot_id_list[6]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_08(self, robot_id_list=robot_id_list):
        id = robot_id_list[7]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_09(self, robot_id_list=robot_id_list):
        id = robot_id_list[8]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    @unittest.skipIf(len(robot_id_list)<10, "Not Test")
    def test_robot_stop_10(self, robot_id_list=robot_id_list):
        id = robot_id_list[9]
        expected = 202
        actual = exec_stop(id)
        self.assertEqual(expected, actual, "The robot is not stopped")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
