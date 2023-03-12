points_left = 50 - gets.to_i

# there's probably a better way
s = 0
p (1..4).sum{|t|
    [*1..12, *2..12].repeated_permutation(t).map(&:sum).count(points_left)
}

