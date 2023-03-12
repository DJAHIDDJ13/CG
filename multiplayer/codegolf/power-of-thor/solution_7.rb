a,b,u,v=gets.split.map(&:to_i);a-=u;b-=v
loop{r='';b>0?(r+=?S;b-=1):(r+=?N;b+=1)unless b==0;a>0?(r+=?E;a-=1):(r+=?W;a+=1)unless a==0;puts r}