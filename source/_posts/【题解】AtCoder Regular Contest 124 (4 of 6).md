---
title: "【题解】AtCoder Regular Contest 124 (4 of 6)"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/b1bb1794503f1e0ea31e048276654c2a.jpeg"
tags:
  - XCPC
  - Atcoder
categories:
  - Competitive Programming
  - Atcoder
excerpt: 很不错的题。
abbrlink: 79e649ee
date: 2021-08-24 21:00:00
updated: 2021-08-24 21:00:00
---


## A. LR Constraints

[Problem](https://atcoder.jp/contests/arc124/tasks/arc124_a)

{% note info %}

题意：从左到右 $n$ 个空卡片，需要在每个卡片上写一个 $x\in[1,k]$，且满足 $k$ 个限制条件。第 $i$ 个条件限定第 $k_i$ 个卡片必须是最左/最右边的写有 $i$ 的卡片。问填写方案数。

$1\le n,k \le 1000$。

{% endnote %}

{% note success %}

直接模拟。开一个桶 $a$ 统计每个卡片能填的数字数量，初始化全为 $a_i=k$。

对于一个限制条件，若限制第 $k_i$ 个卡片是最左边的写有 $i$ 的卡片，则 $a_{j\in[1,k_i-1]}\leftarrow a_{j\in[1,k_i-1]}-1$。

若限制第 $k_i$ 个卡片是最右边的写有 $i$ 的卡片，则 $a_{j\in[k_i+1,n]}\leftarrow a_{j\in[k_i+1,n]}-1$。

最后 $ans = \prod a_i$。

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
	int n=read(),k=read();
	vector<int> a(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=k;
	}
	for(int i=1;i<=k;++i) {
		char opt[3];
		scanf("%s",&opt);
		int x=read();
		if(opt[0]=='L') {
			for(int j=1;j<x;++j) {
				if(a[j]!=1) {
					a[j]--;
				}
			}
			a[x]=1;
		} else {
			for(int j=x+1;j<=n;++j) {
				if(a[j]!=1) {
					a[j]--;
				}
			}
			a[x]=1;
		}
	}
	int ans=1;
	for(int i=1;i<=n;++i) {
		ans*=a[i];
		ans%=modp;
	}
	printf("%lld\n",ans);
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

## B. XOR Matching 2

[Problem](https://atcoder.jp/contests/arc124/tasks/arc124_b)

{% note info %}

题意：给定两个长为 $n$ 的序列 $a,b$。找到所有的 $x$ 使得能使 $b$ 按一定顺序重排后对于所有 $1\le i\le n$ 都有 $a_i\oplus b_i = x$。

$1\le n\le 2000$，$0\le a_i,b_i\le 2^{30}$。

{% endnote %}

{% note success %}

略加思考，如果要对所有 $i$ 都满足 $a_i \oplus b_i=x$，那么 $x$ 的可能值最多就 $n$ 个，且一定是 $a_1\oplus b_1,a_1\oplus b_2,\dots ,a_1\oplus b_n$ 中的若干。逐个去试即可。

最方便的方法是对 $b$ 排序，用 $a$ 的每一项去异或可能的 $x$ 得到 $c$，再将 $c$ 排序后和 $b$ 比较。

一个坑点是答案需要去重。

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
	vector<int> a(n+1),b(n+1),c(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
	}
	for(int i=1;i<=n;++i) {
		b[i]=read();
	}
	sort(b.begin()+1,b.end());
	vector<int> ans;
	for(int i=1;i<=n;++i) {
		int x=a[1]^b[i];
		for(int j=1;j<=n;++j) {
			c[j]=a[j]^x;
		}
		sort(c.begin()+1,c.end());
		if(c==b) {
			ans.push_back(x);
		}
	}
	ans.erase(unique(ans.begin(),ans.end()),ans.end());
	printf("%lld\n",ans.size());
	sort(ans.begin(),ans.end());
	for(auto i:ans) {
		printf("%lld\n",i);
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

{% note warning %}

`std::vector` 去重方法：


```cpp
sort(res.begin(),res.end());
res.erase(unique(res.begin(),res.end()),res.end());
```

{% endnote %}

## C. LCM of GCDs

[Problem](https://atcoder.jp/contests/arc124/tasks/arc124_c)

{% note info %}

题意：给定 $n\le 50$ 对数。对于每一对数，选一个放入集合 $A$，另一个则放入集合 $B$，最后对两个集合里所有数求 $\gcd$ 得到 $a$ 和 $b$，求最大的 $\text{lcm}(a,b)$。

{% endnote %}

{% note success %}

经典 trick。

如果直接暴力搜索，复杂度将会是 $O(2^n)$。

但这里最后是拿两个集合的 $\gcd$ 做 $\text{lcm}$，而实际上这 $50$ 对数的 $\gcd$ 个数并没有那么多。

所以还是暴搜，用一个 `std::set` 记录选到当前位置的集合里是否有与当前相同的 $\gcd$，有就跳过，否则把当前两个集合里的 $\gcd$ 用一个 `std::pair` 记录到 `std::set` 里。

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

set<pair<int,int>> q[55];
void solve()
{
	int n=read();
	vector<int> a(n+1),b(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
		b[i]=read();
	}
	int res=0;
	auto dfs = [&](auto self,int p,int x,int y) {
		if(p==n+1) {
			res=max(res,x/__gcd(x,y)*y);
			return ;
		}
		if(q[p].count({x,y})) {
			return ;
		}
		q[p].insert({x,y});
		self(self,p+1,__gcd(x,a[p]),__gcd(y,b[p]));
		self(self,p+1,__gcd(x,b[p]),__gcd(y,a[p]));
	};
	dfs(dfs,1,0,0);
	printf("%lld\n",res);
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

## D. Yet Another Sorting Problem

[Problem](https://atcoder.jp/contests/arc124/tasks/arc124_d)

{% note info %}

题意：给定一个长 $n+m$ 的排列，每次可以从前边 $n$ 个数和后边 $m$ 个数里挑一个出来交换，问至少交换多少次能使整个序列呈升序。

$1\le n,m\le 10^5$。

{% endnote %}

{% note success %}

挺新颖的思路。先考虑如果没有左边 $n$ 个和右边 $m$ 个的限制，从整个序列里挑两个数交换的最少方案数。

我们将每个数和它对应的下标连边，那么最终升序的状态是每个点和自己连边，即一共 $n+m$ 个连通块。我们再考虑交换两个数会发生什么。

1. 如果 $i,a_i$ 和 $j,a_j$ 位于两个连通块，那么交换会让它们合并成一个连通块。

2. 如果 $i,a_i$ 和 $j,a_j$ 位于同一连通块，交换之后仍为一个连通块。

3. 如果 $i,j,a_i,a_j$ 中有两个数相等，那这四个数一定位于一个连通块，交换之后会把相等的那个数移出该连通块，连通块数 $+1$。比如 $i=a_j$，则连边情况为 $a_i -a_j/i-j$，交换后 $a_i$ 和 $i$ 连边，$a_j$ 和 $j$ 连边，变成两个连通块。

4. 如果 $i=a_j,j=a_i$，交换后分离，变成两个连通块，连通块数目 $+1$。

因为最终目标是 $n+m$ 个连通块，所以只需要用后两个操作不断增加连通块即可。

再考虑有限制怎么做 ：因为我们只能对前 $n$ 个数和后 $m$ 个数成对操作，所以将前 $n$ 个点染成红色，后 $m$ 个点染成蓝色，每次只能对红色点和蓝色点执行交换操作。

那么对于只有红色或蓝色的纯色且大小大于 $1$ 的连通块，只能执行操作 $1$ 合并在一起变成杂色连通块，再用后两个操作分开。

假设大小 $>1$ 的纯红色连通块有 $a$ 个，纯蓝色连通块有 $b$ 个，总连通块个数为 $cnt$，那么 ：
$$
\text{ans}=n+m-cnt+2\times \max(a,b)
$$

假设 $a<b$，因为把红色连通块与蓝色连通块合并的需要 $a$ 步，把剩下的蓝色连通块合并到杂色连通块要 $b-a$ 步，一共少了 $a+(b-a)=b$ 个连通块，所以还需要 $b$ 次分离操作，那么现在一共 $2\times b$ 次操作。$a>b$ 同理。

前面的 $n+m-cnt$ 即本来需要分离的连通块数量。

整个过程都可以用并查集维护。

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

struct DSU {
	vector<int> f,siza,sizb;
	DSU() {}
	DSU(int n) {init(n);}
	void init(int n){
		f.resize(n+2);
		siza.resize(n+2);
		sizb.resize(n+2);
		for(int i=0;i<=n+1;++i)
			f[i]=i,siza[i]=sizb[i]=0;
	}
	int find(int x){
		if(x==f[x]) return x;
		return f[x]=find(f[x]);
	}
	bool same(int x,int y){
		return find(x)==find(y);
	}
	bool merge(int x,int y){
		x=find(x);
		y=find(y);
		if(x==y) return false;
		siza[x]+=siza[y];
		sizb[x]+=sizb[y];
		f[y]=x;
		return true;
	}
	int sizea(int x){
		return siza[find(x)];
	}
	int sizeb(int x){
		return sizb[find(x)];
	}
};


void solve()
{
	int n=read(),m=read();
	DSU dsu(n+m);
	for(int i=1;i<=n+m;++i) {
		i<=n ? dsu.siza[i]++ : dsu.sizb[i]++;
	}
	for(int i=1;i<=n+m;++i) {
		int x=read();
		dsu.merge(x,i);
	}
	vector<bool> vis(n+m+1);
	int cnt=0,cnta=0,cntb=0;
	for(int i=1;i<=n+m;++i) {
		int x = dsu.find(i);
		if(!vis[x]) {
			vis[x]=true;
			cnt++;
			cnta+=(dsu.sizea(x)>=2 && !dsu.sizeb(x));
			cntb+=(dsu.sizeb(x)>=2 && !dsu.sizea(x));
		}
	} 
	printf("%lld\n",n+m-cnt+2*max(cnta,cntb));
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
