# Test_task
___
## Docker-compose
Складається із двох контейнерів : minio, python
___

## Реалізація
Я недочитав умову та занадто піздно зрозумів що файли повинні зберігатися у minio, тож невстиг переписати свої скрипти. Вони оптимально працюють якщо у їх дерикторії
знаходятся папки з файлами :(

### Скрипти python:
#### main.py
Скрипт транфорує данні з папки 02-src-data та заповнює файл all_data.csv.

#### add_data.py
Скрипт трансформує нові данні з папки new_data та додає їх до файла all_data.csv. Далі він переносить усі данні з папки new_data у папку 02-src-data. Якщо файли мають однакову назву, то новий файл заміню старий.

#### server.py
Скрипт сервера, який приймає HTTP запроси (port:8080) та активує інші скрипти.  
/ - виводить напис 'Start' на екран.  
/GET/data - виводить таблицю з усією доступною інформацією. Має фільтрацію за параматрами (is_image_exist, min_age, max_age) за умовою задачі.  
/POST/data - за замовчуванням активує скрипт main.py. Я додав філтраціний параметр(add_data), при його значенні "True", 
запускається скрипт add_data.py.
/GET/stats - виводить середній вік користувачів, які знаходяться у таблиці.Має фільтрацію за параматрами (is_image_exist, min_age, max_age) за умовою задачі.  

___
