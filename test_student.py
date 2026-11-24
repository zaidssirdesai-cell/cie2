from student import calculate
def test_1calculate():
    total,avg,per = calculate(10,10,10)
    assert total == 30
    assert avg == 10
    assert per == 10

def test2_calculate():
    total,avg,per = calculate(5,5,5)
    assert total == 15
    assert avg == 5
    assert per == 5
    
