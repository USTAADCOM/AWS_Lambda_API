# AWS Lambda API 
Here we develop AWS lambda API for the following task.
* Word Counter 
* Prime Number Checker
* Word Frequency Counter
* Encryption and Decryption Tool
* Palindrome Checker
## Setup
  ```code
  conda create -n <env_name>
  conda activate <env_name>
  git clone https://github.com/USTAADCOM/AWS_Lambda_API.git
  cd AWS_Lambda_API
  ```
## Project Structure
```bash
AWS_Lambda_API
   │   lambda_function.py
   │   test_encryption_decyption.py
   │   test_frequency_counter.py
   │   test_pladirme_checker.py
   │   test_prime_checker.py
   │   test_word_counter.py
   ├───module
       |  ceasrer_cipher_encryption_decryption.py
       │   pladirme_checker.py
       │   prime_checker.py
       │   word_counter.py
       │   word_frequency_counter.py
```

## Word Counter 
Payload
```code
    {
      "type" : "word_count",
      "word_str" : "Pakistan Pakistan is is my country",
      "word_to_count" : "Pakistan"
    }
```
Response 
```code
    {
      'statusCode': 200, 
      'body': '{"Pakistan": 2}'
    }
```
Note: replace word_str and word_to_count with your data. 

## Prime Number Checker: 
Payload
```code
    {
      "type" : "prime_check",
      "num" : 5
    }
```
Response 
```code
    {
      'statusCode': 200, 
      'body': '{"result": "Is Prime"}'
    }
```
Note: replace num with your data. 

## Word Frequency Counter 
Payload
```code
    {
      "type" : "frequency_count",
      "input_str" : "Pakistan Pakistan is is my country",
    }
```
Response 
```code
    {
      'statusCode': 200, 
      'body': '{"Pakistan": 2, "is": 2, "my": 1, "country": 1}'
    }
```
Note: replace input_str with your data. 

## Encryption and Decryption Tool 
Encryption Payload
```code
    {
      "type" : "encryption",
      "input_str" : "aamir sohail",
    }
```
Encryption Response 
```code
    {
      'statusCode': 200, 
      'body': '{"result": "eeqmv wslemp"}'
    }
```
Decryption Payload
```code
    {
      "type" : "decryption",
      "input_str" : "aamir sohail",
    }
```
Decryption Response 
```code
    {
      'statusCode': 200, 
      'body': '{"result": "eeqmv wslemp"}'
    }
```
Note: replace input_str with your data. 

## Palindrome Checker 
Payload
```code
    {
      "type" : "pladirme_check",
      "input_str" : "Was it a car or a cat I saw"
    }
```
Response 
```code
    {
      'statusCode': 200, 
      'body': '{"result": "Is Plandirme"}'
    }
```
Note: replace input_str with your data. 