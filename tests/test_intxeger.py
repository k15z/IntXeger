import re
import unittest

from parameterized import parameterized

import intxeger


class TestIntXeger(unittest.TestCase):
    def test_build_1(self):
        x = intxeger.build("[a-z]")
        self.assertEqual(len(x), 26)

    def test_build_2(self):
        x = intxeger.build("[a-z][0-9]")
        self.assertEqual(len(x), 26 * 10)

    def test_build_3(self):
        x = intxeger.build("[abc]-[def]")
        self.assertEqual(len(x), 9)

    def test_build_4(self):
        x = intxeger.build("[abc]+")
        self.assertEqual(x[0], "a")
        self.assertEqual(x[1], "b")
        self.assertEqual(x[2], "c")
        self.assertEqual(x[3], "aa")
        self.assertEqual(x[4], "ab")
        self.assertEqual(x[5], "ac")

    def test_build_5(self):
        x = intxeger.build("[abc]*")
        self.assertEqual(x[0], "")
        self.assertEqual(x[1], "a")
        self.assertEqual(x[2], "b")
        self.assertEqual(x[3], "c")
        self.assertEqual(x[4], "aa")

    @parameterized.expand(
        [
            (r"[a-z]+", 100),
            (r"[a-z]{4}", 1000),
            (r"[a-z]{4,6}", 1000),
            (r"\w\d", 10),
            (r"/json/([0-9]+)", 100),
            (r"/json/([0-9]{4})/([a-z]{4})", 100),
            (r"[a-z]{4}-[a-z]{4}-[a-z]{4}-[a-z]{4}", 100),
            (r"[^a]", 10),  # anything except a
            (r"[abc]+?", 10),
        ]
    )
    def test_match(self, regex, nb_samples):
        x = intxeger.build(regex)
        matcher = re.compile(regex)
        for result in x.sample(nb_samples):
            assert matcher.match(result)
