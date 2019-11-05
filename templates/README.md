# 不定项选择题 (单选与多选)
## 横向
```latex
\question[$(分数)$] $(题干)$\par
\begin{不定项选择}
	\choice $(错误答案)$
	\CorrectChoice $(正确答案)$
\end{不定项选择}
\begin{解析}
	$(解析)$
\end{解析}
```

## 纵向
```latex
\question[$(分数)$] $(题干)$
\begin{纵向不定项选择}
	\choice $(错误答案)$
	\CorrectChoice $(正确答案)$
\end{纵向不定项选择}
\begin{解析}
	$(解析)$
\end{解析}
```


# 填空题
## 不定数填空
```latex
\question[$(分数)$] $(题干)$ \填空{$(正确答案)$}
\begin{解析}
	$(解析)$
\end{解析}
```

## 判断正误
```latex
\question[$(分数)$] \判断正误{$(正确答案)$} $(题干)$
\begin{解析}
	$(解析)$
\end{解析}
```


# 简答题
```latex
\question[$(分数)$] $(题干)$
\begin{parts}
	\part[$(分数)$] $(题干)$
		\begin{subparts}
			\subpart[$(分数)$] $(题干)$
			\subpart[$(分数)$] $(题干)$
		\end{subparts}
	\part[$(分数)$] $(题干)$
\end{parts}
\begin{解答}
	$(解答)$
\end{解答}
\begin{解析}
	$(解析)$
\end{解析}
```
