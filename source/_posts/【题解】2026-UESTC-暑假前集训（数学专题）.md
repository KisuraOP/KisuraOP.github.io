---
title: 【题解】2026 UESTC 暑假前集训（数学专题）
sticky: 100
math: true
index_img: 'https://pic.rmb.bdstatic.com/bjh/d21fc45dd075b42e039ef1a7ad4dbca2.jpeg'
tags:
  - UESTC
categories:
  - Competitive Programming
  - Other
abbrlink: b15f5f41
date: 2026-06-14 14:48:38
---

可能是第一次完整地来做数学专题。

整体写下来我的感觉是，题目缺少趣味性，做起来很枯燥。题目肯定是没经过挑选的，题面写的也丑，所以没什么好的体验。总的来说，明显感觉到近三年数学专题的质量不断在下滑 (´・︵・｀)。

上班很忙，我没有时间把这份题解写的很细，但要点肯定是全的，可以当作官方题解的 tldr 版本。

任何问题可以 qq 和我交流。（工作日可能很晚才回复）

## A. 还原符号

[Code](https://cdoj.site/d/training_2026/record/6a252fdebbcebd48c85813bc)

题目给出了 $v_1=|\text{det}(A)|$ 和 $A$。先算出 $v_2=\text{det}(A)$，再选一个大质数 $p$，如果 $v_1\equiv v_2\pmod {p}$，就能断定行列式的值是正数。会判错当且仅当 $v_1\equiv -v_1\pmod {p}$，也就是 $p\mid v_1$，概率极小。亦可选择多个 $p$ 验证，时间复杂度 $O(n^3)$。

## B. Xor and And

[Code](https://cdoj.site/d/training_2026/record/6a25379bbbcebd48c85816ba)

令 $S=\oplus_{i=1}^{n} a_i$，转化为求 $f(A)\ \& \ (S \oplus f(A))$ 的最大值。按位来看，$S$ 的某一位是 $1$，这个式子恒等于 $0$；$S$ 的某一位是 $0$，贡献是 $f(A)$。综上，答案是 $f(A)\ \& \ (\sim S)$。

按位与运算对异或运算满足分配律，设 $A=\{a_{i_1}, a_{i_2},a_{i_3},\ldots\}$，那么 

$$
\begin{align}
&\quad\  f(A)\ \& \ (\sim S) \\
&=(a_{i_1}\oplus a_{i_2}\oplus a_{i_3}\oplus \cdots) \ \& \ (\sim S) \\
&=(a_{i_1}\ \&\ (\sim S))\oplus (a_{i_2}\ \&\ (\sim S))\oplus (a_{i_3}\ \&\ (\sim S))\oplus \cdots
\end{align}
$$

令 $a_i\leftarrow a_i\ \& \ (\sim S)$，用线性基求一组最大异或和即可。时间复杂度 $O(n\log w)$。

## C. 简单的排列题

[Code](https://cdoj.site/d/training_2026/record/6a22f68abbcebd48c857cd82)

将 $P$ 视作边集是 $i\to P_i$ 的有向图，$Q$ 视作边集是 $Q_{i}\to Q_{i+1}$ 的有向图，则 $Q_{i+1}\neq P_{Q_i}$ 就表示 $Q$ 不包含任何一条 $P$ 中的边。一些观察：

- $P$ 由若干互不相交的简单环构成。
- $Q$ 是一条完全图上，不包含任何 $P$ 中的边的哈密顿路径。

由容斥原理
$$
\begin{align}
合法\ Q\ 的数量 &=\sum_{k=0}^{n}(-1)^k\times(包含\ k\ 条 \ P\ 中的边的 \ Q\ 的数量)\\
&=\sum_{k=0}^{n}(-1)^k\times\underbrace{(钦定\ k\ 条 \ P\ 中的边属于 \ Q \ 的方案数)}_{\large f_k}\times (n-k)!
\end{align}
$$
对于 $P$ 中长度为 $l$ 的环，选 $i\in [0,l)$ 条边作为 $Q$ 的一部分都是合法的（即只要不选完一个完整的环就行）。令 $\large G_l(x)=\sum\limits_{i=0}^{l-1}\dbinom{l}{i}x^i$，则 $\large f_k=[x^k]\prod\limits_{i=1}^{m}G_{l_i}(x)$。其中 $l_1,l_2,\ldots,l_m$ 表示 $P$ 中每个环的长度。

每次合并两个次数最低的多项式，依据主定理，时间复杂度为 $O(n\log^2 n)$。

## D. 简单博弈论题

[Code](https://cdoj.site/d/training_2026/record/6a245b0ebbcebd48c857fd6b)

相当于算 $\oplus_{i=1}^{n}a_i=0$ 且 $a_i$ 均为不大于 $m$ 的质数的 $\{a\}$ 的数量。

令 $f[x]=\begin{cases}1 &, \ x \ 是不大于 \ m \ 的质数\\ 0 &, \ \text{otherwise}\end{cases}$，答案就是 $f$ 自身经过 $n$ 次异或卷积之后，下标为 $0$ 处的值。

注意到 $FWT(f\oplus g)=FWT(f)\cdot FWT(g)$ 有结合律，我们先对 $f$ 做一次 FWT，把数组中的每个元素 $n$ 次方一下，再 IFWT 回去即可。时间复杂度 $O(T\cdot 2^{16}\cdot 16)$。

## E. counting stars

[Code](https://cdoj.site/d/training_2026/record/6a1f557cbbcebd48c85674fb)

设答案的 EGF 是 $F(x)=\sum\limits_{n=1}^{\infty}f_n\dfrac{x^n}{n!}$，去掉联通性限制的 EGF 是 $G(x)=\sum\limits_{n=0}^{\infty}g_n\dfrac{x^n}{n!}$，那么有 $G(x)=\text{exp}(F(x))$。[Exponential formula](https://en.wikipedia.org/wiki/Exponential_formula)

显然 $g_n=2^{\binom{n}{2}}$，构造出 $G(x)$ 再 $\ln$ 回去即可，时间复杂度 $O(n\log n)$。

## F. 多项式乘法

[Code](https://cdoj.site/d/training_2026/record/6a1f50debbcebd48c85674d8)

板题。

## G. 拉格朗日插值

[Code](https://cdoj.site/d/training_2026/record/6a24773ebbcebd48c8580521)

板题。

ps1：建议到 [Link](https://judge.yosupo.jp/problem/polynomial_interpolation) 测板子而不是这里。

ps2：明明插值有很多应用场景，非要出个板子，感觉偷懒了。

## H. 来玩游戏吧

[Code](https://cdoj.site/d/training_2026/record/6a253a27bbcebd48c8581798)

先考虑所有 $a_i$ 出现次数只有偶数的情况，此时如果一个人拿了最大的，另一个人必须跟着拿，因此可以两两配对。从小到大考虑每个数，如果新加进一个数 $x$，导致 $x$ 的出现次数变成奇数，先手肯定将 $x$ 拿走一个，回到刚刚的情况。也就是说多出来的这一个 $x$ 肯定在操作序列的最前面，位置固定。

对操作序列计数，设 $f[i]$ 为当前最大的数为 $i$ 的答案，用隔板法试图将 $i$ 插进序列
$$
f[i]=f[i-1]\cdot \binom{cnt[i]/2+\sum_{j=1}^{i-1}cnt[j] }{cnt[i] / 2}\cdot cnt[i]!
$$
最后乘阶乘表示分配这 $cnt[i]$ 个 $i$ 的次序。时间复杂度 $O(n)$。

## I. 异或序列计数

不会线性代数。

## J. 海猫鸣泣之时

[Code](https://cdoj.site/d/training_2026/record/6a2e4a18bbcebd48c858f391)

前置：反射容斥。可以参考 [Link1](https://www.cnblogs.com/g1ove/p/18448337)，[Link2](https://www.luogu.com.cn/article/3boyop85)。

首先，题目要求每行 $m$ 个元素严格递增，且候选数字只有 $0\sim m$ 这 $m+1$ 个，即每行都有且仅有一个数字不被选中，第 $i$ 行缺失的数设为 $y_i$。则第 $i$ 行第 $j$ 列的元素可以表示为 $x_{i,j}=(j-1)+[j>y_i]$。
$$
\begin{align}
x_{i,j}<x_{i-1,y+1}
&\longrightarrow (j-1)+[j>y_i]< j+[j+1 > y_{i-1}]\\
&\longrightarrow [j>y_i]\le [j\ge y_{i-1}]\\
&\longrightarrow y_{i-1}\le y_i+1
\end{align}
$$
很接近单调增了，我们用经典的构造手法，令 $z_i=y_{i}+i$，此时就有 $z_{i-1}\le z_i$ 了。于是题目转化为计数序列 $\{z\}$ 的数量：

- $0\le y_i\le m\  \longrightarrow \ i\le z_i\le m+i$
- $1\le z_1\le z_2\le \ldots\le z_n\le m+n$

注意到：$\{z\}$ 完全等价于一条从 $(0,0)$ 出发，到达 $(m+n,n)$，且不越过 $y=x$ 和 $y=x-(m+1)$ 的自由路。

- $z_i$ 表示 "当前是第 $i$ 次选择向上走" 这一步所处的横坐标。因为 $z_i$ 最大值是 $m+n$，所以终点也选择在 $(m+n,n)$。
- 在一次向上走之后，来到 $(z_i,i)$，此时 $z_i\ge i$ 意味着 $X_i\ge Y_i$，即折线向上不能越过 $y=x$；在一次向上走之前，位于 $(z_i,i-1)$，此时 $z_i\le m+(i-1)+1$ 意味着 $X_i\le m+Y_i+1$，即折线向下不能穿过 $y=x-(m+1)$。

运用反射容斥求解，时间复杂度 $O(n+m)$。

## K. 海猫鸣泣之时2

[Code](https://cdoj.site/d/training_2026/record/6a2e023dbbcebd48c858eac5)

固定一张图和一个点 $x$，这个点贡献了 $d(x)^k$。这个过程可以看成

- 从 $x$ 的 $d(x)$ 个邻居中选出一个长度为 $k$ 的有序序列，允许重复。

换一个视角，先固定 $x$ 和序列，然后数有多少个图满足要求。考虑一个长为 $k$ 的序列 $(a_1,a_2,\ldots,a_k)$，每个 $a_i$ 都来自除了 $x$ 之外的 $n-1$ 个点。硬性要求是：序列中出现过的每个点，都必须和 $x$ 连边。设序列 $\{a\}$ 中有 $t$ 个不同的元素，那这 $t$ 个点和 $x$ 的边强制存在，剩下 $\dbinom{n}{2}-t$ 条边任选，图的数量是 $2^{\binom{n}{2}-t}$。问题转换成：

- 从 $n-1$ 个点中选一个长度为 $k$ 的有序序列，恰好出现 $t$ 个不同点，有多少种选法？

等价于 "将 $k$ 个位置划分成 $t$ 个非空的无区别集合" 的方案数（同一个组里的视为同一个点），这恰好是第二类斯特林数 $S(k,t)$ 的定义。接下来，还要为这 $t$ 个集合分配编号，方案数是 $(n-1)(n-2)\cdots(n-t)$，即 $A_{n-1}^{t}$。

上面我们考虑的都是一个点，因为每个点贡献相同，乘个 $n$ 就行，最终
$$
\text{Ans}=n\sum_{t=0}^{k}S(k,t)A_{n-1}^{t}2^{\binom{n}{2}-t}
$$
用 ntt 可以一次性求出同一行的第二类斯特林数，时间复杂度 $O(k\log k)$。[Stirling Number](https://oi-wiki.org/math/combinatorics/stirling/#同一行第二类斯特林数的计算)

## L. 有趣的矩阵乘法

[Code](https://cdoj.site/d/training_2026/record/6a2dddccbbcebd48c858e8fe)

定义一个 $n$ 行 $m$ 列的矩阵 $S$，其中 $S_{i,j}$ 表示第 $i$ 个矩阵的第 $j$ 列的所有元素之和。

设 $S$ 右乘 $B$ 得 $S'$，$A_i$ 右乘 $B$ 得 $A_i'$，因为
$$
S_{i,c}'
=\sum_{k=1}^{m}S_{i,k} B_{k,c}=\sum_{k=1}^{m}\left(\sum_{r=1}^{m}(A_i)_{r,k}B_{k,c}\right)
=\sum_{r=1}^{m}\left(\sum_{k=1}^{m}(A_i)_{r,k}B_{k,c}\right)=\sum_{r=1}^{m}(A_i')_{r,c}
$$
意味着右乘前后 $S$ 保留了 $A$ 的完整列信息。且 $S$ 右乘 $B$ 后，只有第 $y$ 列的值会发生改变。

- 当 $x\neq y$ 时，$S'_{i,y}=\sum\limits_{k=1}^{m}S_{i,k}B_{k,y}=S_{i,y}B_{y,y}+S_{i,x}B_{x,y}=S_{i,y}+S_{i,x}\cdot z$
- 当 $x=y$ 时，$S'_{i,y}=\sum\limits_{k=1}^{m}S_{i,k}B_{k,y}=S_{i,y} B_{y,y}=S_{i,y}\cdot z$

对于一个询问 $(x,y,z)$，只用 $O(n)$ 更新 $S$ 的第 $y$ 列。时间复杂度 $O(nm^2+qn)$。

## M. 我喜欢芭~菲↑

[Code](https://cdoj.site/d/training_2026/record/6a2dda42bbcebd48c858e89f)

回顾 burnside 引理：对于一个群 $G$ 和群 $G$ 作用下的状态空间集合 $X$，能得到的本质不同的状态数量等于 $\dfrac{1}{|G|}\sum\limits_{g\in G}\sum\limits_{x\in X}[gx=x]$。

对于有 $i$ 个针尖的指南针，设颜色序列为 $\{a_0,a_1,\ldots,a_{i-1}\}$，"旋转 $r$" 对应 $a_j\to a_{(j+r)\ \bmod \ i}$，"光照 $c$" 对应 $a_j\to (a_j+c)\bmod m$。二者同时可做，因此作用群大小 $|G|=im$，答案 $\text{Ans}_i=\dfrac{1}{im}\sum\limits_{r=0}^{i-1}\sum\limits_{c=0}^{m-1}\text{Fix}(r,c)$，其中 $\text{Fix}(r,c)$ 表示在固定旋转和光照下的不动点（序列）个数。 

对于一个固定的旋转 $r$，记 $d=\gcd(i,r),\ l=\dfrac{i}{d}$，此时该旋转将 $\{a\}$ 分成了 $d$ 个长度为 $l$ 的置换环。若一个序列在 "旋转 $r$ $+$ 光照 $c$" 下不变，等价于沿着一个置换环走一步，颜色都要 $+c$，且走一圈后必须回到原色，即 $l\cdot c\equiv 0\pmod {m}$，这样的 $c$ 有 $\gcd(m,l)$ 个。一旦 $c$ 固定，每个环的起始颜色可以任取 $m$ 种，各环彼此独立，故不动点总数为 $m^d\cdot \gcd(m,l)$。另一方面，满足 $\gcd(i,r)=d$ 的旋转有 $\varphi(l)$ 种，于是
$$
\text{Ans}_i=\frac{1}{im}\sum_{l\mid i}\varphi(l)m^{i/l}\gcd(m,l)
$$
时间复杂度 $O(n\log n)$。

## N. 奥日与风袭废墟

[Code](https://cdoj.site/d/training_2026/record/6a256cbdbbcebd48c8581c92)

$\varphi,\mu,\sigma_0,\sigma_1$ 可以线性筛出来。$f$ 的话枚举因数算贡献即可，时间复杂度是调和级数。

## O. 禁言时长

[Code](https://cdoj.site/d/training_2026/record/6a257816bbcebd48c8581e44)

题意：有 $A$ 个 $a$，$B$ 个 $b$，$C$ 个 $c$，有多少个字符串满足子串 $ab$ 恰好出现 $k$ 次。

令 $f_n$ 表示恰好出现 $n$ 次 $ab$ 的字符串数量，$g_m$ 表示挑出并标记了 $m$ 个 $ab$ 的字符串数量。二项式反演
$$
g_m=\sum_{n\ge m}\binom{n}{m}f_n \qquad \longrightarrow \qquad  f_m=\sum_{n\ge m}(-1)^{n-m}\binom{n}{m}g_n
$$
算 $g_n$，只用把 $ab$ 看作一个整体 $x$。此时有 $A-n$ 个 $a$，$B-n$ 个 $b$，$C$ 个 $c$，$n$ 个 $x$。于是
$$
g_n=\frac{(A+B+C-n)!}{(A-n)!(B-n)!C!n!}
$$
时间复杂度线性。

## P. 来修评测机的

[Code](https://cdoj.site/d/training_2026/record/6a25c0c1bbcebd48c8582ca9)

首先，令 $x=Mt+R\ (t=0,1,\ldots,\left\lfloor\frac{N-R}{M}\right\rfloor)$。按位考虑，对于第 $i$ 位，满足 $x\bmod 2^{i+1}\ge 2^i$ 的 $x$ 会有 $1$ 的贡献。

于是，第 $i$ 位的总贡献是
$$
\sum_{t=0}^{\left\lfloor\frac{N-R}{M}\right\rfloor}[(Mt+R)\bmod 2^{i+1}\ge 2^i]
$$
被[2025武汉区域赛A](https://kisuraop.github.io/posts/1fbf08d.html#a.-planting-trees)折磨过的一定能想到 $[u\ge v]=1+\left\lfloor\dfrac{u-v}{m}\right\rfloor\ (0\le u,v<m)$，再把 $\bmod$ 展开，化简得到
$$
\sum_{t=0}^{\left\lfloor\frac{N-R}{M}\right\rfloor}\left\lfloor\dfrac{Mt+R}{2^{i+1}}+\frac{1}{2}\right\rfloor-\left\lfloor\dfrac{Mt+R}{2^{i+1}}\right\rfloor
$$
由 $\lfloor x \rfloor + \lfloor x + \frac{1}{2} \rfloor = \lfloor 2x \rfloor$（[Hermite's identity](https://handwiki.org/wiki/Hermite's_identity)），最终得到
$$
\sum_{t=0}^{\left\lfloor\frac{N-R}{M}\right\rfloor}\left\lfloor\frac{Mt+R}{2^i}\right\rfloor-2\left\lfloor\frac{Mt+R}{2^{i+1}}\right\rfloor
$$
套用 Floor_Sum 板子即可。时间复杂度 $O(T\log N)$。

## Q. 能量回响

[Code](https://cdoj.site/d/training_2026/record/6a25e225bbcebd48c8582d66)

手推一下 $f$ 前几项的展开式，就全看出来了。

首先 $f$ 每一项可以表示成 $f_i=f_1^{x_i}f_2^{y_i}f_3^{z_i}c^{w_i}$，而 $x_i,y_i,z_i,w_i$ 的递推式都能写出来，再改写成矩阵快速幂的形式就行。时间复杂度 $O(5^3\log n)$。
$$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
\times
\begin{bmatrix}
x_{i-1} \\
x_{i-2} \\
x_{i-3}
\end{bmatrix}
=
\begin{bmatrix}
x_i \\
x_{i-1} \\
x_{i-2}
\end{bmatrix}
\qquad
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 1
\end{bmatrix}
\times
\begin{bmatrix}
w_{i-1} \\
w_{i-2} \\
w_{i-3} \\
2(i-1)-6 \\
2
\end{bmatrix}
=
\begin{bmatrix}
w_i \\
w_{i-1} \\
w_{i-2} \\
2i-6 \\
2
\end{bmatrix}
$$

## R. 愿期望不会落空

[Code](https://cdoj.site/d/training_2026/record/6a2dac7cbbcebd48c858e74f)

设第 $i$ 天随机出的数是 $x_i$，我们想求出使得 $\gcd(x_1,x_2,\ldots,x_t)=1$ 的 $t$ 的期望。

由莫比乌斯反演的推论
$$
[\gcd(x_1,x_2,\ldots,x_n)=1]=\sum_{d\mid x_1,d\mid x_2,\ldots,d\mid x_n} \mu(d)
$$
因此，长度为 $n$ 的序列中 $\gcd$ 为 $1$ 的数量为 $\sum\limits_{d=1}^{m}\mu(d)\left\lfloor\dfrac{m}{d}\right\rfloor^{n}$。总序列数 $m^n$，故
$$
\text{Pr}(\gcd(x_1,x_2,\ldots,x_n)=1)=\frac{1}{m^n}\sum_{d=1}^{m}\mu(d)\left\lfloor\dfrac{m}{d}\right\rfloor^{n}
$$
列出期望的式子
$$
\begin{align}
\mathbb{E}[t]
&=1+\sum_{n=1}^{\infty}\text{Pr}(t > n)\\
&=1+\sum_{n=1}^{\infty}(1-\text{Pr}(\gcd(x_1,x_2,\ldots,x_n)=1))\\
&=1+\sum_{n=1}^{\infty}(1-\frac{1}{m^n}\sum_{d=1}^{m}\mu(d)\left\lfloor\dfrac{m}{d}\right\rfloor^{n})\\
&=1+\sum_{n=1}^{\infty}(-\frac{1}{m^n}\sum_{d=2}^{m}\mu(d)\left\lfloor\dfrac{m}{d}\right\rfloor^{n})\\
&=1-\sum_{d=2}^{m}\mu(d)\sum_{n=1}^{\infty}\left(\frac{\left\lfloor\frac{m}{d}\right\rfloor}{m}\right)^n
\end{align}
$$
其中 $\sum\limits_{n=1}^{\infty}\left(\frac{\left\lfloor\frac{m}{d}\right\rfloor}{m}\right)^n$ 是一个首项和公比均为 $\frac{1}{m}\left\lfloor\frac{m}{d}\right\rfloor$ 的等比数列。注意到公比 $<1$，依据无穷等比数列求和公式，这一项等于 $\dfrac{\left\lfloor\frac{m}{d}\right\rfloor}{m-\left\lfloor\frac{m}{d}\right\rfloor}$。

时间复杂度 $O(m)$。

## S. 贪心大王

[Code](https://cdoj.site/d/training_2026/record/6a2c46dfbbcebd48c858c83b)

通过交换论证，可以发现 $(1,2),(3,4),\ldots,(2n-1,2n)$ 这么配对肯定是最优的。我们用 $i$ 来表示 $(2i-1,2i)$ 这个配对中的 $2i-1$ 和 $2i$，题目就等价于

- 有一个长度为 $2n$ 的序列 $\{p\}$，其中 $1\sim n$ 每个数字恰好出现 $2$ 次。我们要计数满足如下条件的 $\{p\}$ 的数量：
  - $\{p\}$ 可以被拆分成两个完全相同的子序列 $\{A'\},\{B'\}$，且 $\{A'\}=\{B'\}=\pi$（其中 $\pi$ 是 $1\sim n$ 的某个排列）。
- 设 $\pi=\{1,2,\ldots,n\}$ 的答案是 $t$，如上问题的答案就是 $n!\cdot t$，整个题的答案就是 $2^n\cdot n!\cdot t$，因为 $2i-1$ 和 $2i$ 都被看作了 $i$，而实际上是可区分的。

接下来算 $t$，问题相当于计数有多少个合法的括号序列（所有左括号依次填 $1,2,\ldots,n$，右括号依次填 $1,2,\ldots,n$，自然构成合法 $\{p\}$），因此 $t=C_n$。[Catalan Number](https://oi-wiki.org/math/combinatorics/catalan/)

时间复杂度 $O(n)$。

## T. 简单计算

[Code](https://cdoj.site/d/training_2026/record/6a2c4ffbbbcebd48c858c89a)

令 $d=\gcd(a,b)$，设 $a=dx,\ b=dy,\ \gcd(x,y)=1$。
$$
a+b+c=n\ \longrightarrow\ dx+dy+c=n\  \xrightarrow{k=x+y}\ c=n-dk
$$
当 $d,k$ 固定，有 $\begin{cases}\varphi(k)&,k>1\\0&,k=1\end{cases}$ 种合法的 $(x,y)$ 组合，不妨令 $\varphi(1)=0$，此时
$$
\begin{align}
\sum_{a+b+c=n}\text{lcm}(\gcd(a,b),c)
&=\sum_{dk\le n-1}\varphi(k)\cdot \text{lcm}(d,n-dk)\\
&=\sum_{d=1}^{n-1}\sum_{k=1}^{\left\lfloor\frac{n-1}{d}\right\rfloor}\varphi(k)\cdot \frac{d(n-dk)}{\gcd(d,n)}
\end{align}
$$
时间复杂度 $O(n\log n)$。

## U. 魔法数对

[Code](https://cdoj.site/d/training_2026/record/6a2c5b3bbbcebd48c858cf64)

令 $\left\lfloor\frac{a}{b}\right\rfloor=a\bmod b=t$，则 $a$ 可以表示成 $a=tb+t$。问题转化成有多少个 $t\in [1,b-1]$ 满足 $t(b+1)\le x$。枚举 $b$，答案是 $\sum\limits_{b=1}^{y}\min(b-1,\left\lfloor\frac{x}{b+1}\right\rfloor)$。改写成分段函数 $\begin{cases}b-1 &,b\le s \\ \left\lfloor\frac{x}{b+1}\right\rfloor &,b > s\end{cases}$，分界点 $s=\left\lfloor\sqrt{x+1}\right\rfloor$。发现 $b\le s$ 是简单的，$b > s$ 进行一个数论分块即可。时间复杂度 $O(T\sqrt{x})$。

## V. 简单的图论题

[Code](https://cdoj.site/d/training_2026/record/6a2c5ebcbbcebd48c858cf96)

全集是 $(n-1)!$，我们只用算期望。首先是从 $k$ 连向 $1\sim k-1$ 的边，期望是 $\begin{cases}1 &,k>1 \\ 0 &,k=1\end{cases}$。然后是从 $k+1\sim n$ 连向 $k$ 的边，期望是 $\sum\limits_{i=k+1}^{n}\dfrac{1}{i-1}$。预处理 $10^7$ 以内的 $\dfrac{1}{i}$ 做前缀和，时间复杂度 $O(n)-O(1)$。

## W. Faker vs Bin

[Code](https://cdoj.site/d/training_2026/record/6a2c6b60bbcebd48c858cffa)

用 SG 函数打一下表就行。时间复杂度 $O(1)$。

## X. 吊灯校准

[Code](https://cdoj.site/d/training_2026/record/6a2ca2debbcebd48c858d119)

非常无聊的题。裴蜀定理判一下无解，然后用 exgcd 解一下 $\dfrac{a_1}{d}t\equiv \dfrac{b_2-b_1}{d}\pmod {\dfrac{a_2}{d}}, \ d=\gcd (a_1,a_2)$，得到一个最小公共解 $x_0=b_1+a_1t$，然后把解调整到大于等于 $\max(L,b_1,b_2)$ 的位置。在 $[L,R]$ 之间，公共解的步长是 $\text{lcm}(a_1,a_2)$，除一下就行。时间复杂度 $O(\log\min(a_1,a_2))$。

## Y. 集合幂但没有级数

[Code](https://cdoj.site/d/training_2026/record/6a2cb9c5bbcebd48c858d1b6)

令模数为 $p$，题目需要求 $m^c\bmod p$，其中 $c=\sum\limits_{d\mid n}\binom{n}{d}$。先把 $p\mid m$ 判掉，然后由费马小定理，$m^c\equiv m^{c \ \bmod \ (p-1)}\pmod {p}$，题目转化为求 $\sum\limits_{d\mid n}\binom{n}{d}\bmod (p-1)$。其中 $p-1$ 是合数，分解出来 $\sum p_i^{k_i}$ 才 $3592$，直接暴力枚举因数 $d$，跑 [ExLucas](https://www.luogu.com.cn/problem/P4720) 即可。时间复杂度 $O(3592\cdot \log n\cdot d(n))$，其中 $d(n)$ 是因数个数函数。

## Z. RNG Manipulation

[Code](https://cdoj.site/d/training_2026/record/6a2dbcc5bbcebd48c858e7e4)

先把 $X_0=y$，$a=0$ 和 $a=1$ 特判掉。当 $a\ge 2$ 时，手推 $X_i$ 前几项，可以发现
$$
X_i\equiv a^iX_0+c\cdot (a^{i-1}+a^{i-2}+\cdots+a+1)\equiv a^iX_0+c\cdot\frac{a^i-1}{a-1}\pmod {m}
$$
我们要求出最小的 $i$ 满足 $X_i=y$，我们将 $X_i=y$ 代入，两边乘 $a-1$ 消去分母
$$
a^iX_0(a-1)+c(a^i-1)\equiv y(a-1)\pmod {m}
$$
整理一下
$$
a^i\underbrace{(X_0(a-1)+c)}_{\large A}\equiv \underbrace{y(a-1)+c}_{\large B}\pmod{m}
$$
判一下 $A\equiv 0\pmod{m}$ 的情况，就变成 $a^i\equiv B\cdot A^{-1}\pmod {m}$，标准的离散对数。使用 BSGS 求解，时间复杂度 $O(T\sqrt{m})$。

