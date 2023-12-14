from aws_cdk import App

from cdk.cdk_stack import S3Stack


app = App()
S3Stack(app, "sbx-aws-infra-testing")

app.synth()