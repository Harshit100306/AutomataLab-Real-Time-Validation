import unittest
from automata.validators import validate_password, validate_email, validate_pin

class TestAutomata(unittest.TestCase):
    def test_password(self):
        for x in ["Abcdef1!","StrongPass9@","Aa1!bcde","Zx7#mnopQ","A1!bcdefghijklmnopq"]:
            self.assertTrue(validate_password(x), x)
        for x in ["abcdef1!","ABCDEFG1!","Abcdefgh!","Abcdefg1","Ab1!xyz","Abc def1!"]:
            self.assertFalse(validate_password(x), x)
    def test_email(self):
        for x in ["alice@example.com","john.doe@mail.co.uk","a_b+c@example-domain.org","user123@sub.example.in","x@y.ab"]:
            self.assertTrue(validate_email(x), x)
        for x in ["@example.com","aliceexample.com","alice@@example.com","alice..bob@example.com",".alice@example.com","alice@-example.com","alice@example","alice@example.c","alice@example..com"]:
            self.assertFalse(validate_email(x), x)
    def test_pin(self):
        for x in ["1234","0000","9071","5555","0420"]: self.assertTrue(validate_pin(x), x)
        for x in ["123","12345","12a4","12 4",""]: self.assertFalse(validate_pin(x), x)

if __name__ == "__main__": unittest.main()
