<?php
session_start();
header("Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self';");
$page = $_GET["page"] ?? "home";
$uuid = $_SESSION["uuid"] ?? null;
switch ($page) {
    case "home":
        include "templates/home.tpl.php";
        break;
    case "login":
        include "templates/login.tpl.php";
        break;
    case "signup":
        include "templates/signup.tpl.php";
        break;
    case "sleep":
        if ($uuid) {
            include "templates/sleep.tpl.php";
        } else {
            header("Location: index.php?page=login");
        }
        break;
    default:
        include "templates/home.tpl.php";
        break;
}
?>