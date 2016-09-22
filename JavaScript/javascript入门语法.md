###JavaScript入门语法

从现有项目迁移参考：
<http://402v.com/react-nativeru-men-shi-li-jiao-cheng-cong-xian-you-xiang-mu-qian-yi/>

####'use strict';-JavaScript严格模式的标志

严格模式的目的：

1. 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为;
2. 消除代码运行的一些不安全之处，保证代码运行的安全；
3. 提高编译器效率，增加运行速度；
4. 为未来新版本的Javascript做好铺垫。


严格模式的调用：

1. 针对整个脚本文件：必须放在产生实际运行效果的第一行
2. 针对单个函数：放在函数体的第一行

语法规则：

1. 全局变量必须显示声明，即先var声明，在使用
2. 禁止使用with语句：因为编译器无法确定属性归属哪个对象
3. eval语句本身就是一个作用域，不再能够生成全局变量了，它所生成的变量只能用于eval内部
4. 禁止this关键字指向全局对象：因此，使用构造函数时，如果忘了加new，this不再指向全局对象，而是报错。
5. 禁止在函数内部遍历调用栈
6. 禁止删除变量：严格模式下无法删除变量。只有configurable设置为true的对象属性，才能被删除。
7. 对一个使用getter方法读取的属性进行赋值，会报错。对禁止扩展的对象添加新属性，会报错。删除一个不可删除的属性，会报错。
8. 对象不能有重名属性，函数不能有重名参数
9. 禁止八进制表示
10. 不允许对argument赋值；禁止使用arguments.callee（你无法在匿名函数内部调用自身了）；arguments不再追踪参数的变化


####require-加载一个node.js模块

语法：

1. var {} = React：引入当前文件会用到的组件
2. render(){} ：组件渲染
3. AppRegistry.registerComponent('SampleApp', () => SampleApp);:模块注册



####模块和文件
模块是node.js的组成部分，一个js文件就是一个模块，所以，文件和模块是一一对应关系

模块又分为核心模块和文件模块

文件模块又分为：

1. .js。通过fs模块同步读取js文件并编译执行。
2. .node。通过C/C++进行编写的Addon。通过dlopen方法进行加载。
3. .json。读取文件，调用JSON.parse解析加载。

Node.提供了exports和require两个对象,其中exports是模块公开的接口,require用于从外部获取一个模块接口,即所获取模块的exports对象.

#####require
require查找策略
![require查找策略](https://nzw3d6nir.qnssl.com/images/2013/05/nodejs-require.jpg-Watermark)

原生模块在Node.js源代码编译的时候编译进了二进制执行文件，加载的速度最快。另一类文件模块是动态加载的，加载速度比原生模块慢。但是Node.js对原生模块和文件模块都进行了缓存，于是在第二次require时，是不会有重复开销的。尽管require方法极其简单，但是内部的加载却是十分复杂的，其加载优先级也各自不同。

require方法中接受的参数：

1. http、fs、path等，原生模块。
2. ./mod或../mod，相对路径的文件模块。
3. /pathtomodule/mod，绝对路径的文件模块。
4. mod，非原生模块的文件模块。

当require一个文件模块时,从当前文件目录开始查找node_modules目录；然后依次进入父目录，查找父目录下的node_modules目录；依次迭代，直到根目录下的node_modules目录。

查找流程：

1. 从module path数组中取出第一个目录作为查找基准。
2. 直接从目录中查找该文件，如果存在，则结束查找。如果不存在，则进行下一条查找。
3. 尝试添加.js、.json、.node后缀后查找，如果存在文件，则结束查找。如果不存在，则进行下一条。
4. 尝试将require的参数作为一个包来进行查找，读取目录下的package.json文件，取得main参数指定的文件。
5. 尝试查找该文件，如果存在，则结束查找。如果不存在，则进行第3条查找。
6. 如果继续失败，则取出module path数组中的下一个目录作为基准查找，循环第1至5个步骤。
7. 如果继续失败，循环第1至6个步骤，直到module path中的最后一个值。
8. 如果仍然失败，则抛出异常。


#####export

export的理解：

1. 一个模块可以通过module.exports或exports将函数、变量等导出，以使其它JavaScript脚本通过require()函数引入并使用。
2. exports默认和module.exports指向同一个空对象。
3. 如果你想你的模块是一个特定的类型就用module.exports。如果你想的模块是一个典型的”实例化对象”就用exports。
4. 如果运行时让exports、this和module.exports指向不同的对象，只有module.exports指向的对象才回被导出。module.exports才是真正的接口，exports只不过是它的一个辅助工具。 最终返回给调用的是module.exports而不是exports。 所有的exports收集到的属性和方法，都赋值给了module.exports。当然，这有个前提，就是module.exports本身不具备任何属性和方法



####import

动态加载js或css文件，方法或变量

被加载文件中需配套使用export关键字导出本类，方法或变量





####参考文章
<http://402v.com/react-nativeru-men-shi-li-jiao-cheng-ge-wan-zheng-de-react-nativeli-zi/>
<https://liuzhichao.com/p/1669.html>


