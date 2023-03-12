main(){
int y,x,p,e[99];scanf("%*d%*d%*d%d%d%*d%*d%d",&y,&x,&p);
e[y]=x;while(p--)scanf("%d%d",&y,&x),e[y]=x;
while(1){char d[9];
scanf("%d%d%s",&y,&x,d);
puts((*d-'R'&&x>=e[y]||*d-'L'&&x<=e[y])?"WAIT":"BLOCK");}}