<?php
$items = [12, 18, 21, 9, 31];
$total = array_sum($items);
echo "Total: " . $total . PHP_EOL;
echo "Average: " . ($total / count($items)) . PHP_EOL;
