# NeuroCurve 🧠📈

**A predictive brain-behavior modeling toolkit** exploring how variables like age, BMI, and functional assessments influence neurological risk over time.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Generate age-functional assessment risk](#1-generate-age-functional-assessment-risk)
  - [2. Visualize risk curve](#2-visualize-risk-curve)
- [Model Training](#model-training)
- [Examples](#examples)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

---

## Overview
NeuroCurve builds dynamic risk curves for neurological conditions (e.g., Alzheimer’s) by simulating how risk evolves across age and functional assessment scores. It combines supervised learning (e.g., Random Forests) with visualization tools to help interpret risk trajectories for individual patients.

---

## Key Features
- **Age-Risk Simulation**: Modify patient age and optionally FunctionalAssessment scores to predict risk.
- **Flexible Feature Support**: Any feature (e.g., BMI, ADL, FunctionalAssessment).
- **Easy-to-Use API**: Plug in your trained `model` and patient features to visualize risk over time.
- **Visualization**: Clear plots showing predicted risk progression.

---

## Installation
```bash
git clone https://github.com/Spakshots/NeuroCurve.git
cd NeuroCurve
pip install -r requirements.txt
