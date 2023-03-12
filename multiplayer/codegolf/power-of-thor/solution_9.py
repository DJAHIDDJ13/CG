a,b,u,v=map(int,input().split())
o,s=u,v
sign=lambda z:1if z>0 else(-1 if z<0 else 0)
while a-u or b-v:
 u,v=u+sign(a-u),v+sign(b-v)
 print({'1,1':'SE','-1,1':'NE','1,-1':'SW','-1,-1':'NW','0,1':'E','0,-1':'W','1,0':'S','-1,0':'N'}[f'{v-s},{u-o}'])
 o,s=u,v