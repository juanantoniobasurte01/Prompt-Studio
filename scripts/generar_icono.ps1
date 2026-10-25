$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$projectRoot = Split-Path -Parent $PSScriptRoot
$source = [System.Drawing.Image]::FromFile((Join-Path $projectRoot 'recursos/PS.png'))
$bitmap = New-Object System.Drawing.Bitmap 256,256
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.Clear([System.Drawing.Color]::Transparent)
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$scale = [Math]::Min(256 / $source.Width, 256 / $source.Height)
$width = [int][Math]::Round($source.Width * $scale)
$height = [int][Math]::Round($source.Height * $scale)
$graphics.DrawImage($source, [int]((256 - $width) / 2), [int]((256 - $height) / 2), $width, $height)
$buffer = New-Object System.IO.MemoryStream
$path = Join-Path $projectRoot 'recursos/promptstudio.ico'
$stream = [System.IO.File]::Create($path)
try {
    $bitmap.Save($buffer, [System.Drawing.Imaging.ImageFormat]::Png)
    $writer = New-Object System.IO.BinaryWriter $stream
    $writer.Write([uint16]0)
    $writer.Write([uint16]1)
    $writer.Write([uint16]1)
    $writer.Write([byte]0)
    $writer.Write([byte]0)
    $writer.Write([byte]0)
    $writer.Write([byte]0)
    $writer.Write([uint16]1)
    $writer.Write([uint16]32)
    $writer.Write([uint32]$buffer.Length)
    $writer.Write([uint32]22)
    $writer.Write($buffer.ToArray())
    $writer.Flush()
} finally { if ($writer) { $writer.Dispose() }; $stream.Dispose(); $buffer.Dispose(); $graphics.Dispose(); $bitmap.Dispose(); $source.Dispose() }
