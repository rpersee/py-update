import unittest
from update import deepupdate


class TestDeepUpdate(unittest.TestCase):
    def setUp(self):
        self.a = {"a": 1, "b": {"c": 2, "d": 3}, "g": 7}
        self.b = {"a": 2, "b": {"c": 4, "e": 5}, "f": 6}
        self.c = [1, 2, 3]
        self.d = [4, 5, 6]

    def test_deep_update_dict_replace_true(self):
        deepupdate(self.a, self.b, replace=True)
        expected = {"a": 2, "b": {"c": 4, "e": 5}, "f": 6, "g": 7}
        self.assertEqual(self.a, expected)

    def test_deep_update_dict_replace_false(self):
        deepupdate(self.a, self.b, replace=False)
        expected = {"a": 1, "b": {"c": 2, "d": 3}, "f": 6, "g": 7}
        self.assertEqual(self.a, expected)

    def test_deep_update_dict_replace_left(self):
        deepupdate(self.a, self.b, replace="left")
        expected = {"a": 1, "b": {"c": 2, "d": 3, "e": 5}, "f": 6, "g": 7}
        self.assertEqual(self.a, expected)

    def test_deep_update_dict_replace_right(self):
        deepupdate(self.a, self.b, replace="right")
        expected = {"a": 2, "b": {"c": 4, "d": 3, "e": 5}, "f": 6, "g": 7}
        self.assertEqual(self.a, expected)

    def test_deep_update_dict_replace_default(self):
        deepupdate(self.a, self.b)
        expected = {"a": 2, "b": {"c": 4, "d": 3, "e": 5}, "f": 6, "g": 7}
        self.assertEqual(self.a, expected)

    def test_deep_update_list_replace_true(self):
        deepupdate(self.c, self.d, replace=True)
        expected = [4, 5, 6]
        self.assertEqual(self.c, expected)

    def test_deep_update_list_replace_false(self):
        deepupdate(self.c, self.d, replace=False)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.c, expected)

    def test_deep_update_list_replace_default(self):
        deepupdate(self.c, self.d)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.c, expected)

    def test_deep_update_mix_replace_true(self):
        a = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        b = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        deepupdate(a, b, replace=True)
        expected = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        self.assertEqual(a, expected)

    def test_deep_update_mix_replace_false(self):
        a = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        b = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        deepupdate(a, b, replace=False)
        expected = {"a": 1, "b": {"c": 2, "d": [3, 4]}, "f": 7}
        self.assertEqual(a, expected)

    def test_deep_update_mix_replace_left(self):
        a = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        b = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        deepupdate(a, b, replace="left")
        expected = {"a": 1, "b": {"c": 2, "d": [3, 4], "e": [5, 6]}, "f": 7}
        self.assertEqual(a, expected)

    def test_deep_update_mix_replace_right(self):
        a = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        b = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        deepupdate(a, b, replace="right")
        expected = {"a": 2, "b": {"c": 4, "d": [3, 4], "e": [5, 6]}, "f": 7}
        self.assertEqual(a, expected)

    def test_deep_update_mix_replace_default(self):
        a = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        b = {"a": 2, "b": {"c": 4, "e": [5, 6]}, "f": 7}
        deepupdate(a, b)
        expected = {"a": 2, "b": {"c": 4, "d": [3, 4], "e": [5, 6]}, "f": 7}
        self.assertEqual(a, expected)


if __name__ == "__main__":
    unittest.main()
