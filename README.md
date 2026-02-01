# 🌾 Agriculture Platform - DevOps Implementation

This project demonstrates a complete, automated CI/CD pipeline and a comprehensive monitoring system for a containerized application.

## 🛠 Technology Stack

* **Application Framework:** Python (Flask)
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube)
* **CI/CD Pipeline:** GitHub Actions & ArgoCD
* **Observability:** Prometheus, Grafana, and Loki (Loki-stack)

## 🚀 CI/CD Workflow

1. **Continuous Integration:** Upon pushing code to the `main` branch, a GitHub Action automatically builds the Docker image and pushes it to Docker Hub as `aslq/agri-app:latest`.
2. **Continuous Deployment:** ArgoCD monitors the `agri-chart/templates` directory in the GitHub repository and automatically synchronizes the cluster state with the manifest files.
3. **Deployment Architecture:** The application is deployed in the `default` namespace using the `agri-app` Deployment and exposed via the `agri-app-service` Service.

## 📊 Monitoring & Observability

A professional Grafana dashboard has been established to provide real-time insights into the project's health:

* **Cluster Resource Usage:** High-level overview of CPU and Memory consumption across the entire cluster.
* **Application Performance:** Granular monitoring of CPU and Memory specifically for the `agri-app` pods using PromQL.
* **Centralized Logging:** Real-time application logs are aggregated and visualized using Loki.

<img width="622" height="572" alt="image" src="https://github.com/user-attachments/assets/87d2e45a-4676-4489-abd5-98e93b4d72e1" />

<img width="2559" height="1333" alt="image" src="https://github.com/user-attachments/assets/50861230-1ab3-46e0-9441-bb0ccfecbac5" />

### **1. Project Structure and CI/CD Implementation**

> **Screenshot: Project Directory Structure**
> "The repository is organized with a clear separation of concerns. The `.github/workflows` directory manages automated build processes, while the `agri-chart/templates` folder contains the core Kubernetes manifests, including `deployment.yaml` and `service.yaml`."

---

### **2. ArgoCD Continuous Deployment**

> **Screenshot: ArgoCD Application Overview**
> "ArgoCD maintains a 'Healthy' and 'Synced' state for the `agri-proj-new` application. It tracks the GitHub repository's `main` branch and ensures the live cluster state matches the defined manifests in `agri-chart/templates`."

> **Screenshot: Resource Tree and Live Objects**
> "The visual resource tree illustrates the successful deployment of the `agri-app-service` and the corresponding `agri-app` Deployment. This confirms that all network and compute resources are correctly provisioned within the Kubernetes cluster."

---

### **3. Monitoring and Observability (Grafana & Prometheus)**

> **Screenshot: Professional Monitoring Dashboard**
> "A centralized Grafana portal provides access to specialized dashboards, including the 'Agriculture Platform Professional Monitoring' suite. This environment allows for real-time tracking of Kubernetes pod metrics and system performance."

> **Screenshot: Resource Usage Analytics**
> "Custom PromQL queries are utilized to calculate precise resource consumption. By analyzing metrics like `container_cpu_usage_seconds_total`, the system provides accurate data on cluster-wide CPU and memory usage."

---

### **4. Centralized Logging (Loki)**

> **Screenshot: Live Application Logs**
> "Integrated logging via Grafana Loki allows for high-velocity log aggregation. Developers can monitor live application streams to quickly identify and troubleshoot runtime events."

> **Screenshot: Multi-Namespace Log Filtering**
> "The logging system supports granular filtering across different namespaces, such as `argocd`, `monitoring`, and the `default/agri-app` production environment, ensuring comprehensive observability across the entire stack."

<img width="2559" height="1313" alt="image" src="https://github.com/user-attachments/assets/eb2aa151-4291-4993-acb0-8297ab7a55b2" />

### **1. Repository Architecture & CI Configuration**

> **Screenshot: Project Directory Structure**
> "The project follows a standard cloud-native structure. The `.github/workflows` directory houses the `docker-build.yml` file for automated integration, while the `agri-chart/templates` folder contains the Kubernetes manifests—`deployment.yaml` and `service.yaml`—required for cluster orchestration."

---

### **2. Continuous Deployment via ArgoCD**

> **Screenshot: ArgoCD Application Status**
> "The `agri-proj-new` application is successfully managed by ArgoCD, maintaining a **Healthy** and **Synced** status. It is configured to automatically track the `HEAD` of the GitHub repository and synchronize changes into the `default` namespace."

> **Screenshot: Live Resource Synchronization**
> "The ArgoCD resource tree confirms the successful provisioning of live objects. This includes the `agri-app-service` (SVC) and the `agri-app` Deployment, which manages the active pods within the cluster."

---

### **3. Advanced Monitoring & Resource Analytics**

> **Screenshot: Cluster Performance Dashboard**
> "Our comprehensive Grafana dashboard provides real-time visibility into cluster health. Key metrics such as **Cluster Memory Usage** (currently at 13.2%) and **Cluster CPU Usage** (currently at 0.72%) are visualized to ensure optimal resource allocation."

> **Screenshot: PromQL Metric Validation**
> "The monitoring system utilizes precise PromQL queries to aggregate data. By calculating the rate of change for counters like `container_cpu_usage_seconds_total`, we generate accurate performance trends for all containerized workloads."

---

### **4. Centralized Observability & Logging**

> **Screenshot: Integrated Logging with Loki**
> "Real-time application logs are aggregated using Grafana Loki. This centralized logging system allows for rapid troubleshooting by streaming live events directly from the ArgoCD application controller and other system components."

> **Screenshot: Namespace & App Filtering**
> "The observability stack supports granular filtering, allowing users to pivot between logs for core system services (like `kube-system`) and application-specific logs for the `default/agri-app` environment."

<img width="2559" height="1424" alt="image" src="https://github.com/user-attachments/assets/d201717b-c5bd-4671-b68e-bac4510fb7e1" />

Agriculture Platform: Professional Monitoring Dashboard
This high-level overview demonstrates the complete observability stack for the agri-app, integrating real-time metrics and logs into a single, unified view.

1. Full Dashboard Overview
The comprehensive dashboard provides a "single pane of glass" view into the application's health, combining availability, resource consumption, and live execution logs.

Application Availability (Uptime): A discrete timeline tracking the operational status of the agri-app pod over time.
Resource Utilization: Side-by-side graphs for CPU and Memory, allowing for quick correlation between performance spikes and resource limits.
Live Application Logs: A bottom-panel stream powered by Loki, providing immediate context for the metrics shown above.
2. Performance Metrics (CPU & Memory)
CPU Usage (%): Tracks the processing power consumed by the application. The cleaned legend (right) identifies specific pods and system components, ensuring the agri-app is monitored without technical clutter.
Memory Usage (MB): Provides a clear visualization of the application's memory footprint (approx. 42 MB). The simplified legend shows the specific pod instance (agri-app-6b7df5f68-z92nd), facilitating precise capacity planning.
3. Log Aggregation (Loki)
Live Application Logs: This panel captures and formats real-time logs directly from the container.
Clean Formatting: Using the | json | line_format parser, raw JSON data is converted into human-readable text (e.g., tracking GET /update requests with 200 OK status).
Incident Response: Critical warnings and errors are highlighted, enabling rapid debugging directly from the Grafana interface.
