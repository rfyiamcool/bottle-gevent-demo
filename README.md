##用ab做个简单的http测试 

```
time ab -c 200 -n 200 xxx.126.84.48:8080/stream
This is ApacheBench, Version 2.3 <$Revision: 655654 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking xxx.126.84.48 (be patient)
Completed 100 requests
Completed 200 requests
Finished 200 requests


Server Software:        
Server Hostname:        xxx.126.84.48
Server Port:            8080

Document Path:          /stream
Document Length:        14 bytes

Concurrency Level:      200
Time taken for tests:   12.620 seconds
Complete requests:      200
Failed requests:        0
Write errors:           0
Total transferred:      25800 bytes
HTML transferred:       2800 bytes
Requests per second:    15.85 [#/sec] (mean)
Time per request:       12620.339 [ms] (mean)
Time per request:       63.102 [ms] (mean, across all concurrent requests)
Transfer rate:          2.00 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       19  429 1009.0    129    4602
Processing:  8009 8551 184.5   8584    8723
Waiting:        6  566 194.7    598     774
Total:       8402 8980 877.9   8792   12617

Percentage of the requests served within a certain time (ms)
  50%   8792
  66%   8904
  75%   8955
  80%   8982
  90%   9039
  95%  11611
  98%  12413
  99%  12616
 100%  12617 (longest request)
ab -c 200 -n 200 xxx.126.84.48:8080/stream  0.01s user 0.05s system 0% cpu 12.629 total

```


