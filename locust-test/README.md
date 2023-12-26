# Stress Testing with Locust

## Introduction
This project uses [Locust](https://locust.io/), a scalable performance testing tool, to conduct stress tests on web applications.

## Stress Testing
Stress testing involves simulating a high volume of users accessing an application to assess how it handles heavy loads.

## Installing and Run Locust
Install and Run Locust using pip:
```python
pip install locust
locust -f locustfile.py --class-picker
