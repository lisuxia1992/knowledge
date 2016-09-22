###React Native开发


####React Native的优势
相比于Hybrid App和Web App： 

1. 不依赖WebView，彻底摆脱WebView让人不爽的交互和性能问题； 
2. 可使用iOS“牛逼的”原生动画； 
4. Facebook维护的开源项目，非常活跃的开源社区，稳定性和可持续性得到保障。站在巨人的肩膀上，不用再造轮子； 
3. 具有较强的扩展性，Native提供的原生控件在JS中可以自有组合使用； 
5. TouchableXXX，点击事件也被抽象成了JS组件，实时的点按和取消能力；

相比于Native App： 

1. 可以通过更新云端JS，直接更新App，大型Native App都在做的Hybrid App方案； 
3. 调试和发布过程无需二次编译，节省调试时间成本； 
4. 复用React系统和css-layout，分层、diff机制、Virtual Dom等NB的架构和设计模式； 
5. React Native可以让JS直接运行在Mac Chrome中，极大的方便了调试。自带Reveal；



####入口文件
React Native项目初始化时默认的入口文件是index.ios.js，根据我们在React Native入门实例教程 - 从现有项目迁移中的配置，运行项目后会将index.ios.js以及所以来的JS文件打包成index.ios.bundle。

通过Node.js Server访问这个bundle，就可以得到所需要的视图。

由于调试server的根目录指向React Native的环境目录（node_modules、package.json等文件所在的目录），因此入口文件访问的路径为：http://localhost:8081/ReactComponents/CustomModule1/custom1.ios.bundle。注意是文件后缀是bundle而不是js。





####常用组件
总体认识react 

	import React, { Component } from 'react';
	import { render } from 'react-dom';

	class HelloMessage extends Component {
  		render() {
    		return <div>Hello {this.props.name}</div>;
  		}
	}
	// 加载组件到 DOM 元素 mountNode
	render(<HelloMessage name="John" />, mountNode);

React 应用都是构建在组件之上。

上面的 HelloMessage 就是一个 React 构建的组件，最后一句 render 会把这个组件显示到页面上的某个元素 mountNode 里面，显示的内容就是 <div>Hello John</div>。

props 是组件包含的两个核心概念之一，另一个是 state（这个组件没用到）。可以把 props 看作是组件的配置属性，在组件内部是不变的，只是在调用这个组件的时候传入不同的属性（比如这里的 name）来定制显示这个组件。


#####props

前面也提到很多次了，props 就是组件的属性，由外部通过 JSX 属性传入设置，一旦初始设置完成，就可以认为 this.props 是不可更改的，所以不要轻易更改设置 this.props 里面的值（虽然对于一个 JS 对象你可以做任何事）。

#####state

state 是组件的当前状态，可以把组件简单看成一个“状态机”，根据状态 state 呈现不同的 UI 展示。

一旦状态（数据）更改，组件就会自动调用 render 重新渲染 UI，这个更改的动作会通过 this.setState 方法来触发。


##### AppRegister

Native和JS沟通的重要桥梁。将当前自定义组件注册成Native可访问的Module，以便Native的React Native视图可以访问这个Module显示到应用中。

##### StyleSheet

样式表组件，提供类似css-layout的语法，很好的配合了JSX构建视图。

##### View&Text etc.

一些普通的视图组件，比较简单，复杂的也有ScrollView、ListView等。有些是桥接的Native控件

它们是React Native视图的核心组成部分，遗憾的是接口API描述并不明确，没有我们开发iOS或者Android应用时的文档详细，有时需要进入到源码中去找。

##### Navigator

导航控制器在任何视图构建模式中都是非常重要的组成部分，尤其在大型项目中往往决定了项目的开发复杂度和成本。有关React Native的Navigator会有专门的文章讲解。

##### TouchableOpacity

React Native的一个强大之处就在于提供接近于Native的交互体验，比如按钮的按下态，从按钮区域移走之后按下态消失，这在Web App中是可望而不可及的。TouchableOpacity提供了手势相关的，类似于iOS Responder Chain的机制

#####Probider
<Provider> 作为一个容器组件，用来接受 Store，并且让 Store 对子组件可用，用法如下：

	import { render } from 'react-dom';
	import { Provider } from 'react-redux';
	import App from './app';

	render(
 		<Provider store={store}>
    		<App />
 		 </Provider>,
 	 	document.getElementById('root')
	);
这时候 <Provider> 里面的子组件 <App /> 才可以使用 connect 方法关联 store。
<Provider> 的实现很简单，他利用了 React 一个（暂时）隐藏的特性 Contexts，Context 用来传递一些父容器的属性对所有子孙组件可见，在某些场景下面避免了用 props 传递多层组件的繁琐


#####组件的生命周期

一般来说，一个组件类由 extends Component 创建，并且提供一个 render 方法以及其他可选的生命周期函数、组件相关的事件或方法来定义。

	import React, { Component } from 'react';
	import { render } from 'react-dom';

	class LikeButton extends Component {
  		constructor(props) {
    		super(props);
    		this.state = { liked: false };
  		}

  		handleClick(e) {
    	this.setState({ liked: !this.state.liked });
  	}
  	render() {
    	const text = this.state.liked ? 'like' : 'haven\'t liked';
    	return (
      		<p onClick={this.handleClick.bind(this)}>
          	You {text} this. Click to toggle.
     		 </p>
    		);
  		}
	}

	render(
    	<LikeButton />,
    	document.getElementById('example')
	);


######装载组件触发

componentWillMount

只会在装载之前调用一次，在 render 之前调用，你可以在这个方法里面调用 setState 改变状态，并且不会导致额外调用一次 render

componentDidMount

只会在装载完成之后调用一次，在 render 之后调用，从这里开始可以通过 ReactDOM.findDOMNode(this) 获取到组件的 DOM 节点。
######更新组件触发

这些方法不会在首次 render 组件的周期调用

- componentWillReceiveProps
- shouldComponentUpdate
- componentWillUpdate
- componentDidUpdate

######卸载组件触发

componentWillUnmount



####项目打包发布
<http://402v.com/react-nativeru-men-shi-li-jiao-cheng-kai-shi-kai-fa/>


####参考文章

<http://blog.csdn.net/wds1181977/article/details/51861779>
<https://hulufei.gitbooks.io/react-tutorial/content/introduction.html>
<http://402v.com/react-nativeru-men-shi-li-jiao-cheng-xi-lie-wen-zhang/>