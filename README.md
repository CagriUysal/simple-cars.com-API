# simple-cars.com-API
Simple cars.com API for certain tasks

## Run
To initialize dataset,
first run `python manage.py shell` in root directory. Then in the shell run following lines,
```python
from api.utils.write_database import main
main()
```

After initialization you can run following to run server,
```bash
python manage.py runserver
```
