<?php
require_once 'cat.inc.php';
if (!isset($_POST['cat'])) {
    die('No file provided');
}
$catdeser = base64_decode($_POST['cat']);

$cat = unserialize($catdeser);
$output = $cat->run();
echo $output;
?>