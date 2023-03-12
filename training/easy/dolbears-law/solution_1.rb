# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = gets.to_i
n60=0.0
all=[]
m.times do
    line = gets.chomp.split.map(&:to_f)
    n60 += 10 + (line.sum - 40) / 7
    all+=line
end
n60 = n60/m
n8 = all.each_slice(2).to_a.select{|n|n.length==2}.map{|n|n.sum+5}.sum / (all.length/2)
puts "%.1f"% [n60]
puts "%.1f"% [n8] unless 5>n60 || n60>30