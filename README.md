# Eisenhower Todo Application — Docker & CI/CD PBL

A Todo web application built using Node.js, Express.js, EJS, and MongoDB.

The application organizes tasks using the Eisenhower Matrix based on their urgency and importance. This project also demonstrates Docker containerization, Docker Compose, automated route testing, and a GitHub Actions CI/CD pipeline.

## Features

- Add new tasks
- View tasks using the 4-quadrant Eisenhower Matrix:
  - Do — Urgent and Important
  - Schedule — Not Urgent and Important
  - Delegate — Urgent and Not Important
  - Eliminate — Not Urgent and Not Important
- Edit existing tasks
- Delete tasks
- Add due dates
- MongoDB database storage
- Responsive layout
- Dockerized application
- Multi-container setup using Docker Compose
- Automated route testing using Python
- CI/CD using GitHub Actions
- Automatic Docker image build and push to Docker Hub

## Technologies Used

- Node.js
- Express.js
- EJS
- MongoDB
- HTML
- CSS
- Docker
- Docker Compose
- Python
- GitHub Actions
- Docker Hub

## Project Structure

```text
eisenhower-todo/
│
├── .github/
│   └── workflows/
│       └── ActionsYaml.yaml
│
├── public/
│   └── style.css
│
├── views/
│   ├── edit.ejs
│   ├── index.ejs
│   └── new.ejs
│
├── .dockerignore
├── .gitignore
├── app.js
├── automationTesting.py
├── docker-compose.yml
├── Dockerfile
├── package.json
├── package-lock.json
└── README.md
```

## Application Routes

| Method | Route | Description |
|---|---|---|
| GET | `/` | Display all tasks |
| GET | `/tasks/new` | Display new task form |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/:id/edit` | Display task edit form |
| POST | `/tasks/:id/update` | Update an existing task |
| POST | `/tasks/:id/delete` | Delete a task |

## Running Locally

Make sure Node.js and MongoDB are installed and MongoDB is running.

Install dependencies:

```bash
npm install
```

Start the application:

```bash
node app.js
```

Open:

```text
http://localhost:3000
```

## Running with Docker Compose

Docker Compose runs both the Node.js application and MongoDB in separate containers.

Build and start the services:

```bash
docker compose up --build
```

Open the application at:

```text
http://localhost:3000
```

Stop the containers using:

```bash
docker compose down
```

MongoDB data is stored using a Docker volume so that the data persists between container restarts.

## Automated Testing

The project contains:

```text
automationTesting.py
```

The automated tests verify the major application routes and operations, including:

- Home page
- New task page
- Input validation
- Task creation
- Task retrieval
- Edit page
- Task update
- Invalid task ID handling
- Task deletion

Install the Python dependency:

```bash
pip install requests
```

With the application running, execute:

```bash
python automationTesting.py
```

A successful run ends with:

```text
ALL AUTOMATED TESTS PASSED
```

## CI/CD Pipeline

GitHub Actions automatically runs whenever code is pushed to the `main` branch.

The pipeline performs:

```text
Git Push
   ↓
GitHub Actions
   ↓
Start Application + MongoDB
   ↓
Run automationTesting.py
   ↓
Automated Tests Pass
   ↓
Login to Docker Hub
   ↓
Build Docker Image
   ↓
Push Docker Image to Docker Hub
```

If automated testing fails, the workflow stops and the Docker image is not pushed.

## Docker Hub

Docker image:

```text
shaily01/eisenhower-todo-pbl:latest
```

The image is automatically built and pushed to Docker Hub after successful automated testing.

To pull the image:

```bash
docker pull shaily01/eisenhower-todo-pbl:latest
```

## MongoDB Configuration

Database:

```text
todo_lab
```

Collection:

```text
tasks
```

For local execution, the default MongoDB URL is:

```text
mongodb://127.0.0.1:27017
```

When running through Docker Compose, the application uses:

```text
mongodb://mongodb:27017
```

through the `MONGODB_URI` environment variable.

## CI/CD Secrets

The GitHub Actions workflow uses repository secrets for Docker Hub authentication:

```text
DOCKERUSERNAME
DOCKERTOKEN
```

Sensitive credentials are not stored directly in the source code.

## Author

Shaily Sinha