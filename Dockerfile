From python:3.9.13
copy . /render_app
# copy XGboost.pkl /XGboost.pkl

WORKDIR /render_app
run pip install -r requirements.txt
expose $PORT
CMD streamlit run main.py

# run this command to start docker on localhost
# docker run -p 8080:8501 docker-xgbc

# build a docker file 
# docker build -t docker-xgbc -f Dockerfile .         