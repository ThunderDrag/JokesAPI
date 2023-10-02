# 🎭 [Jokes API](https://github.com/ThunderDrag/JokesAPI/)

## 🌟 **About the API:**

This API fetches a random joke from its database. To access it, you'll need a valid authentication token. Without one, you'll face an HTTPS Status Code 401 error.

Here's what sets it apart:
- Exception handling 🛠️
- Detailed logging 📝
- In the rare event of a server glitch, it'll advise you to pause usage and return an HTTPS Status Code 500 🚫

Under the hood, it's powered by AWS Lambda, AWS API Gateway, and AWS DynamoDB. 🚀

## 📬 **Sample Request Header:**

\```
GET /Production/api/jokes HTTP/1.1
Host: h0zensjtaj.execute-api.ap-south-1.amazonaws.com
auth: 0
\```

## 🎉 **Sample Successful Response:**

\```
{
    "content": "What did the ocean say to the beach? Nothing, it just waved.",
    "authenticationStatus": true,
    "error": null
}
\```

## 📌 **Highlights:**

✅ Ensures Proper Authentication <br />
✅ Robust Exception Handling <br />
✅ Comprehensive Logging <br />
✅ Built for Speed 🚀<br />
✅ Delivers Possibly Hilarious Jokes 😂
