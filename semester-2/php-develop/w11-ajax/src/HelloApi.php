<?php

namespace Pan93412\S2PhpW11Ajax;

class HelloApi {
    static function call(): void {
        header("Content-Type", "text/plain");
        echo $_POST["name"]."你好!";
    }
}
