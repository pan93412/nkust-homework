<?php

namespace App\Services;

final readonly class PodcastParser
{
    public function parse(string $url): array
    {
        return ["url" => $url];
    }
}
