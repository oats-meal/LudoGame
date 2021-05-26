"""
This is where we will create the piece objects.
"""

class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def getColor(self):
        return self.color
    def getName(self):
        return self.name
    def getPieceInfo(self):
        return (self.color, self.name)
        
    