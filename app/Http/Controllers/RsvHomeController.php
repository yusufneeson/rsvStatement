<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;
use Symfony\Component\Process\Process as ProcessProcess;

class RsvHomeController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return view('welcome');
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $rsv_file = $request->file('rsv');
        $name = 'rsv_' . time() . '_pdf_' . '.' . $rsv_file->getClientOriginalExtension();

        if ($rsv_file->move(public_path('rsv0x0ff/files'), $name)) {
            // $proc = new ProcessProcess(['python' . ' ' . app_path('../python/main.py', app_path('../python/' . $name))]);
            $proc = Process::path(app_path('../python'))
                ->env([
                    'SYSTEMROOT' => getenv('SYSTEMROOT'),
                    'PATH' => getenv("PATH")
                ])
                ->run('C:\Users\yusuf\AppData\Local\Programs\Python\Python38\python.exe main.py ' . public_path('rsv0x0ff/files/' . $name));

            // return response()->download(public_path('rsv0x0ff/files/' . $name));

            return back()->with('rsvLink', url('rsv0x0ff/files/' . str_replace('.pdf', '.csv', $name)));
        } else {
            dd('ERROR UPLOAD, refresh halaman ini atau laporkan ke developer bank mandiri');
        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
