
def _is_hex(hex_num: str) -> bool:
    HEX_NUMBERS = '0123456789abcdef'
    return all(num in HEX_NUMBERS for num in hex_num)


def get_fixed_xor_of_two_hex_nums(buffer_a: str, buffer_b: str) -> str:
    assert len(buffer_a) == len(buffer_b)
    assert _is_hex(buffer_a), "Buffer A must be a hex number!"
    assert _is_hex(buffer_b), "Buffer B must be a hex number!"

    xored_buffer = []
    for a,b in zip(buffer_a, buffer_b):
        xor_result = int(a, 16) ^ int(b, 16)
        xor_result = '{:x}'.format(xor_result)
        xored_buffer.append(xor_result)

    return ''.join(map(str, xored_buffer))


def main():
    BUFFER_A = '1c0111001f010100061a024b53535009181c'
    BUFFER_B = '686974207468652062756c6c277320657965'
    EXPECTED_RESULT = '746865206b696420646f6e277420706c6179'

    result = get_fixed_xor_of_two_hex_nums(BUFFER_A, BUFFER_B)
    assert result == EXPECTED_RESULT, f"{result=} must be equal to {EXPECTED_RESULT=}"
    assert get_fixed_xor_of_two_hex_nums('a', 'b') == '1'


if __name__ == '__main__':
    main()
