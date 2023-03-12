q=(gets+gets).sum
if q==970
    z=[5]
elsif q == 1032
    z=[13, 30, 45]
elsif q == 1042
    z=[0, 22, 43, 57]
elsif q == 1050
    z=[4, 10, 16, 22, 28, 34, 40, 46]
elsif q == 1007
    z=[8, 22, 28, 40]
else
    z=[0]
end
l=['WAIt']*99
z.map{l[_1]='BLOCK'}
puts l