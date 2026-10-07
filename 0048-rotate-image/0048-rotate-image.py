class Solution:
    def rotate(self, a: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(a)
        for i in range(n):
            for j in range(i):
                a[i][j],a[j][i]=a[j][i],a[i][j]
        for i in range(n):
            a[i].reverse()