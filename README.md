# LLM Summarizer

A DevOps project deploying a text summarization API using `facebook/bart-base` on Kubernetes with a GitHub Actions CI/CD pipeline.

## Features
- FastAPI app for text summarization.
- Dockerized deployment.
- Kubernetes orchestration with HPA.
- Automated CI/CD with GitHub Actions.

## Setup
1. Clone the repo.
2. Set up a Kubernetes cluster (e.g., Minikube).
3. Add `GHCR_TOKEN` and `KUBE_CONFIG` to GitHub Secrets.
4. Push to `main` to trigger deployment.

## Testing
```bash
curl -X POST http://<service-ip>/summarize -H "Content-Type: application/json" -d '{"text": "Your text here", "max_length": 50, "min_length": 10}'