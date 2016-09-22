###React Native中postion、flexbox布局

主要包含以下几种：

(1)  flex

(2)  position

(3)  flexDirection

(4)  flexWrap

(5)  justifyContent

(6)  alignItems

(7)  alignSelf


####flex

flex键的类型是数值，取值为0或者大于0的整数，默认值为0。当它的值为1时且子组件只有自己时，子组件将自动缩放以适应父组件剩下的所有空白空间。

当一个父组件中有多个子组件时，比如下面的案例中，container组件中有4个子组件，子组件的flex值分别为，1，1，2，1，那么 container就会被平分为5份，他们所占的面积比例关系为:1:1:2:1

![](http://img0.tuicool.com/zm2iUfu.png)

####position
position，它是字符串类型，可以取值为relative(默认值)或者absolute，表示当前描述的位置是相对位置还是绝对定位的。 与位置相关样式设置键还有：top、bottom、left、right。它们都是数值类型，表示描述的位置从左或者右多少位置显示，或者从上或者下多少位置显示。

当position键的值为absolute时，描述位置可以使用top、bottom、left、right四个键，表示当前组件的位置距离父组件上（下、左、右）沿有多少pt。
![](http://img1.tuicool.com/AJfyiiV.png)

当postion键的值为relative时，不可以使用bottom和right键继续描述位置。top和left键的值默认为0.top和left键表示当前组件距离上一个同级组件最上（左）沿有多少pt。

![](http://img0.tuicool.com/UjURRv.png)

####flexDirection

flexDirection键决定了组件内部的子组件是如何排列的，它的取值可以为column、row，对应下图中的左起第二个、第三个图。而W3C提出的row-reverse和column-reverse则不支持，如果View的样式里没有定义flexDirection，则默认值为column。
![](http://img0.tuicool.com/vYFbmmA.png)

####flexWrap

在默认情况下，组件中的子组件按照flexDirection键决定的方向一直排列下去，即使超出了该方向的宽度或者高度也不管。 对flexWrap键赋值可以改变这种情况。它可以取两个字符串类型值中的一个：wrap或者nowrap，默认的值为nowrap，表示不会自动换行(或者换列)排列。flexDireaction为row、flexWrap为wrap时工作示意图如下图所示。
![](http://img2.tuicool.com/vYNjIbI.png)

####justifyContent

justifyContent键用来定义方向上如何排列子组件。它有5种可能的字符串值：flex-start、flex-end、center、space-between、space-around,它们对应的布局示意图如下图所示。
![](http://img0.tuicool.com/7juimif.png)


####alignItems

alignItems键定义了View组件中所有子组件的对其规则。它有4种可能的字符串值：flex-start、flex-end、center、stretch。其中，flex-start代表顶部对齐；flex-end代表底部对齐；center 代表中部对齐；stretch代表拉长对齐。它们的布局示意图如下图所示：
![](http://img0.tuicool.com/IFfemmA.png)

####alignSelf

alignSelf键有5种可能的字符串类型值：auto、flex-start、flex-end、center、stretch。其用途是让组件忽略它的父组件样式中的alignItems键的取值，而对该组件使用的alignSelf键对应的规则。当它取值为auto时，表示使用父View组件的alignSelf值，其它4个值的汉语与alignItems相同。下图显示了当父组件的alignItems设置为flex-start ，而第三个字组件的alignSelf设置flex-end时的情况。
![](http://img2.tuicool.com/NZbMNve.png)



####参考文章
[http://www.tuicool.com/articles/UzI7J3V](http://www.tuicool.com/articles/UzI7J3V)