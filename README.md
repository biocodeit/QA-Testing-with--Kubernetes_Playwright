# QA-Testing-with--Kubernetes_Playwright
Amino Guesser is a web-based interactive quiz game designed to help users playfully memorize and learn.  This repository demonstrates a complete, professional Quality Assurance (QA) workflow using modern DevOps practices. It serves as an end-to-end showcase of my skills in automated testing, containerization, and deployment on a Kubernetes cluster.

## Key Highlights for Quality Assurance
This project showcases core competencies required for a QA Engineer role, including:

- **Automated Testing**: Implementation of an end-to-end test suite using Playwright to mimic user interactions, such as navigating the game and clicking buttons. The tests validate the correctness of the game logic and the integrity of visual assets (SVGs).

- **Containerization**: The application and the testing environment are independently containerized using Docker. This ensures a reproducible and isolated environment for testing, eliminating issues with dependencies.

- **Kubernetes-based Deployment**: The entire QA environment is orchestrated using Kubernetes (Minikube). A dedicated Job runs the test suite within its own pod, separate from the main application, reflecting a robust, real-world testing approach.

- **Debugging and Maintenance**: The configuration includes a hostPath volume to automatically export test reports and screenshots, addressing common challenges in a containerized QA environment. The setup also demonstrates a systematic approach to debugging common Kubernetes and Docker issues.(Not working!)

```
.
├── Kubernetes-files
|   ├── application.yaml          # Kubernetes Deployment and Service for the app
|   └── test.yaml                 # Kubernetes Job for running the test suite
├── amino-guesser/
│   ├── assets/               # SVG and SDF files for amino acids
│   ├── index.html            # The main game page
│   ├── style.css             # Styling for the application
│   ├── game.js               # Core game logic
│   |── aminoAcid.js          # Amino acid data
|   └── Dockerfile                # Dockerfile for building the web app image
└── playwright-tests/
    ├── Dockerfile # Dockerfile for building the test runner image
    ├── reports/
    ├── pages/
    ├── conftest.py
    ├── pytest.ini
    └── tests/test_svg.py           # Playwright tests
```

## Technologies Used
- Front-end: HTML, CSS, JavaScript, 3Dmol.js, jQuery
- Containerization: Docker
- Orchestration: Kubernetes (with Minikube)
- Testing: Playwright, Pytest

# How to Run Locally
Follow these steps to set up the project locally using Minikube.

# Prerequisites
- Docker
- Minikube
- kubectl
