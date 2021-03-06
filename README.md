# Django based Excelsheet Data Validator
> Use Docker Deployed API as it is more stable and will not run in 503 Temporary error in Heroku free dyno
> https://assigndjango.herokuapp.com/api/upload  (Docker Deployed on Heroku)\
> https://developershome.herokuapp.com/api/upload  (Normally Deployed on Heroku)

### POSTMAN Preview for Docker Deployed Django app on Heroku
<img src="testimages/docker_postman.JPG" width="900">

### POSTMAN Preview for Normal Deployed Django app on Heroku
<img src="testimages/postman.JPG" width="900">

## Features ð
â¡ï¸ Put Api URL using POST option.\
â¡ï¸ Use **excelfile** as parameter.\
â¡ï¸ Select **File** from dropdown.\
â¡ï¸ Click on **Send** button.\
â¡ï¸ Error Response will be shown as in image.\
â¡ï¸ You can use **Orders-With Nulls.xlsx** present in **unit_test** folder for your reference if you donât have any.


### Save Data Preview
<img src="testimages/docker_admin_data.JPG" width="900">

## Features ð
â¡ï¸ Correct data is saved in databse for future use.\
â¡ï¸ Can Implement functions to make use of data to its best.\
â¡ï¸ Admin URL for both platform 
> https://assigndjango.herokuapp.com/admin/ \
> https://developershome.herokuapp.com/admin/ \
â¡ï¸ Username : test \
â¡ï¸ Password : iamawesome 

## Installation ð¦

>pip install -r requirements.txt

#### Clone

- Clone this repo to your local machine.

#### Run server locally

```shell
$ python manage.py runserver
```
> Go to localhost:8000

## OR
```shell
$ docker build -t web:latest .
$ docker run -d --name django-docker -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
```
> Go to localhost:8007

## For Stopping Docker Server
```shell
$ docker stop django-docker
$ docker rm django-docker
```




---

## Contributing ð¡


#### Step 1

- **Option 1**
    - ð´ Fork this repo!

- **Option 2**
    - ð¯ Clone this repo to your local machine.


#### Step 2

- **Build your code** ð¨ð¨ð¨

#### Step 3

- ð Create a new pull request.

