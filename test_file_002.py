
class Test_Credence:

    def test_minus_001(self):
        a = 50
        b = 60
        subtracted = a - b

        if subtracted == -10:
            print(f"\n The Result of Subtraction is {subtracted} and Matched with Expected")
            assert True

        else:
            print(f"\n The Result of Subtraction is {subtracted} and Not Matched with Expected")
            assert False

