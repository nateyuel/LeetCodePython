class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(i, val):
            i += size
            tree[i] = val

            while i > 1:
                i //= 2
                tree[i] = tree[2 * i] + tree[2 * i + 1]

        def find(node, left, right, start):
            if right <= start or tree[node] == 0:
                return -1

            if right - left == 1:
                return left

            mid = (left + right) // 2

            res = find(node * 2, left, mid, start)

            if res == -1:
                res = find(node * 2 + 1, mid, right, start)

            return res

        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                update(server, 1)

            server = find(1, 0, size, i % k)

            if server == -1:
                server = find(1, 0, size, 0)

            if server == -1 or server >= k:
                continue

            update(server, 0)
            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]