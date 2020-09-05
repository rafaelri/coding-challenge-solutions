class LCS():
    def __init__(self, s1, s2):
        self.__s1 = s1
        self.__s2 = s2
        self.__h = len(s2)+1
        self.__w = len(s1)+1
        self.__table = self.__lcs(s1,s2)

    def size(self):
        return self.__table[self.__h-1][self.__w-1]

    def occurrences(self):
        return self._occurrences(self.__h-1, self.__w-1, "")

    def _occurrences(self, i, j, s):
        if i == 0 and j == 0:
            return s
        if self._split_pos(i,j):
            return [self._occurrences(i,j-1, s), self._occurrences(i-1,j, s)]
        elif self._diag_add(i,j):
            return self._occurrences(i-1, j-1, self.__s2[i-1]+s)
        else:
            new_i, new_j = self._get_move(i,j)
            return self._occurrences(new_i, new_j, s)

        return self.__table[self.__h-1][self.__w-1]

    def _split_pos(self, i, j):
        return self.__table[i-1][j-1] == self.__table[i][j]-1 and \
                 self.__table[i][j-1] == self.__table[i][j] and \
                 self.__table[i-1][j] == self.__table[i][j]

    def _diag_add(self, i, j):
        return self.__table[i-1][j-1]+1 == self.__table[i][j] and \
                 self.__table[i][j-1] == self.__table[i-1][j-1] and \
                 self.__table[i-1][j] == self.__table[i-1][j-1]

    def _get_move(self, i, j):
        if self.__table[i-1][j] == self.__table[i][j]:
            return i-1,j
        else:
            return i,j-1

    def __lcs(self,s1, s2):
        res = [ [0] * (self.__w) for i in range(self.__h) ]

        for i in range(1,self.__h):
            for j in range(1,self.__w):
                if s1[i-1] == s2[j-1]:
                    res[i][j]=res[i-1][j-1]+1
                else:
                    res[i][j]=max(res[i][j-1], res[i-1][j])

        return res      

print(LCS("ABCD", "ABDC").occurrences())
