<?php

use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/welcome1', function () {
    return "Welcome!!";
});

Route::get('/users', [UserController::class, 'index']);
