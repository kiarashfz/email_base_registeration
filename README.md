# EMAIL BASE REGISTRATION

This is a Django project that uses an email instead of a username for users.
I've used version 3.2 of Django because it's the latest LTS version.
## Pre requirements
| Docker      | Docker compose |
| ----------- | ----------- |
## Installation
#### 1. First step is cloning the project
```bash
$ git clone https://github.com/kiarashfz/email_base_registeration.git
```
#### 2. Next step is changing your terminal directory into root of the project
```bash
$ ls
runner.sh   manage.py   ...
```
#### 3. Create a file named .env to set your own environment variables
```bash
$ touch .env
```
#### - sample .env content:

```bash
POSTGRES_DB=postgres
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=1
ALLOWED_HOST=*
DJANGO_LOG_LEVEL=INFO
```
> **_NOTE:_**  You should put your secure data in .env file. so change it in production mode.

#### 4. The final step is running runner.sh file with your terminal
> **_NOTE:_**  This command will download some docker images from dockerhub, so you may need to use a VPN.
```bash
$ ./runner.sh
or
$ sh runner.sh
```
####  5. Now open your browser and paste these urls and enjoy it :wink:
```sh
0.0.0.0
or
YOUR.OWN.SERVER.IP
```
- See also for API documentations
```sh
0.0.0.0/redoc
or
YOUR.OWN.SERVER.IP/redoc
```
> **_NOTE:_**  Now you have a superuser to using hostname/admin panel or using admin permission required APIs
> 
> ### superuser:
> 
> username/email: admin@admin.admin
> 
> password: admin

> **_WARNING:_** `Change superuser password in production mode for security reasons.`

You can also use postman collection placed in documentation and import it to your own postman.
