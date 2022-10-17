# REST API

Before starting functionality implementation,

the server needs to integrate the REST API first so that external users can interact with the server though that.

Therefore, djangorestframwork library is used to introude the REST API in the server.
<img width="597" alt="Screen Shot 2022-10-16 at 11 17 12 PM" src="https://user-images.githubusercontent.com/103418311/196088336-67de8743-9b17-4e08-a409-4464b612656d.png">



Through this design, the server will accept HTTP request from any external device (can be the system's frontend or simulation or the system's hardware)
and it will react identically so that it makes the system's design and testing easy and credible

# Data Acquisition
In the design doc, the software is divided in to 4 parts

1. Data Acquisition
2. Analyzer
3. Adjuster
4. StatsAnalyzer


In this note, it is focusing on the first part: `Data Acquisition`

<img width="561" alt="Screen Shot 2022-10-16 at 11 06 40 PM" src="https://user-images.githubusercontent.com/103418311/196087156-3a67eef4-de9c-4c8a-b9e8-374d3eb39023.png">



As explained in the screenshot, Data Acquisition's role is to consistantly storing the light intensity data points sent from the photosensor.

Therefore when a data point is passed from the photosensor, 

the server will first create a django object before storing the data in the database


### DJango LightIntensityPoint Model

```python
class LightIntensityPoint(models.Model):
    sensor = models.CharField(db_index=True, max_length=20)
    time = models.DateTimeField(auto_now_add=True, db_index=True, null=False)
    value = models.FloatField(null=False)
```

This model's object represents one data point reported by one photosensor

1. `sensor`: the name of the sensor that reported
2. `time`: the time when this data was reported
3. `value`: the reported value


Even though this model is very simple, this is the most fundamental(therefore important) model in the system.

The system will constantly calculate the difference between this reported value and its desired value and adjust the system to reduce the difference.

In order to be used for the calculation, created data points will be stored in a database(permanent storage) as shown below

<img width="1423" alt="Screen Shot 2022-10-16 at 11 29 58 PM" src="https://user-images.githubusercontent.com/103418311/196089637-4c0b9c5c-1756-4a02-a5e1-63a62dcb8463.png">



## Testing

1. Prepare random values
2. Send all data points to the system using a simulator
3. Retrieve all data points from the database
4. Check whether they matched or not


## result

<img width="1173" alt="Screen Shot 2022-10-16 at 11 55 52 PM" src="https://user-images.githubusercontent.com/103418311/196092475-b3c90c36-191d-4a37-a151-b9bc45110609.png">



<img width="1555" alt="Screen Shot 2022-10-16 at 11 52 24 PM" src="https://user-images.githubusercontent.com/103418311/196092107-621d533a-3a6e-4966-bd01-50a3b09232b2.png">
