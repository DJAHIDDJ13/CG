a,b,u,v=gets.split.map(&:to_i);a-=u;b-=v
puts ([b>0??S:?N]*b.abs+[""]*[0,a.abs-b.abs].max).zip([a>0??E:?W]*a.abs+[""]*[0,b.abs-a.abs].max).map(&:join).join("\n")