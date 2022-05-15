# Welcome to the CryptoWeb
David Gauthier, Boris Bellanger, Nathalie Bou Farhat, Giuseppe Deni

## To run the crypto web project

    git clone https://github.com/davidgaut/CryptoWeb.git
    cd ./CryptoWeb/
    sudo docker-compose build
    sudo docker-compose up
    google-chrome http://172.20.0.2:5000/

## Functionalities (Web paths)
- history: shows the history for each crypto
- prediction: use a model to predict the next crypto value
- prediction history: store the past predictions in a single table

## Files
- get_bitcoins.py : load data using yahoo finance api
- make_model.py: create a prediction model for cryptos
- db.py: create a database to store predictions
- test_app.py: perform basic sanity checks
- prediction history: store the past predictions in a single table
