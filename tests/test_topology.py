#! /usr/local/bin/python

import sys
import unittest

sys.path.append('../')
from geometry import *
import topology


class TestTopololy(unittest.TestCase):

  def test_LineString_plain_repr(self):
    line = LineString(1, 2, 3, 4, 5)
    self.assertEqual(repr(line), "lineString([1, 2, 3, 4, 5])")

  def test_LineString_Point_repr(self):
    line = LineString(Point(-1,1), Point(-2,2), Point(-3,3))
    self.assertEqual(repr(line), "lineString([point(-1, 1), point(-2, 2), point(-3, 3)])")

  def test_LineString_eq_plain(self):
    line1 = LineString(1, 2, 3, 4, 5)
    line2 = LineString(1, 2, 3, 4, 5)
    self.assertEqual(line1, line2)

if __name__ == '__main__':
  unittest.main()
