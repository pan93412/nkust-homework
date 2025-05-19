<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class TokenValidationMiddleware
{
    public function handle(Request $request, Closure $next)
    {
        if ($request->header('Authorization') !== 'Token -laravel-') {
            return response('Unauthorized', 401);
        }

        return $next($request);
    }
}
