class api:
    '''不定数填空 API

    Argument
    --------
    description: DataRequired
    score: DataRequired
    difficulty: Optional, NumberRange(0, 1): float
    analysis: Optional
    remark: Optional

    Example
    -------
    {
        "type": "不定数填空",
        "description": "本题为\\填空{不定数填空}.",
        "score": "5",
        "difficulty": "0.1",
        "analysis": "这里为解析部分.",
        "remark": "本题考察了模板的使用."
    }
    '''
    def __init__(self, info):
        # set attributions
        requires = ('description', 'score')
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
        '''
        _remark = self._remark or '%'
        _question = f'\\question[{self._score}] {self._description}\\par'
        if self._analysis is not None:
            _analysis = f'\\begin{{解析}}\n{self._analysis}\n\\end{{解析}}'
        else: _analysis=''
        return begin + '\n'.join((_remark, _question, _analysis)) + end

    def _preprocess(self):
        # score
        self._score = int(self._score)
        # difficulty
        if self._difficulty is not None:
            self._difficulty = float(self._difficulty)
        # remark
        if self._remark is not None:
            _remarks = (f'% {line}' for line in self._remark.splitlines())
            self._remark = '\n'.join(_remarks)
