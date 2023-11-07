## Overview
* This image can be used for troubleshooting/ debugging issues. 
* Following are some of the utilities that are pre-installed on this container image:

```
ping
dig
nslookup
traceroute
curl
wget
nc
netstat
iostat
top
free
vmstat
python3
pip
```

## Run as a pod on Kubernetes
```
kubectl run debug --image=vineethac/debug -n default -- sleep infinity
```

## Exec into the debug pod
```
kubectl exec -it debug -n default -- bash 
```