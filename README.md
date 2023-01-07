# fasumgaz
Web-applicatation for newspaper summarization,
based on Ilya Gusev's model 
[link to model](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta)
FastAPI is used as web-interface.

## Create virtual environment
```
$ conda create --name py37 python=3.7
```

### To activate this environment, use
```
$ conda activate py37
```

### To deactivate an active environment, use
```
$ conda deactivate
```

## Install dependancies
```
$ pip install -r requirements.txt

```

## Run web-application
```
$ uvicorn main:app
```
URL of service will be printed in command line.
Use curl or postman for acces to service. 
