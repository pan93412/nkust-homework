<?php

namespace App\Services;

use Illuminate\Support\Carbon;

final readonly class NowDateHelper
{
    public function getNowTime(): Carbon {
        return now();
    }
}
