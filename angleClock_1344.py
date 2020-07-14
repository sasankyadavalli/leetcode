class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 6     # Scale up minutes [0, 360): 360/60 = 6
        h = (hour%12) * 30  # Hours to [0, 12), then scale up to [0, 360): 360/12 = 30
        h += m / 12         # Adjust hour hand: full rotation of minute hand moves hour hand 1/12th of the circle
        angle = abs(m - h)  # Get rid of the smallest hand by adjusting it to 0. This moves the largest to -smallest
        return angle if angle < 180 else 360 - angle
