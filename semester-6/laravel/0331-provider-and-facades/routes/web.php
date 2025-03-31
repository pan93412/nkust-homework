<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/riak-test', function (\App\Services\Riak\Connection $connection) {
    return $connection->connect();
});
