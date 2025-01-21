<!DOCTYPE html>
<html>
<body>
    <?php include 'header.html'; ?>

    <?php
    $dbpath = __DIR__ . '/DATABASE/nbastats.db';
    $db = new SQLite3($dbpath);

    $query = $db ->query("select * from allstats");
    $result = $query->fetchArray(SQLITE3_ASSOC);
    $query1 = $db -> query("SELECT name FROM PRAGMA_table_info('allstats');");
    //TODO: Reformat Database, Add Filter
    //if ($result) {
        // Loop through the result and display each column
        //foreach ($result as $key => $value) {
           // echo "$key: $value<br>";
       // }
    //} else {
        //echo "No results found.";
    //}
    ?>
    <table id = "playersTable" border = "1">
        <thead>
            <tr>
            <?php
               
                while ($row = $query1 -> fetchArray(SQLITE3_ASSOC)){
                    echo "<th>{$row['name']}</th>";
                }
            ?>
            </tr>
        </thead>
        <?php 
            while ($row = $query -> fetchArray(SQLITE3_ASSOC)){
                echo "<tr>";
                foreach($row as $cell){
                    echo "<td>{$cell}</td>";
                }
                echo "</tr>";
            }

        ?>
    </table>

</body>
</html>

