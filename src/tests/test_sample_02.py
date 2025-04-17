import pytest
import allure


@allure.title("Sample Testcase")
def test_sample():
    assert True == True



    @allure.title("Sample Testcase02")
    def test_sample02():
        assert False == False
