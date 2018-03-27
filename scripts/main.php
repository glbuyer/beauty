<?php
$matchBinary = '/Users/xiaojiew1/Applications/anaconda3/envs/py36/bin/match';
$imgFilepath = '/Users/xiaojiew1/Projects/beauty/data/ye.png';


$fullCommand = sprintf('%s %s', $matchBinary, $imgFilepath);
// echo $fullCommand;
$matchResult = shell_exec($fullCommand);
$matchResult = json_decode($matchResult, true);
var_dump($matchResult);
?>