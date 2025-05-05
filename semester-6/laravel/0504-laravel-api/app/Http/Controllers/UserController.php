<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Support\Facades\Route;

class UserController extends Controller
{
    public function index()
    {
        return response()->json([
            'users' => User::all(),
        ]);
    }

    public function show(User $user)
    {
        return response()->json([
            'user' => $user,
        ]);
    }
}
