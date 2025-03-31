<?php

namespace App\Services;

use App\Contracts\DowntimeNotifier;

class PingdomDowntimeNotifier implements DowntimeNotifier
{
    public function notify(string $message): string
    {
        return "Sending downtime notification: {$message}";
    }
}
