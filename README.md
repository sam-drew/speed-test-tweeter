# Tweet your ISP!
This project uses the speedtest.net command line interface, that can be found 
over at https://github.com/sivel/speedtest-cli, along with the documentation 
for its use.


This project also uses Twitter's API, for which the full documentation can be 
found at https://dev.twitter.com/rest/public.




To use this project, you will need to add an application to the twitter 
account that you want to tweet from. This is fairly self explanitory, and can 
be done from https://apps.twitter.com.


The instructions for generating your OAuth tokens can be found at: 
https://dev.twitter.com/oauth/overview/application-owner-access-tokens.




Run the file 'speed_test_tweet.py' from the command line or Python interpreter 
(Python 3 please).
This will prompt you to enter several different details such as: 
Authentication tokens, the root path to the 'speedtest_cli.py' file, whether
you wish to log speed test results to file or not, the amount of time to wait 
between testing the speed, the threshold at which tweets should be published, 
and the tweet that will be published if the speed drops below the threshold.


Reccomend using a Raspberry Pi or similar so that this can be running all the 
time, as it uses very little bandwidth or processing power.
