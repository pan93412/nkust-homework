<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\Cache;

class UserController extends Controller
{
    public function showProfile(string $id)
    {
        /**
         * @var array{name: string} $user
         */
        $user = Cache::get("user:$id", ["name" => "Guest user"]);

        return view('profile', [
            'user' => $user,
        ]);
    }
}
