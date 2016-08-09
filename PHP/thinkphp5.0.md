###thinkPHP5.0


####准备工作
1.下载thinkphp安装

获取ThinkPHP的方式很多，[官方网站](http://thinkphp.cn) 是最好的下载和文档获取来源。

官网提供了稳定版本的下载：[http://thinkphp.cn/down/framework.html]()

2.安装Javasdk服务,xampp服务和MySQL服务

	注意：xampp在电脑重启之后，服务开启不了，原因为：端口被占用或与mac系统默认的Apache服务冲突，解决办法：sudo apachectl stop停掉系统预装的Apache

3.数据库支持:Navicat MySQL

4.安装开发环境:ZendStudio1202

####基础语法
文件起始标识:

</php

?>

注意:如果文件内容是纯 PHP 代码，最好在文件末尾删除 PHP 结束标记。这可以避免在 PHP 结束标记之后万一意外加入了空格或者换行符，会导致 PHP 开始输出这些空白，而脚本中此时并无输出的意图.
一段 PHP 代码中的结束标记隐含表示了一个分号；在一个 PHP 代码段中的最后一行可以不用分号结束。如果后面还有新行，则代码段的结束标记包含了行结束。


echo和print输出语句

####命名规范
1. 不允许使用关键字开头命名文件
2. URL默认不区分大小写
3. 

####命名空间和引用
解决以下问题:

1.用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突。

2.为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性。

namespace:用于表示当前文件所在位置

use:引用文件所在位置

####目录结构
project  应用部署目录

├─application           应用目录（可设置）

│  ├─common             公共模块目录（可更改）

│  ├─index              模块目录(可更改)

│  │  ├─config.php      模块配置文件

│  │  ├─common.php      模块函数文件

│  │  ├─controller      控制器目录

│  │  ├─model           模型目录

│  │  ├─view            视图目录

│  │  └─ ...            更多类库目录

│  ├─command.php        命令行工具配置文件

│  ├─common.php         应用公共（函数）文件

│  ├─config.php         应用（公共）配置文件

│  ├─database.php       数据库配置文件

│  └─route.php          路由配置文件

├─extend                扩展类库目录（可定义）

├─public                WEB 部署目录（对外访问目录）

│  ├─static             静态资源存放目录(css,js,image)

│  ├─index.php          应用入口文件

│  ├─router.php         快速测试文件

│  └─.htaccess          用于 apache 的重写

├─runtime               应用的运行时目录（可写，可设置）

├─vendor                第三方类库目录（Composer）

├─thinkphp              框架系统目录

│  ├─lang               语言包目录

│  ├─library            框架核心类库目录

│  │  ├─think           Think 类库包目录

│  │  └─traits          系统 Traits 目录

│  ├─tpl                系统模板目录

│  ├─.htaccess          用于 apache 的重写

│  ├─.travis.yml        CI 定义文件

│  ├─base.php           基础定义文件

│  ├─composer.json      composer 定义文件

│  ├─console.php        控制台入口文件

│  ├─convention.php     惯例配置文件

│  ├─helper.php         助手函数文件（可选）

│  ├─LICENSE.txt        授权说明文件

│  ├─phpunit.xml        单元测试配置文件

│  ├─README.md          README 文件

│  └─start.php          框架引导文件

├─build.php             自动生成定义文件（参考）

├─composer.json         composer 定义文件

├─LICENSE.txt           授权说明文件

├─README.md             README 文件

├─think                 命令行入口文件


####相关配置
	修改环境路径:
	xamppfiles/etc/httpd.conf/DocumentRoot&Directory
	修改重定向URL:xamppfiles/htdocs/index.php
	Apache配置文件:这个配置文件的位置是：
	/private/etc/apache2/httpd.conf
	定位或者设置 DocumentRoot。这是网站所有文件的根目录。此目录中	的文件由 web 服务器提供服务，从而使得 PHP 文件将在输出到浏览器	之前解析为 PHP 脚本。通常情况下默认的路径是:
	 /Library/WebServer/Documents，但是可以根据需要在 	httpd.conf中设置为任何其他目录。另外，用户自己的缺省 	DocumentRoot 是 /Users/yourusername/Sites。
	注意:配置文件修改之后需要重启Apache服务


公用参数配置:
		
	在ThinkPHP中，一般来说应用的配置文件是自动加载的，加载的顺序是：
	惯例配置->应用配置->模式配置->调试配置->状态配置->模块配置->扩展配置->动态配置
	以上是配置文件的加载顺序，因为后面的配置会覆盖之前的同名配置（在没有生效的前提下），所以配置的优先顺序从右到左。
	惯例配置:
	框架内置有一个惯例配置文件（位于thinkphp/convention.php）
	应用配置:
	应用配置文件是应用初始化的时候首先加载的公共配置文件，默认位于application/config.php。
	场景配置:
	每个应用都可以在不同的情况下设置自己的状态（或者称之为应用场景），并且加载不同的配置文件。
	举个例子，你需要在公司和家里分别设置不同的数据库测试环境。那么可以这样处理，在公司环境中，我们在应用配置文件中配置：
	'app_status'=>'office'
	那么就会自动加载该状态对应的配置文件（默认位于application/office.php）。
	状态配置文件都是可选的
	模块配置:
	每个模块会自动加载自己的配置文件（位于application/当前模块名/config.php）。
	模块还可以支持独立的状态配置文件，命名规范为：application/当前模块名/应用状态.php。
	模块配置文件是可选的
	加载配置文件:
	Config::load('配置文件名');
	配置文件一般位于APP_PATH目录下面，如果需要加载其它位置的配置文件，需要使用完整路径，例如：

	Config::load(APP_PATH.'config/config.php');
	系统默认的配置定义格式是PHP返回数组的方式，例如：
	return [
    '配置参数1'=>'配置值',
    '配置参数1'=>'配置值',
    // ... 更多配置
	 ];
	如果你定义格式是其他格式的话，可以使用parse方法来导入，例如：
	Config::parse(APP_PATH.'my_config.ini','ini');
	Config::parse(APP_PATH.'my_config.xml','xml');
	parse方法的第一个参数需要传入完整的文件名或者配置内容。
	如果不传入第二个参数的话，系统会根据配置文件名自动识别配置类型，所以下面的写法仍然是支持的：
	Config::parse('my_config.ini');
	
	更改配置目录:
	如果不希望配置文件放到应用目录下面，可以在入口文件中定义独立的配置目录，添加CONF_PATH常量定义即可，例如：
	// 定义配置文件目录和应用目录同级
	define('CONF_PATH', '../config/');
	配置目录下面的结构类似如下：
	├─application         应用目录
	├─config              配置目录
	│  ├─config.php       应用配置文件
	│  ├─database.php     数据库配置文件
	│  ├─route.php        路由配置文件
	│  ├─...              其它配置文件
	│  ├─index            index模块配置文件目录
	│  │  ├─config.php    index模块配置文件
	│  │  └─ ...          index模块其它配置文件




####标签
1.volist:循环输出一个数组
示例:
>{volist name="teachers" id="teacher" key="key"}
 	<tr>
    <td>{$key}</td>
    <td>{$teacher->getData('name')}</td>
    <td>{$teacher->getData('sex')}</td>
    <td>{$teacher->getData('email')}</td>
    <td>{$teacher->getData('username')}</td>
{/volist}

2.eq:通过判断显示不同结果
示例:如果是0,则显示男,是1则显示女
{eq name='teacher->getData("sex")' value='0'}男{else /}女{/eq}

详解:
{eq}{/eq}我们叫做非自闭合标签，也就是肯定有自己的另一半的。
{else /}我们叫做自闭全标签，不需要找自己的另一半。


####sublime 编辑器的使用
常用插件

#####语法检测



#####断点debug
安装xdebug

在mac下非常方便：

	brew install php55-xdebug
	然后进行配置，在/usr/local/etc/php/5.5/conf.d/ext-xdebug.ini中添加
	xdebug.remote_enable=1
	xdebug.remote_handler=dbgp
	xdebug.remote_host=127.0.0.1
	xdebug.remote_port=9000
	xdebug.remote_log="/var/log/xdebug/xdebug.log"

重启apache

	sudo apachectl restart
配置sublime

要调试某一个项目，首先得把这个项目在sublime下保存成一个project

	sublime->project->save project as ...
	然后用package control安装xdebug client

接下来配置项目

sublime->project->edit poject
配置文件类似以下内容：
		
	{
	    "folders":
	    [
	        {
	            "follow_symlinks": true,
	            "path": "."
	        }
	    ],
	    "settings": {
	        "xdebug": {
	             "url": "http://my.local.website/",
	        }
	    }
	}

其中url是项目所在url，记得在hosts里头将这个url指向127.0.0.1，还有在apache的virtualhost里将其指向项目根目录

这样就OK了，准备开启调试吧

开启调试

	开启调试方式也比较简单，在想要加断点的地方右键
	xdebug->Add/Remove breakpoint
	这样项目在运行到本行的时候就会停止下来

然后开始调试，在菜单栏选择

	tools->xdebug->start debugging(launch browser)
	sublime会自动打开浏览器，进入配置时写的网站链接，进行调试
	调试中所用的功能可以在调试文件中右键查看之

可能问题

无法跟踪断点

这可能是xdebug端口被占用，按Ctrl+`或者菜单栏View->show Console查看错误信息，有可能是xdebug端口已经被占用的缘故。

在sublime xdebug中关闭调试，或者重启sublime可以解决这个问题。

参考

[Debugging with Xdebug and Sublime Text 3]()


####URL配置与路由配置



