<?php
session_start();

require_once (dirname(__FILE__) ."/utils.inc.php");
function checkValidUUID($uuid) {
    $db = connect();
    $sql = "SELECT * FROM users WHERE uuid = :uuid";
    $result = execute($db,$sql,["uuid" => $uuid]);
    if (!$result -> fetchArray()) {
        onError("Invalid UUID", 400);
    }
    $db -> close();
    return true;
}
verifyParams($_GET, ["errorMessage"]);
$messageOnError = $_GET["errorMessage"];
$limit = isset($_GET["limit"])?$_GET["limit"]:1000000;

if (!isset($_SESSION['uuid']) || $_SESSION['uuid'] == null) {
    onError("You are not logged in!", 400);
}
$uuid = $_SESSION["uuid"];
checkValidUUID($uuid);

$db = connect();
$sql = "SELECT `startTime`,`endTime`,`desc`,`scheduleID` FROM schedules WHERE uuid = :uuid
        LIMIT :limit";
$result = execute($db,$sql,["uuid"=> $uuid,"limit"=> $limit]);
$data = [
    "rows" => [],
    "awakeHours" => 0,
];
while ($row = $result -> fetchArray(SQLITE3_ASSOC)) {
    $data["rows"][] = $row;
    $data["awakeHours"] += strtotime($row["endTime"]) - strtotime($row["startTime"]);
}

$db -> close();

onSuccess($data);

if ($data["awakeHours"] <= 0 && sizeof($data['rows'])>0) {
    echo $messageOnError;
}



?>