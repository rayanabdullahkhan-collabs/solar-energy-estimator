import math

# Simple Solar Panel Energy Output Estimator

# Panel parameters
panel_area = 1.6  # m² (typical panel)
panel_efficiency = 0.18  # 18% efficient panel

# Average solar irradiance (W/m²) for different cities
irradiance = {
    "Dhaka": 180,
    "Ann_Arbor": 150,
    "Los_Angeles": 220,
    "Stanford": 210
}

def estimate_energy(city, hours=5):
    if city not in irradiance:
        return "City not in database."
    power = irradiance[city] * panel_area * panel_efficiency
    energy_output = power * hours  # watt-hours
    return f"Estimated daily energy in {city}: {energy_output/1000:.2f} kWh"

if __name__ == "__main__":
    for city in irradiance:
        print(estimate_energy(city))
