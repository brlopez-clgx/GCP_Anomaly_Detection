# GCP_Anomaly_Detection

Google Cloud Platform is a crucial tool for CoreLogic’s Science and Analytics team. It enables the storage and analysis of the company’s data assets among other tasks. Some common tools are Cloud Storage and BigQuery used for storage and Vertex AI which provides artificial intelligence and machine learning capabilities. As volume of data and use of machine learning methods grow so does the need to effectively monitor GCP cost. The goal of my project is to create a system to monitor and detect anomalies using machine learning and analytics methods.

The architecture I used is Isolation Forest, a tree-based ensemble algorithm. The model constructs binary decision trees to isolate data points. Isolation Forest measures a data point path length through a tree. The shorter the path, in other words the easier it is to isolate the point the more  likely the point is to be an anomaly. The outputs of the model is a label 1 being normal and -1 being an anomaly  along with a confidence score reflecting the model’s confidence in its prediction.


This repository contains a Jupyter Notebook containing model code.
