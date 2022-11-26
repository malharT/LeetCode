class SegmentTree:
    def __init__(self, items, value, offset) -> None:
        self.value = value
        self.l = None
        self.r = None
        self.index = None
        self.max_gather = int(value/items)
        if items == 1:
            self.l_lim = offset
            self.r_lim = offset + 1
            self.index = 0
        else:
            left_items = items//2
            right_items = items - left_items
            left_value = int((value/items) * left_items)
            right_value = value - left_value
            self.l_lim = offset
            self.r_lim = offset + items
            if left_items > 0:
                self.l = SegmentTree(left_items, left_value, offset)
            if right_items > 0:
                self.r = SegmentTree(right_items, right_value, offset + left_items)

    def fill_leaf_if_available(self, fill, maxRow):
        if self.max_gather < fill:
            return []
        if self.r_lim - self.l_lim == 1 and maxRow >= self.l_lim:
            rem = max(0, fill - self.value)
            if rem > 0:
                return []
            else:
                index = self.index 
                self.value -= fill
                self.index += fill
                self.max_gather = self.value
                return [self.l_lim, index]
        else:
            if self.l.value >= fill and self.l_lim <= maxRow:
                ans = self.l.fill_leaf_if_available(fill, maxRow)
                if ans != []:
                    self.value -= fill
                    self.max_gather = max(self.l.max_gather, self.r.max_gather)
                    return ans
            if self.r.value >= fill and self.r.l_lim <= maxRow:
                ans = self.r.fill_leaf_if_available(fill, maxRow)
                if ans != []:
                    self.value -= fill
                    self.max_gather = max(self.l.max_gather, self.r.max_gather)
                    return ans
            return []

    def fill_leaves_dfs(self, fill, maxRow):
        if self.r_lim - self.l_lim == 1:
            rem = max(0, fill - self.value)
            new_value = self.value - fill + rem
            new_index = self.index + fill - rem 
            return [(self, rem, new_value, new_index)]
        else:
            ans = []
            rem = fill
            ans_l = []
            ans_r = []
            if self.l.value > 0 and self.l_lim <= maxRow:
                ans_l = self.l.fill_leaves_dfs(fill, maxRow)
                if ans_l != []:
                    rem = ans_l[0][1]
            if rem > 0 and self.r.value > 0 and self.r.l_lim <= maxRow:
                ans_r = self.r.fill_leaves_dfs(rem, maxRow)
                if ans_r != []:
                    rem = ans_r[0][1]
            ans = ans_l + ans
            ans = ans_r + ans
            if rem < fill:
                new_value = self.value - fill + rem
                return [(self, rem, new_value, None)] + ans
            return []


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.rows = [(0, m)]*n
        self.n = n
        self.m = m
        self.st = SegmentTree(n, n*m, 0)

    def gather(self, k: int, maxRow: int) -> list:
        return self.st.fill_leaf_if_available(k, maxRow)

    def scatter(self, k: int, maxRow: int, book=True) -> bool:
        node = self.st
        if node.value < k:
            return False
        nodes_to_modify = []
        to_fill = k
        while node.r_lim > maxRow and to_fill:
            if node.l is not None:
                if node.l.r_lim <= maxRow:
                    curr_fill = min(to_fill, node.l.value)
                    nodes_to_modify.append((node.l, curr_fill))
                    to_fill -= curr_fill
                    if node.r.r_lim == maxRow + 1:
                        curr_fill = min(to_fill, node.r.value)
                        nodes_to_modify.append((node.r, curr_fill))
                        to_fill -= curr_fill
                        break
                    else:
                        node = node.r
                elif node.l.r_lim == maxRow + 1:
                    curr_fill = min(to_fill, node.l.value)
                    nodes_to_modify.append((node.l, curr_fill))
                    to_fill -= curr_fill
                    break
                else:
                    node = node.l
            else:
                if node.r_lim == maxRow + 1:
                    curr_fill = min(to_fill, node.value)
                    nodes_to_modify.append((node, curr_fill))
                    to_fill -= curr_fill
                    break

        if to_fill:
            return False
        ans = self.st.fill_leaves_dfs(k, maxRow)
        ans.reverse()
        for node, _, value, index in ans:
            node.value = value
            if node.l is None and node.r is None:
                node.max_gather = node.value
            elif node.l is None:
                node.max_gather = node.r.max_gather
            elif node.r is None:
                node.max_gather = node.l.max_gather
            else:
                node.max_gather = max(node.l.max_gather, node.r.max_gather)
            node.index = index
        return True