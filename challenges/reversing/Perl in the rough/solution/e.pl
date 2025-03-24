use strict;
use warnings;
use POSIX;
my(%O1111O0) = ('a', sub {
    return $_[0] + $_[1];
}
, 's', sub {
    return $_[0] - $_[1];
}
, 'm', sub {
    return $_[0] * $_[1];
}
, 'd', sub {
    return $_[0] / $_[1];
}
);
my(%IO0l1IO1I) = ('+', 'a', '-', 's', '*', 'm', '/', 'd');
my $o0Il0l0I0 = '76358m75s';
my $oOllIIO = '';
sub IoooOll {
    my $O1lll = shift();
    return $O1lll =~ /^\d+(\.\d+)?$/;
}
my(@lOoII100lO, $Il0lO0l0o);
my $lIIOI = 0;
while ($lIIOI == 0) {
    print '>> ';
    chomp(my $ll0lO1O = readline STDIN);
    my @IOl0lo1 = split(' ', $ll0lO1O, 0);
    foreach my $oI1olll0I11 (@IOl0lo1) {
        if (IoooOll $oI1olll0I11) {
            $oOllIIO .= $oI1olll0I11;
            push @lOoII100lO, $oI1olll0I11 + 0;
        }
        elsif ($oI1olll0I11 =~ m[[+\-/*]]) {
            my $OO0Ol = pop @lOoII100lO;
            my $ll1ll = pop @lOoII100lO;
            if (defined $OO0Ol and defined $ll1ll) {
                $Il0lO0l0o = $O1111O0{$IO0l1IO1I{$oI1olll0I11}}($OO0Ol, $ll1ll);
                $oOllIIO .= $IO0l1IO1I{$oI1olll0I11};
                print "$OO0Ol $ll1ll $oI1olll0I11 = $Il0lO0l0o. ";
                push @lOoII100lO, $Il0lO0l0o + 0;
            }
        }
        elsif ($oI1olll0I11 == 'exit') {
            $lIIOI = 1;
            last;
        }
    }
    print "\n";
}
continue {
    if ($oOllIIO eq $o0Il0l0I0) {
        if ($Il0lO0l0o == -27133) {
            my $oO1oIIIo1 = qq[4;j\cPs\1776\cK"i.s**'?6u0\$f}\cK\177h-\a5r"x\177cqt}hhzjkg"0+-7<7?j\cPs\1776\cK"i.stf\ahs!\cP.~5y# f!i\cK!6-~d`\cR!u\cK\cE:|h\0366n{\cR!t{\cE:yj\0366kw\cR!t|\cE:yl\0366nv\cR!pw\cE:y`\0366ks\cR!u\cO\cE:yj\0366n\cA\cR!v~\cE:xk\0366oq\cR!u{\cE:xo\0366os\cR!uz\cE:x\034\0366lz\cR!t\cH\cE:|i\0366n\cA\cR!v\cK\cE:x\037\0366nu\cR!t|\cE:yl\0366mt\cR!uw\cE:yh\0366ow\cR!u}\cE:y\034\0366o\a\cR!t\cH\cE:y`\0366k\cC\cR!t{\cE:}\e\0366nq\cR!t~{y# f\a5\r\cAi-~5rs{\0366o\a\cR!v\cH\cE:{\035\0366oq\cR!t|\cE:yl\0366nv\cR!t\cK\cE:xi\0366ov\cR!p\cH\cE:x\034\0366o\cD\cR!p\f\cE:|o\0366n{\cR!t{\cE:yi\0366or\cR!u}\cE:yl\0366op\cR!p{\cE:|\034\0366op\cR!p\cO\cE:x\034\0366l\cA\cR!t\cK\cE:x\037\0366ns\cR!t{\cE:xk\0366nw\cR!uz\cE:xa\0366op\cR!pw\cE:yl\0366j\a\cR!uz\cE:}\035\0366o\a\cR!t\cH\cE:|h\0366n\cAlb/7}\r\177\cV\cK\cA\cV-!6rs{\0366m{\cR!p\r\cE:x\cX\0366jv\cR!p{\cE:|\e\0366nr\cR!p\f\cE:xo\0366k\cC\cR!t{\cE:|\e\0366m\cC\cR!p\r\cE:}k\0366m\000\cR!qy\cE:xo\0366np\cR!u\n\cE:z\e\0366nu\cR!qw\cE:zk\0366o\cC\cR!q\cO\cE:y\cZ\0366n\000\cR!u{\cE:|\e\0366m\cA\cR!pz\cE:z\cX\0366oz\cR!w\cO\cE:z\034\0366ks\cR!qw\cE:{a\0366j{\cR!tz\cE:|n\0366ou\cR!t{\cE:}\cZ\0366oslb/7}\r\ai."\cVr!i\177"<,)-*f}-~\cP-!6rge.+7%:1jj\cP.\cA\cVr!i.~p}"<,)-*f}-~\cP-!6rgc.+7%:1jj\cP.\cA\cVr!i.~py# f!hr\a6s\1775r~h\177l{y(60f4;j5r\cAhr~i.~dru}.~\cVs~ir"i~j\cV\cK~5.\cAi-~bf"i\r\177ir~5rerk5}-\177i\cK!hs"ir\177w\177-10f60*q1;;1:+jj6r\a6-!inj5r\cAhr~i.~usgp\034!+&f*7,*6<qf\a5\r\cAi-~5rb}.~\cVs~ir"in\177pkg\$/7}\r!h.\a6\177l{y(60f4;j5r\cAhr~i.~dru}.~\cVs~ir"i~j\cV\cK~5.\cAi-~bf"i\r\177ir~5rerk5}\r!h.\a6ls:*<q-<=j=, =-0f}\r\177\cV\cK\cA\cV-!6rb}.~\cVs~ir"in\177pk\cP60*q1;;1:+jj6s~\cP-\177h.~isb}.~\cVs~ir"in\177pkg\$2<0,:{f\cA6s"\cP-l];
            print 'Oop, whats here... ';
            $oO1oIIIo1 = I0OO0O1($oO1oIIIo1);
            $oO1oIIIo1 = eval "sub{ $oO1oIIIo1 }";
            &$oO1oIIIo1($Il0lO0l0o);
        }
    }
}
sub I0OO0O1 {
    my $oOllOlll = $_[0];
    my $o1oOlo = 'YBN';
    if ($lOoII100lO[0] != -27133) {
        exit;
    }
    my $I0lOI011O0 = length $oOllOlll;
    my $Io0o1 = '';
    for (my $llI11o10O0l = 0; $llI11o10O0l < $I0lOI011O0; ++$llI11o10O0l) {
        $Io0o1 .= chr(ord substr($oOllOlll, $llI11o10O0l, 1) ^ ord substr($o1oOlo, $llI11o10O0l % 3, 1));
    }
    return $Io0o1;
}
