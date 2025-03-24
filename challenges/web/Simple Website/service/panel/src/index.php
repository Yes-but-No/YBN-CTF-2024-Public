<!DOCTYPE html>
<html>
<head>
    <title>Simple CTF Challenge</title>
</head>
<body>
    <h1>Welcome to the Simple CTF Challenge</h1>
    <p>Can you find the flag?</p>

    <?php
    if(isset($_GET['page'])) {
        $page = $_GET['page'];
        // Vulnerable include - allows LFI
        include($page);
    }
    ?>

    <div>
        <a href="?page=home.php">Home</a> |
        <a href="?page=about.php">About</a>
    </div>
</body>
</html>
