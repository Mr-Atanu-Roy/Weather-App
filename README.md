
## Features

- Check compete weather of a perticular city/place
- Check lowest, highest, current temperature
- Check Humidity
- Check wind speed
- Check Pressure
- Check Visibility
## Tech Stack

**Client Side:** HTML, SCSS, TailwindCSS

**Server Side:** Django, Open weather(for api)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = TRUE`

`SECRET_KEY = 'django-insecure-&lbc+zw$)wd&66ik^^)@rxdc&47ppd=d+k@*l2^hq(@73tu)89'`

### Open Weather API KEY
`API_KEY = "9361f3813cd19596e39e9b6318ccbcbf"`

## Installation

Create a folder and open terminal and install this project by
command 
```bash
git clone https://github.com/Mr-Atanu-Roy/Weather-App

```
or simply download this project from https://github.com/Mr-Atanu-Roy/Weather-App

In project directory Create a virtual environment(say env)

```bash
  virtualenv env

```
Activate the virtual environment

For windows:
```bash
  env\Script\activate

```
Install dependencies
```bash
  pip install -r requirements.txt

```
To migrate the database run migrations commands(not necessary for this project)
```bash
  py manage.py magemigrations
  py manage.py migrate

```

Create a super user(not necessary for this project)
```bash
  py manage.py createsuperuser

```

To run the project in your localserver
```bash
  py manage.py runserver

```
Then go to http://127.0.0.1:8000 in your browser to see the project

## Author

- [@Mr-Atanu-Roy](https://www.github.com/Mr-Atanu-Roy)

