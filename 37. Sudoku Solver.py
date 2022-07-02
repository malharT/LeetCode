class Solution:
    def solve_by_trial_and_error(self, values_to_fill, rows, cols, boxes, board):
        if not values_to_fill:
            return True
        row, col = values_to_fill.pop(0)
        box_i = 3*(row//3) + (col//3)
        candidate_vals = rows[row].intersection(cols[col])
        candidate_vals = candidate_vals.intersection(boxes[box_i])
        sol = False
        if candidate_vals:
            for value in candidate_vals:
                rows[row].remove(value)
                cols[col].remove(value)
                boxes[box_i].remove(value)
                board[row][col] = value
                sol = self.solve_by_trial_and_error(values_to_fill, rows, cols, boxes, board)
                if not sol:
                    rows[row].add(value)
                    cols[col].add(value)
                    boxes[box_i].add(value)
                    board[row][col] = "."
                if sol:
                    break
        values_to_fill.insert(0,(row, col))
        return sol

    def solveSudoku(self, board):
        rows = []
        cols = []
        boxes = []
        all_nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        values_to_fill = set()
        for _ in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    cols[col].add(board[row][col])
                    rows[row].add(board[row][col])
                    box_i = 3*(row//3) + col//3
                    boxes[box_i].add(board[row][col])
                else:
                    values_to_fill.add((row, col))
        while values_to_fill:
            all_candidates = []
            did_single_fill = False
            did_candidate_fill = False
            for row, col in list(values_to_fill):
                box_i = 3*(row//3) + col//3
                candidates = all_nums - rows[row] - cols[col] - boxes[box_i]
                all_candidates.append(((row, col), candidates))
                if len(candidates) == 1 and board[row][col] == ".":
                    num = candidates.pop()
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_i].add(num)
                    values_to_fill.remove((row, col))
                    did_single_fill = True
                    continue
            if not did_single_fill:
                rows_options = dict()
                cols_options = dict()
                boxes_options = dict()
                for row, col in list(values_to_fill):
                    box_i = 3*(row//3) + col//3
                    candidates = all_nums - rows[row] - cols[col] - boxes[box_i]
                    for item in candidates:
                        if item not in rows_options:
                            rows_options[item] = {row: [col]}
                        else:
                            if row not in rows_options[item]:
                                rows_options[item][row] = [col]
                            else:
                                rows_options[item][row] += [col]
                        if item not in cols_options:
                            cols_options[item] = {col: [row]}
                        else:
                            if col not in cols_options[item]:
                                cols_options[item][col] = [row]
                            else:
                                cols_options[item][col] += [row]
                        if item not in boxes_options:
                            boxes_options[item] = {box_i: [(row, col)]}
                        else:
                            if box_i not in boxes_options[item]:
                                boxes_options[item][box_i] = [(row, col)]
                            else:
                                boxes_options[item][box_i] += [(row, col)]
                for num in rows_options:
                    for row in rows_options[num]:
                        options = rows_options[num][row]
                        if len(options) == 1:
                            col = options[0]
                            if board[row][col] == ".":
                                board[row][col] = num
                                did_candidate_fill = True
                                rows[row].add(num)
                                cols[col].add(num)
                                box_i = 3*(row//3) + col//3
                                boxes[box_i].add(num)
                                values_to_fill.remove((row, col))
                for num in cols_options:
                    for col in cols_options[num]:
                        options = cols_options[num][col]
                        if len(options) == 1:
                            row = options[0]
                            if board[row][col] == ".":
                                board[row][col] = num
                                did_candidate_fill = True
                                rows[row].add(num)
                                cols[col].add(num)
                                box_i = 3*(row//3) + col//3
                                boxes[box_i].add(num)
                                values_to_fill.remove((row, col))
                for num in boxes_options:
                    for box in boxes_options[num]:
                        options = boxes_options[num][box]
                        if len(options) == 1:
                            row, col = options[0]
                            if board[row][col] == ".":
                                board[row][col] = num
                                did_candidate_fill = True
                                rows[row].add(num)
                                cols[col].add(num)
                                box_i = 3*(row//3) + col//3
                                boxes[box_i].add(num)
                                values_to_fill.remove((row, col))
            if not did_single_fill and not did_candidate_fill:
                break
        rows_options = []
        cols_options = []
        boxes_options = []

        for row in rows:
            rows_options.append(all_nums - row)

        for col in cols:
            cols_options.append(all_nums - col)

        for box in boxes:
            boxes_options.append(all_nums - box)

        new_values_to_fill = []
        for val in values_to_fill:
            row, col = val
            box_i = 3*(row//3) + (col//3)
            candidate_vals = rows[row].intersection(cols[col])
            candidate_vals = candidate_vals.intersection(boxes[box_i])
            new_values_to_fill.append((row, col, len(candidate_vals)))

        values_to_fill = sorted(new_values_to_fill, key=lambda s: s[2])
        values_to_fill = [(row,col) for row, col, _ in values_to_fill]

        solution = self.solve_by_trial_and_error(
            values_to_fill, rows_options, cols_options, boxes_options, board)
        return board