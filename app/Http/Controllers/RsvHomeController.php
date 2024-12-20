<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

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
        $name = strtolower($request->bank) . '_' . time() . '_' . preg_replace("/[^A-Za-z0-9._]/", "", str_replace(".pdf", "", $rsv_file->getClientOriginalName())) . '.' . $rsv_file->getClientOriginalExtension();
        $password = !empty($request->password) ? " --paswd " .  $request->password : "";
        if ($rsv_file->move(public_path('rsv0x0ff/files'), $name)) {
            $proc = app()->isLocal()
                ? Process::forever()->path(app_path('../'))
                ->env([
                    'SYSTEMROOT' => getenv('SYSTEMROOT'),
                    'PATH' => getenv("PATH")
                ])
                ->run('C:\Users\yusuf\AppData\Local\Programs\Python\Python38\python.exe conv.py ' . $request->bank . ' ' . public_path('rsv0x0ff/files/' . $name . $password))
                : Process::forever()->run('sudo docker exec python-rsv python /usr/src/app/conv.py ' . $request->bank . ' /usr/src/app/public/rsv0x0ff/files/' . $name . $password);


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
