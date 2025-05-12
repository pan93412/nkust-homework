<?php

use App\Http\Controllers\UserController;
use App\Http\Controllers\UserResourceController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::post('/auth/register', [UserController::class, 'register']);
Route::post('/auth/login', [UserController::class, 'authenticate']);
Route::post('/auth/logout', [UserController::class, 'logout'])->middleware('auth:sanctum');

Route::resource('users', UserResourceController::class)->middleware('auth:sanctum');
