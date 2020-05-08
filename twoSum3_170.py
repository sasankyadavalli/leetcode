class TwoSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.ht:
            self.ht[number] += 1
        else:
            self.ht[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        h = self.ht
        for n in h:
            if value-n in h and (value - n != n or h[n] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)