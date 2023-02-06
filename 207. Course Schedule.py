class Solution:
    def dfs(self, node, completed, visited, course_tree):
        if node not in completed: return True
        if node in visited: return False
        visited.add(node)
        if node in course_tree:
            for par in course_tree[node]:
                out = self.dfs(par, completed, visited, course_tree)
                if not out: return False
        completed.remove(node)
        return True

        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_tree = {}
        completed = set()
        for pre in prerequisites:
            source = pre[1]
            target = pre[0]
            completed.add(target)
            if target not in course_tree:
                course_tree[target] = []
            course_tree[target].append(source)
        children = {}

        for course in course_tree:
            out = self.dfs(course, completed, set(), course_tree)
            if not out: return False
            if course in completed:completed.remove(course)
        return all(completed)