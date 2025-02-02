a= {}#empty dictionary
a = {
"key": "value",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]
# it is of class <dict>
'''1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.

Dictionary methods:-
len(a) : lenght of dictionary

a.items(): Returns a list of (key,value)tuples.

a.keys(): Returns a list containing dictionary's keys.

a.values(): returns a list of values in the dictionary

a.clear() : clears the dictionary

a1=a.copy() : copies the dictionary to another dictionary

keys=['a','b','c']
a1=a.fromkeys(keys,value) : creates a new dictionary with the keys and values set to value

x=a.pop('key','default_value')
:removes a specified key and returns its corresponding value and if the key is not found default is returned if given 

a.update({"marks":99}): Updates the dictionary with supplied key-value pairs.

a.get("marks"): Returns the value of the specified keys.

print(a["marks"]) will give error if the marks doesnt exists in the dictionary.
print(a.get["marks]) will give none if the marks doesnt exists in the dictionary.
'''