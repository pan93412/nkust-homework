<?php

namespace App\Providers;

use Illuminate\Support\Facades\View;
use Illuminate\Support\ServiceProvider;

class ComposerServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        View::composer('composer-test', function (\Illuminate\View\View $view) {
            $view->with('globalVariable', '這是來自 ComposerServiceProvider 的全域變數');
        });
        //
    }
}
