class Group(object):
    def __init__(self,*args):
        return self.combine(args)
    def combine(self,args*):
        pass
class Compounds(Group):
    def combine(self,args):
        return reduce(lambda x,y: x and y, args)

