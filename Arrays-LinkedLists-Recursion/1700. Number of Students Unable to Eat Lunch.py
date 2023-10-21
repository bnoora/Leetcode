class Solution:
    def countStudents(self, students: [int], sandwiches: [int]) -> int:
        sandwiches = sandwiches[::-1]
        rot = 0
        while students:
            if rot == len(students):
                return len(students)
            if not sandwiches:
                return len(students)
            
            if students[0] == sandwiches[-1]:
                sandwiches.pop()
                students.pop(0)
                rot = 0
            else:
                students.append(students.pop(0))
                rot += 1
        return 0





from collections import deque

class Solution:
    def countStudents(self, students: [int], sandwiches: [int]) -> int:
        students_queue = deque(students)
        sandwiches_stack = sandwiches[::-1]  # reversing the sandwiches to make it a stack
        
        rotations = 0
        
        while students_queue and sandwiches_stack:
            if students_queue[0] == sandwiches_stack[-1]:
                sandwiches_stack.pop()
                students_queue.popleft()
                rotations = 0
            else:
                students_queue.append(students_queue.popleft())
                rotations += 1
                
                # If we have rotated through all the students and the first student still can't eat the sandwich
                if rotations == len(students_queue):
                    break
        
        return len(students_queue)
