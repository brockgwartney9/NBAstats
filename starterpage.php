<!DOCTYPE html>
<html>
<body>
    <?php include 'header.html'; ?>

    <?php
    $dbpath = __DIR__ . '/DATABASE/nbastats.db';
    $db = new SQLite3($dbpath);

    $query = $db ->query("select * from allstats limit 1");
    $result = $query->fetchArray(SQLITE3_ASSOC);
    if ($result) {
        // Loop through the result and display each column
        foreach ($result as $key => $value) {
            echo "$key: $value<br>";
        }
    } else {
        echo "No results found.";
    }
    ?>

</body>
</html>

