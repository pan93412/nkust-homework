<?php

namespace App\Services;

use App\Contracts\Publisher;
use App\Models\Podcast;
use Illuminate\Support\Facades\Log;

class PublisherService implements Publisher
{
    public function publish(Podcast $podcast): void
    {
        Log::info('Podcast published', [
            'podcast_id' => $podcast->id,
            'name' => $podcast->name,
            'published_at' => $podcast->published_at,
        ]);
    }
}
