<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\Route;

class UserController extends Controller
{
    public function index()
    {
        return response()->json([
            'message' => 'It works!',
        ]);
    }
}
