

<#

Simple script to add a touch function for windows powershell.
Creates a new file and shows minimal output.

Add to powershell profile to use.

#>

function touch {
  if ($args.Length -lt 1) { Write-Error "Need a filename" }

  else { 
    $newFile = $args[0]
    New-Item -ItemType File -Name ($newFile) > $null
    Write-Host "${newFile} created" -ForegroundColor Green
  }  
}