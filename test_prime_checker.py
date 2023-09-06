"""
module contain the testing method for the created lambda endpoints.
"""
import json
from lambda_function import lambda_handler
def test_frequency_count(json_data: json, content)-> None:
    """
    input json file and test the prime checker method fore the required results.

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
data = {"type" : "prime_check",
        "num" : 5,
       }
json_data["body"] = json.dumps(data)
test_frequency_count(json_data, CONTENT)
