%abbrev = (sp=>" ", bS=>"\\", sQ=>"'", nl=>"\n");
print<>=~s/(\d*)(\S+) ?/($abbrev{$2}||$2)x($1||1)/reg