---
title: "【NNSZCP2023】南宁三中第13届科技文化节程序设计竞赛 G,H,I"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/e72b221a2309d40cab8bfe1e4b265c00.jpeg"
tags:
  - XCPC
  - NNSZ
categories:
  - Competitive Programming
  - Other
excerpt: 很棒的参赛体验（指名次高 bushi）
abbrlink: 996d8e6
date: 2023-12-14 09:00:00
updated: 2023-12-14 09:00:00
---


[![](https://kisuraop.github.io/image/nnsz/1.jpg)](https://kisuraop.github.io/image/nnsz/1.jpg)

[![](https://kisuraop.github.io/image/nnsz/2.jpg)](https://kisuraop.github.io/image/nnsz/2.jpg)

## 闲话

比赛的前一天下午听[NNSZ捞王](https://www.luogu.com.cn/user/137242)说明天母校要办比赛，后面再打听说还是 $\text{IOI}$ 赛制，很快啊，马上就来捧场了。

明明才毕业不到半年，就已经要用“母校”称呼了，真是令人感慨。

比赛快开始的时候跟 $\text{hdm}$ 要了账号，感觉上次打 $\text{OI}$ 还是在不久前（实际已经退役一年半了），又感慨了一下。

赛题质量高得出乎意料，尤其是最后几题。我曾经也办过三场 $\text{Eden Round}$，知道每一道原创题背后的付出远比表面看上去要多，所以赛后还是很欣喜的。

题是好，但时间真的太仓促了，$\text{I}$ 题刚出了思路，比赛啪的一下就结束了，$\text{3h}$ 的时间感觉真对不起这些题。不过后来看了终榜才发现来比赛的基本都是初学者，那也怪不得。

赛时前半段状态不是很好，前 $6$ 题签了大概 $90\min$（主要 $\text{C}$ 题题意想岔了浪费了 $20$ 来分钟，$\text{D}$ 题又愣了一下才推出来）。后面一个半小时也只是做了两题，不过已经相当满意了。因为上次写换根 $\text{dp}$ 都不知道是几年前了，能调出来说明脑子还是稍微能动的。$\text{J}$ 题看了一眼就爆炸了，所以做完 $\text{H}$ 之后都在想 $\text{I}$。没注意到 $2$ 的幂次的奇偶性，还以为是一堆线段的容斥，把每种同余情况列成了一个表，感觉是 $\text{2-SAT}$ +线段树优化建图类物，赛后发现对了一半。$\text{GHI}$ 三题我都觉得很棒，就写了题解放在下面，加深一下印象。

希望能参加下一次，如果还能有的话）

我们 $01$ 社正在蒸蒸日上啊！（无贬义

## G. 排序算法

{% note info %}

题意：给定长为 $n$ 的序列 $a_i$。

判断以下算法是否能将 $a$ 排序为严格不下降序列。

若能，输出 `std::swap(a[i],a[j])` 的执行次数。


```cpp
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        if (a[i] < a[j]) 
            std::swap(a[i], a[j]);
```

$1\le n\le 2 \cdot 10^5$，$1\le a_i\le 10^9$。

{% endnote %}

{% note success %}

考察直观想象，样例那个 `5 4 3 2 1` 给的就很不错，手推一下就能发现性质。

首先算法一定是正确的，外层执行完 $i$ 时，$a_i$ 必定是 $i$ 前缀的最大值，且第一轮循环已经把序列最大值放到了 $a_1$，那么当 $j>i$ 时也不会出现 $a_i<a_j$ 的情况，即不会交换。

那么我们只需要计算 $i$ 前缀的贡献，不难发现这个值是前缀中比 $a_i$ 大的不同元素的个数。

用一个支持插入元素和查询大于某个元素的不同元素个数的数据结构维护：树状数组、线段树和平衡树都是不错的选择。

时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define ck(x) printf("check %lld\n",x);fflush(stdout);
#define die(x) puts(x);return ;
#define int long long
#define double long double
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

struct Fenwick {
	int n;
	vector<int> tr;
	Fenwick() {}
	Fenwick(int n) {init(n+1);}
	void init(int n){
		this->n = n;
		tr.assign(n+1,0);
	}
	void add(int pos,int x){
		while(pos<=n){
			tr[pos]+=x;
			pos+=pos&-pos;
		}
	}
	int sum(int pos){
		int res=0;
		while(pos){
			res+=tr[pos];
			pos-=pos&-pos;
		}
		return res;
	}
	int rangeSum(int l,int r){
		return sum(r)-sum(l-1);
	}
	int kth(int k){
		// tr[x] count the cnt of x
		int res=0,cnt=0;
		for(int i=20;i>=0;--i){
			res+=(1<<i);
			if(res>n || cnt+tr[res]>=k){
				res-=(1<<i);
			} else {
				cnt+=tr[res];
			}
		}
		return res+1;
	}
};
void solve()
{
	int n=read();
	vector<int> a(n+1),b(n+1);
	for(int i=1;i<=n;++i) {
		a[i]=read();
		b[i]=a[i];
	}
	sort(b.begin(),b.end());
	b.erase(unique(b.begin(),b.end()),b.end());
	map<int,int> pos;
	for(int i=1;i<b.size();++i) {
		pos[b[i]]=i;
	}
	int ans=0;
	for(int i=2;i<=n;++i) {
		if(a[i]>a[1]) {
			++ans;
			swap(a[i],a[1]);
		}
	}
	vector<int> vis(n+1);
	Fenwick fen(n+1);
	int tot=0;
	for(int i=1;i<=n;++i) {
		ans+=tot-fen.sum(pos[a[i]]);
		if(!vis[pos[a[i]]]) {
			vis[pos[a[i]]]=true;
			tot++;
			fen.add(pos[a[i]],1);
		}
	}
	puts("YES");
	printf("%lld\n",ans);

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

## H. 购买车券

{% note info %}

题意：给定一棵 $n$ 个点的无根树，每次删去一个叶子节点（指上一次操作后度数不大于 $1$ 的节点），直至删空。问合法的操作序列数。操作序列不同，当且仅当某一次删去的叶子节点不同。

$1\le n\le 2\cdot 10^5$。

{% endnote %}

{% note success %}

换根 $\text{dp}$。先计算一个根 $x$ 的结果（即 $x$ 最后才删的方案数）$dp_x$，再转移，答案就是 $\sum dp_x$。

第一遍 $\text{dfs}$，对于当前子树和其它子树的状态合并（即一段操作序列插到另一端操作序列中），其实就是一个多重集的排列：具体的，两段长分别为 $n,m$ 的序列相互插（元素互不相同），相当于 $n$ 个无区别球放入 $m$ 个有区别盒子且允许空盒，即能形成 $C_{m+n-1}^{n}$ 种序列（[参考this](https://kisuraop.github.io/posts/f9da5f78.html#j.-ihis-homework)）。

用 $sz_x$ 表示 $x$ 的子树大小，那么对于 $x$ 的一个儿子 $y$，这里 $n,m$ 就分别是 $sz_{y}$ 和 $sz_{x}-sz_y$，状态转移可以写成：
$$
dp_x=\prod\limits_{y\in son_x} \bigg[\binom{sz_x-1}{sz_y}dp_y\bigg]
$$

第二遍 $\text{dfs}$，考虑将根从 $x$ 转移到 $y$，此时序列 $n$ 中的一个节点跑到了 $m$ 中，即：
$$
sz_y\rightarrow sz_y-1
$$

$$
sz_x-sz_y\rightarrow sz_x-sz_y+1
$$

也可以根据 $C_{m+n-1}^{n}$ 的结构得知：底数 $m,n$ 一加一减抵消，贡献就从 $\binom{n-1}{sz_y}\rightarrow \binom{n-1}{sz_y-1}$。

那么转移可以写成：
$$
dp_y=dp_x\cdot\frac{\binom{n-1}{sz_y-1}}{\binom{n-1}{sz_y}}=dp_x\cdot\frac{sz_y}{n-sz_y}
$$

时间复杂度 $O(n)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define ck(x) printf("check %lld\n",x);fflush(stdout);
#define die(x) puts(x);return ;
#define int long long
#define double long double
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
mint C(mint n,mint m) {
	return binom.C(n.val(),m.val()); 
}

void solve()
{
	int n=read();
	vector<vector<int>> adj(n+1);
	for(int i=1;i<n;++i) {
		int x=read(),y=read();
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	vector<mint> sz(n+1),dp(n+1);
	auto dfs1 = [&](auto self,int x,int fath) -> void {
		sz[x]=1;
		dp[x]=1;
		for(auto y:adj[x]) {
			if(y!=fath) {
				self(self,y,x);
				dp[x]*=dp[y]*C(sz[x]+sz[y]-1,sz[y]);
				sz[x]+=sz[y];
			}
		}
	};
	dfs1(dfs1,1,0);
	auto dfs2 = [&](auto self,int x,int fath) -> void {
		for(auto y:adj[x]) {
			if(y!=fath) {
				dp[y]=dp[x]*C(n-1,sz[y]-1)/C(n-1,sz[y]);
				self(self,y,x);
			}
		}
	};
	dfs2(dfs2,1,0);
	printf("%lld\n",accumulate(dp.begin(),dp.end(),(mint)0));
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

## I. 花卉培育

{% note info %}

题意：构造序列 $\{a_i\}$ 使其同时满足 $q$ 个限制。

其中第 $j\in[1,q]$ 个限制形如 $\bigg(\prod\limits_{i=l_j}^{r_j}a_i\bigg)\equiv v_j\pmod{3}$ .

$1\le n,q \le 3\cdot 10^5$，$0\le a_i \le 10^9$。

{% endnote %}

{% note success %}

首先，在模 $3$ 意义下，$0\le a_i\le 10^9$ 等价于 $0\le a_i \le 2$。

那么我们只需考量 $a_i=0/1/2$ 时在序列中的性质：

若 $a_i=0$，那么所有含 $a_i$ 的区间乘积都是 $0$。因此在每个 $v_j\neq 0$ 的区间中不能含有 $0$。

再考虑 $v_j=0$ 的限制，$a_i=1$ 对乘积没有任何影响，对于 $a_i=2$ 则有一个经典结论：
$$
\begin{cases}3|(2^n+1)\ ,n\textbf{ 为奇数}\\3|(2^n-1)\ ,n\textbf{ 为偶数}\end{cases}\quad\Longrightarrow\quad 2^k \bmod{3} = \begin{cases}2\ ,k\textbf{ 为奇数}\\1\ ,k\textbf{ 为偶数}\end{cases}
$$

{% endnote %}

{% spoiler 证明? %}

当 $n$ 为偶数时，令 $n=2k$，则：
$$
\begin{align}\quad2^{2k}-1&=4^k-1\\&=(3+1)^k-1\\&=3^k+\tbinom{k}{1}3^{k-1}+\tbinom{k}{2}3^{k-2}+\dots+1-1\\&\equiv1-1\pmod{3}\\&\equiv 0 \pmod{3}\end{align}
$$

当 $n$ 为奇数时，令 $n=2k+1$，则：
$$
\begin{align}2^{2k+1}+1&=2\cdot{2^{2k}+1}\\&=2\cdot (3+1)^{k}+1\\&=2(3^k+\tbinom{k}{1}3^{k-1}+\tbinom{k}{2}3^{k-2}+\dots+1)+1\\&\equiv 2\cdot1+1\pmod{3}\\&\equiv 0 \pmod{3}\end{align}
$$

证毕。

{% endspoiler %}

{% note success %}

这能带来两个巧思：
1. 若干个 $1,2$ 相乘不会出现 $3$ 的倍数，意味着满足限制 $v_j=0$ 的充要条件是 $[l_j,r_j]$ 间有 $0$。即若有 $v_j=0$ 的区间完全包含在 $v_j\neq0$ 的区间的并中，无解。

2. 有解情形下，只要每个限制区间 $2$ 的个数的奇偶性满足条件，通过用 $1$ 补齐的方式一定能构造出可行解。

那么问题转化为是否能有一种构造方案使得每个限制区间中 $2$ 的个数的奇偶性满足要求。

妙手：记 $a_i=2$ 的位置 $i$ 有 $x_i=1$，那么对于 $[l,r]$，有如下等价形式：
$$
x_l\oplus x_{l+1}\oplus \dots\oplus x_{r-1}\oplus x_{r}=\begin{cases}0\ ,[l,r]\textbf{ 中有偶数个 }2\\1\ ,[l,r]\textbf{ 中有奇数个 }2\end{cases} \ =s_{l-1}\oplus s_r
$$

其中 $s_i$ 是 $x_i$ 的前缀异或和。

换言之，对于一个限制条件，可以转化为两个单点的异或，进而转化为如下二元按位关系：
$$
\begin{align}s_{l-1} \oplus s_r=1 \rightarrow (s_{l-1}\lor s_r)\land(\neg s_{l-1} \lor \neg s_r)\\s_{l-1} \oplus s_r=0 \rightarrow (s_{l-1}\lor \neg s_r)\land(\neg s_{l-1} \lor s_r)\end{align}
$$

用 $\small\text{2-SAT}$ 求解，时间复杂度 $O(n+q)$。

{% endnote %}

{% spoiler Code %}


```cpp
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout)
#define ck(x) printf("check %lld\n",x);fflush(stdout);
#define die(x) puts(x);return ;
#define int long long
#define double long double
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


struct TwoSet {
	int n;
	vector<vector<int>> adj;
	vector<int> ans;
	TwoSet(int n) {
		this->n = n;
		adj.resize(2*n+1);
		ans.resize(n+1);
	}
	void addbind(int x,bool ok1,int y,bool ok2) {
		adj[x+n*(!ok1)].push_back(y+n*ok2);
		adj[y+n*(!ok2)].push_back(x+n*ok1);
	}
	bool work() {
		vector<int> dfn(2*n+1),low(2*n+1),stack_(2*n+1),c(2*n+1);
		vector<bool> vis(2*n+1,false);
		vector<vector<int>> scc(2*n+1);
		int tim=0,top=0,cnt=0;
		function<void(int)> tarjan = [&](int x) {
			dfn[x]=low[x]=++tim;
			vis[x]=true;
			stack_[++top]=x;
			for(auto y:adj[x]) {
				if(!dfn[y]) {
					tarjan(y);
					low[x]=min(low[x],low[y]);
				} else if(vis[y]) {
					low[x]=min(low[x],dfn[y]);
				}
			}
			if(dfn[x]==low[x]) {
				int now;++cnt;
				do{
					now=stack_[top--];
					vis[now]=false;
					c[now]=cnt;
					scc[cnt].push_back(now);
				}while(x!=now);
			}
		};
		for(int i=1;i<=2*n;++i) {
			if(!dfn[i]) tarjan(i);
		}
		for(int i=1;i<=n;++i) {
			if(c[i]==c[i+n]) return false;
			ans[i]=c[i]>c[i+n]?1ll:0ll;
		}
		return true;
	}
	vector<int> getans() {
		return ans;
	}
};


void solve()
{
	int n=read(),q=read();
	#define FAIL while(n--) printf("-1 ");return ;

	TwoSet ts(n+1);
	vector<int> sum(n+2);
	vector<array<int,3>> arr0;
	for(int i=1;i<=q;++i) {
		int l=read(),r=read(),x=read();
		if(x==0) {
			arr0.push_back({l,r+1,x});
		} else {
			sum[l]++;sum[r+1]--;
			if(x==1) {
				ts.addbind(l,0,r+1,1); 
				ts.addbind(l,1,r+1,0); 
			} else {
				ts.addbind(l,0,r+1,0);
				ts.addbind(l,1,r+1,1);
			}
		}
	}

	for(int i=1;i<=n+1;++i) {
		sum[i]+=sum[i-1];
	}
	sum.insert(sum.begin(),0);
	sum.pop_back();
	for(auto &i:sum) {
		i=(bool)i;
	}
	for(int i=1;i<=n+1;++i) {
		sum[i]+=sum[i-1];
	}
	for(auto [l,r,x]:arr0) {
		if(sum[r]-sum[l]==r-l) {
			FAIL;
		}
	}

	if(!ts.work()) {
		FAIL;
	}
	for(int i=1;i<=n;++i) {
		if(sum[i]!=sum[i+1]) {
			ts.ans[i]==ts.ans[i+1] ? printf("1 ") : printf("2 "); 
		} else {
			printf("0 ");
		}
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
