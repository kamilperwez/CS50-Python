from bank import value
def test_main():
    test_hello()
    test_h()
    test_()
def test_hello():
    assert value('hello')==0
    assert value('Hello 1234')==0
    assert value('hello who?')==0
def test_h():
    assert value('h')==20
    assert value('H 1234/')==20
    assert value('How r You')==20
def test_():
    assert value('others')==100
    assert value('Yeah')==100
    assert value('cs50 ?Best')==100
