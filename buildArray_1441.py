class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        build_arr = []
        for i in range(n):
            if build_arr == target:
                break
            if i+1 in target:
                res.append("Push")
                build_arr.append(i+1)
            else:
                res.append("Push")
                res.append("Pop")

        return res
