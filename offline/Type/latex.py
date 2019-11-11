from .config import preamble


class api:
    '''Convert to \\LaTeX format.

    Argument
    --------
    学校全称: Optional
    学校英文: Optional
    学校简称: Optional
    学年学期: Optional
    科目全称: Optional
    科目代码: Optional
    试卷类别: Optional
    考试方式: Optional
    打印纸张: Optional
    展示答案: Optional
    '''
    def __init__(self, **kwargs):
        self._info = {
            '学校全称': '南方科技大学',
            '学校英文': 'Southern University of Science and Technology',
            '学校简称': 'SUSTech',
            '学年学期': '2019--2020学年秋季学期',
            '科目全称': '计算金融',
            '科目代码': 'MA216',
            '试卷类别': 'A',
            '考试方式': '闭卷',
            '打印纸张': 'a4paper',
            '展示答案': 'false',
        }
        self._info.update(kwargs)

    def render(self, body='', customization=''):
        '''Render the template.

        Argument
        --------
        body: str, document body
        customization: str, customized preamble
        '''
        _question = f'\\begin{{questions}}\n{body}\n\\end{{questions}}'
        _document = f'\\begin{{document}}\n{_question}\n\\end{{document}}'
        return '\n'.join((self._preamble(customization), _document))

    def _preamble(self, customization=''):
        '''Preamble of \\LaTeX file.

        TODO
        ----
        1. 目前仅支持 a4paper, 有待处理 a3paper 的结构问题.
        2. 常用的用户自定义 (math=True).
        3. 将设置统一放在 `config.py` 下.
        '''
        _head = '% !Mode:: "TeX:UTF-8"\n% !TEX program  = xelatex'
        _commands = '\n'.join(f'\\newcommand{{\\{k}}}{{{v}}}' for k, v in self._info.items())
        _preamble = preamble
        return '\n'.join((_head, _commands, _preamble, customization))
