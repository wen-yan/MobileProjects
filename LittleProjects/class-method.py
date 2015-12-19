class myclass:
    @staticmethod
    def staticask():
        print "donot ask"
        
    @classmethod
    def classask(cls):
        print str(cls) + " donot ask too"
        
    def instanceask(self):
        print str(self) + " do ask"

myclass.staticask()
myclass.classask()
a = myclass()
a.instanceask()
a.staticask()
a.classask()

print myclass.__dict__

