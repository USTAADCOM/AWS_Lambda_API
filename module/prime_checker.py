"""
word count module will take the string and return the word count of each word.
"""
def check_prime_method(num: int)-> dict:
    """
    check_prime_method will take the num as innput and ckeck whther it is prime
    or not.

    Parameters
    ----------

    num: int
        number to check prime or not.
    
    Return
    ------
        return dictionary as output with result isPrimr or not.
    """
    output_dict = {}
    if num > 1:
        if num == 2 or num == 3:
            output_dict["result"] = "Is Prime"
        else:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    output_dict["result"] = "Not Prime"
                    break
                else:
                    output_dict["result"] = "Is Prime"
    else:
        output_dict["result"] = "Not Prime"
    return output_dict
