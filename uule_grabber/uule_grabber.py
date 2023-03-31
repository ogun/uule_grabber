""" Generates UULE codes for Google Search """
import base64


def uule(city: str) -> str:
    """Creates UULE code"""
    city_length = len(city.encode("utf-8"))

    # v1 implementation details
    # https://valentin.app/uule.html
    hashed = (
        base64.standard_b64encode(
            bytearray([8, 2, 16, 32, 34, city_length]) + city.encode()
        )
        .decode()
        .strip("=")
    )
    return f"w+{hashed}"
