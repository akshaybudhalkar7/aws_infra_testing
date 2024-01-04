import json
import requests


def lambda_handler(event, context):

    # Making a POST request
    r = requests.get('https://reqres.in/api/users?page=2')

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    print(r.json())

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
