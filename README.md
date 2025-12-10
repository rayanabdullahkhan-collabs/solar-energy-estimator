# Solar Energy Estimator ☀️

A tiny Python tool to **estimate daily solar energy generation** for a 1.6 m² panel in different locations using average solar irradiance values.

This project reflects my interest in **sustainable energy systems** and how geography, irradiance, and panel efficiency combine to shape real-world output.

---

## 🔍 What This Project Does

- Estimates **daily energy output (kWh)** for a simple solar panel.
- Compares different cities (e.g., Dhaka, Ann Arbor, Los Angeles, Stanford).
- Shows how **irradiance × area × efficiency** affect usable energy.

---

## 🧠 Core Idea

Energy output is approximated with:

\[
\text{Power (W)} = \text{Irradiance (W/m²)} \times \text{Panel Area (m²)} \times \text{Efficiency}
\]

Then:

\[
\text{Energy (Wh)} = \text{Power} \times \text{Sunlight Hours}
\]

The script prints estimated **kWh per day** for each location.

---

## 🛠 Requirements

- Python 3.x

No external libraries needed.

---

## 🚀 Usage

```bash
python solar_estimator.py
