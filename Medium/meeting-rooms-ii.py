from heapq import heappush as push
from heapq import heappop as pop
from heapq import heappushpop as pushpop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = [(intervals[0][1], 1)]
        nrooms = 1
        for intv in intervals[1:]:
            end, room = rooms[0]
            if end <= intv[0]:
                pushpop(rooms, (intv[1], room))
            else:
                # New room
                nrooms += 1
                push(rooms, (intv[1], nrooms))
        
        return nrooms



        
            

