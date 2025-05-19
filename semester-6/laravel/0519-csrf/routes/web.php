<?php

use App\Http\Controllers\CsrfFormController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/csrf-form', [CsrfFormController::class, 'index'])->name('csrf-form');
Route::post('/csrf-form', [CsrfFormController::class, 'store'])->name('csrf-form.store');

Route::match(['get', 'post'], '/webhook/test', function () {
    return 'webhook tested!';
});
