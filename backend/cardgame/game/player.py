import logging

class Player():
    # Globally relevant
    name:       str
    is_host:    bool
    # ingame information
    sex:        bool    # The player char's sex (0 = f,1 = m)
    level:      int     # current level [1..10]
    races:      list    # race (human, orc)
    classes:    list    # class (pries, cleric, ...)
    equip:      list    # Equip, items, curses ...
    cards:      list    # cards in players hand
    
    def __init__(self, name, sex):
        self.name = name
        self.is_host = False
        
        self.sex = sex
        self.race = ""
