<?php
session_start();
$uuid = $_SESSION["uuid"];
if (empty($uuid)) {
    echo "Please Login First";
    exit;
} else {
    $url = $_ENV["ADMIN_URL"];
    $data = json_encode(["uuid" => $uuid]);

    $options = [
        "http" => [
            "header"  => "Content-Type: application/json
",
            "method"  => "POST",
            "content" => $data,
        ],
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    echo $result;
}
