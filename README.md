# topopy
Experiments in Python point munging

To Do:
[ ] What is a set of geometry and how do I deal with it?

A set of geometry is a collection of primitives.  I propose to do what mbostok does in his TopoJSON implementation and break up multi-part geometries into their individual primitives.  This means that for something like Hawaii, I'll need a lookup table that stores a primitive ID and the original feature_id, so that I can reassemble things by their feature_id.
