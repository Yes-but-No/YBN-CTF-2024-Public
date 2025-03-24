<?php
session_start();
require_once (dirname(__FILE__) ."/utils.inc.php");
verifyParams($_POST, ["username", "password"]);
$db = connect();
$username = $_POST["username"];
$password = $_POST["password"];
$hashed = hash("sha256", $password . SALT);
$sql = "SELECT * FROM users WHERE username = :username";
$result = execute($db,$sql,["username" => $username]);
if ($result -> fetchArray()) {
    onError("Username already exists", 400);    
}

$uuid = generateUuidV4();
$sql = "INSERT INTO users (uuid, username, password) VALUES (:uuid, :username, :password)";
execute($db,$sql,["username"=> $username, "password"=> $hashed, "uuid"=> $uuid]);
$db -> close();
$_SESSION["uuid"] = $uuid;
onSuccess(data: ["uuid"=>$uuid]);


?>