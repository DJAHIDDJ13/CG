n = gets.to_i
tasks = []
n.times do
  j, d = gets.split(" ").collect { |x| x.to_i }
  tasks << [j, j + d]
end
cur_e = 0
count = 0
tasks.sort_by{_2}.each do |s, e|
  if s >= cur_e
      cur_e = e
      count += 1
  end
end

p count
