## python环境搭建

### 安装python

- 如果已经存在python了，就不需要在安装了，但是需要确认安装的python版本必须是3.9版本以及以上。否则按照下面的步骤安装python。

1. 下载python安装包(略)
2. 安装python(略)，注意安装时需要勾选`Add Python 3.x to PATH`
3. 配置环境变量
4. 测试安装是否成功

#### tips

- windows环境可以输入`py`来检测是否安装成功，如果安装成功，会显示python的版本信息。
- 进入idle后，退出的方式是`exit()`，而不是`exit`。也可以是
    - win: Ctrl+Z，然后回车。
    - mac: Ctrl+D
    - linux: Ctrl+D

### 安装VSCode

1. 下载VSCode安装包
2. 安装VSCode
3. 配置VSCode

#### 配置VSCode

- 这里主要是配置VSCode的python插件，以及配置python解释器。

1. 安装python插件
  - 扩展，搜索python，安装微软的python插件。
2. 配置调试环境
  - 点击调试，选择添加配置，选择python，然后选择python文件，这样就会在.vscode文件夹下生成一个`launch.json`文件。
  - 在`launch.json`文件中添加如下配置:
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "console": "internalConsole",
                "justMyCode": true
            }
        ]
    }
    ```
    - 需要注意，这里的配置是为了在调试时，使用内部控制台，而不是使用外部控制台。这种情况不会出现交互，也就意味着无法输入，即当前控制台是只读的，后续如果需要输入，则需要改为(默认)`integratedTerminal`。
3. 配置其他
    - 配置行宽，设置-用户设置-搜索`editor.rulers`，然后添加`80`，`100`，`120`，这样就会在编辑器中显示三条竖线，分别代表80，100，120列。
        ```json
        "editor.rulers": [80, 100, 120]
        ``` 
        - 这样的配置是为了方便查看代码的行宽，以及方便调整代码的行宽。