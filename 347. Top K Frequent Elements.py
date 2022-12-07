class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        solution = []
        i = 0
        for num in nums:
            if num not in counts:
                counts[num] = (1, i)
                i += 1
                solution.append(num)
            else:
                count, idx = counts[num]
                init_idx = idx
                if idx == 0:
                    counts[num] = count + 1, idx
                else:
                    while idx > 0 and (count + 1) > counts[solution[idx-1]][0]:
                        counts[solution[idx-1]] = counts[solution[idx-1]][0], counts[solution[idx-1]][1] + 1
                        idx -= 1
                    solution.insert(idx, solution.pop(init_idx))
                    counts[num] = count + 1, idx
        return solution[:k]