---
title: "【笔记】《动手学深度学习》随笔 part1 —— pytorch 基本操作"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/2a0a04ba8c63c76919fe2f0286af7d96.jpeg"
tags:
  - Note
  - ML
  - pytorch
categories:
  - Machine Learning
  - pytorch
abbrlink: a3c53bfd
date: 2023-10-07 15:00:00
updated: 2023-10-07 15:00:00
---


## 数值操作

模块导入：


```python
import torch
```


用 `torch.arange()` 创建向量：


```python
>>> torch.arange(12)
```


```python
tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
```

{% note info %}

参数列表：`torch.arange(start=0, end, step=1, \*, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) → Tensor`

`start` `end` `step` ：起始值，结束值和步长。

`dtype` ：指定数据类型。

`out` ：输出张量。

`layout` ：布局方式，一般有以下两种：

* `torch.strided` ：密集布局，张量元素按一定步幅排列在内存中，相邻元素间地址差距连续，但元素不一定连续存储。

* `torch.sparse_coo` ：稀疏布局。只存储非零元素的索引和值，节省内存。访问 [Link](https://runebook.dev/zh/docs/pytorch/sparse#sparse-docs) 获取更多信息。

`device` ：设备。例如可选 `cpu` 或 `cuda` 。

`requires_grad` ：是否为张量启用梯度计算。

{% endnote %}

用 `torch.reshape()` 改变张量形状：


```python
>>> x = torch.arange(12).reshape((2, 3, 2))
>>> x
```


```python
tensor([[[ 0,  1],
         [ 2,  3],
         [ 4,  5]],

        [[ 6,  7],
         [ 8,  9],
         [10, 11]]])
```

{% note info %}

注：可以用 $-1$ 表示自动填充某一个轴的大小。

如 `x = torch.arange(12).reshape((-1, 3, 2))` 就和以上语句等价。

{% endnote %}

用 `shape` 获取沿所有轴的元素个数：


```python
>>> x.shape
```


```python
torch.Size([2, 3, 2])
```

{% note info %}

如果只对张量的第一个维度感兴趣，可以用 `len(x)` 。

{% endnote %}

用 `torch.zeros(),torch.ones()` 获得全0 / 全1 张量：


```python
>>> torch.zeros(2, 3)
```


```python
tensor([[0., 0., 0.],
        [0., 0., 0.]])
```


```python
>>> torch.ones(2, 3)
```


```python
tensor([[1., 1., 1.],
        [1., 1., 1.]])
```


用 `torch.randn()` 随机采样（会生成均值为 0，标准差为 1 的正态分布）：


```python
>>> torch.randn(2, 3, 4)
```


```python
tensor([[[ 0.2692,  0.0791,  0.0039, -0.1389],
         [-0.1045, -0.3420,  0.2542,  1.4940],
         [ 1.5095,  1.1909, -0.5695,  1.4376]],

        [[ 0.5032, -0.1839, -0.0568,  0.1740],
         [-0.2951,  2.4619,  1.2984,  0.0647],
         [-0.5046,  0.9516, -0.0810, -0.3269]]])
```

{% note success %}

更一般地，有库函数 `torch.normal(mean, std, size, out=None)` 。

`mean` ：正态分布的均值。

`std` ：正态分布的标准差。

`size` ：生成的张量形状。可以是整数（一维向量），也可以是元组或列表（多维张量）。

`out` ：如果提供了一个输出张量，随机生成的值将存储在这个张量中，而不是创建一个新的张量。

故 `torch.randn(2, 3, 4)` 等效于：


```python
>>> torch.normal(0.0, 1.0, (2, 3, 4))
```

{% endnote %}

指定值：


```python
>>> x = torch.tensor([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
>>> x
```


```python
tensor([[1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3]])
```


用 `sum()` 求和：


```python
>>> x.sum()
```


```python
tensor(24)
```


用 `axis=0` 指定沿列求和：


```python
>>> x.sum(axis=0)
```


```python
tensor([6, 6, 6, 6])
```


用 `axis=1` 指定沿行求和：


```python
>>> x.sum(axis=1)
```


```python
tensor([4, 8, 12])
```


用 `keepdims=True` 非降维求和（保持原有行/列的形状）：


```python
>>> x.sum(axis=1, keepdims=True)
```


```python
tensor([[ 4],
        [ 8],
        [12]])
```


用 `numel()` 获取总元素个数：


```python
>>> x.numel()
```


```python
12
```


四则运算：形状相同，按元素操作


```python
>>> x = torch.tensor([1, 2, 4, 8])
>>> y = torch.tensor([2, 2, 2, 2])
>>> x + y, x - y, x * y, x / y, x ** y
```


```python
( tensor([ 3,  4,  6, 10]), 
  tensor([-1,  0,  2,  6]), 
  tensor([ 2,  4,  8, 16]), 
  tensor([0.5000, 1.0000, 2.0000, 4.0000]), 
  tensor([ 1,  4, 16, 64]) )
```


其中，单纯两个矩阵中每个值按元素相乘，称为 `Hadamard 积` 。

`x.exp()` $\to$ $e^x$


```python
>>> x.exp()
```


```python
tensor([2.7183e+00, 7.3891e+00, 5.4598e+01, 2.9810e+03])
```


用 `dtype` 指定元素类型：


```python
>>> x = torch.arange(12, dtype=torch.float32).reshape((3, 4))
>>> x
```


```python
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
```


用 `cat` 沿行（轴 0）拼接张量：


```python
>>> y = torch.tensor([[1.0, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
```


```python
tensor([[1., 1., 1., 1.],
        [2., 2., 2., 2.],
        [3., 3., 3., 3.]])
```


```python
>>> torch.cat((x, y), dim=0)
```


```python
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.],
        [ 1.,  1.,  1.,  1.],
        [ 2.,  2.,  2.,  2.],
        [ 3.,  3.,  3.,  3.]])
```


用 `cat` 沿列（轴 1）拼接张量：


```python
>>> torch.cat((x, y), dim=1)
```


```python
tensor([[ 0.,  1.,  2.,  3.,  1.,  1.,  1.,  1.],
        [ 4.,  5.,  6.,  7.,  2.,  2.,  2.,  2.],
        [ 8.,  9., 10., 11.,  3.,  3.,  3.,  3.]])
```


按元素比较：


```python
>>> x == y
```


```python
tensor([[False,  True, False, False],
        [False, False, False, False],
        [False, False, False, False]])
```


利用广播机制使得不同形状的张量执行按元素操作，`tensor` 会自动扩充维度。

两个“可广播的” `tensor` 满足以下条件：

* 每个 `tensor` 至少一个维度。

* 从末尾遍历 `tensor` 所有维度时，出现以下情况：

  * 维度相等。

  * 维度不等 && 其中一个维度为 $1$。

  * 维度不等 && 其中一个维度不存在。


满足规则，将小的扩展成大的 `tensor` 。


```python
>>> x = torch.arange(2).reshape((2, 1))
>>> y = torch.arange(4).reshape((1, 4))
>>> x, y
```


```python
(tensor([[0],
        [1]]), tensor([[0, 1, 2, 3]]))
```


```python
>>> x + y
```


```python
tensor([[0, 1, 2, 3],
        [1, 2, 3, 4]])
```


这时候就体现非降维求和的优势了：


```python
>>> x = torch.arange(12).reshape((3, 4))
>>> x
```


```python
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
```


```python
>>> sum_x = x.sum(axis=1, keepdim=True)
>>> sum_x
```


```python
tensor([[ 6],
        [22],
        [38]])
```


```python
>>> x / sum_x
```


```python
tensor([[0.0000, 0.1667, 0.3333, 0.5000],
        [0.1818, 0.2273, 0.2727, 0.3182],
        [0.2105, 0.2368, 0.2632, 0.2895]])
```


可以看到对每一行/列求了平均，而不会因维度对不上而报错。

与 python 字符串类似地进行索引。


```python
>>> x = torch.arange(12).reshape((3, 4))
>>> x
```


```python
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
```


```python
>>> x[-1]
```


```python
tensor([ 8,  9, 10, 11])
```


```python
>>> x[1:3]
```


```python
tensor([[ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
```


将指定元素写入：


```python
>>> x[2, 2] = 114514
```


```python
tensor([[     0,      1,      2,      3],
        [     4,      5,      6,      7],
        [     8,      9, 114514,     11]])
```


多元素赋值，先 0 轴后 1 轴。


```python
>>> x[0:2, 0:3] = 1919810
```


```python
tensor([[1919810, 1919810, 1919810,       3],
        [1919810, 1919810, 1919810,       7],
        [      8,       9,  114514,      11]])
```


以分配新内存的方式分配 $x$ 的副本给 $y$：


```python
>>> y = x.clone()
```


用 `mean()` 求所有均值（注意必须是浮点型）：


```python
>>> x = torch.arange(12, dtype=torch.float32).reshape((3, 4))
>>> x
```


```python
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
```


```python
>>> x.mean()
```


```python
tensor(5.5000)
```

`x.mean(axis=0)` 等价于 `x.sum(axis=0) / x.shape[0]`

用 `cumsum` 沿着某个维度计算累计总和：


```python
>>> x.cumsum(axis=0)
```


```python
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  6.,  8., 10.],
        [12., 15., 18., 21.]])
```


用 `torch.unsqueeze()` 增加数据维度：


```python
>>> x = torch.arange(4)  # tensor([0, 1, 2, 3])
>>> x = torch.unequeeze(x, 0)
>>> x
```


```python
tensor([[0, 1, 2, 3]])
```


可以看到最外层增加了一维。

{% note info %}

参数列表：`new_tensor = torch.unsqueeze(input, dim)`

`input`：需要操作的张量。

`dim`：要在哪个维度上增加一个维度。

返回值是一个新的张量。

{% endnote %}

## 线性代数操作

矩阵转置：


```python
>>> A = torch.arange(20, dtype=torch.float32).reshape(4, 5)
>>> A
```


```python
tensor([[ 0.,  1.,  2.,  3.,  4.],
        [ 5.,  6.,  7.,  8.,  9.],
        [10., 11., 12., 13., 14.],
        [15., 16., 17., 18., 19.]])
```


```python
>>> A.T
```


```python
tensor([[ 0.,  5., 10., 15.],
        [ 1.,  6., 11., 16.],
        [ 2.,  7., 12., 17.],
        [ 3.,  8., 13., 18.],
        [ 4.,  9., 14., 19.]])
```


点积（Dot Product）$\textbf{x}^\top \textbf{y} = \sum x_iy_i$：


```python
>>> x = torch.arange(5, dtype=torch.float32)
>>> y = torch.ones(5, dtype = torch.float32)
>>> x, y
```


```python
(tensor([0., 1., 2., 3., 4.]), tensor([1., 1., 1., 1., 1.]))
```


```python
>>> torch.dot(x, y)
```


```python
tensor(10.)
```


等效表达 `torch.sum(x * y)` 。

矩阵-向量积：

对于一个矩阵 $^{mn}$，和向量 $\textbf{x}\in \mathbb{R}^{n}$。$\textbf{Ax} = \begin{bmatrix} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \ldots & a_{mn} \end{bmatrix}$ $\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_m \end{bmatrix}$ $= \begin{bmatrix} \left\langle a_1x\right\rangle \\ \left\langle a_2x\right\rangle \\ \vdots \\ \left\langle a_mx\right\rangle \end{bmatrix}$

$\left\langle a_ix \right\rangle$ 表示矩阵的第 $i$ 行构成的行向量和向量 $x$ 的点积。

利用 `mv(A, x)` 进行矩阵-向量积：


```python
>>> A, x
```


```python
(tensor([[ 0.,  1.,  2.,  3.,  4.],
        [ 5.,  6.,  7.,  8.,  9.],
        [10., 11., 12., 13., 14.],
        [15., 16., 17., 18., 19.]]), tensor([0., 1., 2., 3., 4.]))
```


```python
>>> torch.mv(A, x)
```


```python
tensor([ 30.,  80., 130., 180.])
```


利用 `mm(A, B)` 矩阵乘法：


```python
>>> B = torch.ones(5, 4)
```


```python
tensor([[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]])
```


```python
>>> torch.mm(A, B)
```


```python
tensor([[10., 10., 10., 10.],
        [35., 35., 35., 35.],
        [60., 60., 60., 60.],
        [85., 85., 85., 85.]])
```

{% note success %}

更加通用地，有库函数 `torch.matmul(input, other, out=None)` 执行矩阵相乘。

`input` ：要进行矩阵相乘的第一个张量（或标量）。

`other` ：要进行矩阵相乘的第二个张量（或标量）。

`out` ：如果提供了输出张量，结果将存储在这个张量中，而不是创建一个新的张量。

`torch.normal()` 的行为取决于输入张量的维度。

1. 若两个张量均一维，执行内积（点积）操作，返回一个标量。

2. 若两个张量均二维，它执行矩阵乘法，返回一个二维矩阵。

3. 若至少一个张量高维，它执行广义矩阵乘法操作，根据广播规则计算结果。

{% endnote %}

利用 `norm(x)` 求 $L_2$ 范数：
$$
\| \mathbf{v} \|_2 = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
$$


```python
>>> v = torch.tensor([3.0,-4.0])
>>> torch.norm(v)
```


```python
tensor(5.)
```


$L_1$ 范数：


```python
>>> torch.abs(v).sum()
```


```python
tensor(7.)
```


矩阵的 $L_2$ 范数：（Frobenius范数）
$$
\|A\|_2=\sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}|a_{ij}|^2}
$$


