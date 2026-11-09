# Azure DevOps CI/CD Demo

A demonstration project showcasing an automated CI/CD pipeline
using Azure DevOps Pipelines and a GitHub repository.

## Technologies

- Azure DevOps Pipelines
- GitHub
- Python 3.12
- YAML
- Microsoft-hosted Ubuntu agent

## Pipeline Overview

The pipeline is triggered automatically when changes
are pushed to the main branch.

It consists of four stages:

### 1. Build
Compiles the Python application.

### 2. Test
Runs automated unit tests using Python unittest.

### 3. Publish
Publishes the application as a build artifact.

### 4. Deploy
Downloads the published artifact, deploys it to a
temporary test environment on the Microsoft-hosted agent,
and verifies that the application runs successfully.

## CI/CD Workflow

GitHub Repository → Azure DevOps Pipeline → Build → Test → Publish → Deploy

## Project Structure

- src/ - Application source code
- tests/ - Automated unit tests
- azure-pipelines.yml - CI/CD pipeline definition
- requirements.txt - Python dependencies

## Purpose

This project demonstrates practical experience with
pipeline automation, YAML configuration, automated testing,
artifact publishing, and deployment verification.
