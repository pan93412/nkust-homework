<?php

namespace App\Services;

final readonly class Transistor
{
    public function __construct(
        private PodcastParser $podcastParser,
    )
    {
    }

    public function broadcast(string $podcast): array
    {
        $parsedPodcast = $this->podcastParser->parse($podcast);

        return ["topic" => "transistor", "@broadcast" => $parsedPodcast];
    }
}
