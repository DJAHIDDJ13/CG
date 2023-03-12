print`tr -d "
"|xxd -b -c1|sed "s/.*: .//;s/ .*//"|tr -d "
"`=~s/(.)\1*/($1?0:"00")." "."0"x length($&)." "/reg=~s!.$!!r