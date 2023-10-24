<?php

namespace App\Http\Controllers;

use App\Exceptions\MissingParameter;
use App\Exceptions\NoSuchItem;
use App\Http\Requests\StoreStudentRequest;
use App\Http\Requests\UpdateStudentRequest;
use App\Models\Student;
use Illuminate\Support\Facades\Request;

class StudentController extends Controller
{
    /**
     * Return the students list.
     *
     * @returns array<Student>
     */
    public function index()
    {
        return Student::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreStudentRequest $request)
    {
        $student = Student::create([
            'name' => $request->input('name'),
            'addr' => $request->input('addr'),
            'birth' => $request->input('birth'),
        ]);

        return response()->json($student, 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return StudentController::findOrFail($id);
    }

    protected static function findOrFail(string $id): Student
    {
        return Student::find($id) ?? throw new NoSuchItem("student", $id);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateStudentRequest $request, string $id)
    {
        $student = StudentController::findOrFail($id);
        $student->name = $request->input('name', $student->name);
        $student->addr = $request->input('addr', $student->addr);
        $student->birth = $request->input('birth', $student->birth);
        $student->save();

        return $student;
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        $student = StudentController::findOrFail($id);
        $student->delete();
    }
}
