<?php
require_once 'cat.inc.php';
if (!isset($_GET['file'])) {
    die('No file provided');
}
$cat = new Cat($_GET['file']);
$sercat = serialize($cat);
$b64cat = base64_encode($sercat);
echo $b64cat;
?>