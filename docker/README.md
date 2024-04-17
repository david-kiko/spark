#本地minikube调试
```text
minikube中需要修改/usr/lib/systemd/system/docker.service
添加--insecure-registry 192.168.200.152:15000

systemctl daemon-reload
systemctl restart docker

docker pull 192.168.200.152:15000/spark:v3.3.5

#创建role
kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
```

```text
构建
./dev/make-distribution.sh --tgz -P"kubernetes,volcano,hive,hive-thriftserver" -Dhadoop-version=3.1.1
```