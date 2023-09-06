"""
module contain the testing method for the created lanbda endpoints.
"""
import json
from lambda_function import lambda_handler
def test_word_count(json_data: json, content)-> None:
    """
    input json file and test the word count method fore the required results.

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
data = {"type" : "word_count",
        "word_str" : "Pakistan Pakistan is is my country",
        "word_to_count" : "Pakistan"
       }
json_data["body"] = json.dumps(data)
test_word_count(json_data, CONTENT)
