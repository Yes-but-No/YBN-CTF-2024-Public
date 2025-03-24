<?php
session_start();
require_once (dirname(__FILE__) ."/utils.inc.php");
if (!isset($_SESSION['uuid']) || $_SESSION['uuid'] == null) {
    onError("You are not logged in!", 400);
}

verifyParams($_POST,["startTime","desc"]);
$startTime = $_POST["startTime"];
$endTime = $_POST["endTime"];
if (!isValidDateTime($startTime) || !isValidDateTime($endTime)) {
    onError("Invalid start time", 400);
}
$desc = $_POST["desc"];
$uuid = $_SESSION["uuid"];

$db = connect();
$sql = "INSERT INTO schedules (uuid, startTime,endTime, desc) VALUES (:uuid, :startTime,:endTime, :desc)";
$result = execute($db, $sql, ["uuid" => $uuid, "startTime" => $startTime, "desc" => $desc, "endTime" => $endTime]);
// Get the ID of the last inserted row
if (!$result) {
    onError("Error during insertion", 500);
}
$scheduleID = $db -> lastInsertRowID();
$db ->close();
onSuccess(["scheduleID" => $scheduleID]);


?>
