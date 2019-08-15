#!/usr/bin/python3

import requests


class Auth(object):
    def __init__(self, apiKey, token):
        self.apiKey = apiKey
        self.token = token

    @staticmethod
    def getAuth(account_id, user_id, password, endpoint_url):
        req = requests.post(
            f'{endpoint_url}/user/{account_id}/{user_id}/auth',
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
    def __init__(self, robotId, secretKey):
        self.robotId = robotId
        self.secretKey = secretKey

    @staticmethod
    def api_stop(apiKey, token, robotId, endpoint_url):
        header = {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apiKey,
            'X-Ciraas-Token': token
        }
        req = requests.put(
            f'{endpoint_url}/robot/{robotId}/stop',
            headers=header)
        if req.status_code != 202:
            raise Exception(f"Stop robot error.({req.status_code})")

        value = {
            "Status": req.status_code
        }

        return value

    @staticmethod
    def api_stop_all(apiKey, token, endpoint_url):
        header = {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apiKey,
            'X-Ciraas-Token': token
        }

        req = requests.put(
            f'{endpoint_url}/robot/stop',
            headers=header)
        if req.status_code != 202:
            raise Exception(f"Stop all robot error.({req.status_code})")

        value = {
            "JSON": req.json(),
            "Status": req.status_code
        }

        return value

    @staticmethod
    def api_robot_list(apiKey, token, endpoint_url):
        header = {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apiKey,
            'X-Ciraas-Token': token
        }
        req = requests.post(
                f'{endpoint_url}/robot',
                headers=header)
        if req.status_code != 201:
            raise Exception(f"Not created.({req.status_code})")

        value = {
            "Robot ID": req.json()['robotId'],
            "Status": req.status_code
        }

        return value

    @staticmethod
    def api_get_robot_list(apiKey, token, endpoint_url):
        header = {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apiKey,
            'X-Ciraas-Token': token
        }
        req = requests.get(
                f'{endpoint_url}/robot',
                headers=header)
        if req.status_code != 200:
            raise Exception(f"Not created.({req.status_code})")

        value = {
            "Robot ID": req.json()['robotId'],
            "Status": req.status_code
        }

        return value


    @staticmethod
    def api_get_single_robot_info(apikey, token, robotId, endpoint_url):
        header = {
            'Content-Type': 'application/json',
            'X-Ciraas-Api-Key': apikey,
            'X-Ciraas-Token': token
        }
        req = requests.get(
            f'{endpoint_url}/robot/{robotId}',
            headers=header)
        if req.status_code != 200:
            raise Exception(f"Not OK.({req.status_code})")

        value = {
            "Robot ID": req.json()['robotId'],
            "State": req.json()['state'],
            "Account ID": req.json()['accountId'],
            "Status": req.status_code
        }

        return value


def get_apikey_token():
    account_id = 'CI0001'
    user_id = 'admin'
    password = 'b8eN3g)g/HhY'
    endpoint_url = 'https://api.t360.raasdev.io'

    apiKey = Auth.getAuth(account_id, user_id, password, endpoint_url)['Api Key']
    token = Auth.getAuth(account_id, user_id, password, endpoint_url)['Token']

    return Auth(apiKey, token)


def exec_stop(id):

    auth = get_apikey_token()
    robotId = id
    endpoint_url = 'https://api.t360.raasdev.io'

    result = RobotAPI.api_stop(auth.apiKey, auth.token, robotId, endpoint_url)['Status']
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


def main():
    robot_id_list = get_robot_id_from_file("text.tfvars")
    print(robot_id_list)
    for robot_id in robot_id_list:
        print (exec_stop(robot_id))


if __name__ == "__main__":
    main()

