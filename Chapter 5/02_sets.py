# Set is a collection of non-repetitive elements.Immutable and  hashable
s = set() #empty set
s.add(1)
s.add(2) # or set ={1,2}    
'''1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

Set methods:-

s.add():adds the value to the set

len(s): Returns 4, the length of the set

s.remove(8): Updates the set s and removes 8 from s.

s.pop(): Removes an arbitrary element from the set and return the element removed.

s.clear():empties the set s.

s.union({8,11})
s.union(s2) : Returns a new set with all items from both sets. {1,8,2,11}.

s.intersection({8,11})
s.intersection(s2): Return a set which contains only item in both sets {8}.

s.add(20) is same as s.add(20.0) but not same as a.add('20') or s.add("20")
'''