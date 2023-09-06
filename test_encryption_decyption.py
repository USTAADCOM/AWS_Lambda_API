"""
module contain the testing method for the created lambda endpoints.
"""
import json
import sys
from lambda_function import lambda_handler
def test_encryption_decryption(json_data: json, content)-> None:
    """
    input json file and test the string pladirme or not the required results.

    Parameters
    ----------
    json_data: json
        json data containing the request content.

    Return
    ------
    None
    """
    result = lambda_handler(json_data, content)
    print(result)

CONTENT = None
json_data = {}
data_encrypt = {
    "type" : "encryption",
    "input_str" : "aamir sohail",
    }
data_decrypt = {
    "type" : "decryption",
    "input_str" : "eeqmv wslemp",
    }
# data = {"type" : "pakistan",
#         "input_str" : "",
#        }
json_data["body"] = json.dumps(data_encrypt)
test_encryption_decryption(json_data, CONTENT)
