<?php
require_once (dirname(__FILE__) ."/utils.inc.php");
session_start();
$uuid = $_COOKIE["uuid"];
$authToken = $_COOKIE["auth_token"];
if (empty($uuid) || empty($authToken) || $authToken !== $_ENV["ADMIN_CREDS"]) {
    echo "Only Admin can access this page";
}
else {
    $db = connect();
    $sql = "SELECT * FROM users WHERE uuid = :uuid";
    $result = execute($db,$sql,["uuid" => $uuid]);
    $data = $result->fetchArray(SQLITE3_ASSOC);
    if (!$data) {
        echo "Invalid uuid";
    }
    else {
        $_SESSION["uuid"] = $uuid;
    }
    $db -> close();
    echo "Welcome Admin";
}
?>