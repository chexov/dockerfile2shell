Usefull for EC2 AMI creation.
Ideally output script may be used as user-data for initial instance setup.

```
cd image/
ls -l Dockerfile
dockerfile2shell.py > userdata.sh
aws ec2 run-instances --image-id ami-7f647f06 --count 1 --user-data file://$PWD/userdata.sh
```

