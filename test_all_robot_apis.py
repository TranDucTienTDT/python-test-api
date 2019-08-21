#!/usr/bin/python3
import unittest
from robot_api.request_robot_api import RobotAPI, get_auth, get_robot_id_from_file


class TestRobotAPI(unittest.TestCase):

    def setUp(self):
        self.url = get_auth()[1]
        self.apiKey = get_auth()[0].apiKey
        self.token = get_auth()[0].token
        self.robotId = get_robot_id_from_file("..\\robot_api\\text.tfvars")
        self.body = {}
        self.key = ""
        self.tagName = ""

    def test_listRobot(self):

        expected = 200
        actual = RobotAPI.listRobot(self.apiKey, self.token, self.url)
        self.assertEqual(expected, actual)

    def test_getRobot(self):

        expected = 200
        actual = RobotAPI.getRobot(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_deleteRobot(self):

        expected = 200
        actual = RobotAPI.deleteRobot(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_getDownload(self):

        expected = 200
        actual = RobotAPI.getDownload(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_getState(self):

        expected = 200
        actual = RobotAPI.getState(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_putState(self):
        self.body = {
            "state": {
                "additionalProp1": {},
                "additionalProp2": {},
                "additionalProp3": {}
            }
        }

        expected = 200
        actual = RobotAPI.putState(self.apiKey, self.token, self.robotId[0], self.body, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_getPartialState(self):
        self.key = "string"

        expected = 200
        actual = RobotAPI.getPartialState(self.apiKey, self.token, self.robotId[0], self.key, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_updateState(self):
        self.key = "unknown"
        self.body = {
            "state": {
                "additionalProp1": {},
                "additionalProp2": {},
                "additionalProp3": {}
            }
        }

        expected = 200
        actual = RobotAPI.updateState(self.apiKey, self.token, self.robotId[0], self.key, self.body, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_deleteState(self):
        self.key = "unknown"

        expected = 200
        actual = RobotAPI.deleteState(self.apiKey, self.token, self.robotId[0], self.key, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_getRobotStats(self):

        expected = 200
        actual = RobotAPI.getRobotStats(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_getTags(self):

        expected = 200
        actual = RobotAPI.getTags(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)


    def test_orderSimultaneousStop(self):

        expected = 202
        actual = RobotAPI.orderSimultaneousStop(self.apiKey, self.token, self.url)
        self.assertEqual(expected, actual)

    def test_orderProtectiveStop(self):

        expected = 202
        actual = RobotAPI.orderProtectiveStop(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_putTags(self):
        self.tagName= "string"
        self.body= {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
        }

        expected = 201
        actual = RobotAPI.putTags(self.apiKey, self.token, self.robotId[0], self.tagName, self.body, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_deleteTag(self):
        self.tagName= "string"

        expected = 201
        actual = RobotAPI.deleteTag(self.apiKey, self.token, self.robotId[0], self.tagName, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_attachSubscriberToRobot(self):
        self.body = {
            "imsi": "string"
        }

        expected = 200
        actual = RobotAPI.attachSubscriberToRobot(self.apiKey, self.token, self.robotId[0], self.body, self.url)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_removeSubscriberFromRobot(self):

        expected = 200
        actual = RobotAPI.removeSubscriberFromRobot(self.apiKey, self.token, self.robotId[0], self.url)
        self.assertEqual(expected, actual)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
