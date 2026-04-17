"""
工具函数模块

提供数学建模论文写作辅助功能
"""

import json
import os

def get_resource_path(resource_name):
    """
    获取资源文件的绝对路径

    Args:
        resource_name: 资源文件名

    Returns:
        资源文件的绝对路径
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(current_dir)
    return os.path.join(skill_root, 'resources', resource_name)

def load_terminology():
    """
    加载术语词典

    Returns:
        dict: 术语词典内容
    """
    path = get_resource_path('terminology.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_phrase_patterns():
    """
    加载短语模式

    Returns:
        dict: 短语模式内容
    """
    path = get_resource_path('phrase_patterns.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_terminology_by_category(category):
    """
    获取指定类别的术语

    Args:
        category: 类别名称（如 'optimization', 'prediction' 等）

    Returns:
        dict: 该类别的术语列表
    """
    terminology = load_terminology()
    return terminology.get(category, {})

def get_all_terminology_categories():
    """
    获取所有术语类别

    Returns:
        list: 所有类别名称列表
    """
    terminology = load_terminology()
    return list(terminology.keys())

def get_phrases_by_category(category):
    """
    获取指定类别的短语

    Args:
        category: 类别名称（如 'abstract', 'introduction' 等）

    Returns:
        list: 该类别的短语列表
    """
    phrases = load_phrase_patterns()
    return phrases.get(category, {}).get('phrases', [])

def get_all_phrase_categories():
    """
    获取所有短语类别

    Returns:
        list: 所有类别名称列表
    """
    phrases = load_phrase_patterns()
    return list(phrases.keys())

def search_terminology(keyword):
    """
    在术语词典中搜索关键词

    Args:
        keyword: 搜索关键词

    Returns:
        list: 匹配的术语列表
    """
    terminology = load_terminology()
    results = []

    for category, data in terminology.items():
        for term in data.get('terms', []):
            if (keyword.lower() in term['term'].lower() or
                keyword.lower() in term['en'].lower() or
                keyword.lower() in term['definition'].lower()):
                results.append({
                    'category': data['name'],
                    **term
                })

    return results

def format_citation(style, citation_type, **kwargs):
    """
    格式化参考文献

    Args:
        style: 引用格式（'gbt7714', 'apa', 'ieee', 'mla'）
        citation_type: 引用类型（'journal_article', 'book', 'conference' 等）
        **kwargs: 引用信息参数

    Returns:
        str: 格式化的引用文本
    """
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'citation_formats.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    template = config['formats'][style]['templates'].get(citation_type, '')

    if not template:
        return ''

    return template

def generate_paper_outline(paper_type='standard'):
    """
    生成论文大纲

    Args:
        paper_type: 论文类型（'standard', 'optimization', 'prediction', 'evaluation'）

    Returns:
        dict: 论文结构大纲
    """
    outlines = {
        'standard': [
            {'section': '摘要', 'description': '简洁概括研究内容'},
            {'section': '问题重述', 'description': '重新表述问题'},
            {'section': '模型假设', 'description': '列出关键假设'},
            {'section': '符号说明', 'description': '定义变量和参数'},
            {'section': '模型建立与求解', 'description': '核心模型和求解方法'},
            {'section': '模型检验与分析', 'description': '验证模型有效性'},
            {'section': '模型评价与推广', 'description': '总结优缺点'},
            {'section': '参考文献', 'description': '引用文献列表'},
            {'section': '附录', 'description': '补充材料'}
        ],
        'optimization': [
            {'section': '摘要', 'description': '简洁概括优化问题和方法'},
            {'section': '问题背景', 'description': '说明优化问题来源'},
            {'section': '模型假设与符号说明', 'description': '明确约束条件'},
            {'section': '目标函数与约束条件', 'description': '建立优化模型'},
            {'section': '算法选择与求解', 'description': '选择合适算法'},
            {'section': '结果分析', 'description': '分析最优解'},
            {'section': '灵敏度分析', 'description': '参数影响分析'},
            {'section': '结论', 'description': '总结模型应用价值'}
        ],
        'prediction': [
            {'section': '摘要', 'description': '概括预测问题和方法'},
            {'section': '数据预处理', 'description': '数据清洗和转换'},
            {'section': '特征工程', 'description': '提取预测特征'},
            {'section': '模型建立', 'description': '选择预测模型'},
            {'section': '模型训练与验证', 'description': '模型调参与验证'},
            {'section': '预测结果分析', 'description': '评估预测效果'},
            {'section': '误差分析', 'description': '分析预测误差'},
            {'section': '结论', 'description': '总结预测结论'}
        ]
    }

    return outlines.get(paper_type, outlines['standard'])

__all__ = [
    'load_terminology',
    'load_phrase_patterns',
    'get_terminology_by_category',
    'get_all_terminology_categories',
    'get_phrases_by_category',
    'get_all_phrase_categories',
    'search_terminology',
    'format_citation',
    'generate_paper_outline'
]
