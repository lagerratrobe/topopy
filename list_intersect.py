#! /usr/local/bin/python

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bar= [7, 8, 9, 10, 11, 12, 13, 14]
compset = set(foo)
crak = [x for x in bar if x in compset]
print "foo = %s" % (foo)
print "bar = %s" % (bar)
print "Intersection of foo and bar is %s" % (crak)
