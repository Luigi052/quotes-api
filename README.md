# Quotes API - DevOps Demo (Docker + Minikube + GitHub Actions + Azure VM)

Este projeto é um pacote mínimo para a aula de DevOps:

- API em FastAPI (`app.py`)
- Testes automatizados simples de API (`tests/test_app.py`)
- Containerização com Docker (`Dockerfile`)
- Manifests Kubernetes para Minikube (`k8s/`)
- Pipeline CI/CD com GitHub Actions (`.github/workflows/ci-cd.yml`)

## Passos principais

1. Suba uma VM Linux na Azure, instale Docker, kubectl e Minikube.
2. Clone este repositório na sua conta GitHub.
3. Configure os *secrets* do GitHub Actions:
   - REGISTRY_URL
   - REGISTRY_USER
   - REGISTRY_TOKEN
   - REGISTRY_NAMESPACE
   - AZURE_VM_HOST
   - AZURE_VM_USER
   - AZURE_VM_SSH_KEY
4. Ajuste o `k8s/deployment.yaml` substituindo REGISTRY_URL, REGISTRY_NAMESPACE e IMAGE_TAG se quiser usar valores fixos.
5. Na VM, certifique-se de que o cluster Minikube está ativo e que `kubectl` funciona.
6. Faça um push para `main` e acompanhe o workflow `ci-cd` no GitHub Actions.

Após a execução bem-sucedida, a API deverá estar acessível em:

```bash
curl http://IP_PUBLICO_DA_VM:30080/healthz
```
