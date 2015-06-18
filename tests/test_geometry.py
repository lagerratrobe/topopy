#! /usr/local/bin/python

import sys
import unittest
sys.path.append('../')
from geometry import *

class TestGeometry(unittest.TestCase):
  def test_Point(self):
    '''Build a point and test its parts'''
    point = Point(-2,2)
    self.assertEqual(point.x, -2)
    self.assertEqual(point.y, 2)

  def test_Point_repr(self):
    '''Test string representation of a Point'''
    point = Point(-2, 2)
    self.assertEqual(repr(point), "point(-2, 2)")

  def test_Point_eq(self):
    '''Make sure that 2 points built with the same values are considered equal'''
    point1 = Point(-4,4)
    point2 = Point(-4,4)
    point3 = Point(-2,2)
    self.assertTrue(point1 == point2)
    self.assertFalse(point1 == point3)

  def test_LineString(self):
    line = LineString(1, 2, 3, 4, 5)
    self.assertEqual(line.points[2], 3)
    self.assertEqual(line.points[3], 4)

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

  def test_LineString_eq_Point(self):
    line1 = LineString(Point(-1,1), Point(-2,2), Point(-3,3))
    line2 = LineString(Point(-1,1), Point(-2,2), Point(-3,3))
    line3 = LineString(Point(-2,2), Point(-4,4))
    self.assertEqual(line1, line2)
    self.assertFalse(line1 == line3)
  

if __name__ == '__main__':
  unittest.main()
