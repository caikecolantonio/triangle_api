# Triangle API / triangle_api

## About / Synopsis

* Code Chalenge for COCUS
* Developed in Python And Django

## Installation

1. You need to have installed Python. [latest version](https://www.python.org/downloads/).
2. You need to create a virtual environment. [Documentation to create according to system operation](https://docs.python.org/3/library/venv.html).
3. You have to active the virtual environment.
4. Install all the dependencies using this command: 
``` sh 
pip install -r requirements.txt
```
5. Create a .env file based on local.env and set the database and secret key 
6. You need to run the migration: 
``` sh 
python manage.py migrate
```
7. To run the server:
``` sh 
python manage.py runserver
```
8. To access the server go to the link:
```
http://localhost:8000/
```
9. Use local.env to create a .env with the credentials send by e-mail.

## Usage

* The DRF it's configured so when you access the endpoint you will see all endpoints with frontend
* To access the endpoints documentation go to this [link](https://ljor47zd7j.execute-api.us-east-1.amazonaws.com/production/doc/).
* To access live DRF and the endtpoint go to this link [link](https://ljor47zd7j.execute-api.us-east-1.amazonaws.com/production/).

## Deploy

* Deployed on AWS Lambda using zappa.
* Created a RDS MYSQL Database and integrate with the project.
* Using AWS Cloudwatch on the Lambda to get errors for requests.
* Using S3 Bucket to storage the static files

## Tests

* To run the tests you have two options `pytest` or `python manage.py test`
* For the tests i used pytest and unittest.

## Example get and post

* Get Example
<img src="https://drive.google.com/uc?id=1A79XzKeJfLb1QPCje4DDGUS2TEnleplZ">

* Post Example
<img src="https://drive.google.com/uc?id=15JNceZp57Mshw5GnrXGjzU_iam3E0KHl">

## Extras

* To format the code i used black
* If you have further questions feels free to contact me