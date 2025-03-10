<?php

namespace App\Providers;

use App\Services\PodcastParser;
use App\Services\Transistor;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        $this->app->bind(Transistor::class, function (Application $app) {
            return new Transistor($app->make(PodcastParser::class));
        });
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        //
    }
}
