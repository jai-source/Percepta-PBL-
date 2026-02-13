# Percepta-PBL-



🧠 Percepta
Implementation of a Perceptual Computing Interface (PCI)

A unified multi-modal human–computer interaction system that enables full computer control using head movement, hand gestures, and eye tracking — built from fundamental Digital Image Processing principles.

🚀 Overview

Percepta is an experimental implementation of a Perceptual Computing Interface (PCI) — a modular framework that translates human perceptual movements into digital computer actions.

Unlike existing systems that focus on a single input modality (only eye tracking or only gesture control), Percepta integrates:

🟢 Head-based cursor control

🟣 Hand gesture navigation

🔵 Eye tracking & blink-based typing

All built using custom mathematical models and tunable interaction constants.

🎯 Vision

The goal of Percepta is to move beyond traditional input devices (mouse & keyboard) and create a unified interaction layer that:

Enhances accessibility

Enables hands-free computing

Demonstrates explainable perceptual control

Provides customizable sensitivity via mathematical constants

Serves as a foundation for future perceptual computing research

🏗 Architecture

Percepta is built around the Perceptual Computing Interface (PCI) layer.

Perceptual Input  →  Mathematical Model  →  PCI Layer  →  OS Action


Each perceptual module follows the same philosophy:

Action = α × Perceptual Change


Where:

α = Tunable interaction constant

Perceptual Change = Head displacement / Gesture velocity / Eye aspect ratio variation
