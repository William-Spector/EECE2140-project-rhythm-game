class Note:
    '''
    class Note
    Struct containing the properties of each note
    attributes:
        timing          int
        color           int
        location        tuple(int) len 2
    '''
    def __init__(self, ms: int, color: int, location: tuple):
        '''
        initializer for Note
        Inputs:
            ms          int
            color       int
            location    tuple(int), len=2
        '''
        self.timing = ms
        self.color = color
        self.location = location

    def draw_note(self):
        '''
        function draw_note
        returns the location and color the note should be in a tuple
        unused, may be deleted in a future commit
        '''
        return (self.location, self.color)
