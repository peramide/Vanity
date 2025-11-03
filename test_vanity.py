import pytest
from vanity import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert(is_valid("AAA222")) == True
    assert(is_valid("AAA22A")) == False
    

if __name__ == "__main__":
    main()