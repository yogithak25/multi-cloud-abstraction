from providers.aws import AWSProvider
from providers.azure import AzureProvider
from providers.gcp import GCPProvider

class CloudProviderFactory:

    @staticmethod
    def get_provider(cloud_name: str, **kwargs):
        cloud_name = cloud_name.lower()

        if cloud_name == "aws":
            return AWSProvider(region=kwargs.get("region", "us-west-2"))
        elif cloud_name == "azure":
            return AzureProvider()
        elif cloud_name == "gcp":
            return GCPProvider()
        else:
            raise ValueError("Unsupported cloud provider")