```python
>>> torch.norm(torch.ones((4, 9)))
```


```python
tensor(6.)
```

## 微分操作

用 `requires_grad = True` 为张量启动梯度计算：


```python
>>> x = torch.arange(4.0, requires_grad = True) 
>>> x
```


```python
tensor([0., 1., 2., 3.])
```


另一种写法：


```python
>>> x.requires_grad_(True)
```


利用 `backward()` 计算梯度：


```python
>>> y = torch.dot(x, x)
>>> y.backward()
```

{% note warning %}

注意，使用点积而不是乘法，因为 pytorch 只能对标量求梯度。

不过可以使用 `y.sum().backward()` 。

效果和 `y.backward(torch.ones_like(y))` 等同。

{% endnote %}

利用 `.grad` 显示梯度：


```python
>>> x.grad
```


```python
tensor([0., 2., 4., 6.])
```


由 $\nabla \textbf{x}^\top\textbf{x}=2\textbf{x}$ 得知答案正确，也可以利用程序验证。


```python
>>> x.grad == 2 * x
```


```python
tensor([True, True, True, True])
```


重置梯度值为 0 ，以便后续计算其它梯度：


```python
>>> x.grad.zero_()
```


利用 `.detach()` 停止梯度传播：对比两个例子：


```python
>>> x = torch.arange(4.0, requires_grad = True) # [0, 1, 2, 3]
>>> y = x * x
>>> y1 = y * x
>>> y1.sum().backward()
>>> x.grad
```


```python
tensor([0., 3., 12., 27.])
```


```python
>>> x = torch.arange(4.0, requires_grad = True) # [0, 1, 2, 3]
>>> y = x * x
>>> y2 = y.detach() * x
>>> y2.sum().backward()
>>> x.grad
```


```python
tensor([0., 1., 4., 9.])
```


可以看到前者计算的是 $y1=x\times x \times x$ 的偏导数为 $3x^2$。

而后者则是 $y2=u\times x$（$u$ 看作常量，数值等于 $y$）的偏导数，即为 $u=x^2$。

{% note info %}

此外，还可以用一个上下文管理器 `torch.no_grad()` 来禁止梯度传播。

例如以下是第二个例子的等价形式：


```python
>>> x = torch.arange(4.0, requires_grad = True) # [0, 1, 2, 3]

>>> with torch.no_grad():
        y = x * x;
    
>>> y2 = y * x;
>>> y2.sum().backward()
>>> x.grad
```


```python
tensor([0., 1., 4., 9.])
```

{% endnote %}

利用 `retain_graph=True` 保留计算图，以便再次 `backward()` ：


```python
>>> x = torch.arange(4.0, requires_grad=True)
>>> y = torch.dot(x, x)
>>> y.backward(retain_graph=True)
>>> y.backward()
```


