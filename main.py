# This is a regula expression exercise by hao 2022-08-30
import re


def test_compile():
    some_text = 'a,b,,,,,c d'
    reObj = re.compile('[, ]+')
    result = reObj.findall(some_text)
    realObj = reObj.split(some_text)
    print(result, realObj)


# match function only find str start with that
# search function find inside str no matter where is it
def test_pattern():
    pattern = re.compile("^[A-Z]+$")
    print('-------pattern one---------')
    print(pattern.search("One Piece"))
    print(pattern.search("ONEPIECE"))
    print(pattern.search("ONE PIECE"))
    print('--------pattern_two---------')
    pattern_two = re.compile("[a-z]+")
    print(pattern_two.match("One Piece"))
    print(pattern_two.match("ONEPIECE"))
    print(pattern_two.match("ONE PIECE"))


if __name__ == '__main__':
    test_compile()
    test_pattern()