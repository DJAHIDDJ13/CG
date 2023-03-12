loop{
    p (0..7).map{[_1, gets.to_i]}.max_by{_2}[0]
}