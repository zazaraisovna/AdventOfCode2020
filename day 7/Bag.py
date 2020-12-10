class Bag:
    def __init__(self,color,parent, children, amount):
        self.color = color
        self.parent = parent
        self.children = children
        self.amount = amount

    def getColor(self):
        return self.color

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def getAmount(self):
        return self.amount

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def setParent(self,parent):
        self.parent = parent

    def getAncestor(self):
        i = 0
        parent = self.getParent()
        while(parent != None):
            if(parent.getParent() == None and i != 0):
                return i
            elif(parent.getParent() == None and i == 0):
                return i
            else:
                parent = parent.getParent()

            i += 1