<?php

$conn_string = "host=localhost port=5432 dbname=counter user=postgres password=Hl0olqwv";
$conn = pg_connect($conn_string);

session_start();

if (isset($_SESSION['timesRefreshed'])) {

    $count = $_SESSION['timesRefreshed'];
    $update_query = "UPDATE pagecounter SET count = $count WHERE id = 1;";
    $result = pg_query($conn, $update_query);

    $_SESSION['timesRefreshed'] = $_SESSION['timesRefreshed'] + 1;
} else {
    $_SESSION['timesRefreshed'] = 0;
}

$fetch_query = "SELECT count FROM pagecounter;";
$result1 = pg_query($conn, $fetch_query);
$current_count = pg_fetch_assoc($result1);

echo "times refreshed = ".$current_count['count'];

