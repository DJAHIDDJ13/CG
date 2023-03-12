# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
require 'prime'

x = gets.to_i
c = gets.to_i
a={}
c.times do
    ai, bi = gets.split(" ").collect { |x| x.to_i }
    div1 = ai.prime_division.sort_by{|n|n[1]}.group_by{|n|n[1]}
    div2 = bi.prime_division.sort_by{|n|n[1]}.group_by{|n|n[1]}
    div1.each {|dictv|
        dictv[1].each {|el1|
            from = el1[0]
            to = div2[el1[1]].map{|v|v[0]};
            a[from] = (a[el1[0]]==nil)?to:a[from]&to
        }
    }
end
b = {}
a.each {|u|
    subset = u[1]
    a.each {|v|
        if(u[0] != v[0] && subset.length > 1)then 
         subset = subset - v[1]
        end
    }
    b[u[0]] = subset
}
p x.prime_division.map{|n|(b[n[0]][0])?b[n[0]][0]**n[1]:n[0]**n[1]}.sum
