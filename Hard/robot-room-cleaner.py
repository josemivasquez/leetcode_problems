# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current 
    cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        global crdir
        global crpos

        cleaned = set()
        crpos = (0, 0)
        crdir = 0
        path = []

        def nextpos():
            if crdir == 0:
                return (crpos[0] + 1, crpos[1])
            elif crdir == 1:
                return (crpos[0], crpos[1] + 1)
            elif crdir == 2:
                return (crpos[0] - 1, crpos[1])
            elif crdir == 3:
                return (crpos[0], crpos[1] - 1)

        def move():
            global crpos
            moved = robot.move()
            if not moved:
                return False
            crpos = nextpos()
            return True

        def turnright():
            global crdir
            robot.turnRight()
            crdir = (crdir + 1) % 4
        
        def revdir(dir):
            return (dir + 2) % 4
        
        def comeback():
            ansdir = path.pop()
            while crdir != revdir(ansdir):
                turnright()
            move()
            for _ in range(3):
                turnright()
        
        while True:
            cleaned.add(crpos)
            robot.clean()
            if nextpos() not in cleaned:
                moved = move()
            else:
                moved = False
            
            if not moved and crdir < 3:
                turnright()
            elif not moved and crdir == 3:
                if len(path) == 0:
                    break
                comeback()
            elif moved:
                path.append(crdir)
                while crdir != 0:
                    turnright()
        
