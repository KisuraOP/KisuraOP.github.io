---
title: "【题解】Codeforces Round 910 (Div.2) B,D,E,F"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/6f20bab430aa7b8084e6a0ece70966a2.jpeg"
tags:
  - XCPC
  - Codeforces
categories:
  - Competitive Programming
  - Codeforces
excerpt: 思维场，都是很巧妙的题呢！
abbrlink: 79faf3ae
date: 2023-11-20 21:00:00
updated: 2023-11-20 21:00:00
---


## B. Milena and Admirer

[Problem](https://codeforces.com/contest/1898/problem/B)

{% note info %}

题意：给定长为 $n$ 的序列 $a$，每次可以选定一个 $a_i$ 和正整数 $x\in[1,x)$，并将 $a_i$ 替换成 $x$ 和 $a_i -x$。问使序列单调不降的最小操作次数。

$1\le n \le 2\times 10^5$，$1\le a_i\le 10^9$。

{% endnote %}

{% note success %}

倒序考虑。

对于每一个 $a_i,a_{i+1}$：
* 若 $a_i\le a_{i+1}$，不进行任何操作。

* 若 $a_i > a_{i+1}$，记操作次数为 $cnt$。可以证明，最优策略肯定是使分裂序列最左端的数（即最小数）最大：例如 $[21,6]$ 中的 $21$ 拆分成 $[{\color{Red}5},5,5,6]$ 肯定要比 $[{\color{Red}3},6,6,6]$ 更优，这样继续倒序操作会有更大的操作空间。具体地：
  * 若 $a_{i+1} \mid a_i$，则将 $a_i$ 拆分成 $\dfrac{a_i}{a_{i+1}}$ 个 $a_{i+1}$，$cnt=\dfrac{a_i}{a_{i+1}}-1$。

  * 否则，会多出一个余数，则 $cnt=\left\lfloor\dfrac{a_{i}}{a_{i+1}}\right\rfloor$。此时最左端的数最大为 $\left\lfloor\dfrac{a_i}{cnt}\right\rfloor$。

  * 每次的 $a_{i+1}$ 其实就是上一次操作后最左端的数。


可以用 `std::queue` 模拟这一加数过程。

时间复杂度 $O(n)$。

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
#define ck(x) printf("check %lld\n",x);fflush(stdout);
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
	vector<int> a(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
	}
	deque<int> q;
	for(int i=n-1;i>=1;--i) {
		q.push_back(a[i]);
	}
	vector<int> b;
	b.push_back(a[n]);
	int res=0;
	while(!q.empty()) {
		int x=q.front();
		if(x<=b.back()) {
			b.push_back(x);
			q.pop_front();
		} else {
			int y=b.back();
			int cnt=x/y;
			res+=cnt-1;
			if(x%y) {
				res++;
				int z=x/(cnt+1);
				b.push_back(z);
			}
			q.pop_front();
		}
	}
	printf("%lld\n",res);
}


signed main()
{
//	fre(test);
	int T=read();
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## D. Absolute Beauty

[Problem](https://codeforces.com/contest/1898/problem/D)

{% note info %}

题意：给定长为 $n$ 的序列 $a,b$。你可以交换 $b$ 中的任意两个数一次或不进行任何操作，求 $\max(\sum\limits_{i=1}^n|a_i-b_i|)$。

$2\le n \le 2\cdot 10^5$，$1\le a_i,b_i \le 10^9$。

{% endnote %}

{% note success %}

将每一组 $(a_i,b_i)$ 看作线段（若 $a_i>b_i$ 则交换），一共 $n$ 条线段。

此时 $|a_i-b_i|$ 即线段的长度，我们要求 $n$ 条线段长度和的最大值。

考虑交换一组 $b_i,b_j$ 对答案的影响：即交换两条线段的某两个端点。

可能的情况如下（不完全）：

![](https://kisuraop.github.io/image/academic/CF910_1.png)

![](https://kisuraop.github.io/image/academic/CF910_2.png)

![](https://kisuraop.github.io/image/academic/CF910_3.png)

会发现只有第一组线段的长度得以扩张，且扩张值为原先线段间空白长度的两倍。

那么我们找到所有 $(a_i,b_i)$ 中最小的右端点 $s$ 和最大的左端点 $t$。

有 $\text{ans}=\max(0,2(t-s))+\sum\limits_{i=1}^n |a_i-b_i|$。

时间复杂度 $O(n)$。

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
#define ck(x) printf("check %lld\n",x);fflush(stdout);
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
	vector<int> a(n+1),b(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
	}
	for(int i=1;i<=n;++i) {
		b[i]=read();
	}
	int minn=inf,maxn=0;
	int res=0;
	for(int i=1;i<=n;++i) {
		res+=abs(a[i]-b[i]);
		minn=min(minn,max(a[i],b[i]));
		maxn=max(maxn,min(a[i],b[i]));
	}
	printf("%lld\n",res+max(0ll,2*(maxn-minn)));
}


signed main()
{
	//fre(test);
	int T=read();
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## E. Sofia and Strings

[Problem](https://codeforces.com/contest/1898/problem/E)

{% note info %}

题意：给定两个由小写字母构成的字符串 $S,T$，长度分别为 $n,m$。你可以进行以下两种操作任意次，问是否能将 $S$ 转化成 $T$。

1. 删除 $S$ 中的一个元素。

2. 使 $S$ 中的某个子段按字典序排序。

$1\le m\le n\le 2 \cdot 10^5$。

{% endnote %}

{% note success %}

首先，因为不计操作次数，所以操作 $2$ 其实可以转化为每次排序两个相邻字母。

例如，$\text{cba}\to$ $\text{abc}$ 其实相当于 $\text{cba} \to \text{cab} \to \text{acb} \to \text{abc}$。

其次，逐个匹配 $T$ 中字符，观察匹配过程：假若当前匹配字母 $\text{d}$，那么在 $S$ 中找到第一个仍未被匹配的 $\text{d}$，由于当且仅当字典序小的字母紧跟在字典序大的字母后面时才会发生交换，那么在确定 $\text{d}$ 的位置的同时，位于 $\text{d}$ 之前且字典序比 $\text{d}$ 小的字母（$\text{a,b,c}$）就失去了贡献，无法参与后续匹配。因为后续匹配继续向 $\text{d}$ 的右侧寻找，而 $\text{a,b,c}$ 无论如何也跨越不了这个 $\text{d}$。

用 `std::vector` 记录每个字母出现的下标，逐个扫描 $T$，并将符合上述要求不再有贡献的下标从容器中移除。若能一直匹配到 $T$ 末尾，则必然存在一个解。否则无解。

时间复杂度 $O(n+m\cdot 26)$。

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
#define ck(x) printf("check %lld\n",x);fflush(stdout);
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
	int n=read(),m=read();
	string s,t;
	cin>>s>>t;
	vector<vector<int>> pos(26);
	for(int i=n-1;i>=0;--i) {
		pos[s[i]-'a'].push_back(i);
	}
	for(int i=0;i<m;++i) {
		int x=t[i]-'a';
		if(pos[x].empty()) {
			puts("NO");
			return ;
		}
		int fir=pos[x].back();
		pos[x].pop_back();
		for(int j=0;j<x;++j) {
			while(!pos[j].empty() && pos[j].back()<fir) {
				pos[j].pop_back();
			}
		}
	}
	puts("YES");
}


signed main()
{
//	fre(test);
	int T=read();
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## F. Vova Escapes the Matrix

[Problem](https://codeforces.com/contest/1898/problem/F)

{% note info %}

题意：给定一个 $n\times m$ 的矩形迷宫和初始坐标，迷宫的出口定义为位于迷宫边缘且没有障碍且能从初始位置走到的格子。一个迷宫有三种状态：没有出口，有一个出口，有两个及以上出口。问在不破坏迷宫状态的前提下，能再往这个迷宫中添加多少障碍物。

$3\le n,m\le 1000$。

{% endnote %}

{% note success %}

先从起点跑一遍 $\text{bfs}$，预处理出 $dis_{i,j}$ 代表起点到点 $(i,j)$ 的最短距离。

设迷宫出口数量为 $k$，初始有 $p$ 个可放障碍的点，出口点集为 $T$：
* $k=0$，把迷宫塞满，$\text{ans}=p$。

* $k=1$，无脑塞，只留一条通向出口的最短路，$\text{ans}=p-\min(dis_T)$。

* $k\ge2$，显然最后只保留两个出口。以 $i\in T$ 为起点再跑 $\text{bfs}$，记录出 $diss_{i,j,0/1}$ 表示点 $(i,j)$ 到最近出口的距离和到次近出口的距离，则 $\text{ans}=p-\min(dis_{i,j}+diss_{i,j,0}+diss_{i,j,1})$。

时间复杂度 $O(mn)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define int long long
#define inf 0x3fffffffffffffff
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
const int modp = 998244353;

void solve()
{
	int n=read(),m=read();
	vector<string> s(n);
	int sx,sy;
	int blank=0;
	for(int i=0;i<n;++i) {
		cin>>s[i];
		for(int j=0;j<m;++j) {
			if(s[i][j]=='V') {
				sx=i;sy=j;
			} else if(s[i][j]=='.') {
				blank++;
			}
		}
	}
	int dx[]={-1,0,1,0};
	int dy[]={0,1,0,-1};
	auto overline = [&](int x,int y) {
		return x<0 || x>=n || y<0 || y>=m;
	};
	auto isexit = [&](int x,int y) {
		return (x==0 || x==n-1 || y==0 || y==m-1) && s[x][y]!='#';
	};
	queue<pair<int,int>> q;
	vector<vector<int>> dis(n,vector<int>(m,-1));
	q.push({sx,sy});
	dis[sx][sy]=0;

	int exit=0;
	while(!q.empty()) {
		auto [x,y]=q.front();
		q.pop();
		exit+=isexit(x,y);
		for(int i=0;i<4;++i) {
			int xx=x+dx[i],yy=y+dy[i];
			if(!overline(xx,yy) && dis[xx][yy]==-1 && s[xx][yy]!='#') {
				dis[xx][yy]=dis[x][y]+1;
				q.push({xx,yy});
			}
		}
	}

	if(!exit) {
		int ans=blank;
		printf("%lld\n",ans);
	} else if(exit==1) {
		int ans=inf;
		for(int i=0;i<n;++i) {
			for(int j=0;j<m;++j) {
				if(isexit(i,j) && dis[i][j]!=-1) {
					ans=min(ans,dis[i][j]);
				}
			}
		}
		ans=blank-ans;
		printf("%lld\n",ans);
	} else {
		queue<array<int,4>> q;
		for(int i=0;i<n;++i) {
			for(int j=0;j<m;++j) {
				if(isexit(i,j)) {
					q.push({i,j,0,i*m+j});
				}
			}
		}
		vector diss(n,vector(m,array{-1,-1}));
		vector id(n,vector<int>(m,-1));
		while(!q.empty()) {
			auto [x,y,d,pid]=q.front();
			q.pop();
			if(diss[x][y][0]==-1) {
				diss[x][y][0]=d;
				id[x][y]=pid;
			} else if(diss[x][y][1]==-1 && pid!=id[x][y]) {
				diss[x][y][1]=d;
			} else {
				continue;
			}

			for(int i=0;i<4;++i) {
				int xx=x+dx[i],yy=y+dy[i];
				if(!overline(xx,yy) && s[xx][yy]!='#' && diss[xx][yy][1]==-1) {
					q.push({xx,yy,d+1,pid});
				}
			}
		}

		int ans=inf;
		for(int i=0;i<n;++i) {
			for(int j=0;j<m;++j) {
				if(s[i][j]!='#' && dis[i][j]!=-1 && diss[i][j][1]!=-1) {
					ans=min(ans,dis[i][j]+diss[i][j][0]+diss[i][j][1]);
				}
			}
		}
		ans=blank-ans;
		printf("%lld\n",ans);
	}
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
