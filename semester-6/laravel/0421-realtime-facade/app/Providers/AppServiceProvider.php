<?php

namespace App\Providers;

use App\Contracts\Publisher;
use App\Services\PublisherService;
use Illuminate\Contracts\Routing\ResponseFactory;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        $this->app->bind(Publisher::class, function ($app) {
            return new PublisherService();
        });
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(ResponseFactory $responseFactory): void
    {
        $responseFactory->macro('success', function (mixed $value) {
            return [
                'success' => true,
                'data' => $value,
            ];
        });
    }
}
