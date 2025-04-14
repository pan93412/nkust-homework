<?php


test('return cache if there is one', function () {
    Cache::shouldReceive('get')
        ->with('api-cached-content')
        ->andReturn('Cached Content');

    $response = $this->get('/api/cache-demo');
    $response->assertSee('Cached Content');
});

test('return default if there is no one', function () {
    Cache::clear();

    $response = $this->get('/api/cache-demo');
    $response->assertSee('Not Cached');
});
