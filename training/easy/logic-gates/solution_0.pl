$n=<>;
$m=<>;
for(1..$n){
    <>=~/ /;
    $s = $';
    chomp($s);
    $bin_num = $s=~y/_-/01/r;
    $sig_len = length($bin_num);
    $in_sig{$`} = eval("0b" . $bin_num)
}
my %operations = (
    AND => sub { $_[0] & $_[1] },
    OR => sub { $_[0] | $_[1] },
    XOR => sub { $_[0] ^ $_[1] },
    NAND => sub { ~($_[0] & $_[1]) },
    NOR => sub { ~($_[0] | $_[1]) },
    NXOR => sub { ~($_[0] ^ $_[1]) },
);

for(<>) {
    /(\S+) (\S+) (\S+) (\S+)/;
    $result = $operations{$2}->($in_sig{$3}, $in_sig{$4});
    $result = sprintf "%0${sig_len}b", $result % (1 << $sig_len);
    print"$1 ", $result=~y/01/_-/r,"\n"
}