from core.factory import CloudProviderFactory

def create_cloud_resource(cloud: str, resource_type: str, **params):
    """
    Common interface for all cloud resource creation
    """
    provider = CloudProviderFactory.get_provider(cloud)
    return provider.create_resource(resource_type, **params)

if __name__ == "__main__":
    result = create_cloud_resource(
        cloud="aws",
        resource_type="ec2",
        region="us-west-2",
        ami_id="ami-0786adace1541ca80",
        instance_type="t3.micro",
        key_name="aws-keypair",
        security_group_ids=["sg-0e534be17d2495bd5"],
        subnet_id="subnet-0b042a54ae85a4dc1",
        name="prod-web-server"
    )

    print(result)
