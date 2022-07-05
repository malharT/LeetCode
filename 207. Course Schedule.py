class Solution:
    def getPrereqs(self, course, prereqs, processing_children, unprocessed_children):
        pre_courses = prereqs[course]
        if processing_children.intersection(pre_courses):
            return False
        all_descendants = set()
        for pre_course in pre_courses:
            if pre_course in unprocessed_children:
                unprocessed_children.remove(pre_course)
                processing_children.add(pre_course)
                result = self.getPrereqs(pre_course, prereqs, processing_children, unprocessed_children)
                if result:
                    result, descendants = result
                    all_descendants.update(descendants)
                    processing_children.remove(pre_course)
                else:
                    return False
        pre_courses.update(all_descendants)
        return True, pre_courses

    def canFinish(self, numCourses, prerequisites):
        prereqs = []
        for course in range(numCourses):
            prereqs.append(set())
        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]
            if not b in prereqs[a]:
                prereqs[a].add(b)
            else:
                return False

        unprocessed_prereqs = set(range(numCourses))
        while unprocessed_prereqs:
            course = unprocessed_prereqs.pop()
            result = self.getPrereqs(course, prereqs, set([course]), unprocessed_prereqs)
            if not result:
                return False
        return True