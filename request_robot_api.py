#!/usr/bin/python3

import requests


class Auth(object):
    def __init__(self, apiKey, token):
        self.apiKey = apiKey
        self.token = token

    @staticmethod
    def getAuth(account_id, user_id, password, endpoint_url):
        req = requests.post(
            f"{endpoint_url}/user/{account_id}/{user_id}/auth",
            json={'password': password},
            headers={'Content-Type': 'application/json'}
        )
        if req.status_code != 200:
            raise Exception(f"Authentication error.({req.status_code})")

        value = {
            "Api Key": req.json()['apiKey'],
            "Token": req.json()['token'],
            "Status": req.status_code
        }

        return value


class RobotAPI(object):
    def __init__(self, name, robotId, secretKey):
        self.name = name
        self.robotId = robotId
        self.secretKey = secretKey

    @staticmethod
    def _get_header(apiKey, token):
        return {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apiKey,
            'X-Ciraas-Token': token
        }

    @staticmethod
    def listRobot(apiKey, token, endpoint_url):
        req = requests.get(
            f"{endpoint_url}/robot",
            headers=RobotAPI._get_header(apiKey, token))
        if req.status_code != 200:
            raise Exception(f"List robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getRobot(apiKey, token, robotId, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get robot information error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def deleteRobot(apiKey, token, robotId, endpoint_url):

        req = requests.delete(
            f"{endpoint_url}/robot/{robotId}",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Delete robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getDownload(apiKey, token, robotId, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}/download",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get list of download tasks error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getState(apiKey, token, robotId, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}/state",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get robot state error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def putState(apiKey, token, robotId, body, endpoint_url):

        req = requests.post(
            f"{endpoint_url}/robot/{robotId}/state",
            headers= RobotAPI._get_header(apiKey, token),
            json= body, timeout = None)
        if req.status_code != 200:
            raise Exception(f"Put robot state error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getPartialState(apiKey, token, robotId, key, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}/state/{key}",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get partial state error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def updateState(apiKey, token, robotId, key, body, endpoint_url):

        req = requests.post(
            f"{endpoint_url}/robot/{robotId}/state/{key}",
            headers= RobotAPI._get_header(apiKey, token),
            json= body, timeout = None)
        if req.status_code != 200:
            raise Exception(f"Update robot state error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def deleteState(apiKey, token, robotId, key, endpoint_url):

        req = requests.delete(
            f"{endpoint_url}/robot/{robotId}/state/{key}",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Delete robot state error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getRobotStats(apiKey, token, robotId, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}/stats",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get robot statistics error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def getTags(apiKey, token, robotId, endpoint_url):

        req = requests.get(
            f"{endpoint_url}/robot/{robotId}/tags",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 200:
            raise Exception(f"Get robot tags error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def orderSimultaneousStop(apiKey, token, body, endpoint_url):

        req = requests.put(
            f"{endpoint_url}/robot/stop",
            headers=RobotAPI._get_header(apiKey, token),
            json=body,timeout=None)
        if req.status_code != 202:
            raise Exception(f"Stop all robot error.({req.status_code})")

        value = {
            "JSON": req.json(),
            "Status": req.status_code
        }

        return value

    @staticmethod
    def orderProtectiveStop(apiKey, token, robotId, endpoint_url):

        req = requests.put(
            f"{endpoint_url}/robot/{robotId}/stop",
            headers= RobotAPI._get_header(apiKey, token), timeout = None)
        if req.status_code != 202:
            raise Exception(f"Stop robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def putTags(apiKey, token, robotId, tagName, body, endpoint_url):

        req = requests.post(
            f"{endpoint_url}/robot/{robotId}/tag/{tagName}",
            headers= RobotAPI._get_header(apiKey, token),
            json= body, timeout=None)
        if req.status_code != 201:
            raise Exception(f"Put tag on robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def deleteTag(apiKey, token, robotId, tagName, endpoint_url):

        req = requests.delete(
            f"{endpoint_url}/robot/{robotId}/tag/{tagName}",
            headers= RobotAPI._get_header(apiKey, token), timeout=None)
        if req.status_code != 200:
            raise Exception(f"Delete a robot from CIRaaS error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def attachSubscriberToRobot(apiKey, token, robotId, body, endpoint_url):

        req = requests.post(
            f"{endpoint_url}/robot/{robotId}/subscriber",
            headers= RobotAPI._get_header(apiKey, token),
            json= body, timeout=None)
        if req.status_code != 200:
            raise Exception(f"Pair SIM and robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def removeSubscriberFromRobot(apiKey, token, robotId, endpoint_url):

        req = requests.delete(
            f"{endpoint_url}/robot/{robotId}/subscriber",
            headers= RobotAPI._get_header(apiKey, token), timeout=None)
        if req.status_code != 200:
            raise Exception(f"Unpair SIM from robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value


def get_auth():
    account_id = 'CI0001'
    user_id = 'admin'
    password = 'b8eN3g)g/HhY'
    endpoint_url = 'https://api.t360.raasdev.io'

    apiKey = Auth.getAuth(account_id, user_id, password, endpoint_url)['Api Key']
    token = Auth.getAuth(account_id, user_id, password, endpoint_url)['Token']

    return Auth(apiKey, token), endpoint_url

# executive command
def exec_stop(robotId):
    auth = get_auth()
    endpoint_url = 'https://api.t360.raasdev.io'

    result = RobotAPI.orderProtectiveStop(auth.apiKey, auth.token, robotId, endpoint_url)['Status']
    return result

def get_robot_id_from_file(name):
    file_str = []

    f = open(name, "rt")

    for x in f:
        y = x.rstrip('\n').rstrip(",").strip('"')
        file_str.append(y)

    f.close()

    a = file_str.index('robot_id_list = [') + 1
    b = file_str.index('robot_secret_list = [') - 1
    id_list = []
    for index in range(a, b):
        id_list.append(file_str[index])

    return id_list

def get_robot_info_from_file(name):
    file_str = []

    f = open(name, "rt")

    for x in f:
        y = x.rstrip('\n').rstrip(",").strip('"')
        file_str.append(y)

    f.close()

    a = file_str.index('robot_name_list = [')
    b = file_str.index('robot_id_list = [')
    c = file_str.index('robot_secret_list = [')
    d = len(file_str)

    name_list = []
    id_list = []
    secret_key_list = []

    for index in range(a+1, b-1):
        name_list.append(file_str[index])
    for index in range(b+1, c-1):
        id_list.append(file_str[index])
    for index in range(c+1, d-1):
        secret_key_list.append(file_str[index])

    return name_list, id_list, secret_key_list

def main():

    result = get_robot_info_from_file("text.tfvars")
    print(result)
    robot_name_list = result[0]
    robot_id_list = result[1]
    robot_secret_key_list = result[2]

    for robot_id in robot_id_list:
        index = robot_id_list.index(robot_id)
        print(f"Name: {robot_name_list[index]}")
        print(f"Id: {robot_id_list[index]}")
        print(f"Secret: {robot_secret_key_list[index]}")
        print(exec_stop(robot_id))


if __name__ == "__main__":
    main()
