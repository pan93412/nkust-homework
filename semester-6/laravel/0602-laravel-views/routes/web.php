<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;

Route::get('/', function () {
    return view('welcome');
});

// Routes for WelcomeController
Route::get('/greeting', [WelcomeController::class, 'greeting']);
Route::get('/data', [WelcomeController::class, 'data']);
