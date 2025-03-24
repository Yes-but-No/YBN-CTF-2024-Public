<?php
require 'vendor/autoload.php';
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
$process = new Process(["list_cat"]);
$files = "";
try{
    $process->mustRun();
    $files = $process->getOutput();
} catch (ProcessFailedException $exception) {
    echo $exception->getMessage();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Cat's PATHway</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #4CAF50;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 1.5em;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        form {
            display: flex;
            flex-direction: column;
        }

        form label {
            margin-top: 10px;
            font-weight: bold;
        }

        form input[type="text"],
        form textarea {
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 100%;
        }

        form button {
            margin-top: 15px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
        }

        form button:hover {
            background-color: #45a049;
        }

        .cat-image-preview {
            margin-top: 20px;
            text-align: center;
        }

        .cat-image-preview img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .cat-love-image {
            text-align: center;
            margin: 20px 0;
        }

        .cat-love-image img {
            max-width: 100%;
            height: 300px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <header>
        A Cat's PATHway
    </header>
    <main>
        <div class="cat-love-image">
            <img src="static/cat.jpg" alt="A cute cat to show my love for cats">
        </div>
        <h2>Submit Your Own Cat Stories!</h2>
        <p>We love all things cats! Use the form below to tell us what types of cats you'd like to see and share your own favorite cats!</p>
        
        <form id="getCat">
            <label for="catSee">What cats would you like to see?</label>
            <input type="text" id="catSee" name="catSee" placeholder="E.g., <?=$files?>.">
            <button type="submit">Send!</button>
        </form>
        <form id="showCat">
            <label for="catShow">What cats would you like to see?</label>
            <input type="text" id="catShow" name="catShow" placeholder="Describe your cat or type">
            <button type="submit">Show!</button>
        </form>
        
        <div id="submissionMessage" style="margin-top: 20px;"></div>
        <div class="cat-image-preview" id="catPreview"></div>
    </main>

    <script>
        document.getElementById('getCat').addEventListener('submit', function(event) {
            event.preventDefault();
            const catSee = document.getElementById('catSee').value;
            fetch(`backend/get_cat.php?file=${catSee}`)
            .then(response => response.text())
            .then(data => {
                const catImagePreview = document.getElementById('catPreview');
                catImagePreview.innerHTML = `Heres a cat for you: ${data}`;
            });
        });

        document.getElementById('showCat').addEventListener('submit', function(event) {
            event.preventDefault();
            const catShow = document.getElementById('catShow').value;
            fetch(`backend/send_cat.php`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `cat=${encodeURIComponent(catShow)}`
            })
            .then(response => response.text())
            .then(data => {
                const submissionMessage = document.getElementById('submissionMessage');
                submissionMessage.innerHTML = `Here's your cat: ${data}`;
            });
        });
    </script>
</body>
</html>