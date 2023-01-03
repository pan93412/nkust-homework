from basic import decrypt, decrypt_chunk


# def test_guess_n():
#     assert guess_n(2) ==
def test_decrypt_chunk():
    assert decrypt_chunk(1) == 2
    assert decrypt_chunk(2) == 4
    assert decrypt_chunk(3) == 6
    assert decrypt_chunk(4) == 1
    assert decrypt_chunk(5) == 3
    assert decrypt_chunk(6) == 5


def test_decrypt():
    assert decrypt("123456") == "246135"
