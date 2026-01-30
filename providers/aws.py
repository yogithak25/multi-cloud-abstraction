import boto3
from core.base import CloudProvider

class AWSProvider(CloudProvider):

    def __init__(self, region="us-west-2"):
        self.ec2_client = boto3.client("ec2", region_name=region)

    def create_resource(self, resource_type: str, **kwargs):
        if resource_type == "ec2":
            return self._create_ec2(**kwargs)
        else:
            raise ValueError(f"AWS resource not supported: {resource_type}")

    def _create_ec2(self, **params):
        """
        Required params:
        - ami_id
        - instance_type
        - key_name
        - security_group_ids
        - subnet_id
        """

        response = self.ec2_client.run_instances(
            ImageId=params["ami_id"],
            InstanceType=params["instance_type"],
            KeyName=params["key_name"],
            SecurityGroupIds=params["security_group_ids"],
            SubnetId=params["subnet_id"],
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": params.get("name", "ec2-instance")}
                    ]
                }
            ]
        )

        instance_id = response["Instances"][0]["InstanceId"]

        return {
            "cloud": "AWS",
            "resource": "EC2",
            "instance_id": instance_id,
            "status": "CREATED"
        }
