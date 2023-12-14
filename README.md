This is a personal project to play 2048 on a webpage using Flask and js

An important note is after each game is finished, a score file will be saved as a csv. This shows all the moves and all the boards that were made during this game. My goal is to use this information for a different data science project. 
# Step 1: Setting up the environment
To run this code you need to do a few python imports first.
You can copy and paste this into your terminal if you use pip.
```
pip install random
pip install numpy
pip install turtle
pip install tk
pip install pandas
pip install Flask 
```


If you use anaconda, you can copy and paste them into your environment.
```
conda install -c conda-forge numpy
conda install -c conda-forge pandas
conda install -c anaconda tk
conda install -c anaconda flask
```

# Step 2: Run the Flask Web Service
Once the dependencies are installed, you can run the Flask web service to play 2048 using the following command:

```
python flaskWebservice.py
```

This command assumes that your Python interpreter is in your system's PATH. If you encounter any issues, make sure your terminal or command prompt is in the same directory as the flaskWebservice.py file, or provide the full path to the file.

# Step 3: Access the Web Service
After running the command, you should see an output indicating that the Flask web service is running. By default, the service will be accessible at http://127.0.0.1:5000/ in your web browser.

Open your preferred web browser and navigate to the provided URL to interact with the Flask web service.

# Additional Notes:
If you encounter any errors or want to customize the behavior of the web service, check the code in the flaskWebservice.py file.
Ensure that no other application is using port 5000 on your machine, as Flask uses this port by default. If needed, you can change the port in the flaskWebservice.py file.
That's it! You should now have the Flask web service up and running. If you have any issues or questions, feel free to consult the project documentation or contact me at guernsgd@mail.uc.edu.
