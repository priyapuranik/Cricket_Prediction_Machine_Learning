# Cricket_Prediction_Machine_Learning

Cricket Match Outcome Predictor is a machine learning-powered web application designed to predict the outcome of a cricket match.<br> Users can input details like the batting and bowling teams, the city where the match is taking place, runs left, balls left, wickets left, total runs, current run rate, and required run rate.<br>The application uses a decision tree model to predict whether the batting team will win the match. This project is built with Flask for the backend and deployed on AWS, providing a user-friendly interface for cricket enthusiasts and analysts.<br>
<br>
1) Exploratory Data Analysis (EDA)<br>
<li>Description:<br></li>
In this section, I explored the dataset to understand its structure and identify any patterns or anomalies. I examined various features such as the teams, match location, and in-game statistics like runs, wickets, and balls remaining. The EDA process helped in identifying correlations between different features and the outcome of the match, which guided feature selection for the model.<br>
<br>
2) Data Cleaning<br>
<li>Description:</li><br>
Data cleaning involved handling missing values, correcting inconsistent data, and preparing the dataset for modeling. This step ensured that the data was accurate, consistent, and free from errors, making it suitable for building reliable predictive models.<br>
<br>
3) Model Building<br>
<li>Description:</li><br>
I built predictive models using both Random Forest and Decision Tree algorithms. The models were trained on the processed dataset to predict the outcome of cricket matches based on in-game statistics and other factors. The Random Forest model provided robust performance due to its ensemble nature, while the Decision Tree offered interpretability.<br>
<br>
4) Model Export<br>
<li>Description:</li><br>
After building and testing the models, I exported the trained model to a .pkl file format for deployment. This step allows the model to be easily loaded and used in a Flask application, enabling real-time predictions.<br>
<br>
<b>Flask Application</b><br>
<li>Overview: The Flask web application serves as the interface for users to interact with the cricket match outcome prediction model. It processes the input provided by users, transforms it using the trained model, and displays the prediction result.</li><br>

-- Features:

<li>Handles user input via forms on the HTML pages.</li><br>
<li>Loads the trained machine learning model and performs predictions based on user input.</li><br>
<li>Displays the prediction result, indicating which team is likely to win the match.</li><br>
<br>
<b>HTML Files</b><br>
--index.html:<br>

<li>Purpose: The main landing page of the application where users input the required match details.</li><br>
<li>Structure: Includes fields for Batting Team, Bowling Team, City, Runs Left, Balls Left, Wickets Left, Total Runs, Current Run Rate, and Required Run Rate.</li><br>
<li>Functionality: Sends the input data to the Flask backend for processing when the user clicks the "Predict" button.</li><br>
<br>
--result.html:<br>
<li>Purpose: Displays the prediction result after processing the input data.</li><br>
<li>Structure: Shows the output in a user-friendly format, indicating which team is predicted to win the match.</li><br>
<li>Design: Styled with a cricket-themed background and enhanced font to make the prediction stand out in the center of the page.</li><br>
<br>
<b>Deployment on AWS</b><br>
<b>Overview: The project was successfully deployed on an Amazon Web Services (AWS) EC2 instance to make the cricket match outcome prediction model accessible online.</b><br>

--Steps:

a)Launch an EC2 Instance:

<li>Selected an appropriate instance type (e.g., t2.micro) and configured security groups to allow HTTP (port 80) and custom ports (e.g., 8080) for the Flask application.</li>
<li>Installed necessary dependencies such as Python, Flask, and scikit-learn.</li>
b)Transfer Files:

<li>Uploaded the project files, including the trained model (.pkl files), Flask application (app.py), and HTML files (index.html and result.html) to the EC2 instance.</li>
c)Run the Flask Application:

<li>Launched the Flask application on a specified port (e.g., 8080) using a command like python3 app.py --port=8080.</li>
<li>Ensured that the application was accessible via the public IP address or DNS of the EC2 instance.</li>
d)Security Group Configuration:

<li>Configured security groups to allow traffic from any IP address (0.0.0.0/0) for the specified port used by the Flask application.</li>
<li>Allowed inbound rules for HTTP (port 80) and the custom port (e.g., 8080) to make the application accessible.</li>
<b>Result: The application was successfully deployed and could be accessed online, allowing users to interact with the prediction model through a web browser.</b>

