from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        taken = set()
        order = []
        q = deque() 
        preqs_needed = [0] * numCourses

        for course in courses:
            for prereq in courses[course]:
                preqs_needed[course] += 1

        for i in range(numCourses):
            if courses[i] == []:
                q.append(i)
                taken.add(i)
 
        
        while q:
            course = q.popleft()
            order.append(course)
            for c in courses:
                if course in courses[c]:
                    preqs_needed[c] -= 1
                    if preqs_needed[c] == 0 and c not in taken:
                        q.append(c)
                        taken.add(c)

        if len(order) != numCourses:
            return []   
        
        return order

            

