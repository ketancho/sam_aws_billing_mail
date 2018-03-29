#!/bin/sh

cd functions/billing_mail/
zip -r billing_mail.zip ./
cd -

aws cloudformation package \
 --template-file template.yaml \
 --s3-bucket billing-mail \
 --output-template-file \
 packaged-template.yaml \
 --profile sam-sample

aws cloudformation deploy \
 --template-file packaged-template.yaml \
 --stack-name billing-mail \
 --capabilities CAPABILITY_IAM \
 --profile sam-sample \