若第三行换成 `y.backward()` 则会报错。

## 线性回归

模块导入


```python
from torch import nn
```


用 `nn.Linear` 定义一个线性层：


```python
>>> model = nn.Linear(2, 1) # 输入特征数为2,输出特征数为1(标量)
```

{% note info %}

参数列表：`torch.nn.Linear(in_features, out_features, bias=True)`

`in_features` ：输入神经元个数，即输入特征数。

`out_features` ：输出神经元个数，即输出特征数。

`bias` ：是否包含偏置。

本质是执行了一个线性变换：
$$
\textbf{Y}_{n\times out} = \textbf{X}_{n\times in}\textbf{W}_{in\times out}+\textbf{b}
$$

其中 $n$ 是样本数量，或者说 `batch_size` 。$in,out$ 为输入和输出的特征维度，$\textbf{b}$ 为 $out$ 维的向量偏置，使用了广播机制。

{% endnote %}

用 `nn.Sequential` 定义神经网络容器：


```python
>>> net = nn.Sequential(model)
```


作用是按顺序组织一系列神经网络的层（layer），例如：


```python
>>> model = nn.Sequential(
        nn.Conv2d(1, 20, 5),
        nn.ReLU(),
        nn.Conv2d(20, 64, 5),
        nn.ReLU()
        )
```


我们可以通过下标访问元素，如：


```python
>>> net = nn.Sequential(
        nn.Linear(2, 1)
        	# other
    )
>>> net[0].weight.data.normal_(0, 0.01)
>>> net[0].bias.data.fill_(0)
```


通过 `net[0]` 去访问了 `Linear` 类中的函数，使模型参数初始化。

其中 `weight` 和 `bias` 指明要访问权值还是偏置数据，`normal_` 和 `fill_` 则是 pytorch 的两个张量方法。

`tensor.normal_(mean=0, std=1)` 指定随机抽样的正态分布均值和标准差。

`tensor.fill_(value)` 则直接填充 `value` 值。

调用损失函数：


```cpp
>>> nn.MSELoss() # 均方误差，或称平方L2范数
PYTHON
```

{% spoiler 常见损失函数 %}

`L1Loss()` ：L1 范数损失（MAE）

`MSELoss()` : 均方误差（MSE）

`SmoothL1Loss()` ：L1 平滑损失。

`CrossEntyopyLoss()` ：交叉熵损失

`NLLloss()` ：负对数似然损失。

`BCELoss()` ：二元交叉熵损失。

{% endspoiler %}

用 `torch.optim.SGD` 执行小批量随机梯度下降算法并更新：


```python
>>> trainer = torch.optim.SGD(net.parameters(), lr=0.03)
>>> trainer.step()
```

`parameters()` 用于自动读取参数，`lr` 为学习率（LearningRate）。

完整实例（《动手学深度学习》章节3.3）：


```python
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l
from torch import nn

true_w = torch.tensor([2, -3.4])
true_b = 4.2

# 生成多个噪声数据
features, labels = d2l.synthetic_data(true_w, true_b, 1000)

# 构建PyTorch数据迭代器
def load_array(data_arrays, batch_size, is_train=True):  #@save
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch_size = 10
data_iter = load_array((features, labels), batch_size)

next(iter(data_iter))

# 创建神经网络
net = nn.Sequential(nn.Linear(2, 1))

# 初始化参数
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)

loss = nn.MSELoss()

trainer = torch.optim.SGD(net.parameters(), lr=0.03)

num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X) ,y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')


w = net[0].weight.data
print('w的估计误差：', true_w - w.reshape(true_w.shape))
b = net[0].bias.data
print('b的估计误差：', true_b - b)

# 访问线性回归的梯度
w_grad = net[0].weight.grad
print('w的梯度：', w_grad)
b_grad = net[0].bias.grad
print('b的梯度：', b_grad)
```


```python
epoch 1, loss 0.000232
epoch 2, loss 0.000101
epoch 3, loss 0.000100
w的估计误差： tensor([ 0.0002, -0.0003])
b的估计误差： tensor([-0.0003])
w的梯度： tensor([[-0.0041, -0.0147]])
b的梯度： tensor([0.0073])
```

## 激活函数

1. $\text{ReLU}(x)$ 函数

$$
\text{ReLU}(x)=\max(x,0)
$$


```python
>>> x = torch.arange(-3.0, 3.0, 0.5, requires_grad=True)
>>> y = torch.relu(x)
>>> x, y
>>> y.backward(torch.ones_like(x), retain_graph=True)
```


```python
(tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
          1.0000,  1.5000,  2.0000,  2.5000], requires_grad=True),
 tensor([0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.5000, 1.0000,
         1.5000, 2.0000, 2.5000], grad_fn=<ReluBackward0>))
```


![](https://zh-v2.d2l.ai/_images/output_mlp_76f463_21_0.svg)

一个显著的性质是对 $\text{ReLU}(x)$ 求导后非 $0$ 即 $1$，即要么让参数消失，要么让参数通过。

![](https://zh-v2.d2l.ai/_images/output_mlp_76f463_36_0.svg)

变体：（即使参数是负的，某些信息仍然可以通过）
$$
\text{pReLU}(x)=\max(0,x) + \alpha\min(0,x)
$$

2. $\text{sigmoid}(x)$ 函数（“S”型函数）

$$
\text{sigmoid}(x)=\dfrac{1}{1+e^{-x}}
$$


```python
>>> y = torch.sigmoid(x)
>>> x.grad.zero_()
>>> y.backward(torch.ones_like(x), retain_graph=True)
```


![](https://zh-v2.d2l.ai/_images/output_mlp_76f463_51_0.svg)

$$
\dfrac{d}{dx}\text{sigmoid}(x)=\dfrac{e^{-x}}{(1+e^{-x})^2}=\text{sigmoid}(x)(1-\text{sigmoid}(x))
$$

![](https://zh-v2.d2l.ai/_images/output_mlp_76f463_66_0.svg)

易知 $x=0$ 时有导数最大值 $\dfrac{1}{4}$。

