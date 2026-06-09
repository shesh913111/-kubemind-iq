# KubeMind IQ

## Reason. Retrieve. Resolve.

KubeMind IQ is an AI-powered AKS Troubleshooting Agent built for the Microsoft Agents League Hackathon.

## Problem Statement

Troubleshooting Kubernetes and Azure Kubernetes Service (AKS) incidents often requires engineers to manually inspect logs, events, runbooks, and documentation.

## Solution

KubeMind IQ leverages Foundry IQ-inspired knowledge retrieval and multi-step reasoning to diagnose incidents, identify root causes, and recommend remediation actions.

## Features

* Incident Summary Generation
* Multi-Step Reasoning
* Root Cause Analysis
* AKS Troubleshooting Guidance
* Confidence Scoring
* Foundry IQ Knowledge Layer

## Supported Incidents

* CrashLoopBackOff
* ImagePullBackOff
* FailedScheduling
* OOMKilled

## Architecture

User → KubeMind IQ → Foundry IQ Layer → Reasoning Engine → Root Cause Analysis → Recommendations

## Technologies Used

* Python
* Streamlit
* Microsoft Foundry
* Foundry IQ
* Azure Kubernetes Service (AKS)

## Challenge Track

Reasoning Agents
