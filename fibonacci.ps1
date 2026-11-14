if ($args.Count -ne 1) {
    [Console]::Error.WriteLine("Usage: fibonacci.ps1 <non-negative-integer>")
    exit 2
}

$index = [System.Numerics.BigInteger]::Zero
if (-not [System.Numerics.BigInteger]::TryParse([string]$args[0], [ref]$index)) {
    [Console]::Error.WriteLine("Index must be an integer.")
    exit 2
}
if ($index -lt 0) {
    [Console]::Error.WriteLine("Index must be non-negative.")
    exit 2
}

$previous = [System.Numerics.BigInteger]::Zero
$current = [System.Numerics.BigInteger]::One
$remaining = $index
while ($remaining -gt 0) {
    $next = $previous + $current
    $previous = $current
    $current = $next
    $remaining = $remaining - 1
}

Write-Output $previous
