import json


def lambda_handler(event, context):
    """
    Handles get requests to the image resource.

    Parameters
    ----------
    event
    context

    Returns
    -------
    API Gateway Lambda Proxy Output Format: dict
        'statusCode' and 'body' are required

        {
            "isBase64Encoded": true | false,
            "statusCode": httpStatusCode,
            "headers": {"headerName": "headerValue", ...},
            "body": "..."
        }
    """
    return {
        "isBase64Encoded": False,
        "statusCode": 201,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(
            {
                "request_type": "post",
                "resource_type": "images"
            }
        )
    }
