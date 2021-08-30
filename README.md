This service is responsible for monitoring the microservice. 

1) It fetches the get result and evaluates to decide if statements need to be printed. 
2) It utilizes cronjob.yaml which decide the type of deployment 
3) config file is mainly used for storing Splunk Paramters.
4) Docker file has all the steps along with Splunk and Dynatrace setup. 
5) Jenkins uses credentials and make file to execute the required pipeline. 
6) Credentials are stored on the Jenkins - manage Jenkins(Configure Credentials).
7) Requirement.txt file mentions library which need to be installed. 

Overall error rate can be removed - 
1) Increased alerting by deploying alerting service with a separate pod which will run at alternate minute. 
2) Check threshold for errors based on last 5 or 10 mins to calculate the error rate. 
3) Alert threshold time - decides when error rate need to be calculated. 
