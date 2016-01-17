$con = getCon();
if ($con->connect_error) {
    echo "Database Error";
    $answer = "Datenbankfehler";
} else {
    $prep = $con->prepare("INSERT INTO entries (id, fid, remote, content, src, created) VALUES (NULL, ?, ?, ?, ?, CURRENT_TIMESTAMP);");

    $prep->bind_param('siss', $fid, $i, $content, $src);
    $prep->execute();
    $answer = "Upload erfolgreich. Weiterleitung in 5 Sekunden.<br>Link: <a href=\"$redir\">Zurück</a>";
    apilog("log","successfully uploaded file (web) ".$src);
}
