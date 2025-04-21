<?php

namespace App\Http\Controllers;

use App\Models\Podcast;

class PodcastController extends Controller
{
    public function list()
    {
        $podcasts = Podcast::all();

        return response()->success($podcasts);
    }

    public function get(Podcast $podcast)
    {
        return response()->success($podcast);
    }

    public function create()
    {
        $name = request()->json('name');
        if (!$name) {
            return response()->error('Name is required', 422);
        }

        $podcast = Podcast::create(['name' => $name]);

        return response()->success([
            'id' => $podcast->id,
        ], 201);
    }

    public function publish(Podcast $podcast)
    {
        if ($podcast->published_at) {
            return response()->error('Podcast already published', 422);
        }

        $podcast->publish();

        return response()->success(['id' => $podcast->id]);
    }
}
