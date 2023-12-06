class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        team=n
        while team!=1:
            if team/2 !=0:
                matches+=(team-1)/2
                team=(team-1)/2 + 1
            else:
                matches+=team/2
                team=team/2

        return ceil(matches)

