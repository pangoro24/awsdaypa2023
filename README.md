# awsdaypa2023
Prueba de concepto del tema: Recolección y análisis de logs en tiempo real usando Amazon Kinesis

cd base/
serverless deploy --param="region=YOUR_AWS_REGION" --param="account=YOUR_AWS_ACCOUNT" --verbose

cd producer/
serverless deploy --param="region=YOUR_AWS_REGION" --param="account=YOUR_AWS_ACCOUNT" --param="streamName=poc-k-stream" --verbose


Delete all objects (for testing)
aws s3 rm s3://YOUR_BUCKET_NAME --recursive

Clean 
serverless remove --param="region=YOUR_AWS_REGION" --param="account=YOUR_AWS_ACCOUNT" --verbose