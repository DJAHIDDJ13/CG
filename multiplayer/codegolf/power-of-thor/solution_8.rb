a,b,u,v=gets.split.map(&:to_i)
a-=u;b-=v
loop{(b>0)?(print "S";b-=1):(print "N";b+=1)unless b==0;(a>0)?(print "E";a-=1):(print "W";a+=1)unless a==0;puts}