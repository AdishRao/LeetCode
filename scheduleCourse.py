# https://leetcode.com/problems/course-schedule-iii/submissions/

# We use a negative sign when using the heapq as heapq only supports minheaps but we need a maxheap. A reversal of signs achieves this.
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses_taken = []
        time = 0
        courses.sort(key=lambda x: x[1])
        for i in range(len(courses)):
            if(time+courses[i][0] <= courses[i][1]):
                heappush(courses_taken, -courses[i][0])
                time += courses[i][0]

            elif ((courses_taken) and (courses[i][0] < -courses_taken[0])):
                time = time - (-heappop(courses_taken)) + courses[i][0]
                heappush(courses_taken, -courses[i][0])
        return len(courses_taken)
