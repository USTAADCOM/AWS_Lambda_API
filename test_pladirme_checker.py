"""
module contain the testing method for the created lanbda endpoints.
"""
import json
from lambda_function import lambda_handler
def test_pladirme_checker(json_data: json, content)-> None:
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
data = {
    "type" : "pladirme_check",
    "input_str" : "Was it a car or a cat I saw",
    }
# data = {"type" : "pakistan",
#         "input_str" : "",
#        }
json_data["body"] = json.dumps(data)
test_pladirme_checker(json_data, CONTENT)
