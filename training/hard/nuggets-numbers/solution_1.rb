# using algorithm presented here https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1r27/pdf
# essentially converting the problem into a shortest path
# or a graph diameter problem


# this could be improved to use priority queue
def dijkstra(mat, init = 0)
  v = mat[0].length
  dist = [Float::INFINITY]*v
  prev = [-1]*v
  vertex = [*0...v]
  
  dist[init] = 0
  
  while vertex.length > 0
    u = vertex.min_by{|q|dist[q]}
    vertex -= [u]
    mat[u].each_with_index do |i,j|
      next if i == 0
      alt =  dist[u] + i
      if alt < dist[j]
        dist[j] = alt
        prev[j]  = i
      end
    end
  end

  return dist,prev
end

n = gets.to_i
nugget_portions = (1..n).map{gets.to_i}.sort
nugget_gcd = nugget_portions.reduce(&:gcd)

if nugget_gcd != 1 then
    p -1
else
    a1 = nugget_portions[0]
    # adjacency matrix
    graph = (0...a1).map{[0]*a1}
    for u in (0...a1)
        for v in (0...a1)
            for k in (1...n)
                if (u + nugget_portions[k]) % a1 == v
                    graph[u][v] = nugget_portions[k]
                    break
                end
            end
        end
    end
    all_shortest_paths, prev = dijkstra(graph)
    graph_diameter = all_shortest_paths.max
    p graph_diameter - a1
end