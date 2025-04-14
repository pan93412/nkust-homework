<?php

namespace App\Providers;

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
        View::composer('example', function (\Illuminate\View\View $view) {
            $view->with('globalVariable', 'This is a global variable from View Composer');
        });
    }
}
