# The csvserver assignment

1. created a VM in AWS using Amazon linux Image:
![image of initial screen](https://raw.githubusercontent.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png)


2. installing docker using yum commands and starting the docker service. <br>
Command used: sudo yum install docker -y && sudo systemctl start docker 

![installation of docker](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/installation-docker.png)

3. yum install python -y --> to install python for script 

4. Issue was missing of the file inputFile. So we will file mount to container.<br>
Resolve it using -v parameter in docker run command.

6. we create a folder /csvserver.

7. run python gencsv.py file to generate inputFile in /csvserver

![python output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/python-op.png)

8. docker command to run with file mount:
   <br>

docker run -v /csvserver/inputFile:/csvserver/inputdata -d infracloudio/csvserver:latest
![docker-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/docker-op.png)

9. To find out the ports exposed. Used inspect command: <br>

docker inspect <container_id>
![docker-inspect-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/docker-inspect.png)
![docker-port-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/ports-op.png)

10. Now run the docker command with environment variable and port mapping. <br>

docker run -v /csvserver/inputFile:/csvserver/inputdata -p 9393:9300 -e CSVSERVER_BORDER=Orange -d infracloudio/csvserver:latest
![docker-part1-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/part1-op.png)

accessing the VM with public IP for output screen
![chrome-part1-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/chrome-out.png)

11. curl -o ./part-1-output http://localhost:9393/raw - *file attached* <br>
![docker-part1-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/part1-op-1.png)

12. curl -o docker logs [container_id] >& part-1-logs - *file attached* <br>
![docker-part1-output](https://github.com/lalith2211/csvserver-app/blob/main/images/vm-initial.png/images/part1-op-2.png)
