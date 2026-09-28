# Adaptive Visual Mapping for UAV-based 3D Reconstruction

An academic graduation project investigating visual mapping, viewpoint adaptation, and 3D reconstruction methodologies for Unmanned Aerial Vehicles (UAVs).

---

## Project Overview

The objective of this project is to develop an adaptive visual mapping framework for UAVs that enhances 3D reconstruction quality and efficiency. By coupling synthetic data generation and simulation with computer vision and reconstruction pipelines, the system aims to dynamically plan and adapt mapping trajectories based on reconstruction feedback.

---

## High-Level Pipeline

```
+------------------+      +-------------------+      +----------------------+
|  UAV Simulation  | ---> |  Computer Vision  | ---> |   3D Reconstruction  |
| (Unity Platform) |      | (Feature/Sensors) |      | (Point Cloud / Mesh) |
+------------------+      +-------------------+      +----------------------+
         ^                                                      |
         |                +------------------+                  |
         +--------------- |  Active Mapping  | <----------------+
                          | (Adaptive Path)  |   Reconstruction
                          +------------------+      Feedback
```

1. **Visual Data Acquisition**: UAV simulated sensors capture visual observation streams (RGB / depth) from defined viewpoints.
2. **Computer Vision Processing**: Feature detection, tracking, and geometric estimation across captured views.
3. **3D Reconstruction**: Incremental structure estimation, point cloud synthesis, and mesh generation.
4. **Adaptive Mapping Feedback**: Ongoing reconstruction uncertainty and geometric coverage inform next-best-view or path adaptation strategies.

---

## Project Structure

```
├── AdaptiveVisualMapping/   # Unity 6 project (simulation, environment, sensors)
├── ActiveMapping/           # Adaptive path planning & viewpoint selection strategies
├── ComputerVision/          # Visual processing pipelines, feature extraction & Python environment
│   ├── .venv/               # Virtual environment (managed via uv)
│   ├── src/                 # Computer vision source code
│   ├── tests/               # Environment & module test suites
│   └── requirements.txt     # Python dependencies
├── Dataset/                 # Synthetic / captured datasets and data loaders
├── Documentation/           # Technical reports, notes, and architectural diagrams
├── Evaluation/              # Benchmarks, quantitative metrics, and reconstruction validation
└── Reconstruction/          # 3D reconstruction algorithms (SfM, point clouds, surface generation)
```

---

## Environment & Prerequisites

- **Unity**: Unity 6 (6000.6.1f1) with Unity MCP support.
- **Python**: Managed with `uv` (using Python 3.12 compatibility runtime).
- **Core Dependencies**:
  - `numpy`
  - `opencv-python`
  - `open3d`
  - `scipy`
  - `matplotlib`

---

## Current Development Status

- [x] Initial Unity project setup and version control configuration.
- [x] Project workspace organization and module skeleton.
- [x] Python virtual environment creation and core dependency installation.
- [ ] UAV flight dynamics & sensor capture implementation *(Planned)*.
- [ ] Computer vision and reconstruction pipeline implementation *(Planned)*.
- [ ] Adaptive active mapping closed-loop integration *(Planned)*.
