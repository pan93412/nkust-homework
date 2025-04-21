<?php

use App\Models\Podcast;
use Facades\App\Contracts\Publisher;
use Illuminate\Foundation\Testing\RefreshDatabase;

uses(RefreshDatabase::class);

test('podcast can be published', function () {
    $podcast = Podcast::factory()->create();

    Publisher::shouldReceive('publish')
        ->once()
        ->with($podcast);

    $podcast->publish();

    $this->assertNotNull($podcast->published_at);
});

test('/api/podcast/:id returns podcast', function () {
    $podcast = Podcast::factory()->create();

    $response = $this->getJson(route('podcast.get', ['podcast' => $podcast]));

    $response->assertOk()
        ->assertJson([
            'data' => [
                'id' => $podcast->id,
                'name' => $podcast->name,
            ],
        ]);
});

test('/api/podcast/:id returns 404 if podcast not found', function () {
    $response = $this->getJson(route('podcast.get', ['podcast' => 999]));

    $response->assertNotFound();
});

test('/api/podcast/:id/publish publishes podcast', function () {
    $podcast = Podcast::factory()->create();

    $response = $this->postJson(route('podcast.publish', ['podcast' => $podcast]));

    $response->assertOk()
        ->assertJson([
            'data' => [
                'id' => $podcast->id,
            ],
        ]);

    $this->assertNotNull($podcast->fresh()->published_at);
});

test('/api/podcast/:id/publish returns 404 if podcast not found', function () {
    $response = $this->postJson(route('podcast.publish', ['podcast' => 999]));

    $response->assertNotFound();
});

test('/api/podcast/:id/publish returns 422 if podcast already published', function () {
    $podcast = Podcast::factory()->create(['published_at' => now()]);

    $response = $this->postJson(route('podcast.publish', ['podcast' => $podcast]));

    $response->assertUnprocessable();
});

test('/api/podcast creates a new podcast', function () {
    $response = $this->postJson(route('podcast.create'), [
        'name' => 'Test Podcast',
    ]);

    $response->assertCreated();

    $this->assertDatabaseHas('podcasts', [
        'name' => 'Test Podcast',
    ]);
});
