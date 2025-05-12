<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Symfony\Component\HttpKernel\Exception\BadRequestHttpException;

class UserResourceController extends Controller
{
    public function index()
    {
        return User::all();
    }

    public function store(Request $request)
    {
        throw new BadRequestHttpException('Use /api/auth/login instead.');
    }

    public function show(int $id)
    {
        return User::find($id);
    }

    public function update(Request $request, int $id)
    {
        User::find($id)->update($request->all());
        return response()->json(['message' => 'User updated successfully.']);
    }

    public function destroy(int $id)
    {
        if ($id !== request()->user()->id) {
            throw new BadRequestHttpException('You can only delete yourself.');
        }

        request()->user()->delete();
        return response()->json(['message' => 'User deleted successfully.']);
    }
}
