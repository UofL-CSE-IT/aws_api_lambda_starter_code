#!/bin/bash

# Variables
TEAM_NUMBER="16"
COURSE_YEAR="2025"
COURSE_SEASON="spring"
AWS_PROFILE="aws_team_16"
LAMBDA_FUNCTION_NAME="$COURSE_YEAR-$COURSE_SEASON-capstone-team-$TEAM_NUMBER"
ZIP_FILE="lambda_function.zip"
HANDLER_FILE="lambda_function.py"
HANDLERS_DIR="handlers"
DB_CREDENTIALS_FILE="db_credentials.py"
AWS_REGION="us-east-1"
SITE_PACKAGES_DIR=$(python3 -c "import site; print(site.getsitepackages()[0])")

# Create a zip file containing the lambda function, handlers, and installed packages
echo "Creating zip file..."
cd $SITE_PACKAGES_DIR
zip -r9 $OLDPWD/$ZIP_FILE .
cd $OLDPWD
zip -g $ZIP_FILE $HANDLER_FILE $HANDLERS_DIR/* $DB_CREDENTIALS_FILE

# Upload the zip file to AWS Lambda
echo "Uploading zip file to AWS Lambda..."
aws lambda update-function-code \
    --function-name $LAMBDA_FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --no-cli-pager

# Clean up
echo "Cleaning up..."
rm $ZIP_FILE

echo "Deployment complete."