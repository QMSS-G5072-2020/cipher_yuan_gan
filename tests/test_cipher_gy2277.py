from cipher_gy2277 import __version__
from cipher_gy2277 import cipher_gy2277

def test_version():
    assert __version__ == '0.1.0'


def test_cipher():
    expected = "ecv"
    result = cipher_gy2277.cipher("cat",2)
    assert expected == result

