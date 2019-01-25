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
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(
            {
                "albums": [
                    {
                        "id": "1",
                        "coverPhotos": [
                            {
                                "metadata": {
                                    "author": "Folkert Gorter",
                                    "caption": "This is a dummy caption."
                                },
                                "medium": {
                                    "size": "1024x1024",
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_b016d7d289_b.jpg"
                                },
                                "large": {
                                    "size": "1600x1600",
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_c265dfa55f_h.jpg"
                                },
                                "small": {
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_b016d7d289_m.jpg"
                                }
                            }
                        ]
                    },
                    {
                        "coverPhotos": [
                            {
                                "metadata": {
                                    "author": "Folkert Gorter",
                                    "caption": "This is a dummy caption."
                                },
                                "medium": {
                                    "size": "1024x1024",
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_b016d7d289_b.jpg"
                                },
                                "large": {
                                    "size": "1600x1600",
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_c265dfa55f_h.jpg"
                                },
                                "small": {
                                    "url": "https://farm4.staticflickr.com/3894/15008518202_b016d7d289_m.jpg"
                                }
                            }
                        ]
                    }
                ]
            }
        )
    }
