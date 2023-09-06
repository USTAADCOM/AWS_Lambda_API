"""
plandirme checker module.
"""
def check_plandirme_method(input_str: str)-> dict:
    """
    check_plandirme_method take two strings as input and check whether it is 
    pladirme or not.

    Parameters
    ----------

    input_str: str
        string for plandirme check.
    Return
    ------
        return dictionary as output output isPlandirme or not.
    """
    output_dict = {}
    input_str_temp = input_str.replace(' ', '')
    input_str_temp = input_str_temp.lower()
    input_str_reverse = input_str_temp[::-1]
    if input_str_temp == input_str_reverse:
        output_dict["result"] = "Is Plandirme"
    else:
        output_dict["result"] = "Not Plandirme"
    return output_dict
