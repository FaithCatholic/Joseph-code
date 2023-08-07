instructions for succesfully running and using this script to call subscription genius's api and pull history data down
from their backend

*** using script ***
populate the testpad .rtf files accordingly. make sure that the subscriber ID at index 1 in testpad is == to renewal code 
at index 1 in testpad_renewal_code. you can change the names of these filetypes too of course to something that makes
more sense. 

make sure genius.py and readfile.py are in the same folder (just pull the whole folder down or download the zip) 
and as long as the testpads are populated it will run and fill in a CSV file with the history. 

additional documentation is commented in the scripts themselves
******************
*** important info for when you go to migrate the CSV ***
the date that is pulled down from subscription genius is in a PHP unfriendly format. it comes in a M/D/Y (note the slashes) formatthat strtotime class inside of php doesn't support. once the CSV is populated your goal will be to get this into this format,
Y-M-D (note the dashes, not slashes). excel doesn't handle this task very well so import the file to google sheets and follow
these steps : highlight date column > click on data > convert text to columns, use comma indentation > swap date format to Y-M-D

when you download the CSV again, make sure not to open it inside of excel or it'll screw up the formatting for the dates again.
if you need to double check it, look at it inside of visual studio. after you have converted the dates succesfully, migrate will
work perfectly. 

**note, you could try your luck with format_date plugin inside of migrate instead of changing format inside of sheets, but I 
had no luck with this approach.

