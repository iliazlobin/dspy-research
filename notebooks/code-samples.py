# task
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """


# test
def check(candidate):
    # Check some simple cases
    assert candidate("a") == False, "a"
    assert candidate("aa") == False, "aa"
    assert candidate("abcd") == True, "abcd"
    assert candidate("aabb") == False, "aabb"
    assert candidate("adb") == True, "adb"
    assert candidate("xyy") == False, "xyy"
    assert candidate("iopaxpoi") == True, "iopaxpoi"
    assert candidate("iopaxioi") == False, "iopaxioi"


# pred
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


# my task
def debt_repayment_time(income, debt, annual_interest_rate) -> None:
    """You are given three numbers: income, debt, and annual interest rate on the debt.
    Your task is to calculate how long it will take to pay off the debt given that you pay 10% of your income each month.
    For example:
    debt_repayment_time(5000, 1000, 5) => 11
    debt_repayment_time(5000, 1000, 5) => 0
    debt_repayment_time(20000, 50000, 10) => 100
    """


def check_debt_repayment_time(candidate):
    assert candidate(5000, 10000, 10) == 22
    assert candidate(10000, 20000, 5) == 21
    assert candidate(15000, 50000, 1) == 33
    assert candidate(15000, 50000, 10) == 40
