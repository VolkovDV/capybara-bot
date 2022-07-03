FROM python:3.9
ADD capybara_bot /usr/local/capybara_bot
WORKDIR /usr/local/
ADD capybara_bot/* .
ADD requirements.txt .
ADD setup.py .
RUN python3 -m setup install
ENV TOKEN='insert your token'
CMD ["python3", "main.py"]


