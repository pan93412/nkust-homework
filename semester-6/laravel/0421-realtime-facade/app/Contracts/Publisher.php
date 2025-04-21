<?php

namespace App\Contracts;

use App\Models\Podcast;

interface Publisher
{
    public function publish(Podcast $podcast): void;
}
