<?php

namespace App\Providers;

use Illuminate\Contracts\Routing\ResponseFactory;
use Illuminate\Support\ServiceProvider;

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
