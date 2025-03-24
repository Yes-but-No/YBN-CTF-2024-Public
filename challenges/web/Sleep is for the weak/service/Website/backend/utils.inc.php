<?php
define("SALT",$_ENV["SALT"] ?? "default_salt");  

// Function to bind parameters for SQLite3 prepared statements
function bindParams(SQLite3Stmt $stmt, array $params) {
    foreach ($params as $key => $value) {
        // Determine the type of value and bind accordingly
        if (is_int($value)) {
            $stmt->bindValue(':' . $key, $value, SQLITE3_INTEGER);
        } elseif (is_float($value)) {
            $stmt->bindValue(':' . $key, $value, SQLITE3_FLOAT);
        } elseif (is_null($value)) {
            $stmt->bindValue(':' . $key, $value, SQLITE3_NULL);
        } else {
            $stmt->bindValue(':' . $key, $value, SQLITE3_TEXT);
        }
    }
}

function verifyParams($POSTGET, $expected): bool {
    foreach($expected as $key){
        if(!isset($POSTGET[$key])){
            onError('Missing parameter: ' . $key, 400);
            return false;
        }
    }
    return true;

}
function connect(): SQLite3 {
    try {
        $conn = new SQLite3("/var/www/private/users.db");
        return $conn;
    } catch (Exception $e) {
        onError($e->getMessage(), 500);
        exit();
    }
}

function execute(SQLite3 $conn,string $sql,array $params): SQLite3Result {
    try{
        $stmt = $conn->prepare($sql);
        bindParams($stmt, $params);
        return $stmt->execute();
    } catch (Exception $e) {
        onError($e->getMessage(), 500);
        exit();
    }
}

function onError(string $error, int $code) {
    http_response_code($code);
    echo json_encode(["error" => $error]);
    exit();
}

function onSuccess(array $data) {
    echo json_encode($data);
}

function generateUuidV4() {
    $data = random_bytes(16);
    $data[6] = chr(ord($data[6]) & 0x0f | 0x40); // Set version to 0100
    $data[8] = chr(ord($data[8]) & 0x3f | 0x80); // Set bits for variant 1
    return vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex($data), 4));
}

function isValidDateTime($datetime) {
    // Try to parse the string using strtotime
    $timestamp = strtotime($datetime);

    // If strtotime returns false or null, it is not valid
    if ($timestamp === false || $timestamp === null) {
        return false;
    }

    // Validate further by checking if the formatted string matches the input
    $formatted = date('Y-m-d H:i:s', $timestamp);
    return $formatted === date('Y-m-d H:i:s', strtotime($formatted));
}
?>