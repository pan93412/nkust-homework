<?php

namespace App\Services;

use App\Contracts\ServerProvider;

class ServerUtilityProvider implements ServerProvider
{
    public function createServer(string $name): string
    {
        return "server-service-{$name}";
    }
}
