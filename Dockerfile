FROM python:3.13.2

WORKDIR /app

COPY . .

RUN pip install numpy pandas scikit-learn opencv-python pillow wandb opencv-python-headless

CMD ["python", "distance_classification.py"]
