<!DOCTYPE html>
<html lang="id">

<!--

 __     _______ _______      __
 \ \   / / ____|  __ \ \    / /
  \ \_/ / (___ | |__) \ \  / /
   \   / \___ \|  _  / \ \/ /
    | |  ____) | | \ \  \  /
    |_| |_____/|_|  \_\  \/    neverending.
                               
                               
Espero que esto te ayude. y que esta historia nunca termine.
-->

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>REFACTORED. BCA, BRI, and Mandiri Converter</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=rubik:400,600" rel="stylesheet" />
    <link rel="stylesheet" href="{{ url('style.css') }}" />
</head>

<body>

    <div class="wrapper">
        <div class="box">
            <h1 class="title_head">Mutasi PDF ke CSV</h1>
            <p class="title_desc">Sudah Support BCA, BRI dan Mandiri (Rek Koran)</p>

            <div class="up_box">
                <form method="POST" enctype="multipart/form-data" action="{{ route('rsv.store') }}">
                    @csrf

                    <div class="bank">
                        <select name="bank" class="form-control" required>
                            <option value="">Pilih Bank</option>
                            <option value="BCA">BCA</option>
                            <option value="BRI">BRI</option>
                            <option value="Mandiri">Mandiri</option>
                        </select>
                    </div>

                    <input type="file" name="rsv" accept="application/pdf" class="form-control" required>

                    <button type="submit" class="button">KIRIM</button>
                </form>
            </div>

            <div>
                @if (Session::has('rsvLink'))
                    <a class="link" href="{{ Session::get('rsvLink') }}">Klik Download CSV</a>
                @endif
            </div>
        </div>
    </div>

    <div class="footer">
        <div class="foot-inside">
            <h3 class="foot-title">Powered On ySRV</h3>
        </div>
    </div>

</body>

</html>
