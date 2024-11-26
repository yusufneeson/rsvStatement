<!DOCTYPE html>
<html lang="id">

<!--

 __     _______ _______      __
 \ \   / / ____|  __ \ \    / /
  \ \_/ / (___ | |__) \ \  / /
   \   / \___ \|  _  / \ \/ /
    | |  ____) | | \ \  \  /
    |_| |_____/|_|  \_\  \/    neverending.
         @yusufneeson
                               
Espero que esto te ayude. y que esta historia nunca termine.
-->

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>FINAL. BCA, BRI, and Mandiri Converter</title>

    <meta name="description" content="Konversikan dari mutasi bank ke CSV, memudahkan untuk rekap data, semoga membantu">
    <meta name="author" content="YSRV">

    <link rel="apple-touch-icon" sizes="57x57" href="/favicon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/favicon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/favicon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/favicon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/favicon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/favicon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/favicon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/favicon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-180x180.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
    <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="/favicon-144x144.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=rubik:400,600" rel="stylesheet" />
    <link rel="stylesheet" href="{{ url('style.css') }}" />
</head>

<body>

    <div class="wrapper">
        <div class="box">
            <h1 class="title_head">Mutasi PDF ke CSV</h1>
            <p class="title_desc">Sudah Support BCA, BRI dan Mandiri (Rek Koran & e-Statement)</p>

            <div class="up_box">
                <form method="POST" enctype="multipart/form-data" action="{{ route('rsv.store') }}">
                    @csrf

                    <div class="bank">
                        <select name="bank" class="form-control" required>
                            <option value="">Pilih Bank</option>
                            <option value="BCA">BCA</option>
                            <option value="BRI">BRI</option>
                            <option value="Mandiri">Mandiri</option>
                            <option value="MandiriPasswd">Mandiri e-Statement</option>
                        </select>
                    </div>
                    <div class="password">
                        <label>Password PDF</label>
                        <input type="password" name="password" class="form-control">
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

    <script>
        const bankSelect = document.querySelector("[name='bank']")
        const divPass = document.querySelector(".password")
        const password = document.querySelector("[name='password']")

        bankSelect.addEventListener("change", function(e) {
            console.log(bankSelect.value)
            if (bankSelect.value == "MandiriPasswd") {
                divPass.classList.add("show");
                password.required = true;
            } else {
                divPass.classList.remove("show");
                password.required = false;
            }
        })
    </script>

</body>

</html>
