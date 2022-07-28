from unittest import TestCase

from main import convert_string


class Test(TestCase):
    def test_convert_string(self):

        test_data = [
            ['din', '((('],
            ['recede', '()()()'],
            ['Success', ')())())'],
            ['(( @', '))(('],
            ['123 321', ')))()))'],
            ['!@  gtG', '(()))()'],
            ['AAbaaBbacdeB', '))))))))((()'],
            ['\t', '('],
            ['', ''],
        ]

        for t in test_data:
            assert convert_string(t[0]) == t[1]
