class CriticalConn():
    def __init__(self, serversNum, connections):
        self.ctr = 0
        self.bridges = []
        self.conns = [ [] for i in range(serversNum+1) ] 
        self.ids = [0]*(serversNum+1)
        self.low = [0]*(serversNum+1)
        self.visited = [False]*(serversNum+1)
        for conn in connections:
            self.conns[conn[0]].append(conn[1])
            self.conns[conn[1]].append(conn[0])
        for i in range(1, serversNum+1):
            if not self.visited[i]:
                self.dfs(i, -1)
        if not self.bridges:
            self.bridges.append([])

    def dfs(self, at, parent):
        self.visited[at] = True
        self.ctr+=1
        self.low[at] = self.ids[at] = self.ctr
        for to in self.conns[at]:
            if to == parent:
                continue
            if not self.visited[to]:
                self.dfs(to, at)
                self.low[at]=min(self.low[at], self.low[to])
                if self.ids[at] < self.low[to]:
                    self.bridges.append([at,to])
            else:
                self.low[at]=min(self.low[at], self.ids[to])                

def findCriticalConn(serversNum, connectionsNum, connections):
    crit = CriticalConn(serversNum, connections)
    return crit.bridges
