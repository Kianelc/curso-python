# content of test_sample.py
def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num - 1)


def eh_par(num):
    if num % 2 == 0:
        return True
    return False


def test_fatorial():
    assert fatorial(0) == 1


def test_eh_par():
    assert eh_par(10) == True