# 🌾 Agriculture Platform - End-to-End DevOps Project

This project demonstrates a production-ready DevOps ecosystem, featuring a complete CI/CD pipeline, GitOps deployment strategy, and an advanced observability stack.

## 🏗 System Architecture & Technologies

* **Backend:** Python Flask application.
* **Database:** Redis (Key-Value store) for caching and data persistence.
* **CI Pipeline:** GitHub Actions.
* **GitOps / CD:** ArgoCD (Automated synchronization).
* **Infrastructure:** Kubernetes (Minikube).
* **Observability:** Prometheus, Grafana, and Loki (Loki-stack).

---

## 🔄 1. Continuous Integration (CI)

The CI pipeline is fully automated via GitHub Actions. Every commit triggers a build-test-push cycle.

* **Workflow:** The `docker-build.yml` workflow builds a Docker image and pushes it to Docker Hub as `aslq/agri-app:latest`.
* **Verification:** The synchronized timestamps between GitHub Actions and Docker Hub confirm a successful integration.

> **[INSERT image_c59bdd.jpg HERE]**
> *Caption: Verified integration between GitHub Actions and Docker Hub.*

---

## ☸️ 2. GitOps Deployment (CD)

We utilize **GitOps** principles where the Git repository is the single source of truth for the cluster state.

* **ArgoCD Orchestration:** ArgoCD monitors the `agri-chart/templates` directory. Any change in the manifest files (e.g., adding `redis.yaml` or changing replicas) is automatically synchronized to the cluster.
* **Traceability:** Every deployment is tracked in the **History & Rollback** section, providing 100% auditability and the ability to revert changes instantly.

> **[INSERT image_c53342.png HERE]**
> *Caption: ArgoCD Resource Tree showing Synced state for Application and Redis DB.*

---

## 📊 3. Advanced Monitoring & Custom Metrics

The observability stack is configured to provide deep insights into the application and infrastructure.

* **Real-time Metrics:** Using **PromQL**, we monitor granular data such as Cluster Memory (13.2%) and CPU Usage (0.72%).
* **Custom Queries:** Metrics are pulled directly from the `agri-app` pods using specialized queries, ensuring the dashboard is tailored to this specific workload.
* **Centralized Logging:** Application and system logs are aggregated via Grafana Loki, allowing for rapid troubleshooting across all namespaces.

> **[INSERT image_163ca0.png HERE]**
> *Caption: Professional Grafana Dashboard with real-time cluster metrics.*

---

## 🛠 Installation & Access

1. **Start Minikube:** `minikube start`.
2. **Access App:** `kubectl port-forward svc/agri-app-service 8085:80`.
3. **Access ArgoCD:** `kubectl port-forward svc/argocd-server -n argocd 8080:443`.
4. **Access Grafana:** `kubectl port-forward svc/loki-stack-grafana -n monitoring 3001:80`.

Loyihangizning barcha qismlari (CI, CD, Monitoring va Database) qanday tartibda joylashganini ko'rsatuvchi professional **Project Structure** bo'limi:

---

## 📂 Project Directory Structure

```text
AgriChain_Project/
├── .github/
│   └── workflows/
│       └── docker-build.yml      # CI pipeline: Builds & pushes Docker image to Hub
├── agri-chart/                   # Helm-style Kubernetes manifest directory
│   ├── templates/
│   │   ├── deployment.yaml       # Main application deployment (agri-app)
│   │   ├── service.yaml          # Load balancer/Service for the application
│   │   ├── redis.yaml            # Database layer: Redis deployment & service
│   │   └── _helpers.tpl          # Template helper functions for Kubernetes
│   ├── Chart.yaml                # Metadata about the agri-chart
│   └── values.yaml               # Configuration variables for the manifests
├── app/
│   ├── main.py                   # Python Flask application source code
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile                # Docker build instructions for the app
└── README.md                     # Project documentation & screenshots

```

<img width="1280" height="285" alt="image" src="https://github.com/user-attachments/assets/cc305f3d-c5a9-4523-98d4-1463867bf21b" />

<img width="554" height="481" alt="image" src="https://github.com/user-attachments/assets/c90826bd-2974-46fb-9784-fbcabafc5f49" />

<img width="1280" height="379" alt="image" src="https://github.com/user-attachments/assets/081b1ea8-0829-425f-af4f-502df044b3d2" />

---

### **Project Technical Validation & Observability Overview**

The following technical documentation provides a visual verification of the automated ecosystem implemented in this project. The integration demonstrates a seamless flow from code commit to cluster-wide observability:

* **Automated CI Pipeline:** Every code change triggers a **GitHub Actions** workflow, successfully building and pushing the updated Docker image to **Docker Hub**.
* **GitOps-Driven Deployment:** **ArgoCD** maintains a "Healthy" and "Synced" cluster state. The deployment history confirms that recent architectural updates—such as scaling the application and introducing a **Redis Database** layer—were automatically reconciled from the Git repository.
* **Infrastructure Monitoring:** A centralized **Grafana** dashboard visualizes real-time performance metrics, showing critical data such as Cluster Memory usage (13.2%) and CPU consumption (0.72%).
* **Centralized Logging Stack:** Utilizing **Loki**, the system aggregates logs across all namespaces (ArgoCD, Kube-System, and Monitoring), providing granular visibility into the behavior of the `agri-app` and supporting infrastructure.

---

<img width="1280" height="96" alt="image" src="https://github.com/user-attachments/assets/a3f65f2e-4370-4cd7-b1db-68d3b7c2c84e" />

<img width="571" height="492" alt="image" src="https://github.com/user-attachments/assets/cb6544ff-a0d0-4a21-b641-d6ee4e30757c" />

<img width="1280" height="513" alt="image" src="https://github.com/user-attachments/assets/24812741-4ee5-444e-ba2a-67938b6146bf" />

---

### **Project Implementation & Technical Validation**

The following documentation provides visual proof of the project's adherence to modern DevOps standards, specifically addressing CI/CD automation, GitOps workflows, and deep system observability.

#### **1. Automated Continuous Integration (CI)**

* **Pipeline Execution**: Every code push to the `main` branch triggers an automated **GitHub Actions** workflow.
* **Build & Push Validation**: The CI pipeline successfully builds the application into a Docker container and pushes it to **Docker Hub**.
* **Artifact Consistency**: Timestamps and commit hashes (e.g., `55bd670`) across GitHub and Docker Hub confirm that the image tagged as `latest` is always up-to-date with the source code.

#### **2. Declarative GitOps Deployment (CD)**

* **ArgoCD Orchestration**: Deployment is managed via **ArgoCD**, ensuring the cluster state is always "Synced" with the Kubernetes manifests in the repository.
* **Database Integration**: To provide a complete environment, a **Redis Database** layer was introduced via `redis.yaml`, appearing as a healthy deployment in the resource tree.
* **Auditability**: The **History and Rollback** feature tracks every architectural change (such as scaling replicas or adding services), allowing for instant recovery and 100% traceability of cluster modifications.

#### **3. Full-Stack Observability & Monitoring**

* **Infrastructure Metrics**: A professional **Grafana** dashboard provides real-time visualization of cluster health, including precise tracking of **Cluster Memory usage (13.2%)** and **Cluster CPU usage (0.72%)**.
* **Granular Performance Tracking**: Custom **PromQL** queries are utilized to monitor pod-level CPU and memory consumption, ensuring resource efficiency for the `agri-app` services.
* **Centralized Logging**: Using **Grafana Loki**, logs are aggregated from multiple namespaces—including `argocd`, `monitoring`, and `kube-system`—providing a unified interface for debugging and auditing the entire platform.

---

