<?php

use App\Http\Controllers\PodcastController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/podcasts', [PodcastController::class, 'list'])
    ->name('podcast.list');

Route::post('/podcasts', [PodcastController::class, 'create'])
    ->name('podcast.create');

Route::get('/podcasts/{podcast}', [PodcastController::class, 'get'])
    ->name('podcast.get');

Route::post('/podcasts/{podcast}/publish', [PodcastController::class, 'publish'])
    ->name('podcast.publish');
