---
title: "【题解】Codeforces Round 729 (Div.2) 4 of 6"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/c17e18190fb6dea6e843b32fb19de3c0.jpeg"
tags:
  - XCPC
  - Codeforces
categories:
  - Competitive Programming
  - Codeforces
excerpt: 哈哈，两年前不会DP，现在也不会。
abbrlink: 49b078d6
date: 2021-07-04 21:00:00
updated: 2021-07-04 21:00:00
---


## A. Odd Set

[Problem](https://codeforces.com/contest/1542/problem/A)

{% note info %}

题意：给出长为 $2n$ 的数组，问是否能分成 $n$ 个长度为 $2$ 的组使每组内两数之和均为奇数。

{% endnote %}

{% note success %}

若和为奇数，则两数一奇一偶，即判断原数列中奇数个数是否等于偶数个数。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define re register int
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=(x<<3)+(x<<1)+(ch^48);ch=getchar();}
	return f==1?x:-x;
}
int main()
{
	int T=read();
	while(T--) 
    {
		int n=read();
		int cnt=0;
		for(re i=1;i<=n*2;++i) {
			int x=read();
			cnt+=(x%2);
		}
		if(cnt==n) {
			puts("Yes");
		} else {
			puts("No");
		}
	}
	return 0;
}
```

{% endspoiler %}

## B. Plus and Multiply

[Problem](https://codeforces.com/contest/1542/problem/B)

{% note info %}

题意：$T\le 10^5$ 组数据，给定正整数 $n,a,b$，每次能将一个数 $\times a$ 或 $+b$，问是否能将 $1$ 经过若干次操作得到 $n$。

$1\le n,a,b\le 10^9$。

{% endnote %}

{% note success %}

若得到了某个数 $x$ 满足 $(n-x)\% b=0$ 那么显然符合要求。

对于 $+b$ 操作，$\%b$ 后余数不变。

意味着只有 $\times a$ 操作会使 $\%b$ 的余数改变。

枚举不超过 $n$ 的 $a$ 的次方数 $x$ 判断是否满足 $(n-x)\%b=0$ 即可。

特判 $a=1$ 的情况。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define re register int
#define int long long
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=(x<<3)+(x<<1)+(ch^48);ch=getchar();}
	return f==1?x:-x;
}
signed main()
{
	int T=read();
	while(T--)
	{
		int x=read(),a=read(),b=read();
		int tmp=a,flag=0;
		if(a==1) {
			if((x-1)%b==0) {
                puts("Yes");
            } else {
                puts("No");
            }
			continue;
		}
		while(1) {
			if(tmp>x) {
                break;
            }
			if((x-tmp)%b==0) {
				flag=1;
				break;
			}
			tmp*=a;
		}
		if(flag || (x-1)%b==0) {
            puts("Yes");
        } else { 
            puts("No");
        }
	}
	return 0;
}
```

{% endspoiler %}

## C. Strange Function

[Problem](https://codeforces.com/contest/1542/problem/C)

{% note info %}

题意：求 $\sum\limits_{i=1}^n f_i$，$f_i$ 为满足 $x\nmid i$ 的最小正整数 $x$。

$1\le T\le 10^4$，$1\le n\le 10^{16}$。

{% endnote %}

{% note success %}

没什么思路，打表得到 $2,3,2,3,2,4,2,3,2,3,2,5,2,\dots$。

令 $p_i$ 为第一次出现 $i$ 的位置，观察有 $p_3=2,p_4=6,p_5=12$，类比得 $p_i=\text{lcm} (1\sim i-1)$。

{% endnote %}

{% spoiler Why? %}

因为对于 $f_x$，$1\sim (f_x-1)$ 必然是 $p_{f_x}$ 的因子，故最优选择就是它们的最小公倍数。

{% endspoiler %}

{% note success %}

其中每个位置贡献至少为 $2$，故初始化 $\text{ans}=2n$。

又若 $i$ 在位置 $pos$ 有贡献，则在 $pos$ 的倍数处也必有贡献，且每次贡献为 $1$。

而每个 $i$ 在 $1\sim n$ 中出现 $\left\lfloor\dfrac{n}{p_i}\right\rfloor$ 次，故 $\text{ans}=2n+\sum\limits_{i=3}^{p_i\le n}\left\lfloor\dfrac{n}{p_i}\right\rfloor$ .

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define re register int
#define int long long
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=(x<<3)+(x<<1)+(ch^48);ch=getchar();}
	return f==1?x:-x;
}
const int maxn=1e16+10,modp=1e9+7;
int gcd(int x,int y)
{
	return !y?x:gcd(y,x%y);
}
int Lcm[50];//lcm[i]表示1~i-1的最小公倍数 
signed main()
{
	int tmp=1,x=1;
	while(1)
	{
		Lcm[tmp]=x;
		x=x*tmp/gcd(x,tmp);
		if(x>maxn)break;
		tmp++;
    }
	int T=read();
	while(T--)
	{
		int n=read(),ans=2*n%modp;
		for(re i=3;i<=tmp;++i)
			ans=(ans+n/Lcm[i])%modp;
		printf("%lld\n",ans);
	}
	return 0;
}
```

{% endspoiler %}

## D. Priority Queue

[Problem](https://codeforces.com/contest/1542/problem/D)

{% note info %}

题意：给定长为 $n$ 的操作序列 $A$，定义操作序列 $B$ 是 $A$ 的一个子序列，并维护一个可重集 $T$。若操作形如 `+ x` 则将 $x$ 插入 $T$，若操作形如 `-` 则将 $T$ 中最小元素删去(若为空则忽略)。令 $f(B)$ 为经过 $B$ 的操作后 $T$ 中剩余元素的和，求 $\sum f(B)$。

$1\le n \le 500$。

{% endnote %}

{% note success %}

类计数 dp，因为我们对于每一个`+ x` 操作只关心数 $x$ 最终出现在多少个 $B$ 中。因为最多有 $n$ 个 `+ x`，所以可以最多进行 $n$ 次 dp 得到结果，每次 $O(n^2)$，一共 $O(n^3)$。

令 $f_{i,j}$ 为前 $i$ 个数中有 $j$ 个数比 $x$ 小的方案数，设当前第 $i$ 位读到 `-`，比 $x$ 大的数和比 $x$ 小的数，由该位选或不选分类讨论写出转移方程。若 $A[k]=x$ :

$$
f_{i,j}=\begin{cases}f_{i-1,j}+f_{i-1,j+1}&,A[i]= \text{'-'}\\f_{i-1,j}+f_{i-1,j}&,A[i]>x \text{ or }A[i]=x,i>k \\f_{i-1,j}+f_{i-1,j-1}&,A[i]<x,j\neq0 \text{ or }A[i]=x,i<k\\f_{i-1,j}&,A[i]<x,j=0 \text{ or }A[i]=x,i<k\end{cases}
$$

特别注意第一种情况当 $i<k$ 且 $j=0$ 时需要加上 $f_{i-1,0}$，因为此时选上 `-` 不会使 $j$ 变小。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define re register int
#define int long long
inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=(x<<3)+(x<<1)+(ch^48);ch=getchar();}
	return f==1?x:-x;
}
const int modp=998244353; 
int A[500+10],f[500+10][500+10];
signed main()
{
	int n=read();
	for(re i=1;i<=n;++i)
	{
		char x[3];scanf("%s",&x);
		if(x[0]=='+') A[i]=read();
		else A[i]=-1;
	}
	int ans=0;
	for(re k=1;k<=n;++k)
	{
		if(A[k]==-1) continue;
		memset(f,0,sizeof f);
		f[0][0]=1;
		for(re i=1;i<=n;++i)
		{
			if(i==k)
			{
				memcpy(f[i],f[i-1],sizeof f[i]);
				continue;
			}
			for(re j=0;j<=n;++j)
			{
				if(A[i]==-1)
				{
					f[i][j]=(f[i-1][j]+f[i-1][j+1])%modp;
					if(j==0 && i<k) f[i][j]=(f[i][j]+f[i-1][j])%modp;
				}
				else if(A[i]<A[k] || (A[i]==A[k] && i<k))
				{
					if(j==0)f[i][j]=f[i-1][j];
					else f[i][j]=(f[i-1][j]+f[i-1][j-1])%modp;
				}
				else f[i][j]=(f[i-1][j]+f[i-1][j])%modp;
			}	
		}
		int sum=0;
		for(re j=0;j<=n;++j)
			sum=(sum+f[n][j])%modp;
		ans=(ans+sum*A[k]%modp)%modp;
	}
	printf("%lld\n",ans);
	return 0;
}
```

{% endspoiler %}
