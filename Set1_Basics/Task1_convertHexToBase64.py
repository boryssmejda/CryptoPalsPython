
base64_conversion_table = {
    "000000" : "A",
    "000001" : "B",
    "000010" : "C",
    "000011" : "D",
    "000100" : "E",
    "000101" : "F",
    "000110" : "G",
    "000111" : "H",
    "001000" : "I",
    "001001" : "J",
    "001010" : "K",
    "001011" : "L",
    "001100" : "M",
    "001101" : "N",
    "001110" : "O",
    "001111" : "P",
    "010000" : "Q",
    "010001" : "R",
    "010010" : "S",
    "010011" : "T",
    "010100" : "U",
    "010101" : "V",
    "010110" : "W",
    "010111" : "X",
    "011000" : "Y",
    "011001" : "Z",
    "011010" : "a",
    "011011" : "b",
    "011100" : "c",
    "011101" : "d",
    "011110" : "e",
    "011111" : "f",
    "100000" : "g",
    "100001" : "h",
    "100010" : "i",
    "100011" : "j",
    "100100" : "k",
    "100101" : "l",
    "100110" : "m",
    "100111" : "n",
    "101000" : "o",
    "101001" : "p",
    "101010" : "q",
    "101011" : "r",
    "101100" : "s",
    "101101" : "t",
    "101110" : "u",
    "101111" : "v",
    "110000" : "w",
    "110001" : "x",
    "110010" : "y",
    "110011" : "z",
    "110100" : "0",
    "110101" : "1",
    "110110" : "2",
    "110111" : "3",
    "111000" : "4",
    "111001" : "5",
    "111010" : "6",
    "111011" : "7",
    "111100" : "8",
    "111101" : "9",
    "111110" : "+",
    "111111" : "/"
}

assert len(base64_conversion_table) == 64, "Base 64 table shall have 64 characters"

hex_to_binary = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "a" : "1010",
    "b" : "1011",
    "c" : "1100",
    "d" : "1101",
    "e" : "1110",
    "f" : "1111"
}

assert len(hex_to_binary) == 16, "Hex to binary shall have 16 elements."


def _convert_hex_to_binary(hex_text: str) -> str:
    binary_form = []
    for hex_char in hex_text:
        binary_form.append(hex_to_binary[hex_char])

    return ''.join(binary for binary in binary_form)


def _add_padding(binary_form: str) -> str:
    if len(binary_form) % 6 == 0:
        return binary_form

    rest_from_division = len(binary_form) % 6
    if rest_from_division == 4:
        return "00" + binary_form
    elif rest_from_division == 2:
        return "0000" + binary_form
    else:
        raise RuntimeError("Unexpected length of binary number!")


def _convert_binary_to_base64(binary_form: str) -> str:
    padded_binary_form = _add_padding(binary_form)
    assert len(padded_binary_form) % 6 == 0, \
        f'Padded binary form must be divisible by 6!'

    base64_form = []
    current_six_bundle = 0

    while current_six_bundle < len(padded_binary_form):
        binary_number = padded_binary_form[current_six_bundle: current_six_bundle + 6]
        base64_symbol = base64_conversion_table[binary_number]
        base64_form.append(base64_symbol)
        current_six_bundle += 6

    return ''.join(str(base64_symbol) for base64_symbol in base64_form)


def convert_hex_into_base64(hex_encoded_text: str) -> str:
    binary_form = _convert_hex_to_binary(hex_encoded_text)
    return _convert_binary_to_base64(binary_form)


def main():
    assert(convert_hex_into_base64("49276d206b696c6c696e6720796f757220627261696e206c696b" \
        "65206120706f69736f6e6f7573206d757368726f6f6d") \
        == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")


if __name__ == '__main__':
    main()
