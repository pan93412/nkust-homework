<?php


test('return cache if there is one', function () {
    Cache::shouldReceive('get')
        ->once()
        ->with('api-cache-helper-content')
        ->andReturn('Cached Content');

    $response = $this->get('/api/cache-helper-demo');
    $response->assertSee('Cached Content');
});

test('return default value if there is no cache', function () {
    Cache::shouldReceive('get')
        ->once()
        ->with('api-cache-helper-content')
        ->andReturn(null);

    $response = $this->get('/api/cache-helper-demo');
    $response->assertSee('Not Cached');
});
