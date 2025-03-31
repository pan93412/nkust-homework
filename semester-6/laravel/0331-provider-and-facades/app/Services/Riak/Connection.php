<?php

namespace App\Services\Riak;

readonly class Connection
{
    public function __construct(
        private array $config,
    )
    {
    }

    public function connect(): string
    {
        return "Connected to Riak with config: " . json_encode($this->config);
    }
}
