from locust import HttpUser, task, between

class WebAppUser(HttpUser):
    wait_time = between(1, 2)  # Simulates a user waiting between 1 and 5 seconds between tasks
    host = "http://127.0.0.1:5000" 

    @task
    def predict(self):
        """
        Test the /predict endpoint of the Flask app.
        """
        with open("locust_test_files/test_image.jpg", "rb") as image:  
            response = self.client.post(
                "/predict",  
                files={"image": image},
                data={"model": "refined_2.keras"}  
            )
            print(f"Prediction response: {response.text}")

    @task
    def train_model(self):
        """
        Test the /train-model endpoint of the Flask app.
        """
        with open("locust_test_files/sample_train_folder.zip", "rb") as zip_file:  
            response = self.client.post(
                "/train-model",  
                files={"zip_file": zip_file}
            )
            print(f"Training response: {response.text}")

class FastAPIUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8000" 

    @task(4)
    def list_models(self):
        """
        Test the /list-models endpoint of the FastAPI app.
        """
        response = self.client.get("/list-models/")  
        print(f"List Models response: {response.text}")
