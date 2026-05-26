# 🏥 MediTrack DevOps Project

A production-grade DevOps project demonstrating end-to-end cloud infrastructure, containerization, orchestration, and CI/CD automation on Microsoft Azure.

---

## 🏗️ Architecture Overview
GitHub (Source Code)
↓
Azure DevOps (CI/CD Pipeline)
↓
Azure Container Registry (Docker Images)
↓
Azure Kubernetes Service (Running App)
↓
Prometheus + Grafana (Monitoring)
---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Terraform** | Infrastructure as Code — provisions all Azure resources |
| **Docker** | Containerizes all 3 microservices |
| **Kubernetes (AKS)** | Orchestrates containers at scale |
| **Helm** | Manages Kubernetes deployments as versioned charts |
| **Azure DevOps** | CI/CD pipeline — automates build and deployment |
| **Azure Container Registry** | Private Docker image storage |
| **Prometheus** | Collects metrics from cluster and services |
| **Grafana** | Visualizes metrics through real-time dashboards |
| **Python/Flask** | Microservice application framework |

---

## 🚀 Microservices

### 1. Backend Service (Port 5000)
REST API serving patient data with health check endpoints.

**Endpoints:**
- `GET /health` — Health check for Kubernetes probes
- `GET /patients` — Returns patient data

### 2. Frontend Service (Port 3000)
Web UI dashboard exposed publicly via Azure Load Balancer.

**Endpoints:**
- `GET /` — Main dashboard
- `GET /health` — Health check
- `GET /patients` — Fetches data from backend

### 3. Notification Service (Port 5002)
Handles system notifications with in-memory storage.

**Endpoints:**
- `GET /health` — Health check
- `GET /notifications` — List all notifications
- `POST /notify` — Send a notification

---

## 📁 Project Structure
meditrack-devops/
├── terraform/                 # Infrastructure as Code
│   └── main.tf               # AKS, ACR, Resource Group
├── services/                  # Microservices
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── frontend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── notification/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
├── kubernetes/                # Raw Kubernetes manifests
│   ├── backend/
│   ├── frontend/
│   └── notification/
└── meditrack-chart/           # Helm Chart
├── Chart.yaml
├── values.yaml
└── templates/
---

## ⚙️ Infrastructure (Terraform)

All Azure infrastructure is provisioned using Terraform:

```hcl
Resources Created:
├── Resource Group (meditrack-rg) — West US
├── Azure Container Registry (mediatrackacr) — Basic SKU
└── AKS Cluster (meditrack-aks)
    └── 1 Node — Standard_D2s_v3 (2 CPU, 8GB RAM)
```

---

## 🔄 CI/CD Pipeline (Azure DevOps)

Automated pipeline triggers on every push to `main` branch:
Stage 1 — Build:
├── Login to ACR
├── Build Backend Docker image (linux/amd64)
├── Build Frontend Docker image (linux/amd64)
└── Build Notification Docker image (linux/amd64)
Stage 2 — Deploy:
├── Connect to AKS
└── Deploy using Helm upgrade
---

## 📊 Monitoring (Prometheus + Grafana)

Installed via Helm using `kube-prometheus-stack`:
Monitoring Stack:
├── Prometheus — scrapes metrics every 15 seconds
├── Grafana — pre-built Kubernetes dashboards
├── AlertManager — configurable alerting rules
└── Node Exporter — node-level metrics
Access Grafana:
```bash
kubectl --namespace monitoring port-forward svc/monitoring-grafana 3001:80
# Open http://localhost:3001
# Username: admin
```

---

## 🚀 How To Deploy

### Prerequisites
- Azure CLI installed and logged in
- Terraform installed
- kubectl installed
- Helm installed
- Docker Desktop running

### Step 1 — Provision Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

### Step 2 — Build and Push Images
```bash
az acr login --name mediatrackacr
cd services/backend
docker buildx build --platform linux/amd64 -t mediatrackacr.azurecr.io/meditrack-backend:v1 --push .
```

### Step 3 — Deploy With Helm
```bash
az aks get-credentials --resource-group meditrack-rg --name meditrack-aks
helm install meditrack ./meditrack-chart
```

### Step 4 — Access Application
```bash
kubectl get services
# Open http://<EXTERNAL-IP>
```

---

## 🎯 Key DevOps Concepts Demonstrated

- **Infrastructure as Code** — All infrastructure defined in Terraform
- **Containerization** — All services packaged as Docker containers
- **Container Orchestration** — Kubernetes manages all containers
- **Helm Package Management** — Versioned, repeatable deployments
- **CI/CD Automation** — Zero manual deployment steps
- **Health Probes** — Liveness and readiness probes on all services
- **Service Discovery** — Services communicate by name not IP
- **Monitoring** — Real-time metrics and dashboards
- **Least Privilege** — Minimal permissions on all service accounts
- **Cross-platform builds** — ARM64 to AMD64 using Docker buildx

---

## 👩‍💻 Author

Built as a portfolio project demonstrating 2.5 years of DevOps experience
with Azure, Kubernetes, Docker, Terraform, and CI/CD pipelines.