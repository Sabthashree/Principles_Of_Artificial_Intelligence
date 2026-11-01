# Exercise 10b: Fuzzy Inference System

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def run_fuzzy_system():
    # Step 1: Define the fuzzy variables (input: temperature, output: fan speed)
    temperature = np.arange(0, 41, 1)  # Temperature from 0 to 40 degrees Celsius
    fan_speed = np.arange(0, 11, 1)     # Fan speed from 0 to 10

    # Step 2: Define fuzzy membership functions
    temp_low = fuzz.trimf(temperature, [0, 0, 20])
    temp_medium = fuzz.trimf(temperature, [10, 20, 30])
    temp_high = fuzz.trimf(temperature, [20, 40, 40])

    fan_low = fuzz.trimf(fan_speed, [0, 0, 5])
    fan_medium = fuzz.trimf(fan_speed, [2, 5, 8])
    fan_high = fuzz.trimf(fan_speed, [5, 10, 10])

    # Step 3: Visualize the membership functions
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(temperature, temp_low, label='Low')
    plt.plot(temperature, temp_medium, label='Medium')
    plt.plot(temperature, temp_high, label='High')
    plt.title("Temperature Membership Functions")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Membership Degree")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(fan_speed, fan_low, label='Low')
    plt.plot(fan_speed, fan_medium, label='Medium')
    plt.plot(fan_speed, fan_high, label='High')
    plt.title("Fan Speed Membership Functions")
    plt.xlabel("Fan Speed")
    plt.ylabel("Membership Degree")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Step 4: Fuzzification
    temperature_input = 28
    temp_low_level = fuzz.interp_membership(temperature, temp_low, temperature_input)
    temp_medium_level = fuzz.interp_membership(temperature, temp_medium, temperature_input)
    temp_high_level = fuzz.interp_membership(temperature, temp_high, temperature_input)

    # Step 5: Apply fuzzy rules
    fan_low_level = temp_low_level
    fan_medium_level = temp_medium_level
    fan_high_level = temp_high_level

    # Step 6: Defuzzification
    aggregated_membership = (fan_low * fan_low_level +
                             fan_medium * fan_medium_level +
                             fan_high * fan_high_level)
    
    fan_output = fuzz.defuzz(fan_speed, aggregated_membership, 'centroid')

    # Step 7: Print results
    print(f"Temperature: {temperature_input}°C")
    print(f"Fuzzified fan speed: {fan_output:.2f}")

if __name__ == "__main__":
    run_fuzzy_system()
