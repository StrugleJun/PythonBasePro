from injector import Injector, inject, Module, provider


class Service:
    def method01(self):
        print("this is service")


class Consumer:

    @inject
    def __init__(self, service: Service):
        self.__service = service

    def consumer01(self):
        self.__service.method01()


class MyModule(Module):
    @provider
    def provide_service(self) -> Service:
        return Service()


if __name__ == '__main__':
    injector = Injector(MyModule())
    consumer = injector.get(Consumer)
    consumer.consumer01()
