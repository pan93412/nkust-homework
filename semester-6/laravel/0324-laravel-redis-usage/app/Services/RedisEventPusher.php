<?php

namespace App\Services;

use App\Contracts\EventPusher;
use Illuminate\Support\Facades\Redis;

class RedisEventPusher implements EventPusher
{
    public function push(string $channel, array $data): void
    {
        Redis::publish($channel, json_encode($data));
    }
}
