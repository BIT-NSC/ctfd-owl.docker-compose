FROM python:3.8-alpine
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
	pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /app
COPY . /app
EXPOSE 8000
ENTRYPOINT ["python3", "app.py"]