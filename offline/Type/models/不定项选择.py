import random


class api:
    '''不定项选择 API

    Argument
    --------
    description: DataRequired
    score: DataRequired
    choices: DataRequired: Dict[str, int]
    difficulty: Optional, NumberRange(0, 1): float
    analysis: Optional
    remark: Optional

    Example
    -------
    {
        "type": "不定项选择",
        "description": "本题为不定项选择.",
        "score": "5",
        "difficulty": "0.1",
        "analysis": "这里为解析部分.",
        "choices": {
            "错误答案-1": "0",
            "错误答案-2": "0",
            "正确答案-3": "1",
            "正确答案-4": "1"
        },
        "remark": "本题考察了模板的使用."
    }
    '''
    def __init__(self, info):
        # set attributions
        requires = ('description', 'score', 'choices')
        options = ('difficulty', 'analysis', 'remark')
        for require in requires:
            setattr(self, '_'+require, info.get(require))
        for option in options:
            setattr(self, '_'+option, info.get(option, None))
        # preprocess
        self._preprocess()

    def render(self, begin='\n', end='\n'):
        '''Render the template using `info`.

        Argument
        --------
        begin: str, at the start of the rendered-text
        end: str, at the end of the rendered-text

        Example
        -------
        >>> print(self.render())
        % 本题考察了模板的使用.
        \\question[5] 本题为不定项选择.\\par
        \\begin{不定项选择}
        \\choice 错误答案-2
        \\CorrectChoice 正确答案-4
        \\CorrectChoice 正确答案-3
        \\choice 错误答案-1
        \\end{不定项选择}
        \\begin{解析}
        这里为解析部分.
        \\end{解析}
        '''
        _remark = self._remark or '%'
        _question = f'\\question[{self._score}] {self._description}\\par'
        _choices = f'\\begin{{不定项选择}}\n{self._choices}\n\\end{{不定项选择}}'
        if self._analysis is not None:
            _analysis = f'\\begin{{解析}}\n{self._analysis}\n\\end{{解析}}'
        else: _analysis=''
        return begin + '\n'.join((_remark, _question, _choices, _analysis)) + end

    def _preprocess(self):
        # score
        self._score = int(self._score)
        # choices
        _choices = list(self._choices.items())
        random.shuffle(_choices)
        self._choices = '\n'.join((f'\\CorrectChoice {c}' if int(f) else f'\\choice {c}')
                for c, f in _choices)
        # difficulty
        if self._difficulty is not None:
            self._difficulty = float(self._difficulty)
        # remark
        if self._remark is not None:
            _remarks = (f'% {line}' for line in self._remark.splitlines())
            self._remark = '\n'.join(_remarks)
