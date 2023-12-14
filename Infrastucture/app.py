from aws_cdk import App

from cdk.cdk_stack import S3Stack


app = App()
S3Stack(app, "sbx-aws_infra_testing")

app.synth()