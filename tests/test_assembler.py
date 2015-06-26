#! /usr/local/bin/python

import sys
import unittest

sys.path.append('../')
import assembler


class TestAssembler(unittest.TestCase):

  def test_MakeWKT(self):
    poly_B = assembler.MakeWKT(polys['B'])
    self.assertEqual(poly_B, "POLYGON ((10 35, 12 34, 14 31, 19 30, 18 26, 21 24, 20 19, 21 15, 17 16, 14 18, 9 17, 9 21, 8 24, 5 25, 7 27, 5 29, 5 33, 10 35))")

if __name__ == '__main__':
  unittest.main()
