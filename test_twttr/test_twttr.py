from twttr import shorten
def test_case1():
    assert shorten('Drake is a guy.')== 'Drk s  gy.'
def test_case2():
    assert shorten('Bayern Munchen')== 'Byrn Mnchn'
def test_case3():
    assert shorten('Manchester United')=='Mnchstr ntd'
def test_case4():
    assert shorten('Number 7654 is 43ish')== 'Nmbr 7654 s 43sh'