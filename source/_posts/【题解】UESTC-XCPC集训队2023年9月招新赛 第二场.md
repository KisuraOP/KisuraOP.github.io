---
title: "【题解】UESTC-XCPC集训队2023年9月招新赛 第二场"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/d3ebda876182694665af2c882af19fc6.jpeg"
tags:
  - XCPC
  - UESTC
categories:
  - Competitive Programming
  - Other
excerpt: 2023.09.24 赛于清水河校区基础实验大楼A232。题很好，但人太菜，补题时学到很多。
abbrlink: f9da5f78
date: 2023-10-27 21:00:00
updated: 2023-10-27 21:00:00
---


比赛链接：[Link](https://vjudge.net/contest/583377#overview)

为避免 MyGO!!!!! 污染，以下均采用原题头。

按个人感官难度排序，及其主观。

题选的相当棒，值得反复品味。

## B. Hello, ACMer!

{% note info %}

题意：统计给定字符串中 `hznu` 的出现次数。

{% endnote %}

{% note success %}

模拟即可。

记得特判字符串长度小于 $4$ 的情况。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}

void solve()
{
	string s;
	cin>>s;
	int res=0;
	if(s.size()<4) {
		return puts("0"),void();
	}
	for(int i=0;i<=s.size()-4;++i) {
		string t=s.substr(i,4);
		if(t=="hznu") {
			res++;
		}
	}
	printf("%lld\n",res);
}

signed main()
{
	int T=1;
	while(T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

## C. New String

{% note info %}

题意：给定一个自定义字典序排序规则以及若干字符串，求字典序第 $k$ 小的串。

$1\le|S|\le 1000$。

{% endnote %}

{% note success %}

用 `std::map` 还原字典序或自定义 `std::sort` 排序规则均可。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}

void solve()
{
	string all;
	cin>>all;
	map<char,char> mp,yl;
	for(int i=0;i<all.size();++i) {
		mp[all[i]]=('a'+i);
		yl['a'+i]=all[i];
	}
	int n=read();
	vector<string> s(n);
	for(int i=0;i<n;++i) {
		cin>>s[i];
		for(int j=0;j<s[i].size();++j) {
			s[i][j]=mp[s[i][j]];
		}
	}
	sort(s.begin(),s.end());
	int K=read();
	for(int i=0;i<s[K-1].size();++i) {
		cout<<yl[s[K-1][i]];
	}
}

signed main()
{
	int T=1;
	while(T--) {
		solve();
	}
}
```

{% endspoiler %}

## L. Klee's Wonderful Adventure

{% note info %}

题意：平面直角坐标系上有 $n$ 个点，相同第 $i$ 象限间点的移动速度为 $v_i$，不同象限间点间的移动速度为 $v_0$，求从起点 $s$ 到终点 $t$ 的最短时间。

$1\le n\le 3\times 10^3$。

{% endnote %}

{% note success %}

注意到 $n$ 很小，直接预处理出通过任意两点所需的时间，再跑 `dijkstra` 就行了。

时间复杂度 $O(n^2)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define inf 0x3fffffffffffffff

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}
const int N = 3002;
struct node{
	int x,y;
}a[N];

double dis[N][N];

int whd(int x,int y) {
	if(x>=1 && y>=1) return 1;
	else if(x<=-1 && y>=1) return 2;
	else if(x<=-1 && y<=-1) return 3;
	else if(x>=1 && y<=-1) return 4;
	return 0;
}
int v[6];

void solve()
{
	int n=read();
	v[1]=read(),v[2]=read(),v[3]=read(),v[4]=read(),v[0]=read();
	int st=read(),ed=read();
	for(int i=1;i<=n;++i) {
		a[i].x=read(),a[i].y=read();
	}

	for(int i=1;i<=n;++i) {
		for(int j=1;j<=n;++j) {
			dis[i][j]=sqrt( (a[i].x-a[j].x)*(a[i].x-a[j].x) + (a[i].y-a[j].y)*(a[i].y-a[j].y));
			int fir=whd(a[i].x,a[i].y);
			int sec=whd(a[j].x,a[j].y);
			if(fir==sec) {
				dis[i][j]/=v[fir];
			} else {
				dis[i][j]/=v[0];
			}
		}
	}

	vector<vector<pair<int,double>>> adj(n+1);
	for(int i=1;i<=n;++i) {
		for(int j=1;j<=n;++j) {
			adj[i].push_back({j,dis[i][j]});
			adj[j].push_back({i,dis[i][j]});
		}
	}
	vector<double> real_dis(n+1);
	vector<int> vis(n+1);
	auto dijkstra = [&] (int s) {
		real_dis.assign(n+1,1.0*inf);
		vis.assign(n+1,false);
		priority_queue<pair<double,int>> q;
		q.push({0.0,s});
		real_dis[s]=0;
		while(!q.empty()) {
			int x=q.top().second;
			q.pop();
			if(vis[x]) {
				continue;
			}
			vis[x]=true;
			for(auto [y,z]:adj[x]) {
				if(real_dis[y]>real_dis[x]+z) {
					real_dis[y]=real_dis[x]+z;
					q.push({-real_dis[y],y});
				}
			}
		}
	};
	dijkstra(st);
	double ans=real_dis[ed];
	printf("%.8lf\n",ans);
}

signed main()
{
	int T=1;
	while(T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

## D. Check Problems

{% note info %}

题意：有 $n$ 个人查验题目，第 $i$ 个人在第 $j$ 秒会查验编号为 $a_i+j-1$ 的题。$q$ 次询问，每次问第 $t$ 秒时有多少道题目已经被查验。

$1\le n,q\le 5\times 10^5$，$1\le a_1 \le a_2 \le \dots \le a_n \le 10^{18}$，$0\le t \le 10^{18}$。

{% endnote %}

{% note success %}

相当于数轴上 $n$ 个点，每个点每次向右扩张一个单位。

那么当一个点触到离它右边的一个点时，往后它就没有贡献了。

并且当一个点没有贡献时，间隔比它小对应的点也都没有了贡献，符合单调性。

因此我们把每个点间的间隔距离 $a_i-a_{i-1}$ 记录下来，排序，记录前缀和，再在上面二分。

每次查询总是前缀和 $+$ 没有扩张完的剩下段。

时间复杂度 $O((n+q)\log n)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}

void solve()
{
	int n=read();
	vector<int> a(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
	} 
	if(n==1) {
		int q=read();
		while(q--) {
			int x=read();
			printf("%lld\n",x);
		}
		return ;
	}
	sort(a.begin()+1,a.end());
	vector<int> d;
	for(int i=2;i<=n;++i) {
		d.push_back(a[i]-a[i-1]);
	}
	sort(d.begin(),d.end());
	vector<int> sum(n+1);
	sum[0]=d[0];
	for(int i=1;i<d.size();++i) {
		sum[i]=sum[i-1]+d[i];
	}
	int q=read();
	for(int i=0;i<q;++i) {
		int x=read(),pos;
		auto p=upper_bound(d.begin(),d.end(),x);
		if(p==d.end()) {
			pos=n-1;
 		} else {
 			pos=p-d.begin();
 		}
 		int res = pos==0 ? 0 : sum[pos-1];
 		res+=(n-pos)*x;
 		printf("%lld\n",res);
	}
}

signed main()
{
	int T=1;
	while(T--) {
		solve();
	}
}
```

{% endspoiler %}

## E. Tree Problem

{% note info %}

题意：给定 $n$ 个点的树，$q$ 次询问每次询问一个点 $x$，问树上有多少条简单路径途径点 $x$。

$2\le n \le 10^5$，$1\le q\le 10^5$。

{% endnote %}

{% note success %}

简单画个图，经过 $x$ 的简单路径的数量就是 $x$ 所有子树大小的两两乘积。

由于每个子树算了两遍，贡献要除以 $2$。

别忘记 $x$ 作为简单路径端点的 $n-1$ 种情况。

时间复杂度 $O(n+q)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return f==1?x:-x;
}

void solve()
{
	int n=read();
	vector<vector<int>> adj(n+1);
	for(int i=1;i<=n-1;++i) {
		int x=read(),y=read();
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	vector<int> sz(n+1),fa(n+1);
	function<void(int,int)> dfs = [&] (int x,int fath) {
		sz[x]=1;
		fa[x]=fath;
		for(auto y:adj[x]) {
			if(y==fath) continue;
			dfs(y,x);
			sz[x]+=sz[y];
		}
	};
	dfs(1,0);

	auto calc = [&](int x){
		int sum=0;
		for(auto y:adj[x]) {
			if(y==fa[x]) {
				sum+=(n-sz[x]);
			} else {
				sum+=sz[y];
			}
		}
		int res=0;
		for(auto y:adj[x]) {
			if(y==fa[x]) {
				res+=(n-sz[x])*(sum-(n-sz[x]));
			} else {
				res+=sz[y]*(sum-sz[y]);
			}
		}
		return res/2+n-1;
	}; 
	vector<int> ans(n+1,0);
	int q=read();
	for(int i=0;i<q;++i) {
		int x=read();
		if(!ans[x]) {
			ans[x]=calc(x);
		}
		printf("%lld\n",ans[x]);
	}
}

signed main()
{
	int T=1;
	while(T--) {
		solve();
	}
}
```

{% endspoiler %}

## G. Subarrays

{% note info %}

题意：给定长度为 $n$ 的正整数序列 $a$，求满足子段和为 $k$ 的倍数的子段数量。

$1\le n \le 10^5$，$1\le k,a_i \le 10^9$。

{% endnote %}

{% note success %}

令 $sum$ 为前缀和，即求满足 $sum[l,r]\equiv 0 \pmod k$ 的区间个数。

即：
$$
sum[l,r] \bmod k =(sum[r]-sum[l-1])\bmod k = 0
$$

也就是：
$$
sum[l-1]\equiv sum[r] \pmod k
$$

于是题目变成了对每个位置 $i$ 求小于 $i$ 的所有前缀和中有多少模 $k$ 值相同，用 `std::map` 维护即可。

时间复杂度 $O(n\log n)$。

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
	vector<int> a(n+1),sum(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
		sum[i]=sum[i-1]+a[i];
	}
	int res=0;
	map<int,int> cnt;
	cnt[0]++;
	for(int i=1;i<=n;++i) {
		res+=cnt[sum[i]%k];
		cnt[sum[i]%k]++;
	}
	printf("%lld\n",res);
}


signed main()
{
	//fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## F. Easy Problem

{% note info %}

题意：$A,B$ 在 $n\times n$ 的网格图上游走，每次移动它们能选择上下左右四个方向中的一个，然后两个人按该方向行走一格（如前方是边界或障碍物则不移动），问两人相遇所需的最小移动步数。

$2\le n \le 50$。

{% endnote %}

{% note success %}

只要想到把两个玩家的位置同时压缩成一个状态就迎刃而解了。

令 $dep[ax][ay][bx][by]$ 为 $A$ 在点 $(ax,ay)$，$B$ 在点 $(bx,by)$ 时两人相遇所需的最短步数。

广度优先搜索，每次移动若新位置对应的状态非 $0$，则代表有更短的路径到达那个位置。

那么我们不移动，否则步数 $+1$ 进行转移。

当 $(ax,ay)=(bx,by)$ 时代表两人到达同一点。

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
	vector<string> s(n);
	int sx,sy,fx,fy;
	for(int i=0;i<n;++i) {
		cin>>s[i];
		for(int j=0;j<n;++j) {
			if(s[i][j]=='a') {
				sx=i;
				sy=j;
			} else if(s[i][j]=='b') {
				fx=i;
				fy=j;
			}
		}
	}
	typedef tuple<int,int,int,int> node;
	int dx[]={-1,0,1,0},dy[]={0,1,0,-1};
	queue<node> q;
	map<node,int> dep;
	dep[{sx,sy,fx,fy}]=0;
	q.push({sx,sy,fx,fy});
	while(!q.empty()) {
		auto point=q.front();
		q.pop();
		auto [ax,ay,bx,by]=point;
		if(ax==bx && ay==by) {
			int res=dep[point];
			printf("%lld\n",res);
			return ;
		}
		for(int i=0;i<4;++i) {
			int nax=ax+dx[i],nay=ay+dy[i];
			int nbx=bx+dx[i],nby=by+dy[i];
			if(nax<0 || nax>=n || nay<0 || nay>=n || s[nax][nay]=='*') {
				nax=ax;
				nay=ay;
			}
			if(nbx<0 || nbx>=n || nby<0 || nby>=n || s[nbx][nby]=='*') {
				nbx=bx;
				nby=by;
			}
			node npoint={nax,nay,nbx,nby};
			if(dep.find(npoint)==dep.end()) {
				q.push(npoint);
				dep[npoint]=dep[point]+1;
			}
		}
	}
	puts("no solution");
}


signed main()
{
	//fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## J. IHI's Homework

{% note info %}

题意：给定整数 $s$ 和序列 $a$，令答案为满足 $x_1+x_2+\dots+x_n\le s$ 且 $\forall x_i \ge a_i$ 的序列 $x$ 的方案数。$q$ 次询问每次更改 $a$ 中的一个数，问每次变动后的答案。

$1\le n,q,a_i \le 2\times 10^5$，$0\le s\le 2\times 10^5$。

{% endnote %}

{% note success %}

简单排列组合，但我不会数学，这题就显得很难。

将题目转化成球盒问题，有 $n$ 个盒子和 $s$ 个球，将无区分的球放进有区分的盒子，可以有空盒，且第 $i$ 个盒子至少得有 $x_i$ 个球，每次修改一个 $x_i$，问方案数。

首先把每个盒子放入 $x_i$ 个球，剩下 $t=s-\sum x_i$ 个球可以任意放入 $n$ 个盒子。

结论：$n$ 个无区别球放入 $m$ 个有区别盒子，允许空盒的方案数是 $C_{m+n-1}^{n}$。

{% endnote %}

{% spoiler Why? %}

高中数学学过插板法。

如果每个盒子至少有一个球，那么我们可以用 $m-1$ 个板去插 $n-1$ 个空，方案数是 $C_{n-1}^{m-1}$。

如果允许空盒，那么要做一个转化：

转化为 $n$ 个无区别球和 $m-1$ 个无区别板的一个自由排列，再把这 $m-1$ 个板选出来，也就是 $C_{n+m-1}^{m-1}=C_{n+m-1}^{n}$。

{% endspoiler %}

{% note success %}

那么答案就是：
$$
\sum_{i=1}^t C_{n+i-1}^{i}
$$

发现对于相同的 $t$ 答案相同，那么只要预处理出上式的前缀和就可以 $O(1)$ 回答询问。

时间复杂度 $O(n+s+q)$。

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
const int modp = 1e9+7;

template<const int T>
struct ModInt {
    const static int mod = T;
    int x;
    ModInt(int x = 0) : x(x % mod) {}
    int val() { return x; }
    ModInt operator + (const ModInt &a) const { int x0 = x + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    ModInt operator - (const ModInt &a) const { int x0 = x - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    ModInt operator * (const ModInt &a) const { return ModInt(1LL * x * a.x % mod); }
    ModInt operator / (const ModInt &a) const { return *this * a.inv(); }
    bool operator == (const ModInt &a) const { return x == a.x; };
    bool operator != (const ModInt &a) const { return x != a.x; };
    void operator += (const ModInt &a) { x += a.x; if (x >= mod) x -= mod; }
    void operator -= (const ModInt &a) { x -= a.x; if (x < 0) x += mod; }
    void operator *= (const ModInt &a) { x = 1LL * x * a.x % mod; }
    void operator /= (const ModInt &a) { *this = *this / a; }
    friend ModInt operator + (int y, const ModInt &a){ int x0 = y + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    friend ModInt operator - (int y, const ModInt &a){ int x0 = y - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    friend ModInt operator * (int y, const ModInt &a){ return ModInt(1LL * y * a.x % mod);}
    friend ModInt operator / (int y, const ModInt &a){ return ModInt(y) / a;}
    friend ostream &operator<<(ostream &os, const ModInt &a) { return os << a.x;}
    friend istream &operator>>(istream &is, ModInt &t){return is >> t.x;}

    ModInt pow(int64_t n) const {
        ModInt res(1), mul(x);
        while(n){
            if (n & 1) res *= mul;
            mul *= mul;
            n >>= 1;
        }
        return res;
    }
    
    ModInt inv() const {
        int a = x, b = mod, u = 1, v = 0;
        while (b) {
            int t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        if (u < 0) u += mod;
        return u;
    }
    
};
using mint = ModInt<modp>;

inline mint qpow(mint k,int n) {
	mint s=1;
	for(;n;n>>=1,k=k*k) if(n&1) s=s*k;
	return s;
}

struct math {
	int size=0;
	vector<mint> frac;
	vector<mint> inv;
	math() {}
	math(int n) {
		init(n);
	}
	void init(int n) {
		frac.resize(n+2);
		inv.resize(n+2);
		frac[0]=1;
		for(int i=size+1;i<=n;++i) {
			frac[i]=frac[i-1]*i;
		}
		inv[n]=qpow(frac[n],modp-2);
		for(int i=n;i>=size+1;--i) {
			inv[i-1]=inv[i]*i;
		}
		size=n;
	}
	mint C(int n,int m) {
		if(n<m || m<0) return 0;
		if(n>size) init(n);
		return frac[n]*inv[m]*inv[n-m];
	}
}binom;

mint C(int n,int m) {
	return binom.C(n,m); 
}

void solve()
{
	int n=read(),s=read(),q=read();
	vector<int> a(n+1);
	int sum=0;
	for(int i=1;i<=n;++i) {
		a[i]=read();
		sum+=a[i];
	}
	vector<mint> p(s+1);
	for(int i=0;i<=s;++i) {
		p[i]=C(n+i-1,i);
		if(i) p[i]+=p[i-1];
	}
	for(int i=1;i<=q;++i) {
		int pos=read(),x=read();
		sum+=x-a[pos];
		a[pos]=x;
		printf("%lld\n",s-sum>=0 ? p[s-sum] : 0ll);
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

## K. IHI's Magic String

{% note info %}

题意：现在有一个空字符串和三种操作，输出 $q$ 次操作后的字符串。

1. 把一个指定小写字母插到末尾。

2. 删除字符串末尾的字符（若为空字符串则不操作）

3. 把目前所有的字符 $x$ 替换成字符 $y$。

$1\le q \le 10^5$。

{% endnote %}

{% note success %}

一般这种正着做简单但时间复杂度高的题总是考虑倒着做。

倒着做的好处在于：假设有操作 $a\to b$，那么之后添加的 $a$ 都可以直接用 $b$ 替代，那如果再有 $b\to c$ 呢？

用 $mp[i]$ 表示在添加 $i$ 时应该添加 $mp[i]$，初始 $mp[i]=i$。

那么对于上面那种情况实际等效于 $a\to c$，我们直接 $mp[a]=mp[b]$。

这其实类似并查集的路径压缩方法。

对于删除操作，可以直接用一个延迟标记（这里是 $\text{del}$），来 $O(1)$ 判断当前字符是否计入答案，很妙。

时间复杂度 $O(q\log 26)$。

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
	vector<array<int,3>> ver;
	int q=read();
	for(int i=1;i<=q;++i) {
		int opt=read(),a=0,b=0;
		char t[3];
		if(opt==1) {
			scanf("%s",&t);
			a=t[0]-'a';
		} else if(opt==3) {
			scanf("%s",&t);
			a=t[0]-'a';
			scanf("%s",&t);
			b=t[0]-'a';
		}
		ver.push_back({opt,a,b});
	}
	map<int,int> mp;
	for(int i=0;i<26;++i) {
		mp[i]=i;
	}
	int del=0;
	string res="";
	for(int i=ver.size()-1;i>=0;--i) {
		auto [opt,a,b] = ver[i];
		if(opt==1) {
			if(del) {
				del--;
			} else {
				res+=mp[a]+'a';
			}
		} else if(opt==2) {
			del++;
		} else {
			mp[a]=mp[b];
		}
	}
	reverse(res.begin(),res.end());
	if(!res.size()) {
		puts("The final string is empty");
	} else {
		cout<<res<<endl;
	}
}


signed main()
{
	//fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## I. Optimal Biking Strategy

{% note info %}

题意：$\text{Alice}$ 要去到 $p$ 米外的超市，他可以走路或骑车。路上有 $n$ 个停车点，能且仅能在停车点上下车，一块钱最多能骑 $s$ 米（骑 $x$ 米需花费 $\left\lceil \frac{x}{s} \right\rceil$ 元）。他现在只有 $k$ 元，问最少需要走路多远。

$1\le n \le 10^6$，$1\le p,s \le 10^9$，$1\le k\le 5$。

{% endnote %}

{% note success %}

场上写了一个 $O(nk\log n)$ 很奇怪的背包一直调不出来，后面发现完全是假的。

感觉我到现在对于 $\text{dp}$ 一直是模棱两可的状态，很烦。

用 $dp_{i,j}$ 代表前 $i$ 个停车点花费 $j$ 能骑的最远距离，那么答案就是 $p-dp_{n,k}$。

至于转移，根据题意算钱要上取整，所以多个相邻的骑车区间肯定是直接合并。

因为连续，所以可以二分，对于每一个 $k\in[1,j]$ 二分出花费 $k$ 能骑到的最远距离再转移。

具体地，当前在 $i$，就从满足 $a_i-a_l\le sk$ 的最远的 $l$ 处转移而来，即：
$$
dp_{i,j}=\max(dp_{i,j},dp_{l,j-k}+a_i-a_l)
$$

时间复杂度 $O(nk^2\log n)$。

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
    int n=read(),dis=read(),per_cost=read();
    vector<int> a(n+1);
    for(int i=1;i<=n;++i) {
        a[i]=read();
    }
    int V=read();
    vector<vector<int>> dp(n+1,vector<int>(V+1));
    for(int i=1;i<=n;++i) {
        for(int j=1;j<=V;++j) {
            dp[i][j]=dp[i-1][j];
            for(int k=1;k<=j;++k) {
                int mx=per_cost*k;
                // a[i]-a[lst]<=mx
                // a[lst]>=a[i]-mx
                int id=lower_bound(a.begin()+1,a.end(),a[i]-mx)-a.begin();
                if(id<=n) {
                    dp[i][j]=max(dp[i][j],dp[id][j-k]+a[i]-a[id]);
                }
            }
        }
    }
    int res=dis-dp[n][V];
    printf("%lld\n",res);
}


signed main()
{
    //fre(test);
    int T=1;
    while(T--) {
        solve();
        //fflush(stdout);
    }
    return 0;
}
```

{% endspoiler %}

## H. Ganyu Segment Tree

{% note info %}

题意：给定一个长度 $n$ 初值全为 $1$ 的序列 $a$，每个位置有上锁和不上锁两种状态。

三种操作，共操作 $m$ 次：

* `flip p` ：改变 $a_p$ 的状态。

* `mul l r x` ：把子段 $[l,r]$ 中所有未上锁元素乘以 $x$。

* `div l r x` ：查询子段 $[l,r]$ 中所有元素（包括上锁）是否是 $x$ 的倍数，输出 `Yes` 或 `No` 。若为 `Yes` ，将 $[l,r]$ 中的所有未上锁元素除以 $x$。

$1\le n,m \le 10^5$，$1\le x \le 30$。

{% endnote %}

{% note success %}

修改的数 $x$ 很小，所以可以把 $x$ 质因数分解，而 $[1,30]$ 内就 $10$ 个质数。

我们对每个质数都建一颗线段树，而处理是否能整除只需判断是否该区间都含有某个质因子。

具体的，对于操作 `mul l r x`，若 $x$ 能分解成 $cnt$ 个质因子 $y$，则在 $y$ 所属的线段树上区间 $+ cnt$。

那么对于操作 `div l r x`，检查 $x$ 的每个质因子 $y$，若 $y$ 所属的线段树在 $[l,r]$ 内的区间最小值比 $cnt$ 小，那么该区间不能被整除。否则区间 $-cnt$。

现在考虑如何维护解锁与未解锁。是一个很清奇的技巧：

对于每颗线段树开两个值 $tr1,tr2$，分别代表当前区间未锁定元素的最小值和区间锁定元素的最小值，初始化 $tr1=0,\ tr2=inf$。

对于 `mul` 和 `div` 操作，只对 $tr1$ 进行操作。

对于 `flip` 操作，只需单点 $swap(tr1,tr2)$。

对于查询操作，我们返回 $\min(tr1,tr2)$。

我们发现 $inf$ 和加减的值不在一个数量级，相当于没有影响，所以这么做是正确的。

时间复杂度 $O(m\log n)$。

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
#define ck(x) printf("check %lld\n",x);fflush(stdout)
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

struct SegmentTree {
	int n;
	vector<int> tree1,tree2;
	vector<int> lazy_add;
	SegmentTree(int size) {
		n = size+1;
		tree1.resize(4*n+1,0);
		tree2.resize(4*n+1,inf);
		lazy_add.resize(4*n+1,0);
	}
	inline void pushup(int p) {
		tree1[p] = min(tree1[p<<1], tree1[p<<1|1]);
		tree2[p] = min(tree2[p<<1], tree2[p<<1|1]);
	}
	inline void pushdown(int p,int left,int right) {
		if(lazy_add[p]) {
			int mid = left + right >> 1;
			lazy_add[p<<1]   += lazy_add[p];
			lazy_add[p<<1|1] += lazy_add[p];			
			tree1[p<<1]       += lazy_add[p];
			tree1[p<<1|1]     += lazy_add[p];
			lazy_add[p] = 0;
		}
	}
	void in_build(int p,int left,int right,vector<int> &nums) {
		if(left == right) {
			tree1[p] = nums[left];
			tree2[p] = inf;
		} else {
			int mid = left + right >> 1;
			in_build(p<<1,left,mid,nums);
			in_build(p<<1|1,mid+1,right,nums);
			pushup(p);
		}
	}
	void update_add(int p,int left,int right,int ql,int qr,int val) {
		if(ql <= left && qr >= right) {
			tree1[p]    += val;
			lazy_add[p] += val;
		} else {
			pushdown(p,left,right);
			int mid = left + right >> 1;
			if(ql <= mid) update_add(p<<1,left,mid,ql,qr,val);
			if(qr > mid)  update_add(p<<1|1,mid+1,right,ql,qr,val);
			pushup(p);
		}
	}
	void update_change(int p,int left,int right,int ql,int qr,int val) {
        if (ql <= left && qr >= right) {
            swap(tree1[p], tree2[p]);
        } else {
            pushdown(p,left,right);
            int mid = left + right >> 1;
            if (ql <= mid) update_change(p<<1,left,mid,ql,qr,val);
            if (qr > mid)  update_change(p<<1|1,mid+1,right,ql,qr,val);
            pushup(p);
        }
    }
	int range_query(int p,int left,int right,int ql,int qr) {
		if(ql <= left && qr >= right) {
			return min(tree1[p], tree2[p]);
		}
		pushdown(p,left,right);
		int mid = left + right >> 1;
		int res = inf;
		if(ql <= mid) res = min(res, range_query(p<<1,left,mid,ql,qr));
		if(qr > mid)  res = min(res, range_query(p<<1|1,mid+1,right,ql,qr));
		return res;
	}
	void build(vector<int> &nums) {
		in_build(1,1,n,nums);
	}
	void add(int ql,int qr,int val) {
		update_add(1,1,n,ql,qr,val);
	}
	void change(int ql, int qr, int val) {
        update_change(1,1,n,ql,qr,val);
    }
	int query(int ql,int qr) {
		return range_query(1,1,n,ql,qr);
	}
};

int prime[]={2,3,5,7,11,13,17,19,23,29};

void solve()
{
	int n=read(),m=read();
	vector<SegmentTree> seg(10,SegmentTree(n));
	vector<int> a(n+1,0);
	for(int i=0;i<10;++i) {
		seg[i].build(a);
	}
	for(int i=1;i<=m;++i) {
		char opt[5];
		scanf("%s",&opt);
		if(opt[0]=='f') {
			int pos=read();
			for(int i=0;i<10;++i) {
				seg[i].change(pos,pos,0);
			}
		} else if(opt[0]=='m') {
			int l=read(),r=read(),x=read();
			for(int i=0;i<10;++i) {
				int cnt=0;
				while(x%prime[i]==0) {
					cnt++;
					x/=prime[i];
				}
				seg[i].add(l,r,cnt);
			}
		} else {
			int l=read(),r=read(),x=read();
			bool ok=true;
			vector<int> cnt(10,0);
			for(int i=0;i<10;++i) {
				while(x%prime[i]==0) {
					cnt[i]++;
					x/=prime[i];
				}
				if(seg[i].query(l,r)<cnt[i]) {
					ok=false;
				}
			}
			if(!ok) {
				puts("No");
			} else {
				puts("Yes");
				for(int i=0;i<10;++i) {
					seg[i].add(l,r,-cnt[i]);
				}
			}
		}
	} 
}


signed main()
{
	//fre(test);
	int T=1;
	while(T--) {
		solve();
		//fflush(stdout);
	}
	return 0;
}
```

{% endspoiler %}

## A. Skills

{% note info %}

题意：现有 $3$ 项技能，编号 $1,2,3$。初始每项技能的熟练度为 $0$。接下来有 $n$ 天，第 $i$ 天可以选择一项技能（假设是第 $j$ 项）进行练习，然后在这天结束时让这项技能的熟练度增加 $a_{i,j}$。同时，如果某一项技能（假设是第 $k$ 项）已经有 $x$ 天没有练习，那么在这天结束时，这项技能的熟练度会减少 $x$（不会减少到 $0$ 以下）。

问在第 $n$ 天结束后，这 $3$ 项技能的熟练度之和最大为多少。

$1\le n \le 1000$，$\forall\text{ } 1\le i\le n$，$1\le j \le 3$，$0\le a_{i,j} \le 10^4$。

{% endnote %}

{% note success %}

$\text{dp}$ 题。

首先要注意到最优解里面，一个技能如果开始学习了，那么中间过程熟练度不会降到 $0$ 以下。否则不如不学。

其次假如一个技能有 $t$ 天没有学习，那么将会损失 $1+2+\dots+t=\dfrac{t(t+1)}{2}$ 点熟练度。

也就是说一个技能如果开始学习了，不会停止学习超过 $2\sqrt W +O(1)$ 天，其中 $W=\max (a_{i,j})$。

令 $dp_{i,j,x,y}$ 代表到第 $i$ 天，在这天选择练习技能 $j$，其它两项技能分别有 $x$ 天和 $y$ 天没有练习了能带来的最大收益。每次转移从上一天练习的三种情况转移而来。

那么 $\text{ans}=\max(dp_{n,1\sim 3,0\sim W,0\sim W})$。

其中第一维可以滚动，总状态数不超过 $O(W^2)$。

时间复杂度 $O(nW^2)$。

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
#define ck(x) printf("check %lld\n",x);fflush(stdout)
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
const int N = 1005;
const int W = 205;
int arr[N][3];
int dp[2][3][W][W];

void solve()
{
	int n=read();
	for(int i=0;i<n;++i) {
		for(int j=0;j<3;++j) {
			arr[i][j]=read();
		}
	}
	memset(dp[0],-0x3f,sizeof dp[0]);
	dp[0][0][0][0]=arr[0][0];
	dp[0][1][0][0]=arr[0][1];
	dp[0][2][0][0]=arr[0][2];
	int lst=1,now=0;
	for(int a=1;a<n;++a) {
		lst^=1;now^=1;
		memset(dp[now],-0x3f,sizeof dp[now]);
		for(int b=0;b<3;++b) {
			for(int c=0;c<W;++c) {
				for(int d=0;d<W;++d) {
					int x=(!c) ? 0ll : c+1;
					int y=(!d) ? 0ll : d+1;
					dp[now][b][x][y]=max(dp[now][b][x][y],dp[lst][b][c][d]+arr[a][b]-x-y);
                    dp[now][(b+1)%3][y][1]=max(dp[now][(b+1)%3][y][1],dp[lst][b][c][d]+arr[a][(b+1)%3]-1-y);
                    dp[now][(b+2)%3][1][x]=max(dp[now][(b+2)%3][1][x],dp[lst][b][c][d]+arr[a][(b+2)%3]-1-x);
				}
			}
		}
	}
	int ans=0;
	for(int a=0;a<3;++a) {
		for(int b=0;b<W;++b) {
			for(int c=0;c<W;++c) {
				ans=max(ans,dp[now][a][b][c]);
			}
		}
	}
	printf("%lld\n",ans);
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
