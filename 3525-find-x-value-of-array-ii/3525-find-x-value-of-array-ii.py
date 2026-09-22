class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]: 
        n = len(nums)

        tree = [[0] * k for _ in range(4 * n)]
        total = [0] * (4 * n)

        def build(node, left, right):
            if left == right:
                r = nums[left] % k
                total[node] = r
                tree[node][r] = 1
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            pull(node)

        def pull(node):
            a = node * 2
            b = a + 1

            total[node] = (total[a] * total[b]) % k

            for r in range(k):
                tree[node][r] = tree[a][r]

            for r in range(k):
                tree[node][(total[a] * r) % k] += tree[b][r]

        def update(node, left, right, pos, value):
            if left == right:
                r = value % k
                total[node] = r

                for x in range(k):
                    tree[node][x] = 0

                tree[node][r] = 1
                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, right, pos, value)

            pull(node)

        def query(node, left, right, ql):
            if ql <= left:
                return tree[node][:], total[node]

            mid = (left + right) // 2

            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql)

            left_count, left_product = query(
                node * 2, left, mid, ql
            )
            right_count, right_product = query(
                node * 2 + 1, mid + 1, right, ql
            )

            result = left_count

            for r in range(k):
                result[(left_product * r) % k] += right_count[r]

            product = (left_product * right_product) % k

            return result, product

        build(1, 0, n - 1)

        ans = []

        for idx, value, start, x in queries:
            nums[idx] = value
            update(1, 0, n - 1, idx, value)

            counts, _ = query(1, 0, n - 1, start)
            ans.append(counts[x])

        return ans