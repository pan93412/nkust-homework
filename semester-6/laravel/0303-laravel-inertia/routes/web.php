<?php

use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/users/{user?}', [UserController::class, 'show']);

// 播客相關路由
Route::prefix('podcasts')->group(function () {
    Route::get('/', [App\Http\Controllers\PodcastController::class, 'index'])->name('podcasts.index');
    Route::get('/search', [App\Http\Controllers\PodcastController::class, 'search'])->name('podcasts.search');
    Route::get('/{id}', [App\Http\Controllers\PodcastController::class, 'show'])->name('podcasts.show');
    Route::get('/{id}/api', [App\Http\Controllers\PodcastController::class, 'getPodcast'])->name('podcasts.api');
});
