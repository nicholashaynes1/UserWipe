$keepUser = "bus-itgroup"
Get-LocalUser | ?{$keepUser -notcontains $_.Name} | Remove-LocalUser