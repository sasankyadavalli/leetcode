class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....",".." \
             ,".---","-.-",".-..","--","-.","---",".--.","--.-" \
             ,".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        D = dict( zip( string.ascii_lowercase,code ) ) # string.ascii_lowercase returns "abc...xyz"

        s = set()
        for word in words:
			# add the joint of letter (in code format) to a set
            s.add("".join( [ D[letter] for letter in word ] ) )
        return len(s)
