[toc]

# Python - Injector 

## 一、什么是 Python Injector

Python Injector 简化依赖注入，是一个轻量级的依赖注入库。它可以帮助开发者更轻松地管理应用程序中的依赖关系，提高可测试性，并减少代码之间的耦合。

官网：[GitHub - python-injector/injector: Python dependency injection framework, inspired by Guice](https://github.com/python-injector/injector)



## 二、Python Injector 入门案例

### 2.1 使用步骤

1.  **安装**：通过 `pip install injector` 安装。
2.  **定义绑定**：创建一个绑定类，使用 `Binder` 来定义依赖关系。
3.  **创建模块**：使用 `Module` 类来组织绑定。
4.  **使用依赖**：在你的类中使用 `@inject` 装饰器来注入依赖。

### 2.2 安装模块

```cmd
E:\PythonProject\PythonBasic>pip --version
pip 24.1.2 from D:\Python\Python312\Lib\site-packages\pip (python 3.12)

E:\PythonProject\PythonBasic>python --version
Python 3.12.1

E:\PythonProject\PythonBasic>
```



```cmd
E:\PythonProject\PythonBasic>pip install injector
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting injector
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/3f/37/37fee65c78ae3f9675e6190bfd12304e5d8d99564f0ec91716bf2bfbbb5f/injector-0.22.0-py2.py3-none-any.whl (20 kB)
Installing collected packages: injector
Successfully installed injector-0.22.0

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

E:\PythonProject\PythonBasic>python.exe -m pip install --upgrade pip
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pip in d:\python\python312\lib\site-packages (24.1.2)
Collecting pip
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/d4/55/90db48d85f7689ec6f81c0db0622d704306c5284850383c090e6c7195a5c/pip-24.2-py3-none-any.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 4.8 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.1.2
    Uninstalling pip-24.1.2:
      Successfully uninstalled pip-24.1.2
Successfully installed pip-24.2

E:\PythonProject\PythonBasic>

```

### 2.3 基本使用

```python
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

```



```cmd
D:\Python\Python312\python.exe E:\PythonProject\PythonBasic\依赖注入\Injector模块\Demo01.py 
this is service

Process finished with exit code 0

```

### 2.4 代码解释

1.  **Service 类**：
    -   这是一个简单的服务提供者，包含一个 `method01` 方法。
    -   这个类的职责是提供某种功能（在这里是问候）。
2.  **Consumer 类**：
    -   这是依赖于 `Service` 的消费者类。
    -   使用 `@inject` 装饰器在构造函数中指明依赖关系。当 `Injector` 创建 `Consumer` 时，会自动传入 `Service` 实例。
3.  **MyModule 类**：
    -   这个模块类用于定义依赖绑定。
    -   `@provider` 装饰器标记 `provide_service` 方法，表示该方法用于提供 `Service` 实例。
    -   当 `Injector` 需要 `Service` 时，它会调用这个方法。
4.  **Injector 实例**：
    -   `Injector([MyModule()])` 创建一个新的 Injector 实例，传入 `MyModule` 以进行依赖管理。
    -   Injector 负责根据模块中的定义来解决依赖关系。
5.  **获取 Consumer 实例**：
    -   使用 `injector.get(Consumer)` 创建 `Consumer` 实例，同时自动注入所需的 `Service` 实例。
    -   最后，调用 `consumer01` 方法会输出 `Service` 提供的问候语。

### 2.5 Consumer 如何构建的

`Injector` 构建 `Consumer` 实例的过程主要涉及以下几个步骤：

1.  **解析依赖关系**：
    -   当你调用 `injector.get(Consumer)` 时，`Injector` 会查看 `Consumer` 类的构造函数。
    -   它会识别构造函数中使用的 `@inject` 装饰器，找出 `Consumer` 依赖的类型（在这里是 `Service`）。
2.  **创建依赖实例**：
    -   `Injector` 会检查是否已经存在 `Service` 的实例。如果没有，它会调用 `MyModule` 中定义的 `provide_service` 方法来创建一个新的 `Service` 实例。
3.  **实例化 Consumer**：
    -   一旦 `Service` 实例被创建，`Injector` 会将其作为参数传递给 `Consumer` 的构造函数。
    -   这时，`Consumer` 被实例化，并且内部的 `Service` 属性会被赋值。
4.  **返回实例**：
    -   最终，`Injector` 返回构建好的 `Consumer` 实例，准备供后续使用。

这个过程使得 `Consumer` 可以在不直接依赖 `Service` 实现的情况下使用它，符合依赖注入的设计原则。



`Consumer` 不需要直接添加到 `MyModule` 中。模块的主要作用是定义和提供依赖关系。下面是一些关键点：

1.  **模块的职责**：
    -   `MyModule` 负责提供 `Service` 实例，而不是直接提供 `Consumer` 实例。这种方式将服务的提供和消费解耦，增强了灵活性和可测试性。
2.  **Consumer 的构造**：
    -   `Consumer` 依赖于 `Service`，而 `Injector` 会根据 `Consumer` 的构造函数自动解析所需的依赖。
3.  **使用场景**：
    -   当你需要使用 `Consumer` 时，可以直接通过 `injector.get(Consumer)` 来获取实例，而无需在模块中显式声明 `Consumer`。



在依赖注入框架中，`Injector` 如何知道调用哪个方法（如 `provide_service`）主要依赖于以下几个方面：

1.  **装饰器标记**：
    -   `@provider` 装饰器用于标记 `provide_service` 方法，表示该方法负责提供某个特定类型的实例（在这里是 `Service`）。
    -   `Injector` 会扫描模块中的方法，寻找带有 `@provider` 装饰器的方法，以确定哪些方法可以用于实例化依赖。
2.  **类型绑定**：
    -   当你在模块中定义一个提供方法时，通常还会有一些绑定逻辑，指明该方法返回的类型。比如，在 `provide_service` 方法中返回的类型是 `Service`。
    -   `Injector` 会将这种类型与需要的依赖进行关联。
3.  **依赖解析过程**：
    -   当 `Injector` 解析依赖时，它会查看构造函数中标记为 `@inject` 的类型。如果需要 `Service`，它就会查找模块中所有的提供方法，找到被 `@provider` 装饰的 `provide_service` 方法。
4.  **方法调用**：
    -   一旦找到合适的提供方法，`Injector` 就会调用它，获取一个 `Service` 的实例，并将其注入到需要 `Service` 的类（如 `Consumer`）中。