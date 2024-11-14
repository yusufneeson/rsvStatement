<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>RESERVED. Mutasi PDF to CSV</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=rubik:400,600" rel="stylesheet" />

    <style>
        * {
            font-family: 'Rubik', sans-serif;
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:svgjs='http://svgjs.dev/svgjs' width='1440' height='560' preserveAspectRatio='none' viewBox='0 0 1440 560'%3e%3cg mask='url(%26quot%3b%23SvgjsMask1000%26quot%3b)' fill='none'%3e%3crect width='1440' height='560' x='0' y='0' fill='%230e2a47'%3e%3c/rect%3e%3cpath d='M474.14 577.75C654.7 562.65 779.36 196.02 1090 195.66 1400.64 195.3 1542.53 410.86 1705.86 414.06' stroke='rgba(51%2c121%2c194%2c0.58)' stroke-width='2'%3e%3c/path%3e%3cpath d='M433.36 641.82C610.07 627.95 709.96 286.17 1040.23 275.17 1370.5 264.17 1490.41 119.63 1647.1 118.37' stroke='rgba(51%2c121%2c194%2c0.58)' stroke-width='2'%3e%3c/path%3e%3cpath d='M67.27 568.57C238.21 515.19 271.77 37.41 532.59 23.97 793.41 10.53 765.24 93.97 997.9 93.97 1230.56 93.97 1345.58 24.17 1463.22 23.97' stroke='rgba(51%2c121%2c194%2c0.58)' stroke-width='2'%3e%3c/path%3e%3cpath d='M609.36 659.44C725.54 631.5 689.37 319.79 944.98 319.11 1200.59 318.43 1443.57 480.36 1616.22 481.51' stroke='rgba(51%2c121%2c194%2c0.58)' stroke-width='2'%3e%3c/path%3e%3cpath d='M157.02 601.44C294.53 580.06 361.44 253 588.27 249.45 815.1 245.9 803.9 319.45 1019.53 319.45 1235.15 319.45 1341.56 249.68 1450.78 249.45' stroke='rgba(51%2c121%2c194%2c0.58)' stroke-width='2'%3e%3c/path%3e%3c/g%3e%3cdefs%3e%3cmask id='SvgjsMask1000'%3e%3crect width='1440' height='560' fill='white'%3e%3c/rect%3e%3c/mask%3e%3c/defs%3e%3c/svg%3e");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .wrapper {
            display: flex;
            justify-content: center;
            margin-top: 20px
        }

        .title_head {
            text-align: center;
            margin: 0;
            padding: 0;
            color: #fff
        }

        .title_desc {
            text-align: center;
            color: #fff
        }

        .up_box {
            border: 2px solid #25568c;
            padding: 40px;
            border-radius: 5px;
        }

        .box {
            margin-top: 40px;
        }

        .form-control {
            color: #fff
        }

        .button {
            background: #25568c;
            outline: none;
            border: none;
            padding: 10px 25px;
            border-radius: 5px;
            color: #ffffff;
            cursor: pointer;
        }

        .foot-title {
            margin: 0;
            background: #1c3a5dc7;
            display: block;
            text-align: center;
            font-size: 9px;
            padding: 10px;
            color: #8094a9;
            font-weight: 400;
            backdrop-filter: blur(3px);
        }

        body {
            margin: 0
        }

        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            z-index: 99;
            background: red;
        }
    </style>
</head>

<body>

    <div class="wrapper">
        <div class="box">
            <h1 class="title_head">Mutasi PDF ke CSV</h1>
            <p class="title_desc">Baru support untuk BCA saja</p>

            <div class="up_box">
                <form method="POST" enctype="multipart/form-data" action="{{ route('rsv.store') }}">
                    @csrf
                    <input type="file" name="rsv" accept="application/pdf" class="form-control">

                    <button type="submit" class="button">KIRIM</button>
                </form>
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
