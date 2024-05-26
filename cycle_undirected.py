from collections import deque

INT_MAX = 4294967296


def DFSRec(adj,s,visited,parent):
    visited[s]= True
    
    for u in adj[s]:
        if visited[u]==False:
            if DFSRec(adj,u,visited,s):
                return True 
        elif u!=parent:
            return True 
    
    return False
        
def addEdge(adj,u,v):
    adj[v].append(u)
    adj[u].append(v)
    
def DFS(adj):
    visited= [False]* len(adj)
    
    for i in range(len(adj)):
        
        if(visited[i]==False):
            
            if DFSRec(adj,i,visited,-1):
                return True
    
    return False
                
v = 4 
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,1,2)
addEdge(adj,2,3)
addEdge(adj,0,2)
addEdge(adj,0,3)
dist =[INT_MAX]*v
dist[0]=0

if(DFS(adj)):
    print("Cycle found")
else:
    print("No cycle")