<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpKernel\Exception\NotAcceptableHttpException;

class JsonMiddleware
{
    public function handle(Request $request, Closure $next)
    {
        if (!$request->wantsJson()) {
            throw new NotAcceptableHttpException(
                'Please request with HTTP header: Accept: application/json'
            );
        }

        return $next($request);
    }
}
