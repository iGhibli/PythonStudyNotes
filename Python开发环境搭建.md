#Python开发环境搭建

***

一、安装`iTerm`、`oh-my-zsh`和`Xcode command line tool`

1. 安装`iTerm`
	1. 在官网<font color=##0C89CF size=3>`http://www.iterm2.com/`</font>下载iTerm。  
	2. 将下载的包应用直接移动到`应用程序`文件夹中。
2. 安装`oh-my-zsh`
	1. 在`Launchpad`中打开`iTerm`。
	2. 输入<font color=#008800 size=3>`sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"`</font>命令安装`oh-my-zsh`。
	3. `oh-my-zsh`官网地址<font color=##0C89CF size=3>`http://ohmyz.sh/`</font>。
3. 安装`Xcode command line tool`
	1. 直接在`App Store`搜索`Xcode`并安装。 
	2. 在`iTerm`中输入<font color=#008800 size=3>`xcode-select --install`</font>命令来安装`Xcode command line tool`。

二、安装`Homebrew` macOS缺失的软件包管理器

1. 按官网<font color=##0C89CF size=3>`https://brew.sh/`</font>提供的方法安装。
2. 打开iterm，执行<font color=#008800 size=3>`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`</font>命令。
3. 等待安装完成。
4. 执行<font color=#008800 size=3>`brew doctor`</font>命令，如果出现`Your system is ready to brew.`代表安装成功，如果有`Warning`的话，也不用担心，可以按照里面的步骤去修正就好喽！

三、安装最新版`Python`

1. 输入<font color=#008800 size=3>`python --version`</font>来查看当前Mac上的`Python`版本。
2. 使用`Homebrew`搜索`Python`，命令<font color=#008800 size=3>`brew search python`</font>。在结果中可以看到所有可以安装的`Python`版本，已经安装的版本会使用`installed`标示出来。
3. 使用命令<font color=#008800 size=3>`brew install python3`</font>安装新版`Python`。
4. 安装过的`Python`在`/usr/local/Cellar`文件夹中。
5. 使用命令<font color=#008800 size=3>`open /usr/local/Cellar/`</font>打开`Python所在文件夹`。

四、设定路径`$PATH`(不与系统自带版本`Python`冲突)

> 什么是路径`$PATH`呢？
> 我们在安装`Python`的时候，输入了`brew`，
> 系统就会自动知道要使用`homebrew`。
> 系统到底怎么知道我们的`brew`在哪里？
> 这就是`$PATH`的用途了！

1. 输入命令<font color=#008800 size=3>`echo $PATH`</font>，就会看到`/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`这段字符串。
	* 分号(:)是分隔的意思,所以当你在`iTerm`里面输入`brew`时系统就会开始从`/usr/bin`找起，如果在`/usr/bin`里面找不到的话，就会往下一个`/bin`去搜索，以此类推。`brew`其实就在`/usr/local/bin`里面！
	* 所以现在就需要设置我们在`/usr/local/Cellar`里面装的`Python`路径优先于系统在`/usr/bin`里面的`Python`路径。
这样在输入`python`命令时，就会优先使用我们安装的在`/usr/local/Cellar`里面装的`Python`。
2. 输入命令<font color=#008800 size=3>`sudo emacs /etc/paths`</font>打开emacs编辑搜索路径顺序，把`/usr/local/bin`移动到最上边。
	* `Ctrl + k`：剪切当前行
	* `Ctrl + y`：粘贴
	* `Ctrl + x + s`：保存
	* `Ctrl + x + c`：关闭emacs
3. 重启下终端变更就生效了。
4. 使用<font color=#008800 size=3>`which python`</font>和<font color=#008800 size=3>`which python3`</font>查看`Python`和`Python3`命令对应的执行路径。

五、安装`Spyder IDE`

1. 按照`Spyder`在`Github`（<font color=##0C89CF size=3>`https://github.com/spyder-ide/spyder/releases`</font>）上的安装方法执行命令<font color=#008800 size=3>`pip install -U spyder`</font>安装。
2. 安装完成后执行命令<font color=#008800 size=3>`spyder`</font>或<font color=#008800 size=3>`spyder3`</font>启动`Spyder`。
3. 如果没有正常启动报`PyQt`的错误，执行<font color=#008800 size=3>`pip install wheel`</font>或<font color=#008800 size=3>`pip3 install wheel`</font>然后执行<font color=#008800 size=3>`cd wheel路径`</font>，然后执行<font color=#008800 size=3>`pip search PyQt`</font>或者<font color=#008800 size=3>`pip3 search PyQt`</font>，然后执行<font color=#008800 size=3>`pip install PyQt5`</font>安装对应版本的`PyQt`。
4. 最后再次尝试执行命令<font color=#008800 size=3>`spyder`</font>或<font color=#008800 size=3>`spyder3`</font>启动`Spyder`。
5. 安装完成。

***