<?php
require '../vendor/autoload.php';
use Symfony\Component\Process\Process;
class Cat {
    public $admin;
    public $name;
    public $command;
    public function __construct($file) {
        $this->command = ["cat", $file];
    }

    public function run(){
        $process = new Process( $this->command);
        $process->run();
        if (!$process->isSuccessful()) {
            echo 'Error output: ' . $process->getErrorOutput() . PHP_EOL;
        }
        return $process -> getOutput();
    }
}

?>