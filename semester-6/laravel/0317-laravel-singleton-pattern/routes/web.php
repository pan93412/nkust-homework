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

Route::get('/is-singleton', function () {
    $firstInstance = app(\App\Services\PodcastParser::class);
    $secondInstance = app(\App\Services\PodcastParser::class);

    $instanceHash = spl_object_hash($firstInstance);

    return response()->json(['is_singleton' => $firstInstance === $secondInstance, 'instance_hash' => $instanceHash]);
});

Route::get('/push-event', [\App\Http\Controllers\EventController::class, 'pushEvent']);
