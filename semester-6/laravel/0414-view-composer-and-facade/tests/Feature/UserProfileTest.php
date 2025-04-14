<?php


test('return "Guest User" if there is no cache', function () {
    Cache::shouldReceive()
        ->with('user:1')
        ->andReturn(null);

    $response = $this->get('/user/1');
    $response->assertSee('Guest user');
});

test('return the username if there is a cache', function () {
    Cache::shouldReceive()
        ->with('user:1')
        ->andReturn(['name' => 'John Doe']);

    $response = $this->get('/user/1');
    $response->assertSee('John Doe');
});
