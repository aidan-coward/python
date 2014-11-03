from sys import argv

script, ftext = argv

print "Here's your file %r:" % ftext
gtext = open(ftext)
htext = gtext
print htext.read()

