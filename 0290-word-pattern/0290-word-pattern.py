class Solution(object):
    def wordPattern(self, pattern, s):
        x=pattern
        t=s.split()
        if map(x.find,x)==map(t.index,t):
            return True
        return False
