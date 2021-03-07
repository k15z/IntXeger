import re
import unittest

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

    def test_build_6(self):
        x = intxeger.build("[a-z]{4}")
        x.sample(10)

    def test_build_7(self):
        x = intxeger.build("[a-z]{4}-[a-z]{4}-[a-z]{4}-[a-z]{4}")
        x.sample(10)

    def test_build_8(self):
        x = intxeger.build(r"\w{4}")
        x.sample(10)

    def test_build_9(self):
        x = intxeger.build(r"/json/([0-9]+)")
        x.sample(10)

    def test_build_10(self):
        regex = r"/json/([0-9]{4})/([a-z]{4})"
        x = intxeger.build(regex)
        data = x.sample(10)[0]
        assert re.compile(regex).match(data), data
