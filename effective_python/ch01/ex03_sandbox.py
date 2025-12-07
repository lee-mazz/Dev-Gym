"""Exercise for Item 3 of Effective Python"""

def to_str(bytes_or_str) -> str:
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str) -> bytes:
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value    

def main() -> None:
    bchars = b'\x71\x72\x73\x74\x75'
    uchars = '\u0061\u0062\u0063\u0064\u0065'
    print(f"Raw bytes: {bchars}")
    print(f"Bytes to String: {to_str(bchars)}")
    print(f"Raw string: {uchars}")
    print(f"String to Bytes: {to_bytes(uchars)}")

if __name__ == "__main__":
    main()