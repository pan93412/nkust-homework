<?php

use App\Services\DemoMessageService;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/demo', function (DemoMessageService $demoMessageService) {
    return $demoMessageService->getMessage();
});

Route::get('/podcast/broadcast', function (App\Services\Transistor $transistor) {
    $url = request()->query('url');
    if (! $url) {
        return response()->json(['error' => 'URL is required'], 400);
    }

    return $transistor->broadcast($url);
});
