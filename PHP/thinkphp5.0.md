###thinkPHP5.0


####准备工作
下载thinkphp安装

获取ThinkPHP的方式很多，[官方网站](http://thinkphp.cn) 是最好的下载和文档获取来源。

官网提供了稳定版本的下载：[http://thinkphp.cn/down/framework.html]()


####基础语法
文件起始标识:

</php

?>


####命名空间和引用


####目录结构



####相关配置
	修改环境路径:
	xamppfiles/etc/httpd.conf/DocumentRoot&Directory
	修改重定向URL:xamppfiles/htdocs/index.php
	Apache配置文件:这个配置文件的位置是：
	/private/etc/apache2/httpd.conf
	定位或者设置 DocumentRoot。这是网站所有文件的根目录。此目录中	的文件由 web 服务器提供服务，从而使得 PHP 文件将在输出到浏览器	之前解析为 PHP 脚本。通常情况下默认的路径是:
	 /Library/WebServer/Documents，但是可以根据需要在 	httpd.conf中设置为任何其他目录。另外，用户自己的缺省 	DocumentRoot 是 /Users/yourusername/Sites。
	注意:配置文件修改之后需要重启Apache服务



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

