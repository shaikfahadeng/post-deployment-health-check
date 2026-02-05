# Post Deployment Health Check Automation

## Problem Statement
In many production environments, deployments succeed technically but fail functionally, leading to high-severity incidents due to lack of immediate validation.

## Solution
This project implements a lightweight post-deployment health check that validates application availability immediately after deployment and prevents faulty releases from progressing further.

## How It Works
1. Code is committed to the repository
2. Azure DevOps pipeline is triggered
3. Pipeline runs a Python-based health check script
4. If the application is reachable, the pipeline succeeds
5. If the application is unreachable, the pipeline fails automatically

## CI/CD Pipeline Overview
- CI/CD tool: Azure DevOps
- Agent: Microsoft-hosted Ubuntu (ubuntu-latest)
- Validation mechanism: Script exit codes (0 = success, 1 = failure)

## Key Benefits
- Early detection of faulty deployments
- Reduced incident recurrence
- Improved deployment reliability
- Clear automation-based decision making

## Technologies Used
- Python
- Azure DevOps Pipelines
- GitHub
