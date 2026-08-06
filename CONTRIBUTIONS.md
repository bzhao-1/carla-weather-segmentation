# Attribution and project scope

This repository began as a fork of [CSAILVision/semantic-segmentation-pytorch](https://github.com/CSAILVision/semantic-segmentation-pytorch). The upstream project supplied the core scene-parsing package, model builders, ADE20K training/evaluation code, and BSD 3-Clause license.

## CARLA capstone work

The Carleton College CV4AD team adapted the framework for its weather-robustness study. Changes represented in this fork include:

- 29-class CARLA dataset support and color mapping;
- deterministic-weather and mixed-weather data-preparation notebooks;
- HRNetV2 and MobileNetV2 configuration files for CARLA experiments;
- cross-weather, multi-process evaluation and visualization;
- class-frequency and per-class mIoU analysis notebooks; and
- model/configuration changes needed for CARLA training.

This was collaborative academic work. The repository does not claim that Ben Zhao authored every CARLA-specific change or the upstream framework. Commit history is retained so individual changes can be inspected.

## Subsequent repository maintenance

The 2026 documentation and maintenance pass added repository-level CI, portable paths, dependency corrections, configuration tests, and clearer separation of upstream and team work. It did not add new experiments or alter the reported capstone metrics.
