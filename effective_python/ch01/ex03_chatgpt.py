"""Exercise for Item 3 of Effective Python.

Helpers for converting safely between bytes and str in Python 3.
"""

from __future__ import annotations
from typing import Union

def to_str(bytes_or_str: bytes | str, encoding: str = "utf-8") -> str:
    """Return a str, decoding bytes with the given encoding if needed.

    Raises:
        TypeError: If `bytes_or_str` is not `bytes` or `str`.
    """
    if isinstance(bytes_or_str, str):
        return bytes_or_str
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode(encoding)
    raise TypeError(f"Expected bytes or str, got {type(bytes_or_str)!r}")

def to_bytes(bytes_or_str: bytes | str, encoding: str = "utf-8") -> bytes:
    """Return bytes, encoding a str with the given encoding if needed.

    Raises:
        TypeError: If `bytes_or_str` is not `bytes` or `str`.
    """
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode(encoding)
    raise TypeError(f"Expected bytes or str, got {type(bytes_or_str)!r}")

def main() -> None:
    bchars = b"\x71\x72\x73\x74\x75"           # q r s t u
    uchars = "\u0061\u0062\u0063\u0064\u0065"  # a b c d e

    print("Raw bytes:          ", bchars)
    print("Bytes to string:    ", to_str(bchars))
    print("Raw string:         ", uchars)
    print("String to bytes:    ", to_bytes(uchars))

    # Tiny sanity checks (Dev-Gym-style self-test)
    assert to_str(b"hello") == "hello"
    assert to_bytes("world") == b"world"

if __name__ == "__main__":
    main()
