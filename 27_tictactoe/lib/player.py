class PlayerError(Exception): pass

class Player(object):
    def __init__(self, name, val):
        if ( len(val) != 1 ): 
            raise PlayerError("player identifier must be 1 character")

        self.name = name
        self.val  = val


