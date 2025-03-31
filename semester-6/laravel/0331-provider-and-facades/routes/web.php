<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/riak-test', function (\App\Services\Riak\Connection $connection) {
    return $connection->connect();
});

Route::get('/test-server', function (\App\Contracts\ServerProvider $serverProvider) {
    return $serverProvider->createServer('test');
});

Route::get('/test-downtime', function (\App\Contracts\DowntimeNotifier $downtimeNotifier) {
    return $downtimeNotifier->notify('Test downtime notification');
});
