<?php

use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/me', [UserController::class, 'profile'])
    ->name('user.profile')
    ->middleware('auth:sanctum');

Route::post('/login', [UserController::class, 'login'])
    ->name('user.login');

Route::post('/register', [UserController::class, 'register'])
    ->name('user.register');

Route::post('/logout', [UserController::class, 'logout'])
    ->name('user.logout')
    ->middleware('auth:sanctum');
