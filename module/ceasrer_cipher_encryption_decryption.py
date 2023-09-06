"""
This mmodule will perform the encryption and decryption on a file content
   using ceaser cipher technique.
"""
   #method caesar_cipher_encryption
def caesar_cipher_encryption(real_text: str, step = 4)-> dict:
    """
    This function will take  a text string , step as input and return
    a list of encrypted text using ceaser cipher.
    Parameters
    ----------
    real_text: str
       string containing the original text.
    step: int
        containing the step for encryption.
    Return
    ------
    list
        return a list of encrypted text.
    """
    output_dict = {}
    output_text_list = []
    encrypt_text_list = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
	            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
		        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for str_letter in real_text:
        if str_letter in uppercase:
            index = uppercase.index(str_letter)
            encryting_text = (index + step) % 26
            encrypt_text_list.append(encryting_text)
            new_char = uppercase[encryting_text]
            output_text_list.append(new_char)
        elif str_letter in lowercase:
            index = lowercase.index(str_letter)
            encryting_text = (index + step) % 26
            encrypt_text_list.append(encryting_text)
            new_char = lowercase[encryting_text]
            output_text_list.append(new_char)
        else:
            output_text_list.append(str_letter)
    output_dict["result"] = ''.join(output_text_list)
    return output_dict

# method caesar_cipher_decryption
def caesar_cipher_decryption(real_text: str, step = 4)-> dict:
    """
    This function will take  a text string , step as input and return
    a list of decrypted text using ceaser cipher. 
    Parameters
    ----------
    real_text: str
       string containing the decrypted text.
    step: int
        containing the step use for encryption.
    Return
    list
        return a list of decrypted text.
    """
    output_dict = {}
    output_text_list = []
    decrypt_text_list = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
	            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
		        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for str_letter in real_text:
        if str_letter in uppercase:
            index = uppercase.index(str_letter)
            encryting_text = (index - step) % 26
            decrypt_text_list.append(encryting_text)
            new_char = uppercase[encryting_text]
            output_text_list.append(new_char)
        elif str_letter in lowercase:
            index = lowercase.index(str_letter)
            encryting_text = (index - step) % 26
            decrypt_text_list.append(encryting_text)
            new_char = lowercase[encryting_text]
            output_text_list.append(new_char)
        else:
            output_text_list.append(str_letter)
    output_dict["result"] = ''.join(output_text_list)
    return output_dict
