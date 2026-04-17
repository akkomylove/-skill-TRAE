import pytest
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))

def test_terminology_structure():
    with open(os.path.join(os.path.dirname(__file__), '..', 'resources', 'terminology.json'), 'r', encoding='utf-8') as f:
        terminology = json.load(f)

    assert isinstance(terminology, dict), "terminology.json should be a dictionary"
    assert len(terminology) > 0, "terminology.json should not be empty"

    for category, data in terminology.items():
        assert 'name' in data, f"Category '{category}' should have 'name' field"
        assert 'terms' in data, f"Category '{category}' should have 'terms' field"
        assert isinstance(data['terms'], list), f"Category '{category}' 'terms' should be a list"
        assert len(data['terms']) > 0, f"Category '{category}' should have at least one term"

        for term in data['terms']:
            assert 'term' in term, f"Each term should have 'term' field"
            assert 'en' in term, f"Each term should have 'en' (English) field"
            assert 'definition' in term, f"Each term should have 'definition' field"

def test_phrase_patterns_structure():
    with open(os.path.join(os.path.dirname(__file__), '..', 'resources', 'phrase_patterns.json'), 'r', encoding='utf-8') as f:
        phrases = json.load(f)

    assert isinstance(phrases, dict), "phrase_patterns.json should be a dictionary"
    assert len(phrases) > 0, "phrase_patterns.json should not be empty"

    required_categories = ['abstract', 'introduction', 'assumption', 'modeling', 'solution', 'validation', 'analysis', 'conclusion']
    for category in required_categories:
        assert category in phrases, f"phrase_patterns.json should contain '{category}' category"
        assert 'name' in phrases[category], f"Category '{category}' should have 'name' field"
        assert 'phrases' in phrases[category], f"Category '{category}' should have 'phrases' field"
        assert isinstance(phrases[category]['phrases'], list), f"Category '{category}' 'phrases' should be a list"
        assert len(phrases[category]['phrases']) > 0, f"Category '{category}' should have at least one phrase"

def test_citation_formats_structure():
    with open(os.path.join(os.path.dirname(__file__), '..', 'config', 'citation_formats.json'), 'r', encoding='utf-8') as f:
        citations = json.load(f)

    assert isinstance(citations, dict), "citation_formats.json should be a dictionary"
    assert 'formats' in citations, "citation_formats.json should have 'formats' field"
    assert 'common_rules' in citations, "citation_formats.json should have 'common_rules' field"
    assert 'in_text_citation' in citations, "citation_formats.json should have 'in_text_citation' field"

    formats = citations['formats']
    assert 'gbt7714' in formats, "formats should include 'gbt7714' (Chinese standard)"
    assert 'apa' in formats, "formats should include 'apa' (APA style)"
    assert 'ieee' in formats, "formats should include 'ieee' (IEEE style)"

    for format_name, format_data in formats.items():
        assert 'name' in format_data, f"Format '{format_name}' should have 'name' field"
        assert 'templates' in format_data, f"Format '{format_name}' should have 'templates' field"

        templates = format_data['templates']
        assert 'journal_article' in templates, f"Format '{format_name}' should have 'journal_article' template"
        assert 'book' in templates, f"Format '{format_name}' should have 'book' template"

def test_paper_structure_template():
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'paper_structure.md')
    assert os.path.exists(template_path), "paper_structure.md should exist"

    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert len(content) > 0, "paper_structure.md should not be empty"

    required_sections = ['摘要', '问题重述', '模型假设', '符号说明', '模型建立', '模型检验', '模型评价', '参考文献']
    for section in required_sections:
        assert section in content, f"paper_structure.md should contain '{section}' section"

def test_formula_guide_structure():
    formula_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'formula_guide.md')
    assert os.path.exists(formula_path), "formula_guide.md should exist"

    with open(formula_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert len(content) > 0, "formula_guide.md should not be empty"

    required_topics = ['目标函数', '约束条件', '优化算法', '预测模型', '统计模型', '微分方程']
    for topic in required_topics:
        assert topic in content, f"formula_guide.md should contain '{topic}' topic"

def test_visualization_guide_structure():
    viz_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'visualization_guide.md')
    assert os.path.exists(viz_path), "visualization_guide.md should exist"

    with open(viz_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert len(content) > 0, "visualization_guide.md should not be empty"

    chart_types = ['折线图', '柱状图', '散点图', '饼图', '热力图']
    for chart in chart_types:
        assert chart in content, f"visualization_guide.md should contain '{chart}' section"

def test_skill_md_structure():
    skill_path = os.path.join(os.path.dirname(__file__), '..', 'SKILL.md')
    assert os.path.exists(skill_path), "SKILL.md should exist"

    with open(skill_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert len(content) > 0, "SKILL.md should not be empty"
    assert '---' in content, "SKILL.md should have frontmatter"
    assert 'name:' in content, "SKILL.md should have 'name' field in frontmatter"
    assert 'description:' in content, "SKILL.md should have 'description' field in frontmatter"

def test_directory_structure():
    skill_root = os.path.join(os.path.dirname(__file__), '..')

    required_dirs = ['templates', 'resources', 'config', 'tests', 'utils']
    for dir_name in required_dirs:
        dir_path = os.path.join(skill_root, dir_name)
        assert os.path.isdir(dir_path), f"Directory '{dir_name}' should exist"

    required_files = [
        'SKILL.md',
        'templates/paper_structure.md',
        'resources/formula_guide.md',
        'resources/visualization_guide.md',
        'resources/terminology.json',
        'resources/phrase_patterns.json',
        'config/citation_formats.json'
    ]

    for file_path in required_files:
        full_path = os.path.join(skill_root, file_path)
        assert os.path.exists(full_path), f"File '{file_path}' should exist"

def test_json_files_valid():
    json_files = [
        'resources/terminology.json',
        'resources/phrase_patterns.json',
        'config/citation_formats.json'
    ]

    for json_file in json_files:
        file_path = os.path.join(os.path.dirname(__file__), '..', json_file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON in {json_file}: {e}")

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
