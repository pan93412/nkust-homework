<?php

namespace App\Providers;

use App\Contracts\EventPusher;
use App\Services\PodcastParser;
use App\Services\RedisEventPusher;
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
        $podcastParser = new PodcastParser();
        $this->app->instance(PodcastParser::class, $podcastParser);

        $this->app->singleton(Transistor::class, function (Application $app) {
            return new Transistor($app->make(PodcastParser::class));
        });

        $this->app->bind(EventPusher::class, RedisEventPusher::class);
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        //
    }
}
