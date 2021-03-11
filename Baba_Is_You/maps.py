class Map():
    def __init__(self, width, height, dir_objects, objects):
        self.width = width
        self.height = height
        self.dir_objects = dir_objects
        self.objects = objects
        self.win = False

test = Map(20, 20, {'baba' : [[5, 5]]},
                    {'flag' : [[15, 15]], 'wall' : [[10, i] for i in range(20)],
                     'text_baba' : [[3, 3]],
                     'text_is' : [[4, 3], [7, 16], [15,4]],
                     'text_you' : [[5, 3]],
                     'text_wall' : [[7, 15]],
                     'text_stop' : [[7, 17]],
                     'text_flag' : [[15, 3]],
                     'text_win' : [[15, 5]]})
