<?php

namespace App\Contracts;

interface EventPusher
{
    public function push(string $channel, array $data): void;
}
