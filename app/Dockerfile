FROM public.ecr.aws/lambda/python:3.9

COPY . requirements.txt ./

RUN python3.9 -m pip install -r requirements.txt -t .

#EXPORT DOCKER_DEFAULT_PLATFORM=linux/amd64

CMD ["app.lambda_handler"]
