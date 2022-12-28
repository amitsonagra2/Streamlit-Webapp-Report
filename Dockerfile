From python:3.9.13
copy . /render_app
WORKDIR /render_app
run pip install -r requirements.txt
expose $PORT
CMD streamlit run main.py
