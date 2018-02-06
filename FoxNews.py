#!/bin/env python

## From https://radio.foxnews.com/player-files/radio.php
import time
import os,subprocess,multiprocessing,sys



def downloadFoxNews(newsFile,e):
    print "sub: " + newsFile
    downloading = subprocess.Popen("curl 'http://fnradio-shoutcast-32.ng.akacast.akamaistream.net/7/115/13873/v1/auth.akacast.akamaistream.net/fnradio-shoutcast-32' -H 'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5' -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Host: fnradio-shoutcast-32.ng.akacast.akamaistream.net' -H 'Range: bytes=0-' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -o " + newsFile, shell=True)
    e.wait()
    downloading.kill()
    
    ## curl 'http://fnradio-shoutcast-32.ng.akacast.akamaistream.net/7/115/13873/v1/auth.akacast.akamaistream.net/fnradio-shoutcast-32' -H 'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5' -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Host: fnradio-shoutcast-32.ng.akacast.akamaistream.net' -H 'Range: bytes=0-' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -o $foxNewsMp3
    
    
foxNewsDir = "/tmp/"
foxNewsMp3 = foxNewsDir + time.strftime("FoxNews%Y%m%d%H%M%Z", time.localtime()) + ".mp3"   ##foxNewsDir/FoxNews`date +%Y%m%d%H%M%Z`.mp3
print 11111111
event = multiprocessing.Event()

subp = multiprocessing.Process(target=downloadFoxNews, args=(foxNewsMp3,event))
subp.start()



print 2222222222
time.sleep(5)
command = "vlc " + foxNewsMp3
vlc = subprocess.Popen(command, shell=True)

vlc.wait()
exitCode = vlc.poll()

if exitCode != "None":
    print "End"
    event.set()
    ##os._exit(0)

