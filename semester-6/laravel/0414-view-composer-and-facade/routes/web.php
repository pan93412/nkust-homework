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

Route::get('/api/users/facade', function () {
    return Response::json([
        'message' => 'Hello, World!',
    ]);
});

Route::get('/api/users/helper', function () {
    return response()->json([
        'message' => 'Hello, World!',
    ]);
});

Route::get('/api/cache-demo', function () {
    return Cache::get("api-cached-content", "Not Cached");
});

Route::get('/api/cache-helper-demo', function () {
    return cache('api-cache-helper-content', "Not Cached");
});
