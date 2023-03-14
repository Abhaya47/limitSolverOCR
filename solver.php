<?php
$latex=($_POST['changedLatex']);
$latex=base64_encode($latex);
echo(exec("python solver.py $latex"));
