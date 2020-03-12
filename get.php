<?php
$email = $_GET["email"];
$dates = $_GET["dates"];
$days = $_GET["days"];
$subject = $_GET["subject"];
$usr = $_GET["usr"];
$pwd = $_GET["pwd"];
$msg = $_GET["msg"];
$command = escapeshellcmd('/home/user/sender/send.py '.$email.' '.$dates.' '.$days.' '.$subject.' '.$usr.' '.$pwd.' '.$msg);
$output = shell_exec($command);
echo $output;
?>
