## Reddit Flair Detector

#### MIDAS Hiring Project

This is the code repository for my attempt at the MIDAS Hiring Project - Reddit Flair Detector. 

[Part I - Reddit Data Collection](https://github.com/vishakha-lall/MIDAS_Hiring_Project/blob/master/Part%201%20-%20Reddit%20Data%20Collection.ipynb) 

[Part II - Exploratory Data Analysis (EDA)](https://github.com/vishakha-lall/MIDAS_Hiring_Project/blob/master/Part%202%20-%20Exploratory%20Data%20Analysis.ipynb)

[Part III - Building a Flare Detector](https://github.com/vishakha-lall/MIDAS_Hiring_Project/blob/master/Part%203%20-%20Build%20a%20Flair%20Detector.ipynb)

Part IV - Building a Web Application

- The web application is a simple Flask web app. 
- To run the application, follow the instructions below. 

Part V - Deployment

- The application is deployed on Heroku [here](http://cryptic-earth-17134.herokuapp.com/)
- For automated testing, use endpoint http://cryptic-earth-17134.herokuapp.com/automated_testing

#### Environment Setup

The code has been built on Windows 10 OS with **Python 3.7**. 

1. Use `requirements.txt` to install dependencies `pip install -r requirements.txt` . Using a virtual environment is recommended. 
2. The code uses some popular corpus' by nltk. Download these from the list available in `nltk.txt` as `nltk.download("<corpus_name>")`.
3. Create a `.env` file with Reddit configs
```
CLIENT_ID=<your client ID>
CLIENT_SECRET=<your client secret>
USER_AGENT=<your user agent>
```

#### Running the web application

1. Run `python app.py` from the project folder, the application is rendered on `127.0.0.1:5000`.
2. To run the automated testing in *local*, use endpoint `127.0.0.1:5000/automated_testing` for POST requests with a file upload. 
   - A sample `file.txt` is available in the repository.
   - Code blocks in `Test.ipynb` can be used for testing.
