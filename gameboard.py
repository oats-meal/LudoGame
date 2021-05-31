"""
Game Board

This is the file that will store the game board and game state
"""

class gameboard(self):
    def __init__(self, players):
        self.players = players
        # Maybe I should add "home" into the board for each color
        board = {
            "A_side":[],
            "B_side":[],
            "C_side":[],
            "D_side":[],
        }
    def move_piece(self, piece_id, steps):
        # Given a piece, move it.
        # Special case if at home

class space(self):
    """ 
    A ludo board has 4 quadrants each corresponding to a color
    Each quadrant has 3 rows. (4 if you count home)
    Each row has 6 spaces (except home which has 4)
    The middle row is only safe spaces that only a piece of its color can enter after traversing the board
    """
    
    def __init__(self, color, occupied_by, safe=False):
        self.color = color
        self.safe = is_safe
        self.occupied_by = occupied_by
        
    def set_safe(self, safe):
        self.safe = safe
        
    def get_safe(self):
        return self.safe
    
class row(self):
    def __init__(self, color, rowtype):
        # Color = the color the row belongs to. In our case this may just be A/B/C/D
        # rowtype = Launching Row, Goal Row, Entry Row,
        
        self.color = color
        self.rowtype = rowtype
        self.spaces = make_spaces(color, rowtype)
        
    def make_spaces(self, color, rowtype):
        temp_row = []
        if (rowtype == "launching"):
            temp_row = ([space(color,[],safe = False)]*6)
            temp_row[1].set_safe(True)            
        elif (rowtype == "goal"):
            temp_row = ([space(color,[],safe = True)]*6)
            temp_row[0].set_safe(False)
        elif (rowtype == "entry"):
            temp_row = ([space(color,[],safe = False)]*6)
            temp_row[3].set_safe(True)
        else:
            raise Exception("Wrong rowtype")
        return temp_row