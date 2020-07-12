class Solution:
    def reverseBits(self, n: int) -> int:
        bits = '{:032b}'.format(n)
        reverse_bits = bits[::-1]
        return int(reverse_bits, 2)
