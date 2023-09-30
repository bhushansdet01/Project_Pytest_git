class Test_Arrithmatic:

    def test_multi_001(self):
        x = 30
        y = 20
        product_of = x * y
        if product_of == 600:
            print(f"The multiplication of given number is {product_of} and matched with expected")
            assert True

        else:
            print(f"The multiplication of given number is {product_of} and not matched with expected")
            assert False

