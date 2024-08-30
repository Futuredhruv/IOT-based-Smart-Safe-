# IOT-based-Smart-Safe
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
</head>
<body>

<h1>IoT-Based Smart Safe Security System</h1>

<p>This project implements a smart safe security system using IoT (Internet of Things) technology. The system is designed to detect various security events such as unauthorized access, motion detection, and more, and then upload these events to a Firebase database for real-time monitoring and alerts.</p>

<h2>Project Overview</h2>
<p>The core components of the system include:</p>
<ul>
    <li><strong>Microcontroller:</strong> A microcontroller like Arduino that reads sensor data (e.g., door sensors, motion detectors) and communicates with the connected devices.</li>
    <li><strong>Sensors:</strong> Various sensors like motion sensors and door sensors that detect events related to security breaches.</li>
    <li><strong>Serial Communication:</strong> The microcontroller communicates with a Python script running on a computer or Raspberry Pi through a serial connection.</li>
    <li><strong>Firebase Integration:</strong> The Python script uploads the event data to Firebase Firestore, where it can be stored and accessed remotely.</li>
</ul>

<h2>Python Script</h2>
<p>The Python script reads data from the serial port, processes the information, and uploads it to Firebase Firestore. The script ensures that all detected events are logged with a timestamp in the Firebase database.</p>

<h2>Example Output</h2>
<p>Here’s an example of what the output might look like when the system is running:</p>

<pre>
<code>
2024-08-28 14:32:15,123 - INFO - Serial communication initialized successfully.
2024-08-28 14:32:15,567 - INFO - Firebase initialized successfully.
2024-08-28 14:32:15,567 - INFO - Starting main loop. Listening for data...

2024-08-28 14:32:18,789 - INFO - Received data: Door Opened!
2024-08-28 14:32:18,900 - INFO - Data uploaded to Firebase: Door Opened!

2024-08-28 14:32:25,456 - INFO - Received data: Motion Detected!
2024-08-28 14:32:25,567 - INFO - Data uploaded to Firebase: Motion Detected!

2024-08-28 14
