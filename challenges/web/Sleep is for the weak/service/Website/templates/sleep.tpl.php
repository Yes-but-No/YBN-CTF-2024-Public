<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awake Schedule Page</title>
    <link rel="stylesheet" href="static/css/tailwind.min.css">
    <script src = "static/js/utils.js"></script>
</head>
<body class="bg-gray-900 text-white font-sans">
    <!-- Header -->
    <header class="text-center py-10 bg-gradient-to-b from-gray-900 to-gray-800">
        <h1 class="text-4xl font-bold">Welcome to Your Awake Schedule</h1>
        <p class="mt-4 text-lg">Here you can track and share your no-sleep lifestyle.</p>
    </header>

    <!-- Awake Schedule Section -->
    <section class="py-10 px-6 md:px-20 bg-gray-800">
        <h2 class="text-3xl font-semibold mb-8">Your Awake Schedules</h2>

        <!-- Total Time Not Spent Sleeping -->
        <div class="mb-6">
            <p class="text-xl font-bold">Total Time Not Spent Sleeping: <span class="text-blue-500" id = "time">0 hours</span></p>
        </div>

        <!-- Awake Schedules List -->
        <div class="space-y-6" id = "schedule">

        </div>
        <!-- Add Schedule Button -->
        <div class="text-center mt-10">
            <button id="add-schedule" class="p-4 bg-green-600 hover:bg-green-700 rounded text-white font-semibold transition duration-200">Add New Schedule</button>
        </div>
    </section>

    <!-- Share Schedule Button -->
    <section class="text-center py-10 px-6 md:px-20 bg-gray-900">
        <h2 class="text-3xl font-semibold mb-8">Want to Share Your Schedule?</h2>
        <p class="text-lg mb-6">Click the button below to share your no-sleep schedule with the admin and contribute to our sleepless community! Our admin will only look at the first 5 schedules you have.</p>
        <button id = "share" class="p-4 bg-blue-600 hover:bg-blue-700 rounded text-white font-semibold transition duration-200">Share Your Schedule</button>
    </section>

    <!-- Footer -->
    <footer class="text-center py-6 bg-gradient-to-t from-gray-900 to-gray-800">
        <p class="text-sm">&copy; 2024 The No-Sleep Advantage. All rights reserved (or not, because who has time to sleep?).</p>
    </footer>
    <script src = "static/js/sleep.js"></script>
</body>
</html>
