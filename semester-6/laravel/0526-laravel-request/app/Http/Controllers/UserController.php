<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{
    public function profile()
    {
        return response()->json(auth()->user()->toResource());
    }

    public function login(Request $request)
    {
        $userAgent = $request->header('User-Agent');
        $credentials = $request->validate([
            'email' => 'required|email',
            'password' => 'required',
        ]);

        if (auth()->attempt($credentials)) {
            // return a token
            return response()->json([
                'token' => auth()->user()->createToken($userAgent, expiresAt: now()->addDays(7)),
            ]);
        }

        return response()->json(['error' => 'Unauthorized'], 401);
    }

    public function register(Request $request)
    {
        $payload = $request->validate([
            'name' => 'required',
            'email' => 'required|email|unique:users',
            'password' => 'required',
        ]);

        $payload['password'] = Hash::make($payload['password']);

        $user = User::create($payload);

        return response()->json($user->toResource(), status: 201);
    }

    public function logout()
    {
        auth()->logout();

        return response()->json(['message' => 'Successfully logged out']);
    }
}
