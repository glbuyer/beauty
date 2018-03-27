<?php
$matchBinary = '/root/anaconda3/envs/py36/bin/match';
$imgFilepath = '../data/xiaojie.jpg';
$imgFilepath = '/var/www/glbuyer_face_features_api_server_test/storage/app/images/customerUpload/5aba318a36594.jpg'
$fullCommand = sprintf('%s --image_file %s', $matchBinary, $imgFilepath);
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);

$matchBinary = '/root/anaconda3/envs/py36/bin/match';
$imageUrl = 'https://asset-face-features.glbuyer.com/72c7afac29c1b102b7567231f1a24b20.jpg';
$fullCommand = sprintf('%s --image_url %s', $matchBinary, $imageUrl);
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);
?>