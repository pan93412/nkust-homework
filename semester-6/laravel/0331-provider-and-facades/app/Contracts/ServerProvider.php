<?php

namespace App\Contracts;

interface ServerProvider
{
    public function createServer(string $name): string;
}
