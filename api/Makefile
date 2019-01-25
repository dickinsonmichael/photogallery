APPLICATION_NAME  ?= "photogallery"
S3_BUCKET         ?= "mjd-sam-build-bucket"
WEBSITE_DIR       ?= "../website/"
JS_VARIABLES_FILE ?= "$(WEBSITE_DIR)lib/aws-variables.js"

phony: all deploy package upload

all: package deploy upload

deploy:
	sam deploy \
		--template-file packaged.yaml \
		--stack-name $(APPLICATION_NAME) \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides "AppName=photo-gallery" \
		--no-fail-on-empty-changeset

package:
	sam package  \
		--output-template-file packaged.yaml \
		--s3-bucket $(S3_BUCKET)

upload:
	sed -e 's%API_URL_PLACEHOLDER%$(shell aws cloudformation describe-stacks --stack-name photogallery --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' --output text)%g' $(JS_VARIABLES_FILE).orig > $(JS_VARIABLES_FILE)
	aws s3 cp $(WEBSITE_DIR) s3://$(shell aws cloudformation describe-stacks --stack-name photogallery --query 'Stacks[0].Outputs[?OutputKey==`FrontendS3BucketName`].OutputValue' --output text) --recursive --exclude "*.yaml" --exclude "*.orig"
	@echo "\nWebsite can be accessed at: $(shell aws cloudformation describe-stacks --stack-name photogallery --query 'Stacks[0].Outputs[?OutputKey==`FrontendWebUrl`].OutputValue' --output text)"
