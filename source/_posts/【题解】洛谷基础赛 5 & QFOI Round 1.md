---
title: "【题解】洛谷基础赛 5 & QFOI Round 1"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/b4f68d06095cbce00bee18def548c97b.jpeg"
tags:
  - OI
  - Luogu
categories:
  - Competitive Programming
  - Luogu
excerpt: 比上一场基础赛要简单。
abbrlink: 31577138
date: 2023-10-05 21:00:00
updated: 2023-10-05 21:00:00
---


## A. 「QFOI R1」贴贴

[Problem](https://www.luogu.com.cn/problem/P9712)

{% note success %}

可以使用 `std::isupper()` 和 `std::tolower()` 。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define int long long
#define double long double
#define PI acos(-1)
#define inf 0x3fffffffffffffff
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
inline void write(int x)
{
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
const int modp = 998244353;


void solve()
{
	string s;
	cin>>s;
	for(int i=0;i<s.size();++i) {
		if(s[i]=='_') {
			s[i]='-';
		} else if(isupper(s[i])) {
			s[i]=tolower(s[i]);
		}
	}
	s="solution-"+s;
	cout<<s<<endl;
}


signed main()
{
	fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## B. 「QFOI R1」抱抱

[Problem](https://www.luogu.com.cn/problem/P9713)

{% note success %}

可以想象，无论怎么切，最后剩下的一定是完整的一个长方体。

分别记录当前切出去的最大 $x_m,y_m,z_m$，答案即 $(a-x_m)(b-y_m)(c-z_m)$。

时间复杂度 $O(m)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define int long long
#define double long double
#define PI acos(-1)
#define inf 0x3fffffffffffffff
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
inline void write(int x)
{
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
const int modp = 998244353;


void solve()
{
	int a=read(),b=read(),c=read(),m=read();
	int xmax=0,ymax=0,zmax=0;
	for(int i=1;i<=m;++i) {
		int opt=read(),k=read();
		if(opt==1) {
			xmax=max(xmax,k);
		} else if(opt==2) {
			ymax=max(ymax,k);
		} else {
			zmax=max(zmax,k);
		}
		int res=(a-xmax)*(b-ymax)*(c-zmax);
		printf("%lld\n",res);
	}
}


signed main()
{
	fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## C. 「QFOI R1」摸摸

[Problem](https://www.luogu.com.cn/problem/P9714)

{% note info %}

题意：给出长度为 $n$ 的数列 $b,t$，每次操作可以将 $t$ 与其翻转数列相加得到新 $t$，或将 $t$ 累加到一开始为空的数列 $a$ 上，问若干次操作后是否能将 $a\rightarrow b$。

$1\le n,b_i,t_i \le 2\times 10^3$。

{% endnote %}

{% note success %}

对于一个初始数列我们考虑它经过若干次翻转相加操作后变成什么样。

初始 $[a_1,a_2,\dots,a_{n-1},a_n]$。

第一次 $[a_1+a_n,a_2+a_{n-1},\dots,a_{n-1}+a_2,a_n+a_1]$。（设为数列 $s$）

第二次 $[2(a_1+a_n),2(a_2+a_{n-1}),\dots,2(a_{n-1}+a_2),2(a_n+a_1)]$。

第三次 $[4(a_1+a_n),4(a_2+a_{n-1}),\dots,4(a_{n-1}+a_2),4(a_n+a_1)]$。

第 $m$ 次 $[2^{m-1}(a_1+a_n),2^{m-1}(a_2+a_{n-1}),\dots,2^{m-1}(a_{n-1}+a_2),2^{m-1}(a_n+a_1)]$。

由此发现，后续无论将多少个经历几次迭代的 $t$ 加到 $a$ 上，一定等价于将若干个 $s$ 乘以一定倍数再累加到 $a$ 上。

令 $t_0$ 为初始 $t$ 数列。于是我们可以枚举 $k_1,k_2$，判断 $k_1\cdot t_{0i}+k_2\cdot s_i$ 是否与 $b_i$ 相等。

时间复杂度为 $O(nw)$，$w$ 为值域。

{% endnote %}

{% note warning %}

涉及整个数列/区间操作的问题可以试着手推操作过程，尝试发现性质。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define int long long
#define double long double
#define PI acos(-1)
#define inf 0x3fffffffffffffff
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
inline void write(int x)
{
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
const int modp = 998244353;


void solve()
{
	int n=read();
	vector<int> t1(n+1),t2(n+1),b(n+1);
	int max1=inf,max2=inf;
	for(int i=1;i<=n;++i) {
		t1[i]=read();
	}
	for(int i=1;i<=n;++i) {
		t2[i]=t1[n-i+1]+t1[i];
	}
	for(int i=1;i<=n;++i) {
		b[i]=read();
		max1=min(max1,b[i]/t1[i]);
		max2=min(max2,b[i]/t2[i]);
	}
	for(int i=0;i<=max1;++i) {
		for(int j=0;j<=max2;++j) {
			bool ok=true;
			for(int k=1;k<=n;++k) {
				if(t1[k]*i+t2[k]*j!=b[k]) {
					ok=false;
					break;
				}
			}
			if(ok) {
				puts("Yes");
				return ;
			}
		}
	}
	puts("No");
}


signed main()
{
	fre(test);
	int T=read();
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## D. 「QFOI R1」头

[Problem](https://www.luogu.com.cn/problem/P9715)

{% note info %}

题意：初始一个没有颜色的 $n\times m$ 网格，现有 $k$ 种颜色编号 $1\sim k$，以及 $q$ 次操作。

每次操作给定 $op,l,r,c,t$ 五个参数：
* $op=1/2$ 代表将第 $l\sim r$ 行 $/$ 列 的所有格子涂成颜色 $c$。

* $t=0/1$ 代表若遇到已被染色的格子，不再染色 $/$ 覆盖染色。

最后输出 $k$ 个整数，每个整数 $x$ 代表被染成颜色 $x$ 的格子数量。

$1\le n,m,q,\le 2\times 10^6$，$1\le k \le 5\times 10^5$。

{% endnote %}

{% note success %}

考虑将操作离线。

对于 $t=0$ 的操作，越排在前面优先级越大。

对于 $t=1$ 的操作，越排在后面优先级越大。

并且先执行完所有 $t=1$ 的操作对 $t=0$ 的操作没有任何影响，因为要被覆盖的早晚被覆盖。

因此可以安排一个操作顺序（先从后往前执行 $t=1$ 操作，再从前往后执行 $t=0$ 操作），使得后面的操作不影响前面的操作。

接着，我们可以维护每一行是否全被染色（记为 $R_i$）和每一列是否全被染色（记为 $C_i$）。

以染色第 $[l,r]$ 行为例，贡献是 $[(r-l+1)-\sum\limits_{i=l}^{r}R_i](m-\sum\limits_{i=1}^{m}C_i)$。列染色同理。

每次计算完贡献后，对于 $i\in[l,r]$，$R_i\leftarrow 1$。

如此一来，转化为区间赋值和区间求和问题。

但线段树的对数时间还是不足以通过，我们可以用链表模拟这个过程。

用两个单向链表维护行列，修改时变更 $nxt$，询问时暴跳 $nxt$，均摊时间复杂度是线性的。

透过代码可能更好理解。

总时间复杂度 $O(n+m+q)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define int long long
#define double long double
#define PI acos(-1)
#define inf 0x3fffffffffffffff
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
inline void write(int x)
{
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
const int modp = 998244353;
const int N = 2e6+10;

struct Chain {
	int covered;
	vector<int> a,nxt; 
	Chain() {}
	Chain(int n) {
		a.resize(n+1);
		nxt.resize(n+1);
		iota(nxt.begin(),nxt.end(),1);
		covered=0;
	}

	void update(int l,int r) {
		for(int i=l,lst=0;i<=r;i=nxt[i]) {
			if(!a[i]) {
				covered++;
				a[i]=1;
			}
			if(lst) {
				nxt[lst]=nxt[r];
			}
			lst=i;
		}
	}

	int query(int l,int r) { //[l,r]内有多少已被占用
		int res=0;
		for(int i=l;i<=r;i=nxt[i]) {
			res+=(a[i]==0);
		}
		return (r-l+1)-res;
	}
};

void solve()
{
	int n=read(),m=read(),k=read(),q=read();
	vector<array<int,5>> qry(q+1);
	for(int i=1;i<=q;++i) {
		qry[i]={read(),read(),read(),read(),read()};
	}
	Chain tr(n),tc(m);
	vector<int> ans(k+1);

	auto work = [&](int id) {
		auto [opt,l,r,c,t]=qry[id];
		if(opt==1) {
			ans[c]+=(r-l+1-tr.query(l,r))*(m-tc.covered);
			tr.update(l,r);
		} else {
			ans[c]+=(r-l+1-tc.query(l,r))*(n-tr.covered);
			tc.update(l,r);
		}
	};

	for(int i=q;i>=1;--i) {
		if(qry[i][4]) {
			work(i);
		}
	}
	for(int i=1;i<=q;++i) {
		if(!qry[i][4]) {
			work(i);
		}
	}
	for(int i=1;i<=k;++i) {
		printf("%lld ",ans[i]);
	}
}


signed main()
{
	fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
C++
```

{% endspoiler %}
