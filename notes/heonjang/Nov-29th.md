# Deployment

In this note, I am going to talk about the deploying the application in the cloud

Because user needs to access the system through the webpage, the server needs to be online.

For that, we decided to use the GCP serverless service to deploy the application image to the server.

<img width="201" alt="Screen Shot 2022-12-08 at 4 48 45 PM" src="https://user-images.githubusercontent.com/103418311/206583438-a9fcdf4d-7e91-4a39-8b5c-c24b6dab71f4.png">


Procedure

1. Build an image using docker
2. Put a "latest" tag and upload it to GCP gcr
3. Run the image with `Cloud Run`

<img width="289" alt="Screen Shot 2022-12-08 at 4 49 07 PM" src="https://user-images.githubusercontent.com/103418311/206583491-d72d6bec-f93c-454c-9de2-6e1f7deb38aa.png">


The good thing about cloud run is that it is a serverless service. Meaning, as long as we deploy the app, the GCP will take care of recoverying and scaling.
