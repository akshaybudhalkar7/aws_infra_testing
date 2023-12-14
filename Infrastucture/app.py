from aws_cdk import App

from cdk.cdk_stack import S3Stack


app = App()
S3Stack(app, "s3")

app.synth()