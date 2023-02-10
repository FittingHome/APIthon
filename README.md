# APIthon
Python API for piloting windows automation for Marvelous using FastAPI, Celery and Flower Interface.


## Acknowledgements

 - [CELERY Queue Documentation](https://docs.celeryq.dev/en/v5.2.7/userguide/application.html)
 - [FastAPI Background Tasking](https://fastapi.tiangolo.com/tutorial/background-tasks/)
 - [FastAPI WebSocket](https://fastapi.tiangolo.com/advanced/websockets/)
## API Reference

#### Get task status

```http
  GET /taskstatus
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `task_id` | `string` | **REQUIRED**  Your task id |

#### Post simulate

```http
  POST /simulate
```

| Parameter     | Type     | Description                                    |
| :--------     | :------- | :--------------------------------              |
| `garment_id`  | `string` | **REQUIRED** Id of the garment to simulate     |
| `user_id`     | `string` | **REQUIRED** Id of the user to save simulation |
| `folder_path` | `string` | **REQUIRED** Folder path for sftp management   |




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file or directly to the docker-compose.yml environment variables.

`CELERY_BROKER_URL=redis://redis:6379/0`

`CELERY_RESULT_BACKEND=redis://redis:6379/0`

`C_FORCE_ROOT=true`
#### docker-compose Stack

```Docker-Compose
    environment:
        - CELERY_BROKER_URL=redis://redis:6379/0
        - CELERY_RESULT_BACKEND=redis://redis:6379/0
        - C_FORCE_ROOT=true
```

## Deployment

To deploy this project run :

```bash
  cd APIthon
  docker-compose up --build
```


![Logo](https://d3uyj2gj5wa63n.cloudfront.net/wp-content/uploads/2021/02/fastapi-logo.png)
![Logo](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_8a31c306355eb532650043bf039d70a7/python-celery.png)


## Flower Task Manager Interface

Flower is a task manager connected to Celery to view, manage and control all your celery's workers and theirs jobs/requests.
You can check all the requests standing in the queue of a worker, view the priority assigned to certains jobs and see their processing.

[Flower Interface](http://localhost:5556/)