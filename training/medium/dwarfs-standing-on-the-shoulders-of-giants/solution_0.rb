graph = {}
graph.default = []
parent = {}
parent.default = []
all_people = []
n = gets.to_i # the number of relationships of influence
n.times do
    x, y = gets.split.map &:to_i
    graph[x] += [y]
    parent[y] += [x]
    all_people += [x,y]
end
all_people.uniq!

def DAG_len(g, c)
    s = g[c]
    if s.size == 0
        return 0
    end

    return s.map{DAG_len(g, _1)}.max+1
end

parents = all_people.select{parent[_1].size == 0}
graph[0] = parents

p DAG_len(graph, 0)