#Sublime text3配置Python开发常用插件

##一、Sublime text3安装Package Control

1. 打开`Sublime text3`。
2. 使用<font color=#008800 size=3>`Ctrl + ~`</font>快捷键或者通过<font color=##0C89CF size=3>`View -> Show Console`</font>菜单打开命令行。
3. 粘贴如下代码，回车执行，等待安装完成。

```
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```

##二、安装Sublime Text插件管理工具Package Control

1. 使用<font color=#008800 size=3>`Shift + Command + P`</font>打开上面安装的`Package Control`。
2. 在打开的输入框中输入<font color=#008800 size=3>`Install Package`</font>， 然后选中匹配出来的<font color=#008800 size=3>`Install Package`</font>选项，回车。
3. 在新弹出的输入框中输入要安装的插件。
4. 搜索出对应插件，选中并回车安装。

##三、安装Anaconda插件

1. 按照<font color=#008800 size=3>`二`</font>中步骤，安装`Anaconda`插件。
2. 安装后就可以直接使用<font color=#008800 size=3>`Command + B`</font>快捷键来运行`Python`文件了。
3. `Anaconda`是一个终极`Python`插件。它为`Sublime Text3`增添了多项`IDE`类似的功能，例如：
	1. `Autocompletion`自动完成，该选项默认开启，同时提供多种配置选项。
	2. `Code linting`使用支持`pep8`标准的`PyLint`或者 `PyFlakes`。因为我个人使用的是另外的`linting`工具，所以我会在`Anaconda`的配置文件`Anaconda.sublime-settings`中将`linting`完全禁用。
	3. `McCabe code complexity checker`让你可以在特定的文件中使用`McCabe complexity checker`。如果你对软件复杂度检查工具不太熟悉的话，请务必先浏览上边的链接。
	4. `Goto Definitions`能够在你的整个工程中查找并且显示任意一个变量，函数，或者类的定义。
	5. `Find Usage`能够快速的查找某个变量，函数或者类在某个特定文件中的什么地方被使用了。
	6. `Show Documentation`能够显示一个函数或者类的说明性字符串(当然，是在定义了字符串的情况下)。
	7. 你可以在这里，或者通过`Sublime Text3`的`Package Settings: Sublime Text > Preferences > Package Settings > Anaconda > README`来查看所有这些特性。
5. 取消`Anaconda`默认的`linting`功能。如果是因为使用`Anaconda`插件而出现一些框框，可以在可以在<font color=#008800 size=3>`Sublime > Preferences > Package Settings > Anaconda > Settings User`</font>中设置关闭：<font color=#008800 size=3>`{"anaconda_linting": false}`</font>

##四、安装SublimeREPL插件配置交互式终端快捷键

1. `Sublime`编辑器默认无法处理`Python`直接在编辑器上的编译运行和交互，需要`SublimeREPL`插件协助。
2. 按照<font color=#008800 size=3>`二`</font>中步骤，安装`SublimeREPL`插件。
3. 安装完成后使用<font color=#008800 size=3>`Tools -> SublimeREPL -> Python -> Run current file`</font>来通过插件运行`Python`文件。
4. 设置执行快捷键
	
	1. 现在系统`设置`应用中添加快捷键。
	2. 点击<font color=#008800 size=3>`Perferences -> Key Bindings-Users`</font>，设置快捷键`F5`:

```json
{
	"keys":["f5"], 
	"caption": "SublimeREPL: Python - RUN current file",
	"command": "run_existing_window_command", 
	"args": 
		{ 
			"id": "repl_python_run", 
			"file": "config/Python/Main.sublime-menu" 
		}
}
```	 
##五、安装SublimeCodeIntel提示插件

1. `SublimeCodeIntel`，输入提示插件，安装后，在输入代码的时候会有提示。
2. 按照<font color=#008800 size=3>`二`</font>中步骤，安装`SublimeCodeIntel `插件。
3. `SublimeCodeIntel`是一个非常流行的插件，它的许多特性与`Anaconda`类似。

##六、安装Python PEP8 Autoformat代码自动格式化插件

1. `Python PEP8 Autoformat`，代码自动格式化成标准`Python`代码风格。

##七、安装SideBarEnhancements侧边栏扩展插件

1. `SideBarEnhancements`: 扩展了侧边栏中菜单选项的数量，从而提升你的工作效率。
2. 诸如`New file`和`Duplicate`这样的选项对于`Sublime Test3`来说实在是太重要了，我甚至觉得`Sublime Text3`本来就应该提供这些功能。
3. 而且仅凭`Delete`这一个功能就让这个插件值得下载。这个功能将你会在你删除文件的时候把它放入回收站。虽然这个功能乍一看没什么用，但是当你没有使用这样的功能而彻底删除了一个文件的时候，除非你用了版本管理软件，否则你将很难恢复这个文件。
4. 具体安装步骤与其他插件相同。

##八、安装pylinter Python基本主题

1. 这个插件提供了目前我所见到的最好的`pylint`编辑器整合。它自动检查`.py`文件，无论其何时被保存，并且会直接在编辑界面显示`pylint`违规。
2. 它还有一个快捷方式来禁用局部的`pylint`检查，通过插入一个`#pylint:`禁用注释。
3. 这个插件对于我确实非常有用。  

##九、安装SublimeTmpl新建文件模板插件

1. `SublimeTmpl`: 新建文件模板插件，可以支持多种语言例如`Python`、`PHP`等。
2. 下面的代码是我在配置文件中的配置信息，在`settings-user`中设置上自己的信息：

```
{  
	"disable_keymap_actions": false, // "all"; "html,css"
	"date_format" : "%Y-%m-%d %H:%M:%S",
	"attr":
		{
			"author": "iGhibli",
			"email": "iGhibli@163.com",
			"link": "http://iGhibli.github.io/"
		}
}
```

3. 我将`Python`的创建模板命令也做了修改，在`key bindings-user`中添加了以下信息，意思是`ctrl+alt+p`就可以创建一个新的`Python`模板。

```
[
	{
		"caption": "Tmpl: Create python",
		"command": "sublime_tmpl",
		"keys": ["ctrl+alt+p"],
		"args": {"type": "python"}
	}  
]  
```
---
