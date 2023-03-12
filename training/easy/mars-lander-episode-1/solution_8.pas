// Auto-generated code below aims at helping you parse
// the standard input according to the problem statement.
program Answer;
{$H+}
uses sysutils, classes, math;

// Helper to read a line and split tokens
procedure ParseIn(Inputs: TStrings) ;
var Line : string;
begin
    readln(Line);
    Inputs.Clear;
    Inputs.Delimiter := ' ';
    Inputs.DelimitedText := Line;
end;

var
    surfaceN : Int32; // the number of points used to draw the surface of Mars.
    landX : Int32; // X coordinate of a surface point. (0 to 6999)
    landY : Int32; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    X : Int32;
    Y : Int32;
    hSpeed : Int32; // the horizontal speed (in m/s), can be negative.
    vSpeed : Int32; // the vertical speed (in m/s), can be negative.
    fuel : Int32; // the quantity of remaining fuel in liters.
    rotate : Int32; // the rotation angle in degrees (-90 to 90).
    power : Int32; // the thrust power (0 to 4).
    i : Int32;
    Inputs: TStringList;
begin
    Inputs := TStringList.Create;
    ParseIn(Inputs);
    surfaceN := StrToInt(Inputs[0]);
    for i := 0 to surfaceN-1 do
    begin
        ParseIn(Inputs);
        landX := StrToInt(Inputs[0]);
        landY := StrToInt(Inputs[1]);
    end;

    // game loop
    while true do
    begin
        writeln('0 4');
        writeln('0 3');
        flush(StdErr); flush(output); // DO NOT REMOVE
    end;
end.