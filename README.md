# [Jokes API](https://github.com/ThunderDrag/JokesAPI/)

## ***About:-***

This API will retrieve a random joke from the database. It needs a valid authentication token without which it would return HTTPS Status Code 401.

It has proper exception handling and logging of every information and warnings. Incase of server error, it will inform the use to refrain from using the service and return HTTPS Status Code 500.

It is made on top of AWS Lambda, AWS API Gateway and AWS DynamoDB.


## ***Example Request Header:-***

    GET /Production/api/jokes HTTP/1.1
    Host: h0zensjtaj.execute-api.ap-south-1.amazonaws.com
    auth: 0

## ***Example Successful Response:-***

    {
    "content": "What did the ocean say to the beach? Nothing, it just waved.",
    "authenticationStatus": true,
    "error": null
    }

## ***Key Points:-***

 - [x] Proper Authentication Validating.
 - [x] Exception Handling
 - [x] Logging
 - [x] Optimized for speed
 - [x] Super Funny Jokes (Maybe)