This is a simple Python script which should run well on any Debian-based OS, but was designed on a Raspberry Pi.

You can change mirrors by changing the src and suf to whatever URL you want, but only if they use non-formatted issue numbers. (e.g. http://www.example.com/the-magpi-issue-1.pdf as opposed to /the-magpi-issue-01.pdf)

I would recommend setting it up to a cron job that runs monthly.

TODO:
    
* The program is not currently pure Python. I had trouble getting urllib2 to work right. Specifically, I could not get the response handler (line 52) to write to newIssue (line 63). I was getting an error. You can try it for yourself by uncommenting lines 62-64 and running it.
