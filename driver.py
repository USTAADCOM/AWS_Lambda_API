"""
module contain the testing method for the created lambda endpoints.
"""
import json
import sys
from lambda_function import lambda_handler
def tool_testing(json_data: json, content)-> None:
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
    "type" : "word_count",
    "word_str" : "Pakistan Pakistan is is my country",
    "word_to_count" : "Pakistan"
}
# data = {       
#     "type" : "frequency_count",
#     "input_str" : "Pakistan Pakistan is is my country",
# }
# data = {
#     "type" : "prime_check",
#     "num" : 5,
# }
# data_encrypt = {
#     "type" : "encryption",
#     "input_str" : "aamir sohail",
# }
# data_decrypt = {
#     "type" : "decryption",
#     "input_str" : "eeqmv wslemp",
# }
# data = {
#     "type" : "pladirme_check",
#     "input_str" : "Was it a car or a cat I saw",
# }
json_data["body"] = json.dumps(data)
tool_testing(json_data, CONTENT)
