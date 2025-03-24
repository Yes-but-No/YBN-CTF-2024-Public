<!-- Yes i chatgpted some of the frontend. I'm sleep deprived ok -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The No-Sleep Advantage</title>
    <link rel="stylesheet" href="static/css/tailwind.min.css">
</head>
<body class="bg-gray-900 text-white font-sans">
    <!-- Header -->
    <header class="text-center py-10 bg-gradient-to-b from-gray-900 to-gray-800 h-screen flex flex-col justify-center">
        <h1 class="text-6xl font-bold">Sleep is for the weak</h1>
        <p class="mt-4 text-2xl">Sleep? Whats that?</p>
        <div class="mt-8">
            <!-- Add your own header image here -->
            <img src="static/sleep.png" alt="Sleep bad" class="mx-auto rounded-lg shadow-lg" width = "300">
        </div>
    </header>

    <section class="py-16 bg-gradient-to-b from-gray-800 to-gray-700 flex flex-row justify-center align-middle h-screen items-center px-40">
        <h2 class="text-5xl font-semibold mb-6 flex justify-center align-middle items-center w-9/12">Did you know that 100% of people who sleep die?</h2>
        
        <div class="mt-8 flex w-full justify-center flex-col items-center gap-4">
            <p class="text-lg leading-relaxed w-8/12">
                According to research conducted by the Anti-Sleep Association, 100% of the people who have said they sleep in their lives have died.
                <br> Additionally, 100% of the people who have died, have slept at least once in their lives. Coincidence? We think not.
            </p>
            <!-- Add your own image for Section 1 here -->
            <img src="static/gravestone.png" alt="death Image" class="mx-auto rounded-lg" width = "100">
        </div>
    </section>

    <section class="py-16 bg-gradient-to-t from-gray-800 to-gray-700 flex flex-row-reverse justify-center align-middle h-screen items-center px-40">
        <h2 class="text-5xl font-semibold mb-6 flex justify-center align-middle items-center w-9/12">Why be active for just 16 hours of the day, when you can use all 24?</h2>
        
        <div class="mt-8 flex w-full justify-center flex-col items-center gap-4">
            <p class="text-lg leading-relaxed w-8/12">
                Approximately 1/3 of a human's life is spent sleeping. 
                <br> Why waste that time when you could be doing something productive?
                <br> like procrastinating the work you have to do!
            </p>
            <!-- Add your own image for Section 1 here -->
            <img src="static/productivity.png" alt="death Image" class="mx-auto rounded-lg" width = "100">
        </div>
    </section>

    <!-- Call to Action Section -->
    <section class="py-16 px-6 md:px-20 bg-gradient-to-t h-screen justify-center items-center flex-col flex from-gray-700 to-gray-800">
        <h2 class="text-5xl text-center font-semibold mb-8">Join the No-Sleep Club</h2>
        <p class="text-lg mb-8 text-center">Ready to embrace the sleepless lifestyle? Click below and flex your lack of sleep with our sleepless admin!</p>
        <div class="text-center">
            <!-- Add your own call-to-action image here -->
            <img src="static/flex.png" alt="Call to Action Image" class="mx-auto rounded-lg shadow-lg mb-8">
            <a href="?page=signup" class="inline-block p-4 bg-blue-600 hover:bg-blue-700 rounded text-white font-semibold transition duration-200">Sign Up Now</a>
        </div>
    </section>

    <!-- Footer -->
     <!-- Yea dont know why chatgpt cooked this footer -->
    <footer class="text-center py-6 bg-gray-900">
        <p class="text-sm">&copy; 2024 The No-Sleep Advantage. All rights reserved (or not, because who has time to sleep?).</p>
    </footer>
</body>
</html>
