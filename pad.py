
# https://www.hackerrank.com/challenges/queens-attack-2

# notes, should have gone for O(n) by checking each line rather than O(k)
# Use vectors to move through grid

# my solution

from collections import defaultdict
from math import abs


class Piece:
    def __init__(self, row, col, n):
        self.row = row
        self.col = col
        self.n = n
        self.path = None

    def coord_diff(self, piece):
        return (self.row - piece.row, self.col - piece.col)

    def on_path(self, piece):
        diff = self.coord_diff(piece)
        # straight line
        if 0 in diff:
            # left-right
            if diff[0] == 0:
                if diff[1] == 0:
                    raise ValueError("clashing pieces")
                if diff[1] > 0:
                    self.path = 2

                else:
                    self.path = 6
            # up-down
            if diff[1] == 0:
                if diff[0] == 0:
                    raise ValueError("clashing pieces")
                if diff[0] > 0:
                    self.path = 0
                else:
                    self.path = 4
            return True

        # diagonal
        if abs(diff[0]) == abs(diff[1]):
            if diff[0] > 0:
                if diff[1] > 0:
                    self.path = 1
                else:
                    self.path = 7
            else:
                if diff[1] > 0:
                    self.path = 3
                else:
                    self.path = 5

            return True
        return False

    def straight_dist(self, path):
        if not path:
            raise ValueError("No path defined")
        if path == 0:
            return self.n - self.row
        elif path == 4:
            return self.row - 1
        elif path == 2:
            return self.n - self.col
        elif path == 6:
            return self.col - 1

    def diag_dist(self, path):
        if not path:
            raise ValueError("No path defined")
        if path == 1:
            return min(self.straight_dist(0), self.straight_dist(2))
        if path == 3:
            return min(self.straight_dist(2), self.straight_dist(4))
        if path == 5:
            return min(self.straight_dist(4), self.straight_dist(6))
        if path == 7:
            return min(self.straight_dist(6), self.straight_dist(0))

    def edge_dist(self, path):
        if path % 2 == 0:
            return self.straight_dist(path)
        return self.diag_dist(path)


def queensAttack(n, k, r_q, c_q, obstacles):
    queen = Piece(r_q, c_q, n)
    closest = defaultdict(int)
    for coords in obstacles:
        piece = Piece(coords[0], coords[1], n)
        if piece.on_path(queen):
            dist = piece.edge_dist(piece.path)
            if dist > closest[piece.path]:
                closest[piece.path] = dist
    result = 0
    for path in range(8):
        result += queen.edge_dist(path)
        result -= closest[path]
    return result


# Optimal Solution

from collections import defaultdict

def queensAttack(n, k, r_q, c_q, obstacles):
    obstacle_set = {(r, c) for r, c in obstacles}
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    count = 0

    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obstacle_set:
            count += 1
            r += dr
            c += dc

    return count
