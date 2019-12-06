# simple-cars.com-API
This project fethces information from cars.com and provides it through an API.

Project consisted of three main stages:
1. Writing web scrapper for fething information from cars.com
2. Saving fetched data into mySQL
3. Provide API

First two is done by scripts in `api/utils`, while providing API utilizes Django Rest Framework.

## Run
To initialize dataset,
first run `python manage.py shell` in root directory. Then in the shell run following lines,
```python
from api.utils.write_database import main
main()
```

After initialization you should do the following to run server,
```bash
python manage.py runserver
```
Now you can access API with,
```
http://localhost:8000/api
```
or make some filtering,
```
http://localhost:8000/api/?ext_color=black&transmission=automatic&&brand=BMW&&year=2012
```
which results in following,
```json
[
    {
        "brand": "BMW",
        "price": "17400",
        "year": "2012",
        "model": "750 i xDrive",
        "ext_color": "black",
        "int_color": "black",
        "transmission": "automatic",
        "contact": "(404) 935-6893"
    }
]
```

`Note:` Don't forget to edit mySQL configurations in `settings.py`. They are currently configured for my local computer.

## TODO
1. Write django custom command to more elegant initilazation. Current one requires opening django shell.
2. Configure Docker.
