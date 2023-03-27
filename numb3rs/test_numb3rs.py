from numb3rs import validate
def test_format():
    assert validate("128.12.14.65.")== False
    assert validate("128.12.14")== False
    assert validate("128...")== False
    assert validate("128.12.14.65")== True
def test_range():
    assert validate("128.12.14.656")== False
    assert validate("256.12.255.6.")== False
    assert validate("255.0.144.65")== True