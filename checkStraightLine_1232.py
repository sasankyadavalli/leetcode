class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        c = coordinates
        if len(c) == 2:
            return True
        i, j = 1, 2
        if (c[1][0]-c[0][0]) == 0:
            return False
        s = (c[1][1]-c[0][1])/(c[1][0]-c[0][0])
        while j < len(coordinates):
            if c[j][0]-c[i][0] == 0:
                return False
            diff = (c[j][1]-c[i][1])/(c[j][0]-c[i][0])
            if (diff != s):
                return False
            
            i +=1
            j += 1
            
        return True