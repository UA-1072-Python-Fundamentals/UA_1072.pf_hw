import unittest
from .funk import largest_number, correct_tail

class MyTest(unittest.TestCase):


    def test1(self):
        expected = 2
        actual = largest_number(1, 2)
        self.assertEqual(expected, actual)
    def test2(self):
        expected = 2
        actual = largest_number(2, -1)
        self.assertEqual(expected, actual)
    def test3(self):
        expected = "numbers are equal"
        actual = largest_number(2, 2)
        self.assertEqual(expected, actual)
    def test4(self):
        expected = "something goes wrong"
        actual = largest_number("2", 2)
        self.assertEqual(expected, actual)
    def test5(self):
        expected = "something goes wrong"
        actual = largest_number(2, "2")
        self.assertEqual(expected, actual)

    def testcorrect_tail(self):
        expected = True
        actual = correct_tail("nsdbvksdl", "l")
        self.assertEqual(expected, actual)


class MyTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def setUp(self):
        print("\tsetUp")
    def tearDown(self):
        print("\ttearDown")
    def test1(self):
        print("\t\ttest_1")
        self.assertTrue(True)
    def test2(self):
        print("\t\ttest_2")
        self.assertTrue(True)
