<?php

namespace App\Providers;

use Illuminate\Routing\ResponseFactory;
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
        // normalize result
        $responseFactory->macro('serialized', function (mixed $data, string $status = 'success') {
            return response()->json([
                'data' => $data,
                'status' => $status,
            ]);
        });
    }
}
