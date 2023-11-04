## Overview
This is the Dockerfile for creating a FIO application container image running on Ubuntu base OS layer.

## To run FIO as a pod on Kubernetes
```
kubectl run fio2 --image=vineethac/fio_image:3.28 -- fio --name=RandomReadWriteTest --readwrite=randrw --rwmixwrite=50 --bs=8k --invalidate=1 --direct=1 --filename=/fio_testfile --size=2g --time_based --runtime=300 --ioengine=libaio --numjobs=2 --iodepth=1 --norandommap --randrepeat=0 --exitall
```

## Verfiy
```
k exec -it fio2 -- iostat -xd 5 --pretty
Linux 4.19.225-3.ph3 (fio2) 	11/04/23 	_x86_64_	(2 CPU)

     r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz Device
  875.60   7004.80     0.00   0.00    0.35     8.00 sda

     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz Device
  847.00   6823.20    14.80   1.72    0.85     8.06 sda

     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz Device
    0.00      0.00     0.00   0.00    0.00     0.00 sda

     f/s f_await  aqu-sz  %util Device
    0.00    0.00    1.03  96.00 sda

```