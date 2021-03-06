#! /usr/bin/python

'''This is not so much a tool as a place to store some of the test geometry I want to work with.'''

node_dict = {
1: (0, 30),
2: (5, 33),
3: (10, 35),
4: (12, 34),
5: (14, 31),
6: (19, 30),
7: (18, 26),
8: (21, 24),
9: (20, 19),
10: (21, 15),
11: (22, 6),
12: (22, 4),
13: (21, 0),
14: (25, -3),
15: (25, -7),
16: (29, -11),
17: (30, -16),
18: (28, -24),
19: (25, -27),
20: (22, -29),
21: (21, -24),
22: (20, -21),
23: (20, -17),
24: (17, -16),
25: (15, -16),
26: (11, -19),
27: (1, -18),
28: (-3, -17),
29: (-7, -14),
30: (-7, -11),
31: (-11, -6),
32: (-11, -4),
33: (-13, -1),
34: (-14, 2),
35: (-12, 5),
36: (-9, 8),
37: (-9, 10),
38: (-8, 12),
39: (-10, 14),
40: (-8, 15),
41: (-6, 18),
42: (-4, 20),
43: (-3, 26),
44: (5, 29),
45: (7, 27),
46: (5, 25),
47: (8, 24),
48: (9, 21),
49: (9, 17),
50: (14, 18),
51: (17, 16),
52: (19, 6),
53: (15, 5),
54: (13, 8),
55: (9, 9),
56: (8, 11),
57: (7, 11),
58: (2, 14),
59: (-3, 12),
60: (-6, 13),
61: (8, 5),
62: (6, 2),
63: (7, -1),
64: (8, -2),
65: (13, -5),
66: (17, -6),
67: (20, -7),
68: (13, -9),
69: (12, -11),
70: (14, -13),
71: (7, -4),
72: (6, -7),
73: (5, -10),
74: (3, -14),
75: (0, -16),
76: (-1, -13),
77: (-3, -11),
78: (-9, -5),
79: (-2, -3),
80: (3, -3),
81: (5, -4),
82: (3, -8),
83: (-1, -8),
84: (-2, -7),
85: (-5, -5),
86: (-1, 48),
87: (2, 46),
88: (3, 42),
89: (2, 39),
90: (-2, 40),
91: (-5, 42),
92: (-3, 46)
}

polys = {
'A': [1,2,44,45,46,47,48,49,56,57,58,59,60,39,40,41,42,43,1],
'A2': [86,87,88,89,90,91,92,86],
'B': [3,4,5,6,7,8,9,10,51,50,49,48,47,46,45,44,2,3],
'C': [49,50,51,10,11,52,53,54,55,56,49],
'D': [[58,57,56,55,61,62,63,64,71,72,73,74,27,75,76,77,78,32,33,34,35,36,37,38,39,60,59,58],
[79,85,84,83,82,81,80,79]],
'E': [11,12,13,14,15,67,66,65,64,63,62,61,55,54,53,52,11],
'F': [79,80,81,82,83,84,85,79],
'G': [64,65,68,69,70,25,26,27,74,73,72,71,64],
'H': [65,66,67,15,16,17,18,19,20,21,22,23,24,25,70,69,68,65],
'I': [32,78,77,76,75,27,28,29,30,31,32]
}


def MakeWKT(polygon):
  '''Takes an ordered list of nodes which represent the geometry of a linear_ring
     NOTE: Only works for POLYGONS. MULTIPOLYGONS must be split ahead of time.'''
  rings = []
  # CHECK WHETHER SIMPLE POLYGON, OR HAS HOLES
  holes = any(isinstance(ring, list) for ring in polygon) # EVALUATES TO TRUE IF LIST IN POLYGON
  if not holes:
    rings.append(polygon)
  else:
    for ring in polygon:
      rings.append(ring)
  polygon_ring_wkt = [] # STRING REPRESENTATIONS OF EACH RING
  # UNWRAP EACH RING, GET THE COORDS FOR EACH NODE, APPEND COORDS TO WKT STRING
  for ring in rings:
    ring_coords = []
    for node in ring:
      (x, y) = node_dict[node]
      coord_string = "%s %s" % (str(x), str(y))
      ring_coords.append(coord_string)
    ring_wkt = ', '.join(ring_coords)
    polygon_ring_wkt.append(ring_wkt)
  polygon_wkt = 'POLYGON ((%s))' % ('), ('.join(polygon_ring_wkt))
  return polygon_wkt

def main():
  for id in polys:
    print "%s|%s" % (id, MakeWKT(polys[id]))


if __name__ == '__main__':
  main()


