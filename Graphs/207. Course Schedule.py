class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        vis = set()
        def dfs(course):
            if course in vis:
                return False
            if not courses[course]:
                return True
            vis.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            vis.remove(course)
            courses[course] = []
            return True
        
        for course in courses:
            if not dfs(course):
                return False
        return True