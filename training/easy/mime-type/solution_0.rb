n = gets.to_i
q = gets.to_i

mime = (0...n).map{a,b=gets.split;[a.downcase,b]}.to_h
mime.default = "UNKNOWN"

q.times do
    gets.chomp.downcase.match(/\.([^\.]*)$/i)
    puts mime[$1]
end
