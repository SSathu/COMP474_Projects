FROM python:3.11
# getting python since its needed

WORKDIR /terminal_io
# setting my root as the same name as in the proj directory, or else its gonna get confusing

COPY requirements.txt .
RUN pip install -r requirements.txt
# copying + pip install the dependencies

COPY . .

CMD rm -rf logs/*.log && python terminal_driver.py



