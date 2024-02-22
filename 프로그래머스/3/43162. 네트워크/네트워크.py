def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    answer = 0

    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)
            answer += 1
    # print(graph)
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
