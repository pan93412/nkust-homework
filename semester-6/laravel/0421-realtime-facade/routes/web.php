<?php

use App\Http\Controllers\PodcastController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/api/test', function () {
    return response()->success([
        'message' => '這是 API 測試',
        'data' => [
            'name' => 'John Doe',
            'age' => 30,
        ],
    ]);
});

Route::get('/composer-test', function () {
    return view('composer-test');
});
