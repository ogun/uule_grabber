""" Generates UULE codes for Google Search """
import string
import base64

SECRET_LIST = (
    list(string.ascii_uppercase)
    + list(string.ascii_lowercase)
    + list(string.digits)
    + ["-", "_"]
)


def uule(city: str) -> str:
    """Creates UULE code"""
    secret = SECRET_LIST[len(city.encode("utf-8")) % 64]
    hashed = base64.standard_b64encode(city.encode()).decode().strip("=")
    return f"w+CAIQICI{secret}{hashed}"
