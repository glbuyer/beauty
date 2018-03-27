<?php
$matchBinary = '/root/anaconda3/envs/py36/bin/match';
$imgFilepath = '../data/xiaojie.jpg';


$fullCommand = sprintf('%s --image_file %s', $matchBinary, $imgFilepath);
// echo $fullCommand;
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);

$matchBinary = '/root/anaconda3/envs/py36/bin/match';
$imageUrl = 'https://asset-face-features.glbuyer.com/72c7afac29c1b102b7567231f1a24b20.jpg';


$fullCommand = sprintf('%s --image_url %s', $matchBinary, $imageUrl);
// echo $fullCommand;
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);

?>