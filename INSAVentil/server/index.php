<?php

header('Content-type: image/jpg');

$API_KEY="APPLICATION_KEY";

try {
    $bdd = new PDO('mysql:host=localhost;dbname=DBNAME', 'DB_USER', 'DB_PASS');
} catch(Exception $e) {
    die('Erreur : ' .$e->getMessage());
}

if(isset($_POST['image']) && isset($_POST['time']) && isset($_POST['API_KEY'])) {
    if($_POST['API_KEY']==$API_KEY) {
        insert_image($_POST['image'], $_POST['time']);
    }
}

$data = get_data();
$image = $data['image'];
$time = $data['time'];

$imsrc = base64_decode($image);
$source_image=imagecreatefromstring($imsrc);

$black = imagecolorallocate($source_image, 0, 0, 0);
$string = "Derniere modification " . date("H:i:s", $time);
imagestring($source_image, 5, 440, 585, $string, $black); 

imagejpeg($source_image);
imagedestroy($source_image);

// Image upload
function insert_image($image, $time) {
    global $bdd;
    $req = $bdd->prepare("UPDATE ventil SET image=:image, time=:time");
    $req->bindValue(":image", $image);
    $req->bindValue(":time", $time); 
    $req->execute();
}

// Displaying image
function get_data() {
    global $bdd;
    $req = $bdd->prepare("SELECT * FROM ventil");
    $req->execute(); 
    $row = $req->fetch();
    return $row;
}

?>