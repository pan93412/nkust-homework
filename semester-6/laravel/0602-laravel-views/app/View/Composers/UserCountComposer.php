<?php

namespace App\View\Composers;

use Illuminate\View\View;

class UserCountComposer
{
    /**
     * Bind data to the view.
     *
     * @param  \Illuminate\View\View  $view
     * @return void
     */
    public function compose(View $view)
    {
        // In a real application, this would likely come from a database or cache
        // For demonstration purposes, we'll use a random number between 1 and 100
        $userCount = rand(1, 100);
        
        $view->with('userCount', $userCount);
    }
}
