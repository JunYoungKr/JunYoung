def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(len(computers))]
    visited = [False] * n
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(len(computers)):
        if not visited[i]:
            dfs(graph, i, visited)
            answer +=1
        
    

    return answer