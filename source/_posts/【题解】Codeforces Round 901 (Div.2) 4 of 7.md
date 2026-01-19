---
title: "【题解】Codeforces Round 901 (Div.2) 4 of 7"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/f96b83a13c4e480cc4ef2d64b9f03230.jpeg"
tags:
  - XCPC
  - Codeforces
categories:
  - Competitive Programming
  - Codeforces
excerpt: CN Round 真是太难力，div2.E 至今尚未搞懂。
abbrlink: 80b55541
date: 2023-10-01 21:00:00
updated: 2023-10-01 21:00:00
---


## A. Jellyfish and Undertale

[Problem](https://codeforces.com/contest/1875/problem/A)

{% note success %}

显然每当倒计时仅剩 $1$ 时依次使用工具会最优。

则第 $i$ 个工具对时间的贡献就是 $\min(a-1,x_i)$。

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
	int a=read(),b=read(),n=read();
	vector<int> x(n+1);
	int sum=0;
	for(int i=1;i<=n;++i) {
		x[i]=read();
		sum+=min(x[i],a-1);
	}
	int res=b+sum;
	printf("%lld\n",res);
}


signed main()
{
	fre(test);
	int T=read();
	while(T--) {
		solve();
		// fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## B. Jellyfish and Game

[Problem](https://codeforces.com/contest/1874/problem/A)

{% note info %}

题意：$A$ 有 $n$ 个物品，$B$ 有 $m$ 个，每个物品有价值。游戏进行 $k$ 轮，奇数轮 $A$ 可以选择与 $B$ 的一个物品交换(或不交换)，偶数轮 $B$ 可以选择与 $A$ 的一个物品交换(或不交换)，问最终 $A$ 拥有物品的总价值。

$1\le n,m\le 50$，$1\le k \le 10^9$。

{% endnote %}

{% note success %}

一开始，$A$ 显然会拿自己的最小价值的和 $B$ 的最大价值进行交换，而 $B$ 的回合会拿 $\min(自己原本的最小价值,\ A\  给的物品价值)$ 和 $\max(A \ 原本最大价值,\ A \ 从\  B\  这拿走的物品价值)$ 进行交换。一个直觉是当游戏进行两轮以上后，双方的决策(即拿的物品的价值)都达到最优，因此游戏最终结果仅和 $k$ 的奇偶性相关。我们只需要暴力模拟 $k=1,2$ 时的结果。

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
	int n=read(),m=read(),k=read();
	vector<int> a,b;
	int sum=0;
	for(int i=1;i<=n;++i) {
		int x=read();
		a.push_back(x);
		sum+=x;
	}
	for(int i=1;i<=m;++i) {
		int x=read();
		b.push_back(x);
	}
	int res=sum;
	for(int i=1;i<=(k&1?1:2);++i) {
		if(i&1) {
			auto posa=min_element(a.begin(),a.end());
			auto posb=max_element(b.begin(),b.end());
			int mina=a[posa-a.begin()];
			int maxb=b[posb-b.begin()];
			if(mina>maxb) {
				continue;
			}
			res-=mina;
			res+=maxb;
			a.erase(posa);
			b.erase(posb);
			a.push_back(maxb);
			b.push_back(mina);
		} else {
			auto posa=max_element(a.begin(),a.end());
			auto posb=min_element(b.begin(),b.end());
			int maxa=a[posa-a.begin()];
			int minb=b[posb-b.begin()];
			if(maxa<minb) {
				continue;
			}
			res-=maxa;
			res+=minb;
			a.erase(posa);
			b.erase(posb);
			a.push_back(minb);
			b.push_back(maxa);
		}
	}
	printf("%lld\n",res);
}


signed main()
{
	fre(test);
	int T=read();
	while(T--) {
		solve();
		// fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## C. Jellyfish and Green Apple

[Problem](https://codeforces.com/contest/1875/problem/C)

{% note info %}

题意：$n$ 个苹果分给 $m$ 个人，每个苹果 $1kg$，每切一刀会均分成重量相同的两瓣，问最少切几刀能使每个人分到的苹果重量都相等，若无法均分输出 $-1$。

$1\le n,m\le 10^9$。

{% endnote %}

{% note success %}

当 $n\ge m$ 时，可以把 $n$ 个中的若干个 $m$ 分出去，剩下 $n\%m$ 个。而剩下不足 $m$ 个的为了能均分必然选择每个切一刀进行加倍，因此可以用递归进行模拟。

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

void divide(int n,int m,int &res,int times) {
	if(times>1000) {
		res=-1;
		return ;
	}
	while(n<m) {
		res+=n;
		n*=2;
	}
	int div=n%m;
	if(!div) {
		return ;
	}
	divide(div,m,res,times+1);
}

void solve()
{
	int n=read(),m=read();
	int res=0;
	divide(n,m,res,0);
	printf("%lld\n",res);
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
C++
```

{% endspoiler %}

{% note success %}

但这样无解条件并不明显，借用官方题解进行形式化的思考。由于苹果 $1kg$，以下用数量指代重量，完全等价。

若能均分，那么必有 $n\times 2^k\equiv0\pmod{m}$，因为只考虑什么时候无解时"先分再加倍"和"先加倍再分"是等价的。接着推出 $n\times 2^k\equiv0\pmod{m} \rightarrow 2^k\equiv 0 \pmod{\frac{m}{\gcd(n,m)}}$ .

{% endnote %}

{% spoiler Why? %}

定理：若 $ac\equiv bc\pmod{m},c\neq 0$，则 $a\equiv b \pmod{\frac{m}{\gcd(c,m)}}$

证明：

* 当 $\gcd(c,m)=1$ 时：

   由定理 "整数 $a,b$ 对模 $m$ 同余的充要条件是 $m\mid (a-b)$ " (比较显然，证明略)

   $\begin{align}\textbf{那么}&\text{ }ac\equiv bc\pmod{m}\\&\rightarrow m\mid(ac-bc)\\&\rightarrow m\mid (a-b)c \\&\rightarrow m\mid (a-b) \\&\rightarrow a\equiv b\pmod{m}\end{align}$
   
   又此时 $\gcd(c,m)=1$，故相当于 $a\equiv b\pmod{\frac{m}{\gcd(c,m)}}$ .

* 当 $\gcd(c,m)\neq 1$ 时：

  设 $\gcd(c,m)=d > 1$，令 $c=c'd$ 和 $m=m'd$，则 $\gcd(c',m')=1$ .

   $\begin{align}\textbf{那么}&\text{ }ac\equiv bc \pmod{m} \\&\rightarrow ac'\equiv bc' \pmod{m'} \\&\rightarrow a\equiv b \pmod{m'}\ (由上文另一点的证明)\\&\rightarrow a\equiv b \pmod{\frac{m}{d}}\\&\rightarrow a\equiv b\pmod{\frac{m}{\gcd(c,m)}}\end{align}$

{% endspoiler %}

{% note success %}

也就是说，当 $\frac{m}{\gcd(n,m)}$ 不是 $2$ 的整数幂时无解，可以用 $\text{std::}$ $\underline{}\underline{}\text{builtin}$ $\underline{}\text{popcount()}$ 快速验证。

接着，若有解，那么每个人分到的苹果数量应该是实数 $\frac{n}{m}$，而具体的，每次一个人得到的苹果数量应该是 $2$ 的整数幂，即存在集合 $S$ 使 $\frac{n}{m}=\sum_{i\in S} \frac{1}{2^i}$。而 $|S|$ 即每个人得到的苹果数量，答案即为 $m\times |S|-n$。

减去 $n$ 是因为苹果总数量 $-$ 原有数量 $=$ 切的刀数。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>

using namespace std;

int n = 0, m = 0;

inline void solve(){
	scanf("%d %d", &n, &m); n %= m;
	int a = n / __gcd(n, m), b = m / __gcd(n, m);
	if(__builtin_popcount(b) > 1) printf("-1\n");
	else printf("%lld\n", 1ll * __builtin_popcount(a) * m - n);
}

int T = 0;

int main(){
	scanf("%d", &T);
	for(int i = 0 ; i < T ; i ++) solve();
	return 0;
}
```

{% endspoiler %}

## D. Jellyfish and Mex

[Problem](https://codeforces.com/contest/1875/problem/D)

{% note info %}

题意：一个有 $n$ 个数的非负数组，$n$ 次操作每次选一个数删掉后计算 $\text{MEX}$ 并累加，问能达到的最小价值。

$1\le n \le 5000$，$1\le a_i\le10^9$。

{% endnote %}

{% note success %}

根据样例就能看明白，让总价值最小就是以最小的价值让 $\text{MEX}$ 变为 $0$，并且我们只关心小于一开始 $\text{MEX}$ 的数的出现次数。

一开始我想假了，认为最优解一定是从小于 $\text{MEX}$ 的某个数开始删一路删到 $0$，喜提 2WA。

耽误了很多时间，直到拍到一组样例：


```cpp
9
1 1 0 3 3 0 2 4 0
Wrong Answer: 8
Correct Answer: 6
```

删法是先删掉 $2$，然后删 $0$，答案并不连续，所以考虑 dp。

$dp[i]$ 表示目前从 $\text{MEX}$ 开始删到 $i$ 的最小价值，则 $dp[i]=\mathop\min\limits_{j\in[i+1,\text{MEX}]}(dp[i],dp[j]+cnt[i]\times j)$ .

因为一开始有一个数是没有贡献的，所以答案是 $dp[0]-\text{MEX}$。

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
	vector<int> a(n+1),cnt(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
		if(a[i]<=n) {
			cnt[a[i]]++;
		}
	}
	int mex=0;
	while(cnt[mex]) {
		mex++;
	}
	vector<int> dp(n+1,inf);
	dp[mex]=0;
	for(int i=mex;i>=0;--i) {
		for(int j=i+1;j<=mex;++j) {
			dp[i]=min(dp[i],dp[j]+cnt[i]*j);
		}
	}
	printf("%lld\n",dp[0]-mex);
}


signed main()
{
	fre(test);
	int T=read();
	while(T--) {
		solve();
		// fflush(stdout);
	}
	return 0;
}
C++
```

{% endspoiler %}
