class Solution:
    def find_prerequisite(self, course,
                          prereq_graph,
                          unprocessed_courses,
                          order_of_courses,
                          children,
                          children_courses):
        if course not in prereq_graph:
            order_of_courses[course] = [course]
            if course in unprocessed_courses:
                unprocessed_courses.remove(course)
            return True
        else:
            order_of_courses[course] = [course]
            if course in unprocessed_courses:
                prereqs = prereq_graph[course]
                children.add(course)
                if children.intersection(prereqs):
                    return False
                for prereq in prereqs:
                    if prereq in children_courses:
                        children_courses.remove(prereq)
                    if prereq in unprocessed_courses:
                        result = self.find_prerequisite(prereq,
                                                        prereq_graph,
                                                        unprocessed_courses,
                                                        order_of_courses,
                                                        children,
                                                        children_courses)
                        if not result:
                            return False
                    order_of_courses[course] = order_of_courses[prereq] + order_of_courses[course]
                        
                children.remove(course)
                unprocessed_courses.remove(course)
        return True
        
    def findOrder(self, numCourses, prerequisites):
        prereq_graph = {}
        order_of_courses = {}
        unprocessed_courses = set(range(numCourses))
        for course, prereq in prerequisites:
            if course in prereq_graph:
                prereq_graph[course].add(prereq)
            else:
                prereq_graph[course] = set([prereq])

        children_courses = set(range(numCourses))
        while unprocessed_courses:
            course = unprocessed_courses.pop()
            unprocessed_courses.add(course)
            result = self.find_prerequisite(course, prereq_graph,
                                            unprocessed_courses,
                                            order_of_courses,
                                            set(),
                                            children_courses)
            if not result:
                return []
        order_to_return = []
        course_in_order = set()
        for child in children_courses:
            for course in order_of_courses[child]:
                if course not in course_in_order:
                    order_to_return.append(course)
                    course_in_order.add(course)
        return order_to_return