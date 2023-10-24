<?php

namespace App\Exceptions;

class MissingParameter extends HttpError
{
    public function __construct(public string $parameter)
    {
        parent::__construct("Missing parameter: $this->parameter", 400);
    }
}
