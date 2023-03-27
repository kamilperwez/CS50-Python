from plates import is_valid
def test_main():
    test_1()
    test_2()
    test_3()
    test_4()
def test_1():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False
def test_2():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False
def test_3():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
def test_4():
    assert is_valid("CS50!") == False
if __name__=="__main()__":
    main()