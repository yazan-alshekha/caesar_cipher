from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,count_words

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_special_character():
    actual=encrypt('a b!c',1)
    expected='bcd'
    assert actual==expected
    
def test_encrypt_function():
    actual=encrypt('abc',1)
    expected='bcd'
    assert actual==expected

def test_decrypt_function():
    actual=decrypt('b!cd',1)
    expected='abc'
    assert actual==expected




def test_count_words():
    expected=3
    actual=count_words('hi my frdfr friend')
    assert expected==actual