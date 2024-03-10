# Summary:
	11:26-am-GMT until 12:45-pm-GMT, the server always respond with status code 500, regardless of page requested. 
	100% of users reported the issue of website not returning requested page.
	after debugging the issue, it was found that during a commit in which we update the wordpress settings, 
 	one of the interns added a letter to a php file suffix, 
	which lead PHP not being able to find the file and returning a server failute.
	
# Timeline:
	 11:22-am-GMT - Modifying Wordpress Settings and commiting the changes.
	11:26-am-GMT - Users Complain they're not able to access some pages in the website.
	11:30-am-GMT - Checking with the Monitoring staff to see if the server is up and running.
	12:05-pm-GMT - After ensuring hardware is in great shape, we start to debug the website itself.
	12:15-pm-GMT - Certain Files are missing.
	12:18-pm-GMT - After taking a second look at the debugger's output, there was an additional 'p' in file "wp-local.phpp".
	12:20-pm-GMT - Locating 'wp-local.phpp' in '/var/www/html/wp-settings.php' and correcting the enxtension suffix to '.php'
	12:30-pm-GMT - After testing the changes locally, then we committed the changes.
	12:45-pm-GMT - The Website is up and running.

The root cause of this issue was that PHP couldn't find a file that was included in the settings of a wordpress php file, the file itself was there, but it was included with a typo(extension suffix wrong), hence why PHP couldn't find it and caused an internal server error.
After Facing the issue, and roundabout it, we realised that it was probably in the files rather than in the hardware, and as such we used Strace to track where the problem lies, after reading the output we realised that the system was lookin for "/var/www/html/class-wp-local.phpp' which doesn't existn and it was included in the '/var/www/html/wp-settings.php', after fixing the typo the server was returning responses as it was intended to be.
