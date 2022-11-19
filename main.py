import json
import boto3
from boto3.dynamodb.conditions import Key
import random


dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")

databaseUserTable = dynamodb.Table("dynamodb-api-jokes-user")
databaseContentTable = dynamodb.Table("dynamodb-api-jokes-content")

def lambda_handler(event, context):
    try:
        print("INFO: Function started.")

        print(f"INFO: Contents of header: {event['headers']}")
        authenticationStatus = authenticateUser(event["headers"])

        if(authenticationStatus != 0):
            print("Function Ending. Sayonara!")
            return {"statusCode": 401, "body": json.dumps(authenticationStatus)}
        

        print("Getting content.")
        content = getContent()

        print(f"Returning content: {content}")

        print("Function Ending. Sayonara!")
        return {"statusCode": 200, "body": json.dumps({"content": content, "authenticationStatus": True, "error": None})}

    except Exception as e:
        print("CRITICAL: EXCEPTION OCCURED.")
        print("EXCEPTION DETAILS: {}".format(repr(e)))

        print("RETURNING STATUSCODE 500")

        return {"statusCode": 500, "body": json.dumps({"content": None, "authenticationStatus": None, "error": "Critical internal server error. Please refrain from using the service until further notice."})}


def authenticateUser(headers):
    print("INFO: Authenticating user.")

    if(not "auth" in headers):
        print("Warning: No auth header was provided.")
        return {"content": None, "authenticationStatus": False, "error": "No auth header was provided."}
    
    print("INFO: Auth header found, querying to database.")
    queryResult = databaseUserTable.query(KeyConditionExpression=Key("auth").eq(headers["auth"]))

    print(f"INFO: Query result: {queryResult}")

    if(queryResult["Items"] == []):
        print("Warning: User not found in the database.")
        return {"content": None, "authenticationStatus": False, "error": "Authentication token is invalid."}
    
    print("INFO: Authentication token is valid.")
    print(f"INFO: Adding the amount of requests of {headers['auth']} by 1")

    databaseUserTable.update_item(Key={"auth": headers["auth"]}, UpdateExpression="ADD requests :q", ExpressionAttributeValues={":q": 1})

    return 0


def getContent():
    return databaseContentTable.get_item(Key={"id": random.randint(0, 49)})["Item"]["content"]


lambda_handler({"headers": {"auth": 0}}, 0)