my $f = shift;
if($f != -(631*43)) {
    return;
}
$f = -$f;
my $s1 = '~!yes%but)y!zs|@bcufatnXo |NowbuFyqes~noy*e;s`';
my $s2 = 'nO]cbutn`d/no+&yep`sub%.b*n\noqebuthb)u>t=no!|';
my $flag='I,j4%+p+f*e+J,2K7fr}Kw9Bj:|{u+L$JhZN!9X9d\'ge<a';
my $l = length($s1) < length($s2) ? length($s1) : length($s2);
my $x_r = "";


for (my $i = 0; $i < $l; $i++) {
    $x_r .= chr(ord(substr($s1, $i, 1)) ^ ord(substr($s2, $i, 1)));
}

my $print_this = "";

for (my $i = 0; $i < $l; $i++) {
    $print_this .= chr(ord(substr($flag, $i, 1)) ^ ord(substr($x_r, $i, 1)));
}
print "$print_this";



#my $shellcode ='my$I11oIl0l=shift;if($I11oIl0l!=-(631*43)){return}$I11oIl0l=-$I11oIl0l;my$o0Iooo0="\x7E\x21\x79\x65\x73\x25\x62\x75\x74\x29\x79\x21\x7A\x73\x7C\x40\x62\x63\x75\x66\x61\x74\x6E\x58\x6F\x20\x7C\x4E\x6F\x77\x62\x75\x46\x79\x71\x65\x73\x7E\x6E\x6F\x79\x2A\x65\x3B\x73\x60";my$IlOO0o0l0="\x6E\x4F\x5D\x63\x62\x75\x74\x6E\x60\x64\x2F\x6E\x6F\x2B\x26\x79\x65\x70\x60\x73\x75\x62\x25\x2E\x62\x2A\x6E\x5C\x6E\x6F\x71\x65\x62\x75\x74\x68\x62\x29\x75\x3E\x74\x3D\x6E\x6F\x21\x7C";my$O1OIOOooo0="\x49\x2C\x6A\x34\x25\x2B\x70\x2B\x66\x2A\x65\x2B\x4A\x2C\x32\x4B\x37\x66\x72\x7D\x4B\x77\x39\x42\x6A\x3A\x7C\x7B\x75\x2B\x4C\x24\x4A\x68\x5A\x4E\x21\x39\x58\x39\x64\x27\x67\x65\x3C\x61";my$OI0llO0o0=length($o0Iooo0)<length($IlOO0o0l0)?length($o0Iooo0):length($IlOO0o0l0);my$o10Io11l001="";for(my$l0O1000l0=0;$l0O1000l0<$OI0llO0o0;$l0O1000l0++){$o10Io11l001.=chr(ord(substr($o0Iooo0,$l0O1000l0,1))^ord(substr($IlOO0o0l0,$l0O1000l0,1)))}my$Oo1lIo="";for(my$l0O1000l0=0;$l0O1000l0<$OI0llO0o0;$l0O1000l0++){$Oo1lIo.=chr(ord(substr($O1OIOOooo0,$l0O1000l0,1))^ord(substr($o10Io11l001,$l0O1000l0,1)))}print"$Oo1lIo"';
