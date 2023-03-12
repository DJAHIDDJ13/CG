main(){
int n,y,x,p,e[99],a,b,u,v;scanf("%d%*d%*d%d%d%*d%*d%d",&n,&y,&x,&p);
e[y]=x;while(p--){scanf("%d%d",&a,&b);e[a]=b;}
while(1){char d[9];
scanf("%d%d%s",&u,&v,d);
printf("%s\n",((*d=='R'&&v<=e[u])||(*d=='L'&&v>=e[u]))?"WAIT":"BLOCK");}}