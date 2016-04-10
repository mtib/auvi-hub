$con = getCon();
// ...
// data wird vom Nutzer empfangen
$data = "1; DROP TABLE *";
$con->query("SELECT column FROM table WHERE name = $data");
// der Programmierer erwartet einen Namen in Data,
// Data enthält stattdessen einen zweiten Befehl, der
// für einen großen Datenverlust sorgen kann.
