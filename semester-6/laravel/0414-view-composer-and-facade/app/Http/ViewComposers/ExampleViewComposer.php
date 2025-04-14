<?php

namespace App\Http\ViewComposers;

use Illuminate\View\View;

class ExampleViewComposer
{
    public function compose(View $view): void
    {
        $view->with('globalVariable', 'This is a global variable from View Composer');
    }
}
