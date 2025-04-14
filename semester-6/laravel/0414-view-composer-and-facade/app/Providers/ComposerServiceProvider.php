<?php

namespace App\Providers;

use App\Http\ViewComposers\ExampleViewComposer;
use Illuminate\Support\Facades\View;
use Illuminate\Support\ServiceProvider;

class ComposerServiceProvider extends ServiceProvider
{
    public function register()
    {
        //
    }

    public function boot()
    {
        View::composer('example', ExampleViewComposer::class);
    }
}
