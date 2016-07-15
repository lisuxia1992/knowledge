###thinkPHP5.0


####准备工作



####基础语法
文件起始标识:

</php

?>



####目录结构



####相关配置
	修改环境路径:xamppfiles/etc/httpd.conf
	修改重定向URL:xamppfiles/htdocs/index.php




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

