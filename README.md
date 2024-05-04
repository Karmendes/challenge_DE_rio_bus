# Rio de Janeiro BRT Data Pipeline
This project is a data pipeline built to collect information about buses from the BRT system in Rio de Janeiro through an API, process it, and store it in a PostgreSQL database. The pipeline consists of three main stages:

API Data Collection and S3 Storage: Using Python, the data is fetched from the BRT API and stored as CSV files in an Amazon S3 bucket.
Transfer to PostgreSQL: The data stored in S3 is then retrieved using Python and transferred to a PostgreSQL database.
Data Transformation with DBT: After transfer to PostgreSQL, a DBT model is executed to transform the data as needed and create a final table for analysis.
Additionally, each of these stages is encapsulated as a route in a Flask API, allowing tasks to be triggered individually as needed.

Environment Setup
This project runs within a Docker Compose environment, which facilitates the creation and execution of containers for each component of the pipeline. Make sure you have Docker and Docker Compose installed on your machine before starting.

Running the Pipeline
To run the pipeline, follow these steps:

Clone this repository to your local machine.
Navigate to the project directory.
Run the command docker-compose up to start the Docker environment.
Once all containers are up and running, you can access the Airflow interface at http://localhost:8080 to monitor and manage the DAG.
The DAG is configured to be triggered automatically at regular intervals, but you can also trigger it manually as needed.
Contributing
If you wish to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!