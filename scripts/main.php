<?php
$matchBinary = '/root/anaconda3/envs/py36/bin/match';
$imgFilepath = '../data/ye.png';


$fullCommand = sprintf('%s --image_file %s', $matchBinary, $imgFilepath);
// echo $fullCommand;
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);
?>