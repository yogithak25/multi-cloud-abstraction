from abc import ABC, abstractmethod

class CloudProvider(ABC):

    @abstractmethod
    def create_resource(self, resource_type: str, **kwargs):
        pass
