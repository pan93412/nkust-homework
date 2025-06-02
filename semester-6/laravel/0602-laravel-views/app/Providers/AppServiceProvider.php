<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\View;
use App\View\Composers\UserCountComposer;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        // Register the UserCountComposer for the greeting view
        View::composer('greeting', UserCountComposer::class);
        
        // Share app name with all views
        View::share('appName', config('app.name'));
    }
}
