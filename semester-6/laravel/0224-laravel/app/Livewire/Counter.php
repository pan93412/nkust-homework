<?php

namespace App\Livewire;

use Livewire\Component;

class Counter extends Component
{
    public $count = 1;

    public function increment(): void
    {
        $this->count++;
    }

    public function decrement(): void
    {
        $this->count--;
    }

    public function increment2(): void
    {
        $this->count += 2;
    }

    public function decrement2(): void
    {
        $this->count -= 2;
    }

    public function render()
    {
        return view('livewire.counter');
    }
}
