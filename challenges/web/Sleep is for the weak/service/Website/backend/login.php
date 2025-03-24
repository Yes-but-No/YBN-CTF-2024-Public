<?php
session_start();
require_once (dirname(__FILE__) ."/utils.inc.php");
verifyParams($_POST, ["username", "password"]);
$username = $_POST["username"];
$password = $_POST["password"];
$hashed = hash("sha256", $password . SALT);
$db = connect();
$sql = "SELECT uuid,password FROM users WHERE username = :username";
$result = execute($db,$sql,["username" => $username]);
$data = $result->fetchArray(SQLITE3_ASSOC);
if (!$data) {
    onError("Invalid username", 400);
}
if (!hash_equals($data['password'], $hashed)) {
    onError("Invalid password", 400);
}
$uuid = $data['uuid'];
$db -> close();
$_SESSION['uuid'] = $uuid;
onSuccess(['uuid' => $uuid]);





?>