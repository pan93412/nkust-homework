<?php

namespace App\Http\Controllers;

class CsrfFormController extends Controller
{
    public function index()
    {
        return view('csrf-form');
    }

    public function store()
    {
        $name = request()->name;
        return "Stored name: $name";
    }
}
