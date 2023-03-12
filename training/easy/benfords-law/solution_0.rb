# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = gets.to_i
log=[0]*10
n.times do
    transaction = gets.chomp
    log[transaction.scan(/[1-9]/)[0].to_i] +=1
end
ben=[0.0,30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
p log.map{|v|100.0*v/n}.zip(ben).map{|a,b|(a-b).abs>10}.any?
