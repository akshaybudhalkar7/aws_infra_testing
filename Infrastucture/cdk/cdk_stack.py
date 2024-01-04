from aws_cdk import (
    aws_s3 as _s3,
    Stack,
    aws_lambda,
    aws_iam
)
from os import path

from constructs import Construct


class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # s3 = _s3.Bucket(self, "s3bucket6432889")

        lambda_role = aws_iam.Role(
            self, 'lambda_role',
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole")
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess")
            ]
        )

        # Defines an AWS Lambda resource
        my_lambda = aws_lambda.Function(
            self,
            'HelloHandler',
            runtime= aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.from_asset(path.join(path.dirname(__file__), '..', '..', 'lambda_app')),
            handler='app.handler',
            function_name='test_app',
            role= lambda_role
        )


