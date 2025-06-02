<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ $appName }}</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 2rem;
        }
        header {
            background: #4a69bd;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        .content {
            background: #fff;
            padding: 2rem;
            margin-top: 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #4a69bd;
            padding: 1rem;
            margin: 1rem 0;
        }
        footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem 0;
            background: #333;
            color: #fff;
        }
    </style>
</head>
<body>
    <header>
        <h1>{{ $appName }}</h1>
    </header>
    
    <div class="container">
        <div class="content">
            <h2>{{ $message }}</h2>
            
            <div class="info-box">
                <p>Current active users: <strong>{{ $userCount }}</strong></p>
                <p>Current time: <strong>{{ now() }}</strong></p>
            </div>
        </div>
    </div>
    
    <footer>
        <p>&copy; {{ date('Y') }} Laravel Views Demo</p>
    </footer>
</body>
</html>
