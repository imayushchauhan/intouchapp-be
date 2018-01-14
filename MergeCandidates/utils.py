import json
import string
import random

def get_response_obj(responseData, message, code):
    return {
        "responseData": responseData,
        "message": message,
        "code": code
    }

def get_random_str(str_len):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(str_len))