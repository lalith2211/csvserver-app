# The csvserver assignment

1. created a VM in AWS using Amazon linux Image:
![vm-initial](https://github.com/user-attachments/assets/eab8f272-6649-4b20-8992-3d27a5ffb4c2)

2. installing docker using yum commands and starting the docker service. <br>
Command used: sudo yum install docker -y && sudo systemctl start docker 

![installation-docker](https://github.com/user-attachments/assets/9b19d9a8-5552-4ebd-8308-e1ee5f23130a)

3. yum install python -y --> to install python for script 

4. Issue was missing of the file inputFile. So we will file mount to container.<br>
Resolve it using -v parameter in docker run command.

5. we create a folder /csvserver.

6. run python gencsv.py file to generate inputFile in /csvserver

![python-op](https://github.com/user-attachments/assets/992839d3-fb3a-48d0-9824-f320872fdcdd)


7. docker command to run with file mount:
   <br>

docker run -v /csvserver/inputFile:/csvserver/inputdata -d infracloudio/csvserver:latest
![docker-op](https://github.com/user-attachments/assets/9f0a3d06-e36a-4b22-a81c-b09db945cc78)


8. To find out the ports exposed. Used inspect command: <br>

docker inspect <container_id>
![docker-inspect](https://github.com/user-attachments/assets/d3eae4c7-9fc9-4c35-afa9-09eb89026e04)

![ports-op](https://github.com/user-attachments/assets/6bacfdc4-a8be-46e2-b488-02cf665fa513)


9. Now run the docker command with environment variable and port mapping. <br>

docker run -v /csvserver/inputFile:/csvserver/inputdata -p 9393:9300 -e CSVSERVER_BORDER=Orange -d infracloudio/csvserver:latest
![part1-op](https://github.com/user-attachments/assets/c8d60f59-ddad-418d-a00d-364ae97efcb5)


10. Accessing the VM with public IP for output screen <br>
![chrome-out](https://github.com/user-attachments/assets/a1113eb5-de34-4ad7-ac13-6e70f32b859a)


11. curl -o ./part-1-output http://localhost:9393/raw - *file attached* <br>
![part1-op-1](https://github.com/user-attachments/assets/ed56d121-71aa-4237-803a-073ca4a8ca80)


12. curl -o docker logs [container_id] >& part-1-logs - *file attached* <br>
![part1-op-2](https://github.com/user-attachments/assets/bd086e05-2f5e-496d-a584-2120110c4142)

