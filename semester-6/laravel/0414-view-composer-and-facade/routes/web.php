<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/example', function () {
    return view('example');
});

Route::get('/api/test', function () {
    return Response::serialized([
        'message' => 'Hello, World!',
    ]);
});

Route::get('/api/cache-demo', function () {
    return Cache::get("api-cached-content", "Not Cached");
});
