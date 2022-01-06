$keepUser = "bus-itgroup", "Administrator", "WDAGUtilityAccount", "DefaultAccount", "u0512666", "Guest"
Get-LocalUser | ?{$keepUser -notcontains $_.Name} | Remove-LocalUser
