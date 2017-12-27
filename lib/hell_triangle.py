class HellTriangle:
  
    def __init__(self, triangle):
        if self._triangle_is_invalid(triangle): raise ValueError('Invalid triangle')
        self.triangle = triangle

    def find_maximum_total(self, x = 0, y = 0):
        nearest_indexes = self.get_two_nearest_x_indexes(x, y)
        if nearest_indexes is None: return self.triangle[y][x]

        left = self.find_maximum_total(nearest_indexes['left'], y+1)
        right = self.find_maximum_total(nearest_indexes['right'], y+1)

        current_value = self.triangle[y][x]
        return current_value + left if left > right else current_value + right

    def get_two_nearest_x_indexes(self, x, y):
        is_last_line = y == len(self.triangle) - 1
        if is_last_line: return None

        is_first_column = x == 0

        if is_first_column: return {"left": 0, "right": x + 1}
        else: return {"left": x, "right": x+1}

    def _triangle_is_invalid(self, triangle):
        if triangle is None or len(triangle) == 0: return True

        for i, element in enumerate(triangle):
            if i == 0: continue
            if len(triangle[i]) - len(triangle[i - 1]) != 1: return True
