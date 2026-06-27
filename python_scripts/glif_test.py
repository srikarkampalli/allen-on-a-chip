"""
This specific test will test the GLIF model.
"""

# Import in the AllenSDK libraries for simulation
import allensdk.core.json_utilities as json_utilities
from allensdk.model.glif.glif_neuron import GlifNeuron

# Matplotlib for plotting, and pathlib for path handling
import matplotlib.pyplot as plt
import os
from pathlib import Path

# Import memory tracker
import tracemalloc

tracemalloc.start()

parent_path = Path(__file__).resolve().parent.parent
os.chdir(parent_path / "neuron_models" / "glif")


def test_glif_model(neuron_config_json_path):
    """
    This function tests a GLIF model from the Allen Cell Types Database by loading the neuron based on config files and sending a stimulus.
    After, the voltage, threshold, and spike times are returned.
    """

    # Load in the neuron
    neuron_config = json_utilities.read(neuron_config_json_path)
    neuron = GlifNeuron.from_dict(neuron_config)

    # This property ensures that there will be no NaN values.
    neuron.spike_cut_length = 0

    # Sending a basic stimulus over time of 150 pA
    stimulus = [0] * 100 + [150e-12] * 100 + [0] * 100

    # Running and obtaining results
    output = neuron.run(stimulus)

    voltage = output["voltage"]
    threshold = output["threshold"]
    spike_times = output["interpolated_spike_times"]

    return voltage, threshold, spike_times


# Create the path to the neuron config file
neuron_config_json_path = "neuron_config.json"

# Obtain resutls from the test
glif_voltage, glif_threshold, glif_spike_times = test_glif_model(
    neuron_config_json_path
)

# Use matplotlib to plot the results
plt.plot([-0.06] * len(glif_voltage) + glif_voltage, label="Voltage Change")
plt.plot(-glif_threshold, label="Threshold")

plt.scatter(
    glif_spike_times / 5e-5,
    [0] * len(glif_spike_times),
    color="red",
    label="Spike Times",
)

plt.xlabel("Time Step")
plt.ylabel("Voltage")

plt.title("GLIF Neuron Simulation")
plt.legend()
plt.show()

# Get memory usage
current, peak = tracemalloc.get_traced_memory()

print(f"Current: {current / (1024 * 1024):.2f} MB")
print(f"Peak: {peak / (1024 * 1024):.2f} MB")

tracemalloc.stop()
