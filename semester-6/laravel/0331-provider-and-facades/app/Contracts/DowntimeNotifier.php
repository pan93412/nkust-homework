<?php

namespace App\Contracts;

interface DowntimeNotifier
{
    public function notify(string $message): string;
}
