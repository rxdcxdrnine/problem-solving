def combinationSum_0(candidates, target):

    graph = {}
    for i, num in enumerate(candidates):
        graph[num] = candidates

    result = []
    def recursive_dfs(v, discovered):
        discovered.append(v)
        
        if sum(discovered) == target:
            if sorted(discovered) not in result:
                result.append(sorted(discovered))
        elif sum(discovered) < target:
            for w in graph[v]:
                discovered = recursive_dfs(w, discovered)
                discovered.pop()
        else:
            pass

        return discovered


    for num in candidates:
        recursive_dfs(num, [])

    return result
