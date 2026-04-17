# 数学建模论文写作助手 (math-modeling-paper)

这是一个专门用于辅助数学建模论文撰写的Skill工具，提供论文结构规划、公式编辑、数据可视化、文献引用管理等核心功能。

## 📁 目录结构

```
.trae/skills/math-modeling-paper/
├── SKILL.md                        # Skill主定义文件
├── README.md                        # 使用说明文档
├── templates/                       # 论文模板
│   └── paper_structure.md          # 论文结构模板
├── resources/                      # 资源文件
│   ├── formula_guide.md            # 公式编辑指南
│   ├── visualization_guide.md      # 数据可视化指南
│   ├── terminology.json            # 术语词典
│   └── phrase_patterns.json        # 常用短语模式
├── config/                         # 配置文件
│   └── citation_formats.json       # 引用格式配置
├── utils/                          # 工具函数
│   └── __init__.py                # 工具函数模块
└── tests/                          # 单元测试
    └── test_skill.py               # Skill功能测试
```

## 🎯 核心功能

### 1. 论文结构规划
提供数学建模论文的标准结构模板，支持根据题目类型自动推荐合适的章节安排。

**支持的功能：**
- 标准论文结构模板
- 不同题型的结构变体（A/B/C/D题）
- 各部分写作要点指导

**使用示例：**
- "帮我规划论文结构"
- "生成摘要模板"
- "我需要写问题重述部分"

### 2. 公式编辑
提供数学建模常用公式的LaTeX模板，支持公式编号和交叉引用。

**支持的公式类型：**
- 优化模型（线性规划、整数规划、非线性规划）
- 预测模型（时间序列、灰色预测、神经网络）
- 统计模型（回归分析、主成分分析、聚类分析）
- 微分方程模型
- 图论模型
- 排队论模型
- 元启发式算法

**使用示例：**
- "插入优化模型的LaTeX公式"
- "帮我写微分方程的公式"
- "生成目标函数的公式模板"

### 3. 数据可视化
提供常见图表的Python/Matlab代码模板。

**支持的图表类型：**
- 折线图
- 柱状图
- 散点图
- 饼图
- 热力图
- 误差棒图
- 3D图
- 直方图
- 箱线图
- 子图布局

**使用示例：**
- "生成数据对比图代码"
- "帮我画结果示意图"
- "创建灵敏度分析图表"

### 4. 文献引用管理
提供多种引用格式，自动生成参考文献。

**支持的引用格式：**
- GB/T 7714-2015（中国国家标准）
- APA（美国心理学会）
- IEEE（电气与电子工程师协会）
- MLA（现代语言协会）

**支持的文章类型：**
- 期刊文章
- 图书
- 会议论文
- 学位论文
- 专利
- 标准
- 网络资源

**使用示例：**
- "生成参考文献格式"
- "帮我整理引用文献"
- "添加期刊文章的引用格式"

## 🔧 使用方法

### 方式一：直接对话
在对话中直接描述您的需求：
```
我要写一篇关于选址问题的数学建模论文
请提供时间序列预测的模型框架
帮我生成灵敏度分析的图表代码
```

### 方式二：使用特定功能
```
structure - 论文结构规划
formula - 公式编辑
visualization - 数据可视化
citation - 文献引用管理
terminology - 术语查询
phrase - 短语模式
```

## 📚 资源文件说明

### terminology.json
数学建模论文常用术语词典，包含12个类别：
- 优化类 (optimization)
- 预测类 (prediction)
- 统计类 (statistics)
- 评价类 (evaluation)
- 图论类 (graph_theory)
- 微分方程类 (differential_equations)
- 排队论类 (queueing_theory)
- 博弈论类 (game_theory)
- 神经网络类 (neural_network)
- 元启发式算法类 (metaheuristics)

每个术语包含：中文名、英文名、定义说明

### phrase_patterns.json
论文各部分常用短语模式，包含8个类别：
- 摘要 (abstract)
- 引言 (introduction)
- 模型假设 (assumption)
- 模型建立 (modeling)
- 模型求解 (solution)
- 模型检验 (validation)
- 结果分析 (analysis)
- 结论 (conclusion)

### citation_formats.json
引用格式配置，支持4种格式：
- GB/T 7714-2015（默认推荐）
- APA
- IEEE
- MLA

### formula_guide.md
LaTeX公式编辑指南，包含：
- 基础语法
- 常用公式模板
- 公式编辑技巧
- 字体规范

### visualization_guide.md
数据可视化指南，包含：
- Python和Matlab双语言实现
- 10种图表类型
- 完整的代码示例
- 图表设计原则

## 🧪 运行测试

```bash
cd .trae/skills/math-modeling-paper
pytest tests/test_skill.py -v
```

## 🔄 扩展指南

### 添加新的公式模板
1. 打开 `resources/formula_guide.md`
2. 在相应类别下添加新的公式模板
3. 包含LaTeX代码和说明

### 添加新的图表类型
1. 打开 `resources/visualization_guide.md`
2. 添加新的图表类型
3. 提供Python和Matlab两种实现

### 添加新的引用格式
1. 打开 `config/citation_formats.json`
2. 在 `formats` 下添加新的格式
3. 包含模板和示例

### 添加新的术语类别
1. 打开 `resources/terminology.json`
2. 添加新的类别
3. 包含术语列表和定义

## 📋 论文结构标准模板

```markdown
1. 摘要
2. 问题重述
   2.1 问题背景
   2.2 问题要求
   2.3 问题分析
3. 模型假设
   3.1 基本假设
   3.2 符号假设
4. 符号说明
5. 模型建立与求解
   5.1 模型类型选择
   5.2 模型建立
   5.3 模型求解
   5.4 结果分析
6. 模型检验与分析
   6.1 稳定性检验
   6.2 误差分析
   6.3 灵敏度分析
   6.4 实用性检验
7. 模型评价与推广
   7.1 优点
   7.2 缺点
   7.3 改进方向
   7.4 应用推广
8. 参考文献
9. 附录
```

## ⚠️ 注意事项

1. **论文结构**：应根据具体题目要求灵活调整，不必完全照搬模板
2. **公式编辑**：建议使用LaTeX以保证格式统一
3. **图表规范**：
   - 分辨率不低于300 DPI
   - 应包含标题、坐标轴标签、图例
   - 图表尺寸应适合论文排版
4. **引用格式**：应统一，建议使用GB/T 7714-2015标准
5. **语言规范**：学术论文应使用规范的学术语言，避免口语化

## 🔗 相关资源

- [LaTeX公式编辑](https://latex.codecogs.com/eqneditor/editor.php)
- [Matplotlib图表库](https://matplotlib.org/)
- [NumPy数值计算](https://numpy.org/)

## 📝 更新日志

### v1.0.0 (2026-04-16)
- 初始版本发布
- 支持论文结构规划
- 支持公式编辑
- 支持数据可视化
- 支持文献引用管理
- 包含术语词典和短语模式
- 完整的单元测试
- 详细的文档说明
