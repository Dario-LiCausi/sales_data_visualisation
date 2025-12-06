This project is a local pilot system for an electronics retail chain.
It processes raw sales data, removes personal information, loads the cleaned data into a MySQL database, and visualises the results using Grafana.
The interface starts as a CLI and will later include a GUI.

Project Summary

The client wants to understand:

• Store performance by sales and profit
• Category and product-level trends
• Customer buying habits
• Payment methods including cash
• How purchasing behaviour changes throughout the day

Data must be cleaned and anonymised at the earliest stage.
The system must run locally on Windows or macOS and be easy to scale to more branches or to the cloud.

The raw data is provided as a TXT file simulating a full day of sales  with multiple products per transaction.