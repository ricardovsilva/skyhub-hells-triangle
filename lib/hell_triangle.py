class HellTriangle:
  
    def __init__(self, triangle):
        self.triangle = triangle

    def find_maximum_total(self):
        pass

    def get_two_nearest_x_indexes(self, x, y):
        is_last_line = y == len(self.triangle) - 1
        if is_last_line: return None

        is_first_column = x == 0

        if is_first_column: return {"left": 0, "right": x + 1}
        else: return {"left": x, "right": x+1}
            
