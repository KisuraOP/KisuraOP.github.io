---
title: 【题解】2025 UESTC 寒假集训
sticky: 100
math: true
index_img: 'https://pic.rmb.bdstatic.com/bjh/63d94834e52e197d0b75e830621ae8e3.jpeg'
tags:
  - XCPC
  - UESTC
categories:
  - Competitive Programming
  - Other
excerpt: 终于又见到大家了。
abbrlink: 1e7fc2bd
date: 2025-02-17 23:35:35
updated: 2025-02-17 23:35:35
---

奇怪，怎么来训的人这么少。

这期间晚上打的 CF 包含在这里面了 $\to$ [Link](https://kisuraop.github.io/posts/abc8fb81.html)。虽然大概率还没来得及补。

训了一个寒假还是希望自己能有一点长进的，虽然现在还看不到...甚至写下这段话的时候 CF 还掉了大分。

## 【2.15】Day 1

[Virtual Judge Link](https://vjudge.net/contest/693557)

尽力了，E、F 我评估了一下已经远超我目前的 dp 水平。那就没题可补了。

菜猫你怎么这么坏。

## 【2.16】Day 2

[Virtual Judge Link](https://vjudge.net/contest/693898)

dp 还在追着我跑QAQ。

{% note info %}

[E. Power Up](https://atcoder.jp/contests/arc160/tasks/arc160_c?lang=en)

题意：给定 $n$ 个元素的可重集，你可以选择出现次数 $\ge 2$ 的 $x$，删除两个 $x$ 然后插入一个 $x+1$。你可以执行任意多次，问能得到多少种不同的集合。对 998244353 取模。

$1 \le n,a_i \le 2\cdot 10^5$。

{% endnote %}

{% note success %}

考虑从小到大合并，

设 $dp[i][j]$ 表示已经将 $< i$ 的数合并，合并后有 $j$ 个 $i$ 的方案数。

设 $cnt[i]$ 表示集合中原始 $i$ 的个数，则有转移：
$$
dp[i][j +cnt[i]]=\sum_{k=j\times2}^{\inf}dp[i-1][k]
$$
对于相同的 $j$，可以用一个后缀和 $O(1)$ 转移，并用 `std::map` 只保留有用的状态。此时状态数就是枚举的 $j$ 的总和，由于每次合并都能将出现次数减半，可以预见 $j$ 的总和不会很大。实际能证明状态数接近线性。

时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------


constexpr int W = 2e5 + 100;
constexpr int mod = 998244353;

void solve() {
	int n;
	cin >> n;
	vector<int> a(n + 1), cnt(W + 1);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		cnt[a[i]]++;
	}
	map<int, vector<array<int, 2>>> dp;
	dp[0].push_back({0, 1});
	for (int i = 1; i <= W; i++) {
		int num = (*dp[i - 1].rbegin())[0];
		vector<int> f(num + 1);
		for (auto [x, y] : dp[i - 1]) {
			f[x] = y;
		}
		for (int j = num - 1; j >= 0; j--) {
			f[j] += f[j + 1];
			f[j] %= mod;
		}
		for (int j = 0; j <= num / 2; j++) {
			dp[i].push_back({j + cnt[i], f[j * 2]});
		}
	}
	int ans = 0;
	for (auto [x, y] : dp[W]) {
		ans = (ans + y) % mod;
	}
	cout << ans << "\n";
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[F. Wish List](https://atcoder.jp/contests/abc288/tasks/abc288_e?lang=en)

题意：有 $N$ 件商品，第 $i$ 件价格 $A_i$，你需要其中的 $M$ 件，编号分别为 $X_1,X_2,\cdots,X_M$。每次购买某个商品 $i$ 时，若其在所有未买商品中编号第 $j$ 小，就要付 $A_i+C_j$ 的钱。求买到这 $M$ 件物品最少需要多少钱。（可以买不想要的商品）

$1 \le M \le N\le 5000$，$1 \le A_i,C_i \le 10^9$。 

{% endnote %}

{% note success %}

令 $dp[i][j]$ 表示前 $i$ 件商品中买了 $j$ 件所需的最少钱数。

- 若不买第 $i$ 件商品，则 $dp[i][j]=dp[i-1][j]$。
- 若买第 $i$ 件商品，考虑到此时第 $i$ 件在所有未买商品中的顺序最小是第 $i-j+1$ 件，最大是第 $i$ 件，并且可以通过调整购买顺序使得该商品位次恰好对应 $C[i-j+1\sim i]$ 中的最小值时买下。故有 $dp[i][j]=dp[i-1][j-1]+\min\limits_{k=i-j+1}^{i}C[k]+A[i]$。

当然若第 $i$ 件商品在必须要买的 $M$ 件之中，就不考虑第一种情况。

时间复杂度 $O(n^2)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff

struct SparseTable {
	int n;
	vector<vector<int>> ST;
	SparseTable(vector<int> &arr) {
		this->n = arr.size() - 1;
		ST.resize(n + 1 ,vector<int>(__lg(n) + 1));
		for (int i = 1; i <= n; i++) {
			ST[i][0] = arr[i];
		}
		for (int j = 1; j <= __lg(n); j++) {
			for (int i = 1; i + (1LL << j) - 1 <= n; i++) {
				ST[i][j] = min(ST[i][j - 1], ST[i + (1LL << (j - 1))][j - 1]);
			}
		}
	}
	int query(int l, int r) {
		int len = __lg(r - l + 1);
		return min(ST[l][len], ST[r - (1LL << len) + 1][len]);
	}
};


//-------------- templates above --------------


void solve() {
	int n, m;
	cin >> n >> m;
	vector<int> a(n + 1), c(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	for (int i = 1; i <= n; i++) {
		cin >> c[i];
	}
	vector<int> need(n + 1);
	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		need[x] = true;
	}
	SparseTable st(c);
	vector dp(n + 1, vector<int>(n + 1, inf));
	dp[0][0] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j >= 1) {
				dp[i][j] = dp[i - 1][j - 1] + st.query(i - j + 1, i) + a[i];
			}
			if (need[i] == 0) {
				dp[i][j] = min(dp[i][j], dp[i - 1][j]);
			}
		}
	}
	int ans = *min_element(dp[n].begin(), dp[n].end());
	cout << ans << "\n";
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[G. Integer Division](https://atcoder.jp/contests/abc288/tasks/abc288_f)

题意：给定一个 $N$ 位数 $X$，可以把 $X$ 分成若干段（或不分割），得分为将每一段数值的乘积。求所有分割方法的得分之和，对 998244353 取模。

$2 \le N \le 2\cdot 10^5$。

{% endnote %}

{% note success %}

令 $dp[i]$ 表示只考虑前 $i$ 位时答案，$s(l, r)$ 表示区间 $[l, r]$ 构成的十进制整数数值，则：
$$
\begin{align}
dp[i] &= \sum_{j=0}^{i-1}dp[j]\cdot s(j+1,i)\\
&=\sum_{j=0}^{i-1}dp[j]\cdot(10\cdot s(j+1,i-1)+X[i])\\
&=10 \sum_{j=0}^{i-2}dp[j]\cdot s(j+1,i-1)+\sum_{j=0}^{i-1}dp[j]\cdot X[i]\\
&=10\cdot dp[i-1]+\sum_{j=0}^{i-1}dp[j]\cdot X[i]
\end{align}
$$
中间求和上标替换成 $i-2$ 是因为 $s(i,i-1)$ 没有意义。

时间复杂度 $O(n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------

constexpr int mod = 998244353;

void solve() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	s = " " + s;

	vector<int> dp(n + 1);
	dp[0] = 1;
	dp[1] = s[1] - '0';
	int sum = dp[0] + dp[1];
	for (int i = 2; i <= n; i++) {
		dp[i] = (10 * dp[i - 1] + sum * (s[i] - '0')) % mod;
		sum = (sum + dp[i]) % mod;
	}
	cout << dp[n] << "\n";
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[H. Mahjong](https://atcoder.jp/contests/arc160/tasks/arc160_d?lang=en)

题意：称一个序列 $\{b\}$ 是好的当且仅当 $\sum b_i=m$ 且可以通过任意次以下两种操作使得 $\{b\}$ 全为 $0$。

- 选一个元素减 $k$。
- 选一个长为 $k$ 的连续段每个元素减 $1$。

问有多少个长为 $n$ 的非负整数序列 $\{a\}$ 是好的，对 998244353 取模。

$1 \le k\le n\le 2000$，$1\le m\le 10^{18}$。

{% endnote %}

{% note success %}

计数 $\{a\}$ 即考虑初始一个全为 $0$ 的序列，通过那两种操作能变成哪些。

首先两种操作每次对总和的贡献都是 $k$，若 $k\nmid m$，一定无解。否则两种操作的次数加起来一定是 $\frac{m}{k}$。

注意到选同一个长为 $k$ 的段进行操作 $2$，反复进行 $k$ 次，等同于对每个位置都进行一次操作 $1$。为了计数不重复，钦定对于同一个段，操作 $2$ 最多进行 $k-1$ 次。

用一个长为 $2n-k+1$ 的序列 $\{c\}$ 来表示一种操作序列：

- $c_1\sim c_{n-k+1}$ 这 $n-k+1$ 个数代表了那 $n-k+1$ 个长为 $k$ 的连续段分别进行了多少次操作 $2$。
- $c_{n-k+2}\sim c_{2n-k+1}$ 这 $n$ 个数代表了每个位置分别进行了多少次操作 $1$。

此时，原问题等价为有多少个长为 $2n-k+1$ 的非负整数序列 $\{c\}$ 满足：

- $\forall i\in [1,n-k+1]$，$c_i<k$。
- $\sum\limits_{i=1}^{2n-k+1}c_i=\dfrac{m}{k}$。

运用容斥和插板法，答案是：
$$
\sum_{t=0}^{n-k+1}(-1)^{t}\binom{n-k+1}{t}\binom{\frac{m}{k}-tk+2n-k}{2n-k}
$$
文末有详细的推导。

时间复杂度 $O(n^2)$。

{% endnote %}

{% spoiler Code %}

```c++
void solve() {
	int n, m, k;
	cin >> n >> m >> k;
	if (m % k) {
		cout << 0 << "\n";
		return ;
	}
	mint s = 0;
	for (int t = 0; t <= n - k + 1; t++) {
		s += (t & 1 ? -1 : 1) * C(n - k + 1, t) * bfC(m / k - t * k + 2 * n - k, 2 * n - k);
	}
	cout << s << "\n";
}
```

{% endspoiler %}

{% note primary %}

给定 $n,m,k,s$，有多少个长为 $n$ 的数列 $\{a\}$ 满足以下要求？

- $\forall i\in [1,n]$，$a_i \ge 0$。
- $\forall i\in[1,m]$，$a_i \le k$。
- $\sum\limits_{i=1}^{n} a_i=s$。

若不考虑条件 $2$，解的数目可以通过经典的隔板法得到：
$$
\binom{s+n-1}{n-1}
$$
即将总和为 $s$ 看成 $s$ 个 $1$，在这 $s$ 个 $1$ 中间插 $n-1$ 个板，分成的 $n$ 个部分每个部分的和对应一个非负整数。

考虑条件 $2$，对每个 $i\in[1,m]$ 的 $a_i$，定义事件 $P_i$："$a_i>k$"。

那么，根据容斥原理：
$$
\begin{align}
\textbf{不违反任何 } P_i \textbf{ 的解数}&= \textbf{总情况数}\\
&-\sum \textbf{违反至少一个 } P_i \textbf{ 的情况数} \\
&+\sum \textbf{违反至少两个 } P_i \textbf{ 的情况数} \\
&- \cdots
\end{align}
$$
我们枚举 $t$，代表违反的约束的个数，那么答案是：
$$
\sum_{t=0}^{m}(-1)^{t}\binom{m}{t}\cdot[\textbf{违反了至少 }t\textbf{ 个 }P_i \textbf{ 的情况数}]
$$
其中 $\binom{m}{t}$ 代表从前 $m$ 个位置中选 $t$ 个位置，钦定这 $t$ 个位置上的数**一定** $>k$。

也就是说，这 $t$ 个位置上的数的合法取值变成了 $[k+1,*]$，而其它位置上的数的合法取值为 $[0,*]$，这等价于将总和 $s$ 替换成 $s'=s-t(k+1)$。

于是，问题转化为有多少个长为 $n$ 的非负整数序列和为 $s-t(k+1)$，根据前文提到的隔板法，答案是：
$$
\binom{s-t(k+1)+n-1}{n-1}
$$
代回容斥后的式子，即得：
$$
ans=\sum_{t=0}^{m}(-1)^{t}\binom{m}{t}\binom{s-t(k+1)+n-1}{n-1}
$$


{% endnote %}

---

{% note info %}

[J. Make Biconnected](https://atcoder.jp/contests/arc160/tasks/arc160_e?lang=en)

题意：给定一棵 $n$ 个点的树，点有点权 $w_i$，且每个点度数至多为 $3$。你可以在树上加边，加一条连接 $i,j$ 的边耗费 $w_i+w_j$。求将这棵树变成点双连通图的最小花费。

$3 \le n \le 2\cdot 10^5$，$1 \le w_i \le 10^9$。

{% endnote %}

{% note success %}

首先优先连叶子肯定不劣。假设我们给这个树选定了一个根，两个叶子能连起来当且仅当它们在这个根的不同的子树中。令这棵树有 $k$ 个叶子：

- 若 $k$ 为偶数，可以证明一定存在一个根使得这这 $k$ 个叶子能够用 $\frac{k}{2}$ 条边两两连接。这个根只需满足叶子最多的子树的叶子个数不超过 $\frac{k}{2}$，可以用反证法证明。

当然我们并不用真的求出这个根：既然一定存在，设这 $k$ 个叶子 dfs 序跑出来的编号为 $d_1,d_2,\cdots d_k$，那么 $d_i$ 连 $d_{(i+\frac{k}{2}) \bmod k\ +1}$ 就是最优的。

- 若 $k$ 为奇数，考虑枚举多出来的那个叶子 $x$，然后剩下的按偶数的方法两两连接。 设 $x$ 往上跳到的第一个三度点是 $y$，那么断言 $x$ 可以和除了 $x\to y$ 路径上的点之外的所有点连边，我们只用挑权值最小的连即可。

tip：dfs 时可以选择一个三度点为根，这样 $x$ 向根的方向一定能跳到一个三度点。

时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------


void solve() {
	int n;
	cin >> n;
	vector<int> w(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> w[i];
	}
	vector<vector<int>> adj(n + 1);
	for (int i = 1; i < n; i++) {
		int x, y;
		cin >> x >> y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	vector<int> is3(n + 1);
	int rt = -1;
	for (int i = 1; i <= n; i++) {
		if (adj[i].size() == 3) {
			is3[i] = true;
			rt = i;
		}
	}
	if (rt == -1) {
		vector<int> ex;
		for (int i = 1; i <= n; i++) {
			if (adj[i].size() == 1) {
				ex.push_back(i);
			}
		}
		cout << "1\n" << ex[0] << " " << ex[1] << "\n";
		return ;
	}

	vector<int> leaf;
	vector<int> f(n + 1);
	auto dfs = [&] (auto self, int x, int fa) -> void {
		f[x] = fa;
		if (adj[x].size() == 1) {
			leaf.push_back(x);
		}
		for (auto y : adj[x]) {
			if (y == fa) {
				continue;
			}
			self(self, y, x);
		}
	}; 
	dfs(dfs, rt, 0);

	int cnt = leaf.size();
	if (cnt % 2 == 0) {
		cout << cnt / 2 << "\n";
		for (int i = 0; i + cnt / 2 < cnt; i++) {
			cout << leaf[i] << " " << leaf[i + cnt / 2] << "\n";
		}
		return ;
	}

	set<array<int, 2>> s;
	for (int i = 1; i <= n; i++) {
		s.insert({w[i], i});
	}
	vector<array<int, 3>> res;
	for (int i = 0; i < cnt; i++) {
		int x = leaf[i];
		vector<array<int, 2>> tmp;
		while (x != 0) {
			s.extract({w[x], x});
			tmp.push_back({w[x], x});
			if (is3[x]) {
				break;
			}
			x = f[x];
		}

		auto [val, anoid] = *s.begin();
		res.push_back({val, anoid, i});

		for (auto x : tmp) {
			s.insert(x);
		}
	}
	sort(res.begin(), res.end());
	auto [_, anoid, mnid] = res[0];

	vector<int> fir, sec;
	array<int, 2> spe;
	for (int i = 0; i < cnt; i++) {
		if (i == mnid) {
			spe = {leaf[i], anoid};
		} else {
			if (fir.size() < cnt / 2) {
				fir.push_back(leaf[i]);
			} else {
				sec.push_back(leaf[i]);
			}
		}
	}

	cout << cnt / 2 + 1 << "\n";
	for (int i = 0; i < fir.size(); i++) {
		cout << fir[i] << " " << sec[i] << "\n";
	}
	cout << spe[0] << " " << spe[1] << "\n";
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

## 【2.17】 Day 3

[Virtual Judge Link](https://vjudge.net/contest/694161)

红了，D 一直 wa，拍完才发现没想清楚。

{% note info %}

[D. Completely Searching for Inversions](https://vjudge.net/problem/CodeForces-1866C)

题意：给一个 $n$ 个点的有向无环图，边权为 $0/1$，且从 $1$ 可以到达任意点。从 $1$ 开始跑一个不带 `vis` 的 dfs，并将沿途边权记录下来，形成一个二进制串。求这个串的逆序对个数，对 998244353 取模。

$2 \le n \le 10^5$。 

{% endnote %}

{% note success %}

将边权为 $0/1$ 的边称为 $0/1$ 边。

先跑一遍正常的 dfs，回溯时统计答案。当我们从终点向前加一个点时，形成的新贡献是从 $1$ 开始 dfs 到这个点的路上经过的 $1$ 边数量乘上这个点后面 $0$ 边的数量。至于这个点后面的 $1$ 边对后面的 $0$ 边造成的贡献，已经包含在后面的答案里了。

令 $pre1[x]$ 表示从 $1$ 开始 dfs 到 $x$ 经过的 $1$ 边的数量，$suf0[x]$ 表示从 $x$ 到 dfs 末尾这一段经过的 $0$ 边的数量，$f[x]$ 表示 $x$ 向后形成的闭合子图的答案，则：
$$
f[x]=\sum_{x\to y} (f[y]+pre1[x]\cdot suf0[y])
$$
时间复杂度 $O(n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------


constexpr int mod = 998244353;


void solve() {
	int n;
	cin >> n;
	vector<vector<array<int, 2>>> adj(n + 1);
	for (int i = 1; i <= n; i++) {
		int num;
		cin >> num;
		for (int j = 0; j < num; j++) {
			int y, w;
			cin >> y >> w;
			adj[i].push_back({y, w});
		}
	}
	int ans = 0;
	vector<int> vis(n + 1);
	vector<int> pre1(n + 1), suf0(n + 1), f(n + 1);
	auto dfs = [&] (auto self, int x) -> void {
		vis[x] = 1;
		for (auto [y, w] : adj[x]) {
			if (w == 0) {
				suf0[x]++;
				f[x] += pre1[x]; 
				f[x] %= mod;
			} else {
				pre1[x]++;
			}
			if (!vis[y]) {
				self(self, y);
			}
			f[x] += f[y];
			f[x] %= mod;

			f[x] += pre1[x] * suf0[y] % mod;
			f[x] %= mod;

			pre1[x] += pre1[y];
			pre1[x] %= mod;

			suf0[x] += suf0[y];
			suf0[x] %= mod;
		}
	};
	dfs(dfs, 1);
	cout << f[1] << "\n";
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[G. GCD Queries](https://vjudge.net/problem/CodeForces-1762D)

题意：交互题，给定一个 $0\sim n-1$ 的排列，你需要通过不超过 $2n$ 次询问找到两个下标 $x$ 和 $y$ 满足 $p_x=0$ 或 $p_y=0$。每次询问你可以问两个下标 $i,j$，交互器返回 $\gcd(p_i,p_j)$。

$2 \le n \le 2 \cdot 10^4$。

{% endnote %}

{% note success %}

题目的要求暗示了 $0$ 的位置是不能确定的，只能是排除到只剩两个位置。考虑三个不同的位置 $i,j,k$，令 $A=\text{query}(i,k)=\gcd(i,k)$，$B=\text{query(j,k)}=\gcd(j,k)$。$A,B$ 间只能是以下三种关系：

- $A=B$。此时能断言 $p_k\neq0$，因为 $p_i\neq p_j$。
- $A<B$。此时能断言 $p_i\neq 0$，因为 $\gcd(p_k,0)=p_k>\gcd(p_k,x),x>0$。
- $A>B$。此时能断言 $p_j\neq 0$，原因同上。

如此一来，我们每次选三个还不确定是不是 $0$ 的下标问两次就能排除一个，排除 $n-2$ 次即可。总共用了 $2(n-2)=2n-4$ 次询问。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------


int query(int i, int j) {
	cout << "? " << i << " " << j << endl;
	int x;
	cin >> x;
	return x;
}

void solve() {
	int n;
	cin >> n;
	set<int> s;
	for (int i = 1; i <= n; i++) {
		s.insert(i);
	}
	while (s.size() > 2) {
		int x = *s.begin();
		s.erase(s.begin());
		int y = *s.begin();
		s.erase(s.begin());
		int z = *s.begin();
		s.erase(s.begin());
		int res1 = query(x, z);
		int res2 = query(y, z);
		if (res1 == res2) {
			s.insert(x);
			s.insert(y);
		} else if (res1 < res2) {
			s.insert(y);
			s.insert(z);
		} else {
			s.insert(x);
			s.insert(z);
		}
	}
	int x = *s.begin();
	s.erase(s.begin());
	int y = *s.begin();
	cout << "! " << x << " " << y << endl;
	int z;
	cin >> z;
}


signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[H. Lost Array](https://vjudge.net/problem/CodeForces-1534E)

题意：交互题，给定 $n,k$，有一个长为 $n$ 的未知序列 $\{a\}$，你需要通过最少次数的询问找出 $\oplus_{i=1}^{n}a_i$。每次你可以询问一个长为 $k$ 的子序列的异或和。

$1\le k\le n\le 500$，$1\le a_i \le 10^9$。 

{% endnote %}

{% note success %}

如果一个下标被选中了两次，那么相当于没问过这个下标。也就是说每个位置都只有被问过和没被问过两种状态。

令 $f_i$ 表示 "知道了 $i$ 个位置的异或和" 这个状态，则连边：

- $\forall i\in[0,n-k]$，$f_i\to f_{i+k}$。
- $\forall i\in [1,n]$，$\forall j\in[k-(n-i),\min(i,k)]$，$f_i\to f_{i+k-2j}$。

第一种连边好理解：如果还有 $k$ 个位置没问，那就问。

第二种连边枚举了需要把 $j$ 个已经问过的下标更新为 "没问过"，不仅失去了 $j$ 个已知的点，也只剩 $k-j$ 次去问其它未知点，故为 $f_{i+k-2j}$。

题目要求询问次数最少，跑 $f_0$ 到 $f_n$ 的最短路（或 bfs）即可。若到达不了 $f_n$ 就是 $-1$，否则记下途径的点用于构造方案。

时间复杂度 $O(n^2)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff


//-------------- templates above --------------


int query(vector<int> &a) {
	cout << "? ";
	for (auto x : a) {
		cout << x << " ";
	}
	cout << endl;
	int x;
	cin >> x;
	return x;
}


void solve() {
	int n, k;
	cin >> n >> k;
	vector<vector<int>> adj(n + 1);
	for (int i = 0; i + k <= n; i++) {
		adj[i].push_back(i + k);
	}
	for (int i = 1; i <= n; i++) {
		for (int j = max(1ll, k - (n - i)); j <= min(i, k); j++) {
			int x = i + k - 2 * j;
			if (x >= 0 && x <= n) {
				adj[i].push_back(x);
			}
		}
	}
	vector<int> vis(n + 1), pre(n + 1, -1);
	queue<int> q;
	q.push(0);
	vis[0] = 1;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		if (x == n) {
			break;
		}
		for (auto y : adj[x]) {
			if (!vis[y]) {
				vis[y] = 1;
				pre[y] = x;
				q.push(y);
			}
		}
	}
	vector<int> path;
	for (int i = n; i != 0; i = pre[i]) {
		if (i == -1) {
			cout << -1 << endl;
			return ;
		}
		path.push_back(i);
	}
	reverse(path.begin(), path.end());

	vis.assign(n + 1, 0);
	int cur = 0, ans = 0;
	for (auto x : path) {
		int back_cover = (cur + k - x) / 2;
		int cover = k - back_cover;
		vector<int> a;

		for (int i = 1, A = 0, B = 0; i <= n; i++) {
			if (!vis[i] && A < cover) {
				vis[i] = 1;
				a.push_back(i);
				A++;
			} else if (vis[i] && B < back_cover) {
				vis[i] = 0;
				a.push_back(i);
				B++;
			}
		}

		assert(a.size() == k);
		ans ^= query(a);
		cur = x;
	}
	cout << "! " << ans << endl;
}


signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[J. Cactus to Tree](https://vjudge.net/problem/CodeForces-980F)

题意：给定一个 $n$ 个点 $m$ 条边的连通无向图。对每个 $i\in[1,n]$，求若以最佳方式断边使得图变成树，$\max\limits_{u\in leaf} dis(i,u)$ 最小是多少。

$1 \le n \le 5\cdot 10^5$。

{% endnote %}

{% note success %}

考虑一个点 $x$，以 $x$ 为根建出 bfs 生成树，生成树上的边就是要保留的边。换句话说，题意等同于对每个点 $i$，求 $i$ 到其它所有点最短距离的最大值。

我们任选一个环，钦定他为整个图的 "根"。同样约定 $x$ 在 $y$ 的子树中当且仅当 $y$ 在从根到 $x$ 的路径上。

定义 $F[x]=\max\limits_{y}dis(x,y)$，其中 $y$ 在 $x$ 的子树内。对于根来说，我们从根的每个点出发向子树内 bfs，可以 $O(n)$ 得到根上每个点的 $F[x]$。

令 $Cir[x]$ 代表 $x$ 所在的环，特别地，单点看作一个环。定义 $G[x]$ 代表从 $x$ 出发向 $Cir[x]$ 方向延伸出的最长距离，那么：
$$
G[u]=\max_{v\in Cir[u]}(dis(u,v)+F[v])
$$
这是一个典型的使用单调队列解决的式子。具体地，拆环成链，单调队列维护最大的 $F[i]-i$，窗口大小不超过 $\frac{1}{2}$ 环长，顺时针逆时针扫两遍。

现在，在知道一个环所有 $F[x]$ 的情况下，可以线性求出 $G[x]$。而对于每个点 $x$，答案就是 $\max(F[x],G[x])$。于是问题转化为如何把 $F$ 从根转移到图上的其它点。

这依然是典型的换根问题，每次转移时的 $\text{UpValue}$ 选择非该当前子树的最大深度，并与当前点的 $G$ 取 $\max$。

时间复杂度 $O(n)$。实现时有若干细节等待你的探索（

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}

template <typename T>
inline void hash_combine(size_t &seed, const T &val) {
    seed ^= hash<T>()(val) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

template <typename T> inline void hash_val(size_t &seed, const T &val) {
    hash_combine(seed, val);
}

template <typename T, typename... Types>
inline void hash_val(size_t &seed, const T &val, const Types &... args) {
    hash_combine(seed, val);
    hash_val(seed, args...);
}

template <typename... Types>
inline size_t hash_val(const Types &... args) {
    size_t seed = 0;
    hash_val(seed, args...);
    return seed;
}

struct custom_hash {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2> &p) const {
        return hash_val(p.first, p.second);
    }
};

unordered_set<pair<int, int>, custom_hash> E;
struct EBCC {
	int n;
	vector<vector<int>> adj;
	vector<int> dfn, low, stk, c;
	int tim, top, cnt;
	EBCC(vector<vector<int>> Adj) : n(Adj.size() - 1), 
	adj(Adj), dfn(n + 1), low(n + 1), stk(n + 1), c(n + 1) {
		tim = top = cnt = 0;
	}
	void tarjan(int x, int par) {
		dfn[x] = low[x] = ++tim;
		stk[++top] = x;
		for (auto y : adj[x]) {
			if (y == par) {
				continue;
			}
			if (!dfn[y]) {
				tarjan(y, x);
				low[x] = min(low[x], low[y]);
				if (low[y] > dfn[x]) {
					E.insert({x, y});
					E.insert({y, x});
				}
			} else if (!c[y] && dfn[y] < dfn[x]) {
				low[x] = min(low[x], dfn[y]);
			}
		}
		if (dfn[x] == low[x]) {
			int now; cnt++;
			do {
				now = stk[top--];
				c[now] = cnt;
			} while (x != now);
		}
	}
	void work(int rt) {
		tarjan(rt, 0);
	}
};


//-------------- templates above --------------


void solve() {
	int n, m;
	cin >> n >> m;
	vector<vector<int>> adj(n + 1);
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}

	EBCC T(adj);
	T.work(1);

	vector<vector<int>> cirs;
	vector<int> cirID(n + 1, -1);
	{
		vector<bool> vis(n + 1);
		vector<int> cir;
		auto dfs = [&] (auto self, int x) -> void {
			cir.push_back(x);
			vis[x] = true;
			for (auto y : adj[x]) {
				if (vis[y] || E.count({x, y})) {
					continue;
				} 
				self(self, y);
			}
		}; 
		for (int i = 1; i <= n; i++) {
			if (!vis[i]) {
				cir.clear();
				dfs(dfs, i);
				for (auto x : cir) {
					cirID[x] = cirs.size();
				}
				cirs.push_back(cir);
			}
		}
	}

	vector<int> F(n + 1), bfsDep(n + 1);
	{
		vector<bool> vis(n + 1);
		vector<int> bfsFa(n + 1);
		vector<int> bfsOrder;
		queue<int> q;
		q.push(1);
		vis[1] = true;
		while (!q.empty()) {
			int x = q.front();
			q.pop();
			bfsOrder.push_back(x);
			for (auto y : adj[x]) {
				if (!vis[y]) {
					vis[y] = true;
					bfsFa[y] = x;
					q.push(y);
				}
			}
		}
		reverse(bfsOrder.begin(), bfsOrder.end());
		for (auto x : bfsOrder) {
			for (auto y : adj[x]) {
				if (bfsFa[y] == x) {
					bfsDep[x] = max(bfsDep[x], bfsDep[y] + 1);
					if (E.count({x, y})) {
						F[x] = max(F[x], bfsDep[y] + 1);
					}
				}
			}
		}
	}

	vector<int> G(n + 1);
	auto scanCircle = [&] (int id) {
		vector<int> cir = cirs[id];
		vector<int> f;
		for (auto x : cir) {
			f.push_back(F[x]);
		}
		int len = cir.size();
		cir.insert(cir.end(), cir.begin(), cir.end());
		f.insert(f.end(), f.begin(), f.end());
		deque<int> q;
		for (int i = 0; i < 2 * len; i++) {
			while (!q.empty() && i - q.front() > len / 2) {
				q.pop_front();
			}
			if (!q.empty()) {
				G[cir[i]] = max(G[cir[i]], f[q.front()] + i - q.front());
			}
			while (!q.empty() && f[q.back()] - q.back() <= f[i] - i) {
				q.pop_back();
			}
			q.push_back(i);
		}
		reverse(cir.begin(), cir.end());
		reverse(f.begin(), f.end());
		q.clear();
		for (int i = 0; i < 2 * len; i++) {
			while (!q.empty() && i - q.front() > len / 2) {
				q.pop_front();
			}
			if (!q.empty()) {
				G[cir[i]] = max(G[cir[i]], f[q.front()] + i - q.front());
			}
			while (!q.empty() && f[q.back()] - q.back() <= f[i] - i) {
				q.pop_back();
			}
			q.push_back(i);
		}
	};

	auto dfs = [&] (auto self, int x, int fa, int up) -> void {
		F[x] = max(F[x], up);
		scanCircle(cirID[x]);
		vector<int> cir = cirs[cirID[x]];
		for (auto x : cir) {
			int firMx = 0, secMx = 0;
			for (auto y : adj[x]) {
				if (y == fa || E.count({x, y}) == 0) {
					continue;
				}
				if (bfsDep[y] + 1 > firMx) {
					secMx = firMx;
					firMx = bfsDep[y] + 1;
				} else if (bfsDep[y] + 1 > secMx) {
					secMx = bfsDep[y] + 1;
				}
			}
			for (auto y : adj[x]) {
				if (y == fa || E.count({x, y}) == 0) {
					continue;
				}
				int nup = max(up, G[x]);
				if (bfsDep[y] + 1 == firMx) {
					nup = max(nup, secMx);
				} else {
					nup = max(nup, firMx);
				}
				self(self, y, x, nup + 1);
			}
		}
	};
	dfs(dfs, 1, 0, 0);

	for (int i = 1; i <= n; i++) {
		cout << max(F[i], G[i]) << " \n"[i == n];
	}
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}

```

{% endspoiler %}

## 【2.18】 Day 4

[Virtual Judge Link](https://vjudge.net/contest/694446)

前面都是一些很无聊的题...

{% note info %}

[H. Simplified Nonogram](https://vjudge.net/problem/CodeForces-534F)

题意：完成一个 $5\times 20$ 的简易版数织。简易即你只知道每行/列有多少段黑色，而不知道每一段黑色具体长多少。

{% endnote %}

{% note success %}

我们把同一行连续的一段黑色称为一个连通块。

令 $dp[col][lst][p_1][p_2][p_3][p_4][p_5]=0/1$ 表示是否能到达 "已经填了 $col$ 列，上一列填了 $lst$，第 $i$ 行已经有 $p_i$ 个连通块" 这个状态。

其中 $lst$ 是一个长为 $n$ 的二进制串，第 $i$ 位为 $0/1$ 代表上一列第 $i$ 行是否涂黑。

由每一行连通块个数 $p_i<\lceil\frac{m}{2}\rceil$，此时的状态数有 $m\cdot 2^n\cdot (\lceil\frac{m}{2}\rceil)^n=6.4\cdot 10^7$，开成 bool 类型的数组为 $61$mB，爆不了。

考虑转移，我们枚举当前列的 $2^n$ 种状态，遍历一遍看该状态是否满足纵向限制。若满足，再枚举每一行看是否 "当前第 $i$ 行为 $1$ 且 $lst$ 第 $i$ 位为 $0$"，若是，则对应行的连通块个数 $+1$；否则不变。

于是对于当前列的每一种状态，纵向和横向的限制都能在 $O(n)$ 内 check out。

使用记忆化搜索转移，时间复杂度的上界是状态数乘上 $n$。

实测仅使用最简单的剪枝就能跑进 150ms。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}


//-------------- templates above --------------


bool f[21][32][11][11][11][11][11];

void solve() {
	int n, m;
	cin >> n >> m;
	vector<int> a(n), b(m);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < m; i++) {
		cin >> b[i];
	}
	vector<int> cnt(1 << n);
	for (int i = 1; i < (1 << n); i++) {
		for (int j = 0; j < n; j++) {
			if ((i >> j & 1) && (j == 0 || (i >> (j - 1) & 1) == 0)) {
				cnt[i]++;
			}
		}
	}
	vector<int> ans(m);
	auto dfs = [&] (auto self, int col, int lst, array<int, 5> p) -> void {
		for (int i = 0; i < n; i++) {
			if (p[i] > a[i] || p[i] + (m - col) < a[i]) { 
				return ;
			}
		}
		if (col == m) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					cout << (ans[j] >> i & 1 ? "*" : "."); 
				}
				cout << "\n";
			}
			exit(0);
		}
		if (f[col][lst][p[0]][p[1]][p[2]][p[3]][p[4]]) {
			return ;
		}
		f[col][lst][p[0]][p[1]][p[2]][p[3]][p[4]] = true;
		for (int i = 0; i < (1 << n); i++) {
			if (cnt[i] != b[col]) {
				continue;
			}
			array<int, 5> cur = p;
			for (int j = 0; j < n; j++) {
				if ((i >> j & 1) && (lst >> j & 1) == 0) {
					cur[j]++;
				}
			}
			ans[col] = i;
			self(self, col + 1, i, cur);
		}
	};
	dfs(dfs, 0, 0, {0, 0, 0, 0, 0});
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[I. A Heap of Heaps](https://vjudge.net/problem/CodeForces-538F)

题意：一棵 $n$ 个节点的堆，点有点权，节点编号为 bfs 序。对 $k\in[1,n-1]$ 求当这个堆是 $k$ 叉堆时有多少个节点的权值比父亲小。

$2 \le n \le 2\cdot 10^5$。

{% endnote %}

{% note success %}

易知对于 $k$ 叉堆，节点 $x$ 的父亲编号为 $\left\lfloor\dfrac{x-2}{k}\right\rfloor+1$。

可以发现对于许多 $k$，节点 $x$ 的父亲都是相同的。

用数论分块对每一个节点 $i$ 求出满足权值比父亲小的 $k$ 的范围，差分一下即可。

时间复杂度 $O(n\sqrt{n})$。 

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}


//-------------- templates above --------------


void solve() {
	int n;
	cin >> n;
	vector<int> a(n + 1), d(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		for (int l = 1, r = 0; l <= i - 2; l = r + 1) {
			r = min(i - 2, (i - 2) / ((i - 2) / l));
			if (a[i] < a[(i - 2) / l + 1]) {
				d[l]++;
				d[r + 1]--;
			}
		}
		if (a[i] < a[1]) {
			d[i - 1]++;
		}
	}
	for (int i = 1; i < n; i++) {
		d[i] += d[i - 1];
		cout << d[i] << " \n"[i == n];
	}
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

## 【2.19】 Day 5

[Virtual Judge Link](https://vjudge.net/contest/694757)

脑子经常不够用，代码经常调不出。

昨晚打 CF 的时候明显脑子转不动啊，有点怀疑是不是最近写题太多了。感觉以后打比赛之前真的要放空一下自己。

{% note info %}

[I. Mobile Phone Network](https://vjudge.net/problem/CodeForces-1023F)

题意：给定 $n$ 个点 $m$ 条边的图，边有边权。另给定 $k$ 条没有权值的边，你需要给每条边赋边权使得将这 $k$ 条边加进图中后，这个图至少有一个最小生成树完全覆盖这 $k$ 条边。输出这 $k$ 条边边权和最大是多少。

$1 \le n,k,m\le 5\cdot 10^5$。

{% endnote %}

{% note success %}

先将给定的 $k$ 条边加进生成树里，再从 $m$ 条边中选权值最小的几条连成一棵完整的生成树。

此时，对于一条非树边 $(x,y,w)$，相当于一个限制 "生成树上 $x\leftrightarrow y$ 这条路径上的边的权值不能超过 $w$"。因为超过了就可以把那条边断掉换成这条非树边。

相当于对于每条非树边，在生成树上将一段路径上的边权取 $\min$。

按边权从小到大枚举非树边，此时每条树边只用访问一次，用并查集维护即可。

时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define inf 0x3fffffffffffffff

struct DSU {
	vector<int> f, siz;
	DSU() {}
	DSU(int n) {
		f.resize(n + 1);
		siz.resize(n + 1);
		for(int i = 0; i <= n; i++) {
			f[i] = i;
			siz[i] = 1;
		}
	}
	int find(int x) {
		if (x == f[x]) {
			return x;
		}
		return f[x] = find(f[x]);
	}
	bool same(int x, int y) {
		return find(x) == find(y);
	}
	bool merge(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y) {
			return false;
		}
		siz[x] += siz[y];
		f[y] = x;
		return true;
	}
	int size(int x) {
		return siz[find(x)];
	}
};


//-------------- templates above --------------


void solve() {
	int n, k, m;
	cin >> n >> k >> m;
	vector<vector<int>> adj(n + 1);
	map<array<int, 2>, int> my;
	DSU dsu(n);
	for (int i = 0; i < k; i++) {
		int x, y;
		cin >> x >> y;
		my[{x, y}] = my[{y, x}] = 1;
		adj[x].push_back(y);
		adj[y].push_back(x);
		dsu.merge(x, y);
	}
	vector<array<int, 4>> E;
	vector<int> f(m);
	for (int i = 0; i < m; i++) {
		int x, y, w;
		cin >> x >> y >> w;
		E.push_back({w, x, y, i});
		if (dsu.merge(x, y)) {
			f[i] = true;
			adj[x].push_back(y);
			adj[y].push_back(x);
		}
	}

	vector<int> val(n + 1, inf), dep(n + 1), fa(n + 1);
	auto dfs = [&] (auto self, int x, int fath) -> void {
		if (my.count({x, fath}) == 0) {
			val[x] = 0;
		} 
		dep[x] = dep[fath] + 1;
		fa[x] = fath;
		for (auto y : adj[x]) {
			if (y == fath) {
				continue;
			}
			self(self, y, x);
		}
	};
	dfs(dfs, 1, 0);

	dsu = DSU(n);
	for (auto [w, x, y, i] : E) {
		if (f[i]) {
			continue;
		}
		while (x != y) {
			x = dsu.find(x);
			y = dsu.find(y);
			if (x == y) {
				break;
			}
			if (dep[x] < dep[y]) {
				swap(x, y);
			}
			val[x] = min(val[x], w);
			dsu.merge(fa[x], x);
		}
	}

	int ans = 0;
	for (int i = 2; i <= n; i++) {
		if (val[i] == inf) {
			cout << "-1\n";
			return ;
		}
		ans += val[i];
	}
	cout << ans << "\n";
}


signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

## 【2.20】 Day 6

[Virtual Judge Link](https://vjudge.net/contest/695051)

A 题输出浮点数因为没设置精度一直 wa，lyc 指导之后才知道直接输出来会是科学计数法，十分难绷。

{% note info %}

[F - Perils in Parallel](https://vjudge.net/problem/AtCoder-abc155_f)

题意：有 $n$ 个灯，给定每个灯的坐标 $A_i$ 和初始状态 $B_i$（亮或灭）。另有 $m$ 个操作，形如 "将坐标在 $L_i$ 和 $R_i$ 之间的灯的状态取反"，问是否能让所有灯全灭。若能，给出操作方案。

$1 \le n \le 10^5$，$1\le m \le 2\cdot10^5$，$1 \le A_i \le 10^9$。

{% endnote %}

{% note success %}

离散化是必要的，我们按坐标从小到大给灯标号，然后预处理出每种操作对应灯的标号范围。

取反等价于异或 $1$。设按坐标排序后的状态序列为 $\{s\}$，求出其异或差分数组 $\{t\}$（即 $t[i]=s[i]\oplus s_[i-1]$）。那么操作 $(L_i,R_i)$ 相当于将 $t[L_i]$ 和 $t[R_i+1]$ 取反，最终目标也转化为使 $\{t\}$ 全为 $0$（$t[n+1]$ 除外）。

对每种操作连边 $L_i \leftrightarrow R_{i}+1$，那么每次肯定是将一条边的两个端点同时取反。

对于每一个连通分量：从任意一个点（设为 $A$）开始 dfs，回溯时可以贪心的将当前点与其 dfs 树上的儿子进行操作，使得儿子全为 $0$。这么做可以使除了 $A$ 之外的所有点为 $0$。

接着，能够断言：无解当且仅当 $A$ 的值为 $1$ 且 $A$ 和 $n+1$ 不在一个连通分量。

因为若在一个连通分量内，可以直接沿着 $A$ 与 $n+1$ 之间的路径一直操作，将 $A$ 的 $1$ 转移给 $n+1$。

方案可以在 dfs 时顺便记录。时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff

struct DSU {
	vector<int> f, siz;
	DSU() {}
	DSU(int n) {
		f.resize(n + 1);
		siz.resize(n + 1);
		for(int i = 0; i <= n; i++) {
			f[i] = i;
			siz[i] = 1;
		}
	}
	int find(int x) {
		if (x == f[x]) {
			return x;
		}
		return f[x] = find(f[x]);
	}
	bool same(int x, int y) {
		return find(x) == find(y);
	}
	bool merge(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y) {
			return false;
		}
		if (siz[x] < siz[y]) {
			swap(x, y);
		}
		siz[x] += siz[y];
		f[y] = x;
		return true;
	}
	int size(int x) {
		return siz[find(x)];
	}
};


//-------------- templates above --------------


void solve() {
	int n, m;
	cin >> n >> m;
	vector<array<int, 2>> a(n + 1);
	for (int i = 1; i <= n; i++) {
		int x, y;
		cin >> x >> y;
		a[i] = {x, y};
	}
	sort(a.begin() + 1, a.end());
	vector<int> b(n + 2), c(n + 1);
	for (int i = 1; i <= n; i++) {
		b[i] = a[i][1] ^ a[i - 1][1];
		c[i] = a[i][0];
	}
	
	map<array<int, 2>, int> mp;
	vector<vector<int>> adj(n + 2);
	DSU dsu(n + 1);
	for (int i = 0; i < m; i++) {
		int l, r;
		cin >> l >> r;
		auto itL = lower_bound(c.begin(), c.end(), l);
		auto itR = upper_bound(c.begin(), c.end(), r);
		if (itL == c.end()) {
			continue;
		}
		int L = itL - c.begin();
		int R = itR == c.end() ? n : itR - c.begin() - 1; 
		if (L > R || mp[{L, R + 1}]) {
			continue;
		}
		dsu.merge(L, R + 1);
		mp[{L, R + 1}] = mp[{R + 1, L}] = i + 1;
		adj[L].push_back(R + 1);
		adj[R + 1].push_back(L);
	}

	vector<int> vis(n + 2), pre(n + 2);
	set<int> ans;
	auto dfs = [&] (auto self, int x) -> void {
		vis[x] = 1;
		int have_T = 0;
		vector<int> son;
		for (auto y : adj[x]) {
			if (vis[y]) {
				continue;
			}
			pre[y] = x;
			self(self, y);
			if (y == n + 1) {
				have_T = 1;
			} else {
				son.push_back(y);
			}
		}
		for (auto y : son) {
			if (b[y]) {
				ans.insert(mp[{x, y}]);
				b[y] = 0;	
				b[x] ^= 1;
			}
		}
		if (b[x] && have_T) {
			ans.insert(mp[{x, n + 1}]);
			b[x] = 0;
		}
	};
	for (int i = 1; i <= n; i++) {
		if (!vis[i]) {
			dfs(dfs, i);
			if (b[i]) {
				if (dsu.same(i, n + 1) == 0) {
					cout << -1 << "\n";
					return ;
				}
				for (int j = n + 1; j != i; j = pre[j]) {
					int id = mp[{j, pre[j]}];
					if (ans.count(id)) {
						ans.erase(id);
					} else {
						ans.insert(id);
					}
				}
			}
		}
	}
	cout << ans.size() << "\n";
	for (auto x : ans) {
		cout << x << " ";
	}
}


signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

---

{% note info %}

[G - Independent Set](https://vjudge.net/problem/CodeForces-1332F)

题意：给定一棵 $n$ 个点的树，求它的 $2^{n-1}-1$ 种非空边导出子图的点独立集个数之和。

$2 \le n \le 3 \cdot 10^5$。

{% endnote %}

{% note success %}

任意选择一个根节点。

令 $dp[x][0/1][0/1]$ 表示 "以 $x$ 为根的子树内，是否选 $x$ 上面的边（$x\leftrightarrow fa[x]$）作为边导出子图的一部分，是否选 $x$ 作为点独立集中的一个元素" 的答案。

转移如下：
$$
\begin{align}
&dp[x][0][0]=\prod_{y\in son[x]}dp[y][0][0]+dp[y][0][1]+dp[y][1][0]+dp[y][1][1]\\
&dp[x][1][0]=\prod_{y\in son[x]}dp[y][0][0]+dp[y][0][1]+dp[y][1][0]+dp[y][1][1]\\
&dp[x][1][1]=\prod_{y\in son[x]}dp[y][0][0]+dp[y][0][1]+dp[y][1][0]\\
&dp[x][0][1]=\left(\prod_{y\in son[x]}dp[y][0][0]+dp[y][0][1]+dp[y][1][0]\right)-\left(\prod_{y\in son[x]}dp[y][0][0]+dp[y][0][1]\right)
\end{align}
$$
前三条根据独立集的定义好理解，最后一条 $dp[x][0][1]$ 代表 $x$ 与其父亲不相连而自己又在独立集中，此时必须保证 $x$ 至少有一个儿子 $y$ 和 $x$ 有边相连。容斥一下就是总方案数减去 "所有儿子都不与 $x$ 连边" 的方案数。

因为要求边导出子图非空，答案还需要 $-1$。

时间复杂度 $O(n)$。

{% endnote %}

{% spoiler Code %}

```c++
void solve() {
	int n;
	cin >> n;
	vector<vector<int>> adj(n + 1);
	for (int i = 1; i < n; i++) {
		int x, y;
		cin >> x >> y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	vector dp(n + 1, vector(2, vector<mint>(2)));
	auto dfs = [&] (auto self, int x, int fa) -> void {
		mint c1 = 1, c2 = 1, c3 = 1;
		for (auto y : adj[x]) {
			if (y == fa) {
				continue;
			}
			self(self, y, x);
			c1 *= dp[y][0][0] + dp[y][0][1] + dp[y][1][0] + dp[y][1][1];
			c2 *= dp[y][0][0] + dp[y][0][1] + dp[y][1][0];
			c3 *= dp[y][0][0] + dp[y][0][1];
		}
		dp[x][0][0] = c1;
		dp[x][1][0] = c1;
		dp[x][1][1] = c2;
		dp[x][0][1] = c2 - c3;
	};
	dfs(dfs, 1, 0);
	cout << dp[1][0][1] + dp[1][0][0] - 1 << "\n";
}
```

{% endspoiler %}

---

{% note info %}

[H - No Monotone Triples](https://vjudge.net/problem/CodeForces-1332G)

题意：给定长为 $n$ 的 $\{a\}$，定义三元组 $(i,j,k)$ 单调当且仅当 $i<j<k$ 且 $a_i\le a_j\le a_k$ 或 $a_i\ge a_j\ge a_k$。$q$ 次询问，每次询问 $l,r$，你需要在 $a[l,r]$ 中找到一个长度至少为 $3$ 且不含单调三元组的子序列 $\{b\}$。

$3\le n \le 2\cdot 10^5$，$1 \le q\le 2\cdot 10^5$，$1 \le a_i\le 10^9$。

{% endnote %}

{% note success %}

对于长度 $\ge 5$ 的任意数列，若元素互不相同，由 Erdős–Szekeres 定理（详见文末）可知至少存在长为 $3$ 的单调子序列；若有相同元素，单调条件更容易满足。故我们要找的 $\{b\}$ 长度只能是 $3$ 或者 $4$。

先说如何找长为 $3$ 的 $\{b\}$。对于 $\{a\}$ 中每个极长的元素相同段 $[L,R]$，若 $(L-1,L,R+1)$ 不是单调三元组，就将 $L-1$ 放入 $\{c\}$ 中。接着还需要预处理 $\text{nxt}[i]$ 代表 $i$ 右侧第一个 $\neq a[i]$ 的元素的下标。对于每个询问 $(l,r)$，二分出 $\{c\}$ 中第一个 $\ge l$ 的 $L$，若 $\text{nxt}[L+1] \le r$，则 $\{b\}=\{L,L+1,\text{nxt}[L+1]\}$ 就是一组合法的答案。

麻烦的是长为 $4$ 的 $\{b\}$。此时序列的特征是：$b_2,b_3$ 是极值，$b_1,b_4$ 落在值域中间且不等于极值。

倒着扫描序列，维护两个单调栈 $mn,mx$ 分别存储当前位置往后的非严格前缀最小值和非严格前缀最大值。设当前位置就是 $b_1$，那么显然 $b_2,b_3$ 一定分别在两个单调栈中，否则更劣。以及 $b_4$ 一定不在两个单调栈中，因为 $b_4$ 不是极值。

此时，我们有了一个能求出 "若当前位置 $i$ 作为 $p_1$，$p_4$ 的最小合法取值（记为 $res[i]$）" 的方法：

- 维护一个 `std::set` 存储不在任何一个单调栈中的元素的下标。
- 从两个单调栈中分别找出第一个 $\neq a[i]$ 的元素的下标 $p_2,p_3$，这可以通过在单调栈上二分实现。
- 从 `std::set` 里二分出第一个 $>\max(p_2,p_3)$ 的下标即为所求最小的 $p_4$（$res[i]=p_4$）。

我们把 $res$ 数组放到线段树上。对于每个询问 $[l,r]$，在线段树上二分找到区间里第一个 $L$ 满足 $res[L]\le r$，再找到 $[L,res[L]]$ 里最大最小值对于的下标 $p_2,p_3(p_2<p_3)$，则 $\{b\}=\{L,p_2,p_3,res[L]\}$ 就是一组合法的答案。

时间复杂度 $O(n\log n)$。

{% endnote %}

{% spoiler Code %}

```c++
#include <bits/stdc++.h>
using namespace std;
#define fre(x) freopen(#x".in", "r", stdin); freopen(#x".out", "w", stdout)
#define ck(x)  { cout << "check " << x << "\n"; cout.flush();}
#define int long long
#define double long double
#define inf 0x3fffffffffffffff

template<class Info>
struct SegmentTree {
    int n;
    vector<Info> tr;
    SegmentTree(vector<Info> &a) {
        n = a.size() - 1;
        tr.assign((4 << __lg(n + 1)) + 5, Info());
        build(1, 1, n, a);
    }
    #define ls (p << 1)
    #define rs (p << 1 | 1)
    void build(int p, int l, int r, vector<Info> &a) {
        if (l == r) {
            tr[p] = a[l];
            return ;
        }
        int m = l + r >> 1;
        build(ls, l, m, a);
        build(rs, m + 1, r, a);
        pushup(p);
    }
    void pushup(int p) {
        tr[p] = tr[ls] + tr[rs];
    }
    void modify(int p, int l, int r, int pos, const Info &x) {
        if (l == r) {
            tr[p] = x;
            return;
        }
        int m = l + r >> 1;
        if (pos <= m) {
            modify(ls, l, m, pos, x);
        } else {
            modify(rs, m + 1, r, pos, x);
        }
        pushup(p);
    }
    void modify(int pos, const Info &x) {
        modify(1, 1, n, pos, x);
    }
    Info query(int p, int l, int r, int ql, int qr) {
        if (l > qr || r < ql) {
            return Info();
        }
        if (ql <= l && qr >= r) {
            return tr[p];
        }
        int m = l + r >> 1;
        return query(ls, l, m, ql, qr) + query(rs, m + 1, r, ql, qr);
    }
    Info query(int ql, int qr) {
        return query(1, 1, n, ql, qr);
    }
    template<class F>
    int findFirst(int p, int l, int r, int ql, int qr, F &&pred) {
        if (l > qr || r < ql) {
            return -1;
        }
        if (ql <= l && qr >= r && !pred(tr[p])) {
            return -1;
        }
        if (l == r) {
            return l;
        }
        int m = l + r >> 1;
        int res = findFirst(ls, l, m, ql, qr, pred);
        if (res == -1) {
            res = findFirst(rs, m + 1, r, ql, qr, pred);
        }
        return res;
    }
    template<class F>
    int findFirst(int ql, int qr, F &&pred) {
        return findFirst(1, 1, n, ql, qr, pred);
    }
    template<class F>
    int findLast(int p, int l, int r, int ql, int qr, F &&pred) {
        if (l > qr || r < ql) {
            return -1;
        }
        if (ql <= l && qr >= r && !pred(tr[p])) {
            return -1;
        }
        if (l == r) {
            return l;
        }
        int m = l + r >> 1;
        int res = findLast(rs, m + 1, r, ql, qr, pred);
        if (res == -1) {
            res = findLast(ls, l, m, ql, qr, pred);
        }
        return res;
    }
    template<class F>
    int findLast(int ql, int qr, F &&pred) {
        return findLast(1, 1, n, ql, qr, pred);
    }
};

struct Info {
	int mn = inf;
	int mx = -inf;
	int res = inf;
    Info() {}
    Info(int x, int y) {
    	mn = mx = x;
    	res = y;
    }
};
Info operator+(const Info &a, const Info &b) {
    Info c;
    c.mn = min(a.mn, b.mn);
    c.mx = max(a.mx, b.mx);
    c.res = min(a.res, b.res);
    return c;
};


//-------------- templates above --------------


void solve() {
	int n, q;
	cin >> n >> q;
	vector<int> a(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}

	vector<int> s, f;
	for (int i = 1; i <= n; i++) {
		if (a[i] != a[i - 1]) {
			s.push_back(i);
			if (s.size() >= 3) {
				int lst = s.back();
				int mid = s[s.size() - 2];
				int pre = s[s.size() - 3];
				if (a[mid] > a[lst] && a[mid] > a[pre]) {
					f.push_back(pre);
				}
				if (a[mid] < a[lst] && a[mid] < a[pre]) {
					f.push_back(pre);
				}
			}
		} else {
			s.pop_back();
			s.push_back(i);
		}
	}
	vector<int> nxt(n + 1, n + 1);
	for (int i = n - 1; i >= 1; i--) {
		if (a[i] == a[i + 1]) {
			nxt[i] = nxt[i + 1];
		} else {
			nxt[i] = i + 1;
		}
	}
	auto get3 = [&] (int l, int r) {
		auto it = lower_bound(f.begin(), f.end(), l);
		if (it == f.end()) {
			return false;
		}
		int L = *it;
		if (nxt[L + 1] > r) {
			return false;
		}
		cout << "3\n";
		cout << L << " " << L + 1 << " " << nxt[L + 1] << "\n";
		return true;
	};

	set<int> outside;
	for (int i = 1; i <= n; i++) {
		outside.insert(i);
	}
	vector<int> res(n + 1, inf), tot(n + 1);
	vector<int> mn, mx;
	for (int i = n; i >= 1; i--) {
		while (!mn.empty() && a[mn.back()] > a[i]) {
			if (--tot[mn.back()] == 0) {
				outside.insert(mn.back());
			}
			mn.pop_back();
		}
		while (!mx.empty() && a[mx.back()] < a[i]) {
			if (--tot[mx.back()] == 0) {
				outside.insert(mx.back());
			}
			mx.pop_back();
		}
		mn.push_back(i);
		mx.push_back(i);
		outside.erase(i);
		tot[i] += 2;

		int resmn = -1, resmx = -1;
		int l = 0, r = mn.size() - 1;
		while (l <= r) {
			int mid = l + r >> 1;
			if (a[i] != a[mn[mid]]) {
				resmn = mn[mid];
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		} 
		l = 0, r = mx.size() - 1;
		while (l <= r) {
			int mid = l + r >> 1;
			if (a[i] != a[mx[mid]]) {
				resmx = mx[mid];
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		if (resmn == -1 || resmx == -1) {
			continue;
		}
		auto it = outside.lower_bound(max(resmn, resmx));
		if (it == outside.end()) {
			continue;
		}
		res[i] = *it;
	}

	vector<Info> tmp(n + 1);
	for (int i = 1; i <= n; i++) {
		tmp[i] = Info(a[i], res[i]);
	}
	SegmentTree<Info> seg(tmp);
	
	auto get4 = [&] (int l, int r) {
		int p1 = seg.findFirst(l, r, [&] (auto A) {
			return A.res <= r;
		});
		if (p1 == -1) {
			return false;
		}
		int p4 = res[p1];
		int mn = seg.query(p1, p4).mn;
		int mx = seg.query(p1, p4).mx;
		int p2 = seg.findFirst(p1, p4, [&] (auto A) {
			return A.mn <= mn;
		});
		int p3 = seg.findFirst(p1, p4, [&] (auto A) {
			return A.mx >= mx;
		});
		if (p2 > p3) {
			swap(p2, p3);
		}
		cout << "4\n";
		cout << p1 << " " << p2 << " " << p3 << " " << p4 << "\n";
		return true;
	};

	while (q--) {
		int l, r;
		cin >> l >> r;
		if (get4(l, r) == 0 && get3(l, r) == 0) {
			cout << 0 << "\n\n";
		}
	}
}


signed main() {
	fre(test);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T = 1;
	while (T--) {
		solve();
	}
	return 0;
}
```

{% endspoiler %}

{% note primary %}

**Dilworth 定理**：任意有限偏序集中，最长链的长度等于最小的反链划分的数量。

- 将序列中的每个值看成一个元素，定义偏序关系：对于集合中的两个元素 $a,b$，$a≺b$ 当且仅当 $a<b$ 。Dilworth 定理在此基础上给出的结论就是：**一个序列的最长上升子序列的长度（LIS）等于将该序列划分成不上升子序列的最小数量**。

通俗来说，若序列的 LIS 长度为 $k$，则至少需要 $k$ 个不上升的子序列才能覆盖整个序列，且无法用更少的子序列完成覆盖。

- 同样地，若定义偏序关系：对于集合中的两个元素 $a,b$，$a\preccurlyeq b$ 当且仅当 $a\le b$。则有：**一个序列的最长不下降子序列的长度等于将该序列划分成严格下降子序列的最小数量**。

**Erdős–Szekeres 定理**是 Dilworth 定理的一个简单推论，内容是：

- 对于 $mn+1$ 个互不相同的实数组成的数列 $(m,n\in \text{N}^+)$，一定存在长为 $m+1$ 的递增子列或长为 $n+1$ 的递减子列。
- 二维欧式平面上任意 $mn+1$ 个点总能构造出 $m+1$ 条正斜率线段或 $n+1$ 条负斜率线段。（只要该坐标系下任意两点横纵坐标都不同） 

对于第一条，设这个序列的 LIS 长度为 $k$，若 $k\ge m+1$，成立；若 $k<m+1$，应用 Dilworth 定理，将该序列划分成下降子序列的最小数量是 $k$。序列被划分成了 $k$ 段，这样划分出最长的下降序列的长度 $l$ 的最小值是 $\lceil\frac{mn+1}{k}\rceil$（因为均分最优），又 $k<m+1$，不难得出 $l\ge n+1$，得证。

{% endnote %}
