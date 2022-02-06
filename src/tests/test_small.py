import unittest
from src.parse_matrices import ParseMatrices

class TestSmallCases(unittest.TestCase):

    def test_empty(self):
        data = ""
        output = ParseMatrices(data).parse_matrix()
        self.assertEqual(output, [])
    
    def test_one_level(self):
        data = "{I, have, studied, computer, science}"
        output = ParseMatrices(data).parse_matrix()
        self.assertEqual(output, ["I", "have", "studied", "computer", "science"])
    
    def test_two_level(self):
        data = "{{And, I, was, the, back-bencher, in, school}, {and, it, helped, me, do, whatever, I, liked}}"
        output = ParseMatrices(data).parse_matrix()
        self.assertEqual(output, [["And", "I", "was", "the", "back-bencher", "in", "school"], ["and", "it", "helped", "me", "do", "whatever", "I", "liked"]])
    
    def test_multiple(self):
        data = "{name, {name, {name}}}"
        output = ParseMatrices(data).parse_matrix()
        self.assertEqual(output, ["name", ["name", ["name"]]])