"""Show Python version information for Dev-Gym exercises."""

import sys


def main() -> None:
    info = sys.version_info
    version_str = sys.version

    print("=== Python Version Info ===")
    print(f"Major: {info.major}")
    print(f"Minor: {info.minor}")
    print(f"Micro: {info.micro}")
    print()
    print("Full version string:")
    print(version_str)


if __name__ == "__main__":
    main()
