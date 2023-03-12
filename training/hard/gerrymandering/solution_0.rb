width, height = gets.split.map(&:to_i)
districts = (1..height).map{gets.split.map(&:to_i)}

(0...width).each{|w|
  (0...height).each{|h|
    districts[h][w] = 
    ( [ districts[h][w] ] +
    (0...w).map{|i| districts[h][i] + districts[h][w-i-1] } +
    (0...h).map{|i| districts[i][w] + districts[h-i-1][w] } )
    .max
  }
}

p districts.last.last