import heapq

def swimInWater(self, grid: List[List[int]]) -> int:
    n = len(grid)
    visited = set()
    heap = [(grid[0][0], 0, 0)]  # (time, r, c)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while heap:
        time, r, c = heapq.heappop(heap)
        if (r, c) == (n-1, n-1):
            return time
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                new_time = max(time, grid[nr][nc])
                heapq.heappush(heap, (new_time, nr, nc))

