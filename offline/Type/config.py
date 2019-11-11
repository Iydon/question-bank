preamble = r'''
\documentclass{exam}
% 使用 XeLaTeX 或者 LuaLaTeX 编译.
\usepackage{ifxetex,ifluatex}
\usepackage{ifthen}
	\ifthenelse{\boolean{xetex}\OR\boolean{luatex}}{}{
		\errmessage{You Should Use XeLaTeX or LuaLaTeX To Compile.}}
% 配置选项.
\usepackage{geometry}
	\geometry{layout=\打印纸张}
\usepackage{xstring}
	\IfStrEq{\展示答案}{true}{\printanswers}{}
% 使用中文, 颜色, 数学符号等.
\usepackage{ctex,xcolor,mathtools,amssymb}
% Exam 文类选项
	% 提示语配置
	\renewcommand{\solutiontitle}{\noindent\textbf{解答:}}
	% 正确答案样式
	\CorrectChoiceEmphasis{\color{black}\bfseries}
	% 分数计量
	\pointpoints{分}{分} % 单复数
	\bonuspointpoints{分 (附加)}{分 (附加)} % 附加分单复数
	% 宏与环境
	\newenvironment{不定项选择}%
		{\begin{oneparchoices}}%
		{\end{oneparchoices}}
	\newenvironment{纵向不定项选择}%
		{\begin{choices}}%
		{\end{choices}}
	\newcommand{\填空}[1]{\fillin[#1]}
	\newcommand{\判断正误}[1]{\fillin[#1][0.25in]}
	\newenvironment{解答}%
		{\begin{solutionorbox}}%
		{\end{solutionorbox}}
	\newenvironment{解析}%
		{\renewcommand{\solutiontitle}{\noindent\textbf{解析:}}\begin{solutionorbox}}
		{\renewcommand{\solutiontitle}{\noindent\textbf{解答:}}\end{solutionorbox}}
% 用户自定义.'''
