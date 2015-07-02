#! /usr/local/bin/python

import sys
import unittest

sys.path.append('../')
import assembler


class TestAssembler(unittest.TestCase):

  def test_MakeWKT_simple_poly(self):
    ring_nodes = assembler.polys['B']
    poly_B_wkt = assembler.MakeWKT(ring_nodes)
    self.assertEqual(poly_B_wkt, "POLYGON ((10 35, 12 34, 14 31, 19 30, 18 26, 21 24, 20 19, 21 15, 17 16, 14 18, 9 17, 9 21, 8 24, 5 25, 7 27, 5 29, 5 33, 10 35))")


  def test_MakeWKT_holey_poly(self):
    ring_nodes = assembler.polys['D']
    poly_D_wkt = assembler.MakeWKT(ring_nodes)
    self.assertEqual(poly_D_wkt, "POLYGON ((2 14, 7 11, 8 11, 9 9, 8 5, 6 2, 7 -1, 8 -2, 7 -4, 6 -7, 5 -10, 3 -14, 1 -18, 0 -16, -1 -13, -3 -11, -9 -5, -11 -4, -13 -1, -14 2, -12 5, -9 8, -9 10, -8 12, -10 14, -6 13, -3 12, 2 14), (-2 -3, -5 -5, -2 -7, -1 -8, 3 -8, 5 -4, 3 -3, -2 -3))")


if __name__ == '__main__':
  unittest.main()
