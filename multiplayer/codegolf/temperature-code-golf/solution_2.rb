p`dd`.split[1..].map(&:to_i).min_by{|v|[v.abs,-v]}||0