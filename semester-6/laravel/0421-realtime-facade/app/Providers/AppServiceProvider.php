<?php

namespace App\Providers;

use App\Contracts\Publisher;
use App\Services\PublisherService;
use Illuminate\Routing\ResponseFactory;
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
        $responseFactory->macro('success', function (mixed $value, int $status = 200) {
            return response()->json([
                'success' => true,
                'data' => $value
            ], status: $status);
        });

        $responseFactory->macro('error', function (string $message, int $status = 400) {
            return response()->json([
                'success' => false,
                'message' => $message
            ], status: $status);
        });
    }
}
