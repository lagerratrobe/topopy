#! /usr/local/bin/python

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "point(%s, %s)" % (self.x, self.y)

  def __eq__(self, other):
    if isinstance(other, Point):
      return ((self.x == other.x) and (self.y == other.y))
    else:
      return False


class LineString(object):
  def __init__(self, *points):
    self.points = []
    for point in points:
      self.points.append(point) 

  def __repr__(self):
    return "lineString(%s)" % (self.points)

  def __eq__(self, other):
    if isinstance(other, LineString):
      return self.__dict__ == other.__dict__
    else:
      return False

