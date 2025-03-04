# Flask Monitoring App with Jenkins and Docker

## 📌 Project Overview
This project is a **Flask application** designed to monitor the health of a service.  
It is tested using **unittest** and automated using **Jenkins CI/CD**.  
**Both Jenkins and Flask applications are containerized in separate Docker containers** to ensure **consistency, portability, and scalability**.

---

## 🐳 How Docker is Used

### **1️⃣ Running Jenkins in a Docker Container**
Jenkins is deployed inside a **Docker container** to automate build and test processes.  
To run Jenkins, execute the following command:

```sh
docker run -p 8080:8080 -p 50000:50000 --name jenkins-container -d jenkins/jenkins:lts-jdk17
```

- **`-p 8080:8080`** → Maps Jenkins web interface to port **8080** on the host.
- **`-p 50000:50000`** → Allows Jenkins agent connections.
- **`--name jenkins-container`** → Assigns the name `jenkins-container`.
- **`-d`** → Runs Jenkins in detached mode.

Once Jenkins is running, access it at:
```
http://localhost:8080
```
Retrieve the initial admin password:
```sh
docker exec jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword
```

---

### **2️⃣ Running Flask Inside a Separate Docker Container**
The **Flask application is containerized separately** to maintain isolation and portability.

#### **Creating a Flask Container Using `Dockerfile`**
A **mandatory `Dockerfile`** defines the containerized Flask environment.

### **`Dockerfile` (For Flask App)**
```dockerfile
# Use an official Python runtime as a base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /usr/app

# Copy the application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "flask-monitoring-app/app.py"]```

---
```

### **3️⃣ Building and Running the Flask Docker Container**
To **build and run the Flask container**, follow these steps:

#### **Step 1: Build the Flask Docker Image**
```sh
docker build -t flask-container .
```

#### **Step 2: Run the Flask Container**
```sh
docker run -d --name flask-container -p 5000:5000 flask-container
```

- **`-d`** → Runs the container in the background.
- **`--name flask-container`** → Assigns the name `flask-container` to this Flask instance.
- **`-p 5000:5000`** → Maps port **5000** inside the container to **5000** on the host.

Once running, the Flask app is accessible at:
```
http://localhost:5000
```

---

## 📂 Files in This Repository

| File | Description |
|------|------------|
| `app.py` | Flask application script |
| `test_app.py` | Unit tests for Flask app |
| `Jenkinsfile` | CI/CD pipeline for Jenkins |
| `Dockerfile` | Defines the **Flask** container environment |
| `requirements.txt` | Python dependencies |

---

## 🛠 How to Run Locally (Without Docker)
If you want to run the Flask app manually **without Docker**, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/your-project.git
   cd your-project
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```sh
   python app.py
   ```

5. **Run unit tests:**
   ```sh
   python -m unittest test_app.py
   ```

---

## 🎯 CI/CD Pipeline (Jenkins Integration)
The **Jenkins pipeline** is defined in `Jenkinsfile`. It automates:
1. **Checking out the latest code from GitHub**
2. **Building and running the Flask app inside Docker**
3. **Running tests inside the Docker container**
4. **Deploying the application**

### **Jenkinsfile Contents**
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-repo/your-project.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-container .'
            }
        }
        stage('Run Flask Container') {
            steps {
                sh 'docker run -d --name flask-container -p 5000:5000 flask-container'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run flask-container pytest test_app.py'
            }
        }
    }
}
```

---

## ✅ **Key Takeaways**
1. **Jenkins runs inside a Docker container** for CI/CD automation.
2. **The Flask application is containerized separately** in a **dedicated `flask-container`**.
3. **Jenkins pulls the latest code from GitHub**, builds a **Docker image for Flask**, and deploys it inside a container.
4. **Tests are run inside the container** using `unittest`.
5. **Both Jenkins and Flask are running in isolated Docker containers** to ensure consistency across environments.

---

---

## **🛠 Stopping and Removing Containers**
To **stop and remove** both the Jenkins and Flask containers, run:
```sh
docker stop jenkins-container flask-container
docker rm jenkins-container flask-container
```

To **remove images**:
```sh
docker rmi flask-container
```

---

## **🎯 Deploying on a Cloud Platform**
For production deployment, you can:
- Use **Docker Compose** to orchestrate both containers together.
- Deploy the Flask container on **AWS, Azure, or Google Cloud**.
- Use **Kubernetes** for container orchestration.

---


