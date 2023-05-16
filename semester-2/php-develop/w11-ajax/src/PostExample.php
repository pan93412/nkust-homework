<?php

namespace Pan93412\S2PhpW11Ajax;

class PostExample {
    static function dump(): void {
        header("Content-Type", "text/plain");
        var_dump($_POST);
    }
}
