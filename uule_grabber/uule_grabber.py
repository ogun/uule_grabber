""" Generates UULE codes for Google Search """
import string
import base64

def uule_secret(length: int) -> str:
    """ Creates UULE secret """
    secret_list = list(string.ascii_uppercase) + \
        list(string.ascii_lowercase) + list(string.digits) + ["-", "_"]
    return secret_list[length % len(secret_list)]


def uule(city: str) -> str:
    """ Creates UULE code """
    secret = uule_secret(len(city))
    hashed = base64.standard_b64encode(city.encode()).decode().strip("=")
    return "w+CAIQICI{}{}".format(secret, hashed)
