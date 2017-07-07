#Sublime text3配置C开发环境
1. 打开Sublime text3。
2. 在顶部工具栏按顺序打开：`Tools --> Build System --> New Build System...`。
3. 然后在新建的配置文件中输入下面的json配置信息。
4. 将配置文件保存成C.sublime-build，保存到默认目录（`/Users/username/Library/Application Support/Sublime Text 3/Packages/User/`）中。
5. 再创建一个新的.c文件，如HelloWorld.c，就可以使用command+b来编译，shift+command+b来运行C文件。

```json
{
	"cmd": ["gcc", "${file}", "-o", "${file_path}/${file_base_name}"],
	"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
	"working_dir": "${file_path}",
	"selector": "source.c, source.c++",
	
	"variants":
		[
			{
				"name": "Run",
				"cmd" : ["${file_path}/${file_base_name}"]
			}
		]
}
```
