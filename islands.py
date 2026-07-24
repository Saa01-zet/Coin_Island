from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands_count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row: int, col: int) -> None:

            queue = deque([(row, col)])
            grid[row][col] = '0'

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if (0 <= new_r < rows and
                            0 <= new_c < cols and
                            grid[new_r][new_c] == '1'):
                        grid[new_r][new_c] = '0'
                        queue.append((new_r, new_c))

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == '1':
                    islands_count += 1
                    bfs(row, col)

        return islands_count

def test_number_of_islands():
    print("ПРОВЕРКА: Количество островов")

    sol = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result1 = sol.numIslands(grid1)
    print(f"\nТест 1:")
    print("Сетка:")
    for row in grid1:
        print(f"  {row}")
    print(f"Результат: {result1}")
    print(f"Ожидалось: 1")
    print("Пройден!" if result1 == 1 else "Не пройден!")

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result2 = sol.numIslands(grid2)
    print(f"\nТест 2:")
    print("Сетка:")
    for row in grid2:
        print(f"  {row}")
    print(f"Результат: {result2}")
    print(f"Ожидалось: 3")
    print("Пройден!" if result2 == 3 else "Не пройден!")

    grid3 = []
    result3 = sol.numIslands(grid3)
    print(f"\nТест 3 (пустая сетка):")
    print(f"Результат: {result3}")
    print(f"Ожидалось: 0")
    print("Пройден!" if result3 == 0 else "Не пройден!")

if __name__ == "__main__":
    test_number_of_islands()