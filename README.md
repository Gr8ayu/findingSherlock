# FInding Sherlock (CTF event)

This project was developed as project work for College fest event.
It is developed in Django  objective.

The portal was designed for CTF event for annual Tech fest of RVCE (8th mile) by Coding club.
It consist of various levels that you need to solve to gain points. It consist of basic levels of cryptography, stenography, binary exploitation and many more fun challenges ideal for promoting CTF and cybersecurity related stuff in college.

PROMO VIDEO https://youtu.be/lUw_igWrS5Y 

this website is hosted on http://relayhack.herokuapp.com/

[![](https://raw.githubusercontent.com/Gr8ayu/findingSherlock/master/Screenshot_2021-05-06%20SherLOCK.png?token=AG4OQBDXQVCBKXXJO7KIDJ3ATTZHW)](https://raw.githubusercontent.com/Gr8ayu/findingSherlock/master/Screenshot_2021-05-06%20SherLOCK.png?token=AG4OQBDXQVCBKXXJO7KIDJ3ATTZHW)

[![](https://raw.githubusercontent.com/Gr8ayu/findingSherlock/master/Screenshot_2021-05-06%20LEVEL%201.png?token=AG4OQBCF4DSFUUF6YRWCE2DATTZFC)](https://raw.githubusercontent.com/Gr8ayu/findingSherlock/master/Screenshot_2021-05-06%20LEVEL%201.png?token=AG4OQBCF4DSFUUF6YRWCE2DATTZFC)
------------


### Steps to run :
- install python 3.6+
- create virtualenv 
`python3 -m venv env`
- activate virtualenv
`source env/bin/activate`
- install dependencies
`pip3 install -r requirements.txt`
- start django server 
```bash
# to start server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000

```

You can access the website on http://127.0.0.1:8000/ and login with superuser account at http://127.0.0.1:8000/admin .

