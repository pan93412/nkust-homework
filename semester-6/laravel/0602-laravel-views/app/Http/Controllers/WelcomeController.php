<?php

namespace App\Http\Controllers;

class WelcomeController extends Controller
{
    /**
     * Show the greeting view
     */
    public function greeting()
    {
        return view('greeting', [
            'message' => 'Welcome to Laravel Views Demo!'
        ]);
    }

    /**
     * Return JSON data
     */
    public function data()
    {
        return [
            'name' => 'Laravel Views Demo',
            'version' => '1.0',
            'timestamp' => now()
        ];
    }
}
