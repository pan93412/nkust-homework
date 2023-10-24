<?php

namespace App\Exceptions;

class NoSuchItem extends HttpError
{
    public function __construct(public string $itemName, public string $itemId = "")
    {
        parent::__construct("No such {$itemName} (id: {$itemId}).", 404);
    }
}
