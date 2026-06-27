# allen-on-a-chip
This is for the Hack Club Stardance challenge. Allen on a Chip is an ESP32-based platform that takes real biophysical models of human/mouse neurons and connects them to physical sensors and outputs. This will include OLED displays and certain sensors such as a motion or humidity/temperature sensor.

AI Declaration: AI was used occasionally for solely planning and searching purposes.

## Stage 1: Python tests
The allensdk and neuron libraries are some of the most popular libraries for coding projects in the world of computational neuroscience. One issue is that while a couple embedded systems can run Python, since this project will be on an ESP32 and can be computationally demanding, another language such as the Arduino language or C++ would be more befitting.

Regardless, Python can still serve a use in this project, as we can test the models that I have downloaded in the allensdk library, and then do some basic development before translating the inner workings into another language for the ESP (keep in mind that while it does have better processing power relative to an Arduino Nano, for example, RAM is sitll a limitation for this project).

Here are the items that I will acheive in this stage:

1. test out the GLIF, perisomatic, and the all-active models in the allensdk/neuron libraries
2. attempt to implement a reduced version of the perisomatic and the all-active models, since they rely on morphology and are therefore more complex
3. investigate the allensdk library to look at how exactly neurons are structured

In addition, here are the Allen neuron IDs for the test models in this stage:

- glif: 333785935 
- perisomatic: 490387590
- all-active: 333785935