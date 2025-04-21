<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Facades\App\Contracts\Publisher as PublisherFacade;

class Podcast extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'published_at'
    ];

    public function publish(): void
    {
        $this->update([
            'published_at' => now(),
        ]);

        PublisherFacade::publish($this);
    }
}
