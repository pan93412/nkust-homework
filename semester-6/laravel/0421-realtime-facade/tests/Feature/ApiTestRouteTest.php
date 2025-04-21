<?php


test('should return 200 in /api/test', function () {
    $response = $this->get('/api/test');
    $response->assertStatus(200);
});

test('should wrap "success: true" in /api/test', function () {
    $response = $this->get('/api/test');
    $response->assertJsonPath('success', true);
});

test('should contain data in /api/test', function () {
    $response = $this->get('/api/test');
    $response->assertJsonIsObject('data');
});
