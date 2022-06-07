<?php
    require __DIR__ . '/vendor/autoload.php';

    $q = $_GET['q'];
    $client = new GuzzleHttp\Client();

    // Create a POST request
    $response = $client->request(
        'POST',
        'http://localhost:5000',
        ['json' => [
            'text' => $q,]]
    );

// Parse the response object, e.g. read the headers, body, etc.
$body = json_decode($response->getBody());

// Output headers and body for debugging purposes
?>
<!DOCTYPE html>
<html>

<head>
    <title><?=$q?> - Google Search</title>
    <link rel="stylesheet" type="text/css" href="css/search.css" />
</head>

<body>
<div id="header">
    <div id="topbar">

        <h1 id="searchbarimage">
           </h1>
        <div id="searchbar" type="text">

            <input id="searchbartext" type="text" value="<?=$q?>" />
            <button id="searchbarmic">

            </button>
            <button id="searchbarbutton">
                <svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path
                        d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z">
                    </path>
                </svg>
            </button>
        </div>


    </div>
    <div id="optionsbar">
        <ul id="optionsmenu1">

        </ul>


    </div>
</div>
<div id="searchresultsarea">

    <?php foreach($body as $bod){ ?>
        <div class="searchresult">
            <h2><?=$res[$bod[0]-1]['title']?> - <?=$bod[0]?> - <?=$bod[1]?></h2>
            <p><?=$res[$bod[0]-1]['text']?></p>
        </div>
    <?php } ?>





</div>

</body>

</html>