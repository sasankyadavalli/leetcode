class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        D = collections.defaultdict(list)
        for student, score in items:
            bisect.insort(D[student], score) # insert in a list in increasing order.
        return [[student, sum(D[student][-5:])//5] for student in D]
