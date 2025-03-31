<?php

namespace App\Services;

use App\Contracts\ServerProvider;

class DigitalOceanServerProvider implements ServerProvider
{
    public function createServer(string $name): string
    {
        return "digital-ocean-server-{$name}";
    }
}
