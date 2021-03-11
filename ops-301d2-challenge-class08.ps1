# Script:                   ops-301d2-challenge-class08.ps1                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/10/2021    
# Purpose:                  Use New-ADUser to create new user with attributes.

# Declaration of variables

# Declaration of functions

# Main

New-ADUser -Name "Franz Ferdinand" -OtherAttributes @{'title'="TPS Reporting Lead";
                                                'mail'="ferdinand.franz@globexpower.com";
                                                'department'="TPS";
                                                'company'="GlobeX USA";
                                             
# End
# References: https://docs.microsoft.com/en-us/powershell/module/addsadministration/new-aduser?view=win10-ps
