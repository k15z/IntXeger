import unittest

from intxeger.core import Choice, Concatenate, Constant, Repeat


class TestCore(unittest.TestCase):
    def test_choice(self):
        x = Choice([Constant("a"), Constant("b")])
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0], "a")
        self.assertEqual(x[1], "b")

    def test_concatenate_1(self):
        x = Concatenate([Constant("a"), Constant("b")])
        self.assertEqual(len(x), 1)
        self.assertEqual(x[0], "ab")

    def test_concatenate_2(self):
        x = Concatenate([Choice([Constant("a"), Constant("b")]), Constant("b")])
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0], "ab")
        self.assertEqual(x[1], "bb")

    def test_repeat_1(self):
        x = Repeat(Constant("a"), min_count=2, max_count=2)
        self.assertEqual(len(x), 1)
        self.assertEqual(x[0], "aa")

    def test_repeat_2(self):
        x = Repeat(Constant("a"), min_count=2, max_count=3)
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0], "aa")
        self.assertEqual(x[1], "aaa")

    def test_repeat_3(self):
        x = Repeat(Choice([Constant("a"), Constant("b")]), min_count=1, max_count=2)
        self.assertEqual(len(x), 6)
        self.assertEqual(x[0], "a")
        self.assertEqual(x[1], "b")
        self.assertEqual(x[2], "aa")
        self.assertEqual(x[3], "ab")
        self.assertEqual(x[4], "ba")
        self.assertEqual(x[5], "bb")
        with self.assertRaises(IndexError):
            x[6]

    def test_sample(self):
        x = Repeat(Choice([Constant("a"), Constant("b")]), min_count=1, max_count=2)
        self.assertEqual(set(x.sample(6)), set(["a", "b", "aa", "ab", "ba", "bb"]))
        with self.assertRaises(ValueError):
            x.sample(10)
