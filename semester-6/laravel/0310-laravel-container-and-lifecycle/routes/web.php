<?php

use App\Services\DemoMessageService;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/demo', function (DemoMessageService $demoMessageService) {
    return $demoMessageService->getMessage();
});
