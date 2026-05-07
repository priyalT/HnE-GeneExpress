# HnE-GeneExpress: Histology-Guided Gene Expression Imputation System

Histology-guided gene expression imputation using H&E tissue images and spatial transcriptomics data.

> Status: Ongoing research-oriented project under active development.

---

## Overview

HnE-GeneExpress is a deep learning project focused on predicting subspot gene expression patterns from H&E histology images.

Spatial transcriptomics technologies such as Visium provide spatially resolved gene expression measurements, but each capture spot typically contains multiple cells, limiting resolution. This project explores whether morphological information from histology images can be used to infer finer-grained transcriptional patterns.

The pipeline combines pretrained histopathology encoders, lightweight neural networks, and spatial smoothing techniques to model relationships between tissue morphology and spatial gene expression.

---
## Core Objectives

- Predict gene expression from H&E histology images
- Improve spatial resolution beyond Visium spot-level measurements
- Explore relationships between tissue morphology and transcriptional states
- Build a reproducible and modular computational pipeline for spatial transcriptomics analysis

---

## Pipeline Architecture

```text
H&E Histology Image
        ↓
Patch Extraction
        ↓
Pretrained Histology Encoder
(UNI / ResNet50 / CTransPath)
        ↓
Feature Embeddings
        ↓
MLP Expression Predictor
        ↓
Spatial Smoothing
        ↓
Predicted Gene Expression