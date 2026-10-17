class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = Counter(s)
        store = defaultdict(list)
        max_uniq = 0
        max_grp = 0

        for ch, freq in counter.items():
            store[freq].append(ch)

            if max_uniq < len(store[freq]):
                max_uniq = len(store[freq])
                max_grp = freq
            elif max_uniq == len(store[freq]) and freq > max_grp:
                max_grp = freq

        return "".join(store[max_grp])
