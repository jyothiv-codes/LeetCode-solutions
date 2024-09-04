class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players=[{} for i in range(n)]
        for pair in pick:
            players[pair[0]][pair[1]]=players[pair[0]].get(pair[1],0)+1
        print(players)
        
        win=0
        for i in range(len(players)):
            print(players[i])
            if len(players[i])>0 and max(players[i].values())>i:
                win+=1
            
        return win
        