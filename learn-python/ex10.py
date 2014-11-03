tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split from the outside in\von a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* "Cat food"
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat 
print backslash_cat
print fat_cat

print "This is the first way of printing things: %s" % fat_cat

print "This is the second way of printing things: %r" % fat_cat
