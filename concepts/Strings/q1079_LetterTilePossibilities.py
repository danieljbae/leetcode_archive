class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        n = len(tiles)
        x = []
        for i in range(1, n+1):
            print(list(set(permutations(tiles,i))))
            x += list(set(permutations(tiles,i)))
        return len(x)