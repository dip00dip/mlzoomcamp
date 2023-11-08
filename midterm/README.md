# Instructions

## Scope of the project
Given the wine reviews dataset the idea is to try to predict the price of the wine based on the rating, year and region.

## How to run

docker build -t zoomcamp-midterm .
docker run -it --rm -p 9696:9696 zoomcamp-midterm

## To test 
python predict_test.py