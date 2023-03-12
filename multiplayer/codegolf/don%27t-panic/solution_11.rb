STDOUT.sync=true
n,_,_,y,x,_,_,q=gets.split.map(&:to_i)
e=[0]*n
e[y]=x
q.times{|n|a,b=gets.split.map(&:to_i);e[a]=b}
loop.each{|n|u,v,d=gets.split;u=u.to_i;v=v.to_i;puts ((e[u]<v&&d=='RIGHT')||(e[u]>v&&d=='LEFT'))?'BLOCK':'WAIT'}