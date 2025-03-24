<?php

namespace App\Http\Controllers;

use App\Contracts\EventPusher;

class EventController extends Controller
{
    public function __construct(
        private readonly EventPusher $eventPusher,
    )
    {
    }

    public function pushEvent()
    {
        $message = request()->input('message');

        $this->eventPusher->push('events', ['message' => $message]);

        return response()->json(['message' => 'Event pushed!']);
    }
}
