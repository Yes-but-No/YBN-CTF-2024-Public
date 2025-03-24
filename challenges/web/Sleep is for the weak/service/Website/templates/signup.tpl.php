<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup Page</title>
    <link rel="stylesheet" href="static/css/tailwind.min.css">
    <script src = "static/js/utils.js"></script>
</head>
<body class="bg-gradient-to-b from-gray-900 to-gray-800 text-white flex items-center justify-center min-h-screen">
    <div class="w-full max-w-md bg-gray-800 shadow-lg rounded-lg p-8">
        <h2 class="text-3xl font-semibold text-center mb-6">Create an Account</h2>
        <form id = "form">
            <div class="mb-4">
                <label for="username" class="block text-sm font-medium text-gray-300 mb-2">Username</label>
                <input type="text" id="username" name="username" class="w-full px-4 py-2 border border-gray-600 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div class="mb-6">
                <label for="password" class="block text-sm font-medium text-gray-300 mb-2">Password</label>
                <input type="password" id="password" name="password" class="w-full px-4 py-2 border border-gray-600 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-200">Sign Up</button>
        </form>
        <p class="mt-6 text-center text-sm text-gray-400">
            Already have an account? <a href="?page=login" class="text-blue-400 hover:underline">Log in here</a>.
        </p>
    </div>
    <script src = "static/js/signup.js"></script>
</body>
</html>