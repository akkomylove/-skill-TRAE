# 数学建模公式编辑指南

## LaTeX公式基础

### 行内公式
使用单个`$`包裹：`$a^2 + b^2 = c^2$`

### 独立公式
使用双个`$$`包裹：
```
$$
f(x) = \int_{-\infty}^{\infty} e^{-x^2}dx
$$
```

### 公式编号
```
\begin{equation}
a^2 + b^2 = c^2 \label{eq:pythagorean}
\end{equation}
```

### 公式交叉引用
```
如式\eqref{eq:pythagorean}所示
```

## 常用公式模板

### 1. 目标函数模板

#### 线性规划目标函数
```
\min（或\max）Z = \sum_{j=1}^{n}c_jx_j
```

#### 二次规划目标函数
```
\min Z = \frac{1}{2}x^TQx + c^Tx
```

#### 多目标规划目标函数
```
\min Z_1 = f_1(x) \\
\min Z_2 = f_2(x) \\
\vdots \\
\min Z_k = f_k(x)
```

### 2. 约束条件模板

#### 等式约束
```
s.t. \quad h_j(x) = 0, \quad j = 1, 2, \ldots, p
```

#### 不等式约束
```
g_i(x) \leq 0, \quad i = 1, 2, \ldots, m
```

#### 变量范围约束
```
x_j^{min} \leq x_j \leq x_j^{max}, \quad j = 1, 2, \ldots, n
```

### 3. 优化算法公式

#### 梯度下降法
```
x_{k+1} = x_k - \alpha \nabla f(x_k)
```

#### 拉格朗日乘数法
```
\mathcal{L}(x, \lambda) = f(x) + \sum_{i=1}^{m}\lambda_i g_i(x)
```

#### KKT条件
```
\begin{cases}
\nabla f(x^*) + \sum_{i=1}^{m}\lambda_i \nabla g_i(x^*) = 0 \\
\lambda_i \geq 0, \quad i = 1, 2, \ldots, m \\
\lambda_i g_i(x^*) = 0, \quad i = 1, 2, \ldots, m
\end{cases}
```

### 4. 预测模型公式

#### 时间序列AR(p)模型
```
x_t = \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + \varepsilon_t
```

#### 指数平滑公式
```
S_t = \alpha x_t + (1-\alpha)S_{t-1}
```

#### 灰色GM(1,1)模型
```
\frac{dx^{(1)}}{dt} + ax^{(1)} = b
```

#### 灰色预测累加生成
```
x^{(1)}(k) = \sum_{i=1}^{k} x^{(0)}(i)
```

### 5. 统计模型公式

#### 多元线性回归
```
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \varepsilon
```

#### 回归系数估计（最小二乘法）
```
\hat{\beta} = (X^TX)^{-1}X^Ty
```

#### 相关系数
```
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}
```

#### 主成分分析
```
Y = X^T W
$$
其中$W$为特征向量矩阵
```

### 6. 微分方程模型

#### 一阶常微分方程
```
\frac{dy}{dt} = f(t, y)
```

#### 阻滞增长模型（Logistic模型）
```
\frac{dN}{dt} = rN(1 - \frac{N}{K})
```

#### SIR传染病模型
```
\begin{cases}
\frac{dS}{dt} = -\beta SI \\
\frac{dI}{dt} = \beta SI - \gamma I \\
\frac{dR}{dt} = \gamma I
\end{cases}
```

### 7. 图论公式

#### 最短路径（Dijkstra算法）
```
d(v) = \min_{u \in V} \{d(u) + w(u,v)\}
$$

其中$d(v)$为到顶点$v$的最短距离，$w(u,v)$为边$(u,v)$的权重
```

#### 最小生成树（Prim算法）
```
T = \{最小生成树的边集\}
$$

满足$\sum_{e \in T} w(e)$最小
```

#### 最大流
```
\max \{f(v_s, V\backslash\{v_s\})\}
$$

满足容量约束和流量守恒约束
```

### 8. 概率模型公式

#### 全概率公式
```
P(B) = \sum_{i=1}^{n} P(A_i)P(B|A_i)
```

#### 贝叶斯公式
```
P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_{j=1}^{n}P(A_j)P(B|A_j)}
$$

其中$i = 1, 2, \ldots, n$
```

#### 马尔可夫链
```
P(X_{n+1}=j|X_n=i) = p_{ij}
$$

其中$p_{ij}$为转移概率
```

### 9. 排队论公式

#### M/M/1排队模型
```
\rho = \frac{\lambda}{\mu}
$$

其中$\lambda$为到达率，$\mu$为服务率
```

#### 队长公式
```
L_s = \frac{\rho}{1-\rho}
$$

当$\rho < 1$时系统稳定
```

#### 等待时间公式
```
W_q = \frac{\rho}{\mu(1-\rho)}
```

### 10. 层次分析法（AHP）公式

#### 判断矩阵
```
A = (a_{ij})_{n \times n}
$$

其中$a_{ij} > 0$，$a_{ij} = \frac{1}{a_{ji}}$
```

#### 一致性指标
```
CI = \frac{\lambda_{\max} - n}{n - 1}
$$

其中$n$为矩阵阶数，$\lambda_{\max}$为最大特征值
```

#### 一致性比例
```
CR = \frac{CI}{RI}
$$

当$CR < 0.1$时认为判断矩阵具有满意的一致性
```

### 11. TOPSIS法公式

#### 规范化决策矩阵
```
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m}x_{ij}^2}}
$$

其中$i = 1, 2, \ldots, m$，$j = 1, 2, \ldots, n$
```

#### 到理想解的距离
```
D_i^+ = \sqrt{\sum_{j=1}^{n}(r_{ij} - r_j^+)^2}
$$

D_i^- = \sqrt{\sum_{j=1}^{n}(r_{ij} - r_j^-)^2}
$$

其中$r_j^+$和$r_j^-$分别为理想解和负理想解
```

#### 相对贴近度
```
C_i = \frac{D_i^-}{D_i^+ + D_i^-}
$$

其中$C_i \in [0, 1]$，越大越优
```

### 12. 模糊评价公式

#### 隶属度函数（三角形）
```
\mu_A(x) =
\begin{cases}
0, & x \leq a \\
\frac{x-a}{b-a}, & a < x < b \\
\frac{c-x}{c-b}, & b \leq x < c \\
0, & x \geq c
\end{cases}
```

#### 模糊综合评价
```
B = A \circ R
$$

其中$A$为权重向量，$R$为隶属度矩阵，$\circ$为模糊算子
```

### 13. 神经网络公式

#### 感知机
```
y = f(\sum_{i=1}^{n} w_i x_i + b)
$$

其中$f$为激活函数
```

#### BP神经网络反向传播
```
\delta_j = y_j(1-y_j)\sum_{k} w_{jk} \delta_k
$$

其中$\delta_j$为误差项
```

### 14. 遗传算法公式

#### 适应度函数
```
fitness = \frac{1}{1 + objective}
$$

其中$objective$为目标函数值
```

#### 交叉概率和变异概率
```
p_c \in [0.6, 0.9] \\
p_m \in [0.01, 0.05]
$$

其中$p_c$为交叉概率，$p_m$为变异概率
```

## 公式编辑技巧

### 1. 多行公式对齐
```
\begin{align}
\max Z = & \; c_1x_1 + c_2x_2 + \cdots + c_nx_n \\
\text{s.t.} \quad & a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \leq b_1 \\
& a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \leq b_2 \\
& \cdots \\
& a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \leq b_m
\end{align}
```

### 2. 分段函数
```
f(x) =
\begin{cases}
x^2, & x \geq 0 \\
-x^2, & x < 0
\end{cases}
```

### 3. 矩阵表示
```
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
```

### 4. 求和与连乘
```
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

\prod_{i=1}^{n} x_i = x_1 \times x_2 \times \cdots \times x_n
```

### 5. 偏导数
```
\frac{\partial f}{\partial x_i}
\quad
\frac{\partial^2 f}{\partial x_i \partial x_j}
\quad
\nabla f = (\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n})
```

### 6. 极限与积分
```
\lim_{x \to \infty} f(x)
\quad
\int_{a}^{b} f(x)dx
\quad
\iint_{D} f(x,y)dxdy
```

## 公式字体规范

- 变量：斜体 $x, y, z$
- 数字：正体 $1, 2, 3$
- 运算符：正体 $+,-,\times,\div$
- 函数名：正体 $\sin, \cos, \log, \exp$
- 矩阵：大写正体 $\mathbf{A}, \mathbf{B}$
- 向量：小写粗体 $\mathbf{x}, \mathbf{y}$
