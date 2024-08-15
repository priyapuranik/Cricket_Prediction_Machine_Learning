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

<li>Handles user input via forms on the HTML pages.<br>
Loads the trained machine learning model and performs predictions based on user input.<br>
Displays the prediction result, indicating which team is likely to win the match.</li><br>
