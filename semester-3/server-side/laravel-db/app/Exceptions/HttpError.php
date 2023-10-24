<?php

namespace App\Exceptions;

/**
 * HttpError represents a Throwable with additional HTTP status code.
 */
interface HttpErrorThrowable extends \Throwable
{
    public function getStatusCode(): int;
}

class HttpError extends \Error implements HttpErrorThrowable {
    public function getStatusCode(): int
    {
        return $this->code;
    }
}
