y,x,p,e[99],d;main(){scanf("%*d%*d%*d%d%d%*d%*d%d",&y,&x,&p);for(e[y]=x;p--;scanf("%d%d",&y,&x),e[y]=x);for(;;scanf("%d%d %c%*s",&y,&x,&d),puts(d-82&&x>=e[y]||d-76&&x<=e[y]?"WAIT":"BLOCK"));}