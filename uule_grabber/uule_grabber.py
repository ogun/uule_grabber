""" Generates UULE codes for Google Search """
import base64


def uule(city: str) -> str:
    """Creates UULE code"""
    # The message should be smth. like that
    # data = {"role": 2, "producer": 32, "canonicalName": city}
    # Since the data in protobuf format, we should mimic the behaviour
    #
    # I'll try to explain why we use 8 (0 0001 000) as first byte
    # "role" is the first field and its type is VARINT
    # 0: we set first bit is zero because this is the most significant bit (MSB) of the byte
    # it is a continuation bit that indicates if the byte that follows it is part of the previous
    # 0001: the other for bits are seperated for the field number
    # 000: the last three bits are for wire types
    # in our case the first field is VARINT (0)
    # 1:VARINT = 0 0001 000 (8)
    #
    # For the other fields the same structure appliesx
    # 2:VARINT = 0 0010 000 (16)
    # 4:LEN    = 0 0100 010 (34)
    # That's why in our case the first bytes are hardcoded
    # (1. field) role: 2 => 1:VARINT:2 => [8, 2]
    # (2. field) producer: 32 => 2:VARINT:32 => [16, 32]
    # (4. field) canonicalName: city => 4:LEN:city => [34, len(city), city...]

    encoded_city = city.encode()
    city_length = len(encoded_city)
    hashed = (
        base64.standard_b64encode(
            bytearray([8, 2, 16, 32, 34, city_length]) + encoded_city
        )
        .decode()
        .strip("=")
        .replace("+", "-")
        .replace("/", "_")
    )
    return f"w+{hashed}"
