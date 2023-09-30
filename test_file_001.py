class TestCredence:

    def test_sum_001(self):
        num1 = 20
        num2 = 20
        total = num1 + num2

        if total == 40:
            print(f"\n The addition of two number is {total} & Matched with Expected")
            assert True

        else:
            print(f"\n The addition of two number is {total} and Not Matched with Expected")
            assert False

# No need to create an instance or manually call the test method

