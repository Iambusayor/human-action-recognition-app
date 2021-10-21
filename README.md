# Human-action-recognition-app
A flask app for human action recognition.
	
## Dependencies
* **Docker**  
You need to have docker installed on your local machine
	
## Get started
* clone or download repository

* Install requirements file  
```
$ pip install -r requirements.txt
```

* Setup depstack image  
For CPU
```
$ sudo docker run  --name deepstack_api -v <path to the directory you cloned the repo into>/detector:/modelstore/detection -p 80:5000 deepquestai/deepstack
```
For GPU
```
$ sudo docker run --gpus all  --name deepstack_api -v <path to the directory you cloned the repo into>/detector:/modelstore/detection -p 80:5000 deepquestai/deepstack:gpu
```
For Windows OS
```
$ deepstack --MODELSTORE-DETECTION "C:/<path to the directory you cloned the repo into>/detector" --PORT 80
```


## Run App
```
$ python run.py
```

