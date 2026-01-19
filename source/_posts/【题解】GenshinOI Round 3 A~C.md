---
title: "【题解】GenshinOI Round 3 A~C"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/52f2babd3ea16fe90a1a607915b5d998.jpeg"
tags:
  - OI
  - Luogu
categories:
  - Competitive Programming
  - Luogu
excerpt: 碰到题才发现已经连倍增都不会写了，好似。
abbrlink: 81a98245
date: 2023-10-31 15:00:00
updated: 2023-10-31 15:00:00
---


![](https://sy.hhwdd.com/RequireFile.do?fid=aZQ9MeAe)

## A. wbyblD

[Problem](https://www.luogu.com.cn/problem/P9815?contestId=141486)

{% note info %}

题意：有 $n+2$ 个点排成一排，编号 $0\sim n+1$。对每个 $0\le i\le n+1$ 号点有两个整数 $a_i,b_i$。初始时 $a_0=b_0=a_{n+1}=b_{n+1}=0$。

设你当前在第 $x$ 号点，移动方向为 $y$，初始时 $x=0,y=1$。

接下来你按如下方式移动直到 $x,y$ 某一次变化后满足 $x=0,y=-1$ 或 $x=n+1,y=1$。

* 若 $y=1$，先将 $x$ 加 $1$，此时若 $a_x>0$ 则将 $y$ 变成 $-1$，否则 $y$ 不变，最后再将 $a_x$ 减 $1$。

* 若 $y=-1$，先将 $x$ 减 $1$，此时若 $b_x>0$ 则将 $y$ 变成 $1$，否则 $y$ 不变，最后再将 $b_x$ 减 $1$。

问最后结束时 $x$ 会在 $0$ 号点还是 $n+1$ 号点。

$1\le \sum n\le 10^6$，$0\le a_i,b_i\le 10^6$。

{% endnote %}

{% note success %}

看到题很快写了个线段树二分。咦，怎么样例不对？哦，看错题了，乐。

脑海里模拟一下，发现对于一组 $a_i,b_{i-1}$ 相当于较量谁大直到一方变为 $0$，而在这之前你只能左右横跳。

如果 $a_i$ 较大，那你往回走，如果凑不够足够的 $\sum b_{j} \text{ }, j\in[1,i-1]$（指比较后剩下的 $b_j$），那你就回家了。

重复这个过程，思路转个弯，实际上就是对每个 $i$ 比较 $\sum a_{1\sim i}$ 和 $\sum b_{1\sim{i-1}}$。

前缀和记录，时间复杂度 $O(n)$。

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
	vector<int> a(n+2),b(n+2);
	for(int i=1;i<=n;++i) {
		a[i]=read();
		b[i]=read();
	}
	int sum=0;
	for(int i=1;i<=n;++i) {
		if(a[i]>0) {
			sum-=a[i];
		}
		if(sum<0) {
			puts("0");
			return ;
		}
		if(b[i]>0) {
			sum+=b[i];
		}
	}
	printf("%lld\n",n+1);
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

## B. 少项式复合幂

[Problem](https://www.luogu.com.cn/problem/P9816?contestId=141486)

{% note info %}

题意：给定多项式 $f(x)=\sum_{i=1}^ma_ix^{b_i}$。定义 $f_1(x)=f(x)$，$f_n(x)=f(f_{n-1}(x))$。

给定模数 $p$。有 $q$ 次询问，每次给出 $x,y$，查询 $f_y(x)\bmod p$ 的值。

$1\le m\le 20$，$0\le a_i,b_i\le 10^5$，$2\le p\le 10^5$，$1\le q\le 3\times 10^5$，$1\le x,y\le 10^7$。

{% endnote %}

{% note success %}

诈骗题。

注意到模数 $p$ 十分小，而每次经过 $f(x)$ 运算后得出的结果只能是 $[0,p)$。

那么只需要对每个 $i\in[0,p)$ 代进函数预处理出 $f(i)$，那么进行一次询问的复杂度降到 $O(y)$。

总复杂度 $O(qy)$，继续优化。

倍增，令 $f_{i,j}$ 为数 $i$ 经过 $2^j$ 次迭代后得到的结果。

询问时对 $y$ 的二进制下的每一位考虑即可。

时间复杂度 $O(mp+q\log y)$。

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

inline int qpow(int k,int n,int p) {
	int s=1;
	for(;n;n>>=1,k=k*k%p) if(n&1) s=s*k%p;
	return s;
}


void solve()
{
	int m=read(),q=read(),modp=read();

	vector<int> a(m+1),b(m+1);
	for(int i=1;i<=m;++i) {
		a[i]=read();
		b[i]=read();
	}

	auto calc = [&] (int x) {
		int res=0;
		for(int i=1;i<=m;++i) {
			res+=a[i]*qpow(x,b[i],modp)%modp;
			res%=modp;
		}
		return res;
	};

	vector<vector<int>> f(modp,vector<int>(26));
	for(int i=0;i<modp;++i) {
		f[i][0]=calc(i);
	}
	for(int j=1;j<=25;++j) {
		for(int i=0;i<modp;++i) {
			f[i][j]=f[f[i][j-1]][j-1];
		}
	}

	for(int i=1;i<=q;++i) {
		int x=read()%modp,y=read();
		for(int j=0;j<=25;++j) {
			if(y>>j&1) {
				x=f[x][j];
			}
		}
		printf("%lld\n",x);
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

倍增的写法：


```cpp
for(int j=1;j<=25;++j) {
	for(int i=0;i<n;++i) {
		f[i][j]=f[f[i][j-1]][j-1];
	}
}
```

选从 $i$ 开始的第 $2^j$ 个相当于选从 $i$ 往后 $2^{j-1}$ 处开始的第 $2^{j-1}$ 个。

{% endnote %}

## C. ImxcslD

[Problem](https://www.luogu.com.cn/problem/P9817?contestId=141486)

{% note info %}

题意：定义长度为 $m$ 的非空序列 $p_1,p_2,...,p_m$ 是**乱**的当且仅当满足以下条件。

* $\sum_{i=1}^m p_i\le n$。

* $\forall\text{ } i\in[1,m]$，$p_i=1$ 或 $p_i$ 为质数。

定义一个**乱**的序列 $p_1,p_2,...,p_m$ 的**乱斗值**为 $\sum_{i=1}^m (p_i-k)^2$。

特别的，定义一个**不乱**的序列的乱斗值为 $0$。

现在给定正整数 $n,k$，问所有序列中**乱斗值**最大的序列的**乱斗值** 是多少。

$1\le T\le 10^3$，$1\le n\le 10^9$，$1\le k\le 5\times 10^4$。

{% endnote %}

{% note success %}

有难度的贪心。

考虑什么时候结果是最优的：我们要让 $(p_i-k)^2$ 尽可能的大，也就是 $p_i$ 和 $k$ 的差值大，分为两种情况：

* 当 $p_i<k$ 时，要离 $k$ 越远，肯定是全为 $1$ 最优。

* 当 $p_i>k$ 时，考虑写上一个 $p_i$ 对答案的影响。

  * 一开始构造序列全为 $1$，答案是 $m(1-k)^2$。

  * 写出一个 $p_i$ 时，相当于划掉了 $p_i$ 个 $1$，答案增加了 $(p_i-k)^2-p_i(1-k)^2$。

  * 发现每次变更总是可以选择大的 $p_i$，而答案也只和当时 $1$ 的个数相关。

  * 所以可以递归，每次选择小于等于 $n$ 的最大的质数 $P$，看看最大值能不能更新，然后将问题递归到 $(n-P,k)$。


这并不严谨，需要感性理解。

复杂度不会分析，只能说感觉能接受？

预处理出质数表能 $O(\frac{\sqrt{n}}{\ln n})$ 查找质数，但事实 $O(\sqrt{n})$ 也完全卡不满。

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

const int N = 1e6+5;
int prime[N],mark[N],phi[N],tot_prime;
void getphi(int n)
{
    phi[1]=1;
    for(int i=2;i<=n;i++) {
        if(!mark[i]) {
            prime[++tot_prime]=i;
            phi[i]=i-1;
        }
        for(int j=1;j<=tot_prime;j++) {
            if(i*prime[j]>n) {
            	break;
            }
            mark[i*prime[j]]=1;
            if(i%prime[j]==0) {
                phi[i*prime[j]]=phi[i]*prime[j];
                break;
            } else {
            	phi[i*prime[j]]=phi[i]*phi[prime[j]];
            }
        }
    }
}
bool isprime(int x) 
{
	if(tot_prime) {
		return x-1==phi[x];
	}
	if(x<=1) return false;
	for(int i=2;i<=sqrt(x);++i) {
		if(x%i==0) {
			return false;
		}
	}
	return true;
}

void solve()
{
	int n=read(),k=read();
	int res=n*(k-1)*(k-1);
	for(int i=n,sum=res;i>=1;--i) {
		if(isprime(i)) {
			sum-=i*(k-1)*(k-1);
			sum+=(k-i)*(k-i);
			res=max(res,sum);
			n-=i;
			i=min(n,i)+1;
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
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

