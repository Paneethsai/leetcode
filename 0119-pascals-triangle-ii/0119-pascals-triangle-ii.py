class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        val = 1
        
        # Iterate c from 1 to rowIndex
        for c in range(1, rowIndex + 1):
            val = val * (rowIndex - c + 1) // c
            row.append(val)
            
        return row

        