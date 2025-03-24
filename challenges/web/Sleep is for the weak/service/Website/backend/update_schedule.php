<?php
session_start();
require_once(dirname(__FILE__) ."/utils.inc.php");
if (!isset($_SESSION['uuid']) || $_SESSION['uuid'] == null) {
    onError("You are not logged in!", 400);
}

verifyParams($_POST,["scheduleID","endTime","startTime","desc"]);
$scheduleID = $_POST["scheduleID"];
$startTime = $_POST["startTime"];
$endTime = $_POST["endTime"];
$desc = $_POST["desc"];
if (!isValidDateTime($endTime) || !isValidDateTime($startTime) ) {
    onError("Invalid end time", 400);
}

$db = connect();
$sql = "SELECT uuid FROM schedules WHERE scheduleID = :scheduleID";
$result = execute($db,$sql, ["scheduleID"=>$scheduleID]);
$data = $result -> fetchArray(SQLITE3_ASSOC);
if (!$data) {
    onError("Invalid schedule ID", 400);
}

$uuid = $data['uuid'];
if ($uuid != $_SESSION['uuid']){
    onError('You do not have permission to update this schedule.', 400);
}

$sql = 'UPDATE schedules SET endTime = :endTime, startTime = :startTime, desc = :desc WHERE scheduleID = :scheduleID';
$result = execute($db,$sql, ['endTime' => $endTime,'scheduleID'=>$scheduleID, 'desc' => $desc, 'startTime' => $startTime]);
$db -> close();
onSuccess(["message" => "Schedule updated successfully"]);

?>
