# Test_task
___
## Docker-compose
It consists of two containers: : minio, python
___

## Realization trouble
I misread the terms and realized too late that the files must be stored in minio, so I didn't have time to rewrite my scripts. They work if there are folders with files in their directory :(

### Python Scripts:
#### main.py
The script transforms the data from the 02-src-data folder and fills the all_data.csv file.

#### add_data.py
The script transforms the new data from the new_data folder and adds it to the all_data.csv file. Next, it moves all the data from the new_data folder to the 02-src-data folder. If the files have the same name, the new file will replace the old one.

#### server.py
A server script that accepts HTTP requests (port:8080) and activates other scripts.  
/ - displays the inscription 'Start' on the screen.  
/GET/data - displays a table with all available information. Has filtering by parameters (is_image_exist, min_age, max_age) according to the condition of the task.  
/POST/data - activates the default main.py script. I added a filter parameter (add_data). If the value is "True", the script will run
add_data.py.  
/GET/stats - displays the average age of users who are in the table. It has filtering by parameters (is_image_exist, min_age, max_age) according to the condition of the task.  

___
