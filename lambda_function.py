"""
lamda metod mmodule 
"""
import json
from module import word_counter
from module import word_frequency_counter
from module import pladirme_checker
from module import prime_checker
from module import ceasrer_cipher_encryption_decryption

def lambda_handler(event_jsonified, context):
    """
    lambda handler method recive the json data and return the reponse as json file.

    Parameters
    ----------

    event_jsonified: json
        json request data.
    context: Null
        null.
    Return
    ------
        return json reposne as a result according to the request.
    """
    try:
        if "body" not in event_jsonified:
            return {'statusCode': 400,
                'Error': json.dumps("Bad Params"),
                'Message': json.dumps("Body Params not found")
                }
        else:
            event = event_jsonified['body']
            event = json.loads(event, strict = False)
            if "type" not in event:
                return {'statusCode': 400,
                        'body': json.dumps("Bad Params"),
                        'Message': json.dumps("Type key missing")
                        }
            elif event["type"] == "":
                return {'statusCode': 400,
                        'body': json.dumps("Bad Params"),
                        'Message': json.dumps("Empty Type Value")
                        }
            else:
                if event["type"] == "word_count":
                    if "word_str" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("word_str key missing")
                            }
                    elif event["word_str"] == "":
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Empty word_str")
                            }
                    elif "word_to_count" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("word_to_count key missing")
                            }
                    elif event["word_to_count"] == "":
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Empty word_to_count")
                            }
                    word_str = event["word_str"]
                    word_to_count = event["word_to_count"]
                    output = word_counter.word_count_method(word_str, word_to_count)
                    response = {
                        "statusCode": 200,
                        "body": json.dumps(output)
                    }
                    return response
                elif event["type"] == "prime_check":
                    if "num" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("num key missing")
                            }
                    elif event["num"] is None:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Num not provided")
                            }
                    num = event["num"]
                    output = prime_checker.check_prime_method(num)
                    response = {
                        "statusCode": 200,
                        "body": json.dumps(output)
                    }
                    return response
                elif event["type"] == "frequency_count":
                    if "input_str" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("input_str key missing")
                            }
                    elif event["input_str"] == "":
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Empty input_str")
                            }
                    input_str = event["input_str"]
                    output = word_frequency_counter.word_frequency_count_method(input_str)
                    response = {
                        "statusCode": 200,
                        "body": json.dumps(output)
                    }
                    return response
                elif event["type"] == "pladirme_check":
                    if "input_str" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("input_str key missing")
                            }
                    elif event["input_str"] == "":
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Empty input_str")
                            }
                    input_str_plandirme = event["input_str"]
                    output = pladirme_checker.check_plandirme_method(input_str_plandirme)
                    response = {
                        "statusCode": 200,
                        "body": json.dumps(output)
                    }
                    return response
                elif event["type"] == "encryption" or "decryption":
                    if "input_str" not in event:
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("input_str key missing")
                            }
                    elif event["input_str"] == "":
                        return {'statusCode': 400,
                            'body': json.dumps("Bad Params"),
                            'Message': json.dumps("Empty input_str")
                            }
                    input_str = event["input_str"]
                    if event["type"] == "encryption":
                        output = ceasrer_cipher_encryption_decryption.caesar_cipher_encryption(''.join(input_str))
                    else:
                        output = ceasrer_cipher_encryption_decryption.caesar_cipher_decryption(''.join(input_str))
                    response = {
                        "statusCode": 200,
                        "body": json.dumps(output)
                    }
                    return response
                else:
                    return {
                        'statusCode': '404',
                        'body': 'Requested URL Not found'
                    }
    except Exception as error:
        response = {
            "statusCode": 500,
            "Error": error,
            "Message" : "Bad Request"
            }
        return response
