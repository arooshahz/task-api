# Task Management API

A simple REST API for managing tasks using **FastAPI** and **PostgreSQL**, with full CRUD operations.

## Technologies

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Gunicorn + Uvicorn
* systemd

## Installation & Running

Clone the repository:

```bash
git clone https://github.com/arooshahz/task-api.git
cd task-api
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL connection in `.env`:

```env
DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:5432/tasks_db
```

Run the application:

```bash
uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint           | Description   |
| ------ | ------------------ | ------------- |
| GET    | `/tasks/`          | Get all tasks |
| POST   | `/tasks/`          | Create a task |
| GET    | `/tasks/{task_id}` | Get a task    |
| PUT    | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Task Fields

* `id` — Integer, primary key
* `title` — Required string
* `description` — Optional string
* `is_completed` — Boolean, defaults to `false`
* `created_at` — Automatically generated timestamp

## Deployment

The API can be deployed on Linux using **Gunicorn with Uvicorn workers** and **systemd**.

Run with Gunicorn:

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

A systemd service template is provided in:

```text
deploy/task-api.service
```

Replace `YOUR_USERNAME` and `/path/to/task-api` with the appropriate values for the target server, then copy the file to:

```text
/etc/systemd/system/task-api.service
```

Run:

```bash
sudo systemctl daemon-reload
sudo systemctl start task-api
sudo systemctl enable task-api
```

Check the service:

```bash
sudo systemctl status task-api
```
