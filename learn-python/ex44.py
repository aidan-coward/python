class Parent(object):

    def implicit(self):
        print "PARENT"

class Child(Parent):
    
    def implicit(self):
        print "rock lobsters"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
