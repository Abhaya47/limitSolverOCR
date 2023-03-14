<?php
//use form  
include('form.html');
if($_SERVER['REQUEST_METHOD']=="POST"){
  $target_dir = getcwd().DIRECTORY_SEPARATOR;
// $target_dir = "uploads/";
$target_file = $target_dir . "img.png";
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
  if($check !== false) {
    echo nl2br("File is an image - " . $check["mime"] . ". \n \n");
    $uploadOk = 1;
  } else {
    echo "File is not an image.\n";
    $uploadOk = 0;
  }
}

// Check if file already exists
if (file_exists($target_file)) {
  unlink($target_file);
  $uploadOk = 1;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 700000) {
  echo "Sorry, your file is too large. \n";
  $uploadOk = 0;
}

// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
  echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed. \n";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded. \n";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo nl2br("The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded. \n");
  } else {
    var_dump($_FILES);
    die;
    echo "Sorry, there was an error uploading your file.";
  }
}
include('idk.html');
echo"</br> <p>Uploaded image</p>";
echo"</br>";
$pred_lex=(exec("python run.py img.png"));
echo($pred_lex);
echo"</br>";
echo"</br>";
echo("<form method='post' action='solver.php'>");
echo"<input type='text' value='{$pred_lex}' style='width:100%' name='changedLatex'>";
echo("<input type='submit'>");
echo("</form>");
}
//rm the image
