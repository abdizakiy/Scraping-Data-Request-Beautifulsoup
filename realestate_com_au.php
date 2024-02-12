<?php
include 'simple_html_dom.php'; // You need to include the simple_html_dom library for HTML parsing

$list_price     = [];
$list_address   = [];
$list_idplace   = [];
$list_state     = [];
$list_bed       = [];
$list_parking   = [];
$list_bath      = [];
$list_type      = [];

$headers = [
    'authority' => 'www.realestate.com.au',
    'accept' => 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language' => 'en-US,en;q=0.9',
    'cache-control' => 'max-age=0',
    'referer' => 'https://www.realestate.com.au/rent/in-qld/list-1',
    'sec-ch-ua' => '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile' => '?0',
    'sec-ch-ua-platform' => '"macOS"',
    'sec-fetch-dest' => 'document',
    'sec-fetch-mode' => 'navigate',
    'sec-fetch-site' => 'same-origin',
    'sec-fetch-user' => '?1',
    'upgrade-insecure-requests' => '1',
    'user-agent' => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
];

$params = [
    'activeSort' => 'list-date',
];

$states = ["qld", "nsw", "vic", "sa", "wa", "act", "nt", "tas"];
$idx = 1;

foreach ($states as $state) {
    $page = 1;
    sleep(10);

    for ($i = 0; $i < 10; $i++) {
        $link = "https://www.realestate.com.au/rent/in-" . $state . "/list-" . $page;
        echo "scanning page " . $page . " state " . $state . PHP_EOL;

        for ($j = 0; $j < 10; $j++) {
            $cookie_list = [
                // Add your cookie data here
                // ...
            ];

            $cookie = $cookie_list[array_rand($cookie_list)];
            $req = requests($link, $params, $cookie, $headers);
            $html = str_get_html($req);

            $stores = $html->find('.Card__Box-sc-g1378g-0.iyqwWq.results-card.residential-card');
            echo count($stores) . PHP_EOL;

            if (count($stores) != 0) {
                break;
            }
        }

        echo $req->url . PHP_EOL;

        if (count($stores) == 0) {
            break;
        }

        $page += 1;

        foreach ($stores as $store) {
            $price = $store->find('.property-price', 0)->plaintext;
            $address = $store->find('.residential-card__address-heading', 0)->plaintext;
            $info = $store->find('.Inline__InlineContainer-sc-lf7x8d-0.iuOPWU div div');
            $bed = $info[0]->getAttribute('aria-label');
            $bath = $info[1]->getAttribute('aria-label');
            $parking = isset($info[2]) ? $info[2]->getAttribute('aria-label') : '';
            $id_place = str_replace("action-menu-button-", "", $store->find('.ButtonBase-sc-18zziu4-0.iqtDgx.MoreButton__StyledButton-sc-hk6ggq-0.elVrsd', 0)->getAttribute('id'));
            $type = $store->find('.residential-card__property-type', 0)->plaintext;

            echo $idx . ' ' . json_encode([$id_place, strtoupper($state), $type, $address, $price, $bed, $bath, $parking]) . PHP_EOL;

            $idx += 1;

            $list_idplace[] = $id_place;
            $list_state[] = strtoupper($state);
            $list_address[] = $address;
            $list_price[] = $price;
            $list_bed[] = $bed;
            $list_bath[] = $bath;
            $list_parking[] = $parking;
            $list_type[] = $type;
        }
    }
}

echo 'Saving Data...' . PHP_EOL;
$data = new \stdClass();
$data->columns = ['ID', 'State', 'Type', 'Address', 'Price', 'Bedroom', 'Bathroom', 'Parking'];
$data->data = array_map(null, $list_idplace, $list_state, $list_type, $list_address, $list_price, $list_bed, $list_bath, $list_parking);

$file_name = str_replace('.', '_', parse_url($link, PHP_URL_HOST)) . '.csv';
file_put_contents($file_name, json_encode($data, JSON_PRETTY_PRINT));

echo 'Data Saved.' . PHP_EOL;

function requests($url, $params, $cookie, $headers)
{
    $options = [
        'http' => [
            'header' => "Cookie: " . http_build_query($cookie, '', '; ') . "\r\n" .
                "User-Agent: " . $headers['user-agent'] . "\r\n" .
                "Referer: " . $headers['referer'] . "\r\n" .
                "Accept: " . $headers['accept'] . "\r\n" .
                "Accept-Language: " . $headers['accept-language'] . "\r\n",
        ],
    ];

    if ($params) {
        $url .= '?' . http_build_query($params);
    }

    $context = stream_context_create($options);
    return file_get_contents($url, false, $context);
}
?>
