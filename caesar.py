import string


def caesar_rotate(text: str, shift: int) -> str:
    """
    Apply Caesar rotation to the given text.

    :param text: The input string to encode/decode.
    :param shift: The number of positions to shift (can be negative for decoding).
    :return: The transformed string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(shift, int):
        raise TypeError("Shift must be an integer.")

    # Normalize shift to range 0-25
    shift %= 26

    # Create translation tables for uppercase and lowercase letters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    trans_table = str.maketrans(
        lowercase + uppercase,
        lowercase[shift:] + lowercase[:shift] +
        uppercase[shift:] + uppercase[:shift]
    )

    return text.translate(trans_table)


if __name__ == "__main__":
    try:
        message = input("Enter your message: ")
        shift_value = int(input("Enter shift value (e.g., 3 for Caesar, 13 for ROT13): "))

        encrypted = caesar_rotate(message, shift_value)
        decrypted = caesar_rotate(encrypted, -shift_value)

        print(f"\nEncrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

    except ValueError:
        print("Invalid input. Shift value must be an integer.")
    except Exception as e:
        print(f"Error: {e}")
