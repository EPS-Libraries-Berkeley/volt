# Introduction to LaTeX Workshop

## LaTeX Basics

### Introduction
LaTeX is a typesetting system that allows you to focus on your content instead of formatting - formatting is done separately from entry.

You tell LaTeX “what it is” not “how it looks.”

### LaTeX using Overleaf
- Create documents via a cloud based account
- Source code or rich text format
- Collaborating and sharing documents
- Versioning and track changes
- Templates for a variety of documents and publishers
- Link with other tools in your research workflow
- Pro account with your *berkeley.edu* address

### Example
Look at the template below to get a sense of how Overleaf works. On the left side, the content is written in LaTeX. On the right side, the rendered document.

![two panel view of Overleaf platform](template.png 'Overleaf template')

### Structure of a document

| Term | Description | Example |
|-|-|-|
| Command | Control sequence which performs an action | `\\newpage`|
| Preamble | Block of commands that define the type of document you are writing,  the language you are writing in, the packages you would like to use. Comes before \\begin{document}| `\\documentclass{article}`|
| Package | Enable you to create bibliographies, insert images and figures, and write formulas. | `\\usepackage{amsmath}` |
| Environment | Block of code with specific behavior depending on its type | `\\begin{}` & `\\end{}` |
| Body | Content of document enclosed inside an environment | `\\begin{document}` |

:::{note}
- Comments: Use % to create a comment. Nothing on the line after the % will be typeset.
- Restricted Characters: Certain symbols require a backslash to appear, like $, &, #, and %.
:::

### Basic Commands
- *Bold*: \textbf{example}
- _Italics_ : \textit{example}
- {u}`Underline`: \underline{example}

Font typefaces:
Change font designations in preamble. More information:
https://v2.overleaf.com/learn/Font_typefaces

### Make Title
The simplest option for making a title is to use the \maketitle command which draws from the following declarations within the preamble:
\author
\date
\thanks
\title

### Lists
Use the \begin{itemize}...\end{itemize} environmetn to create unnumbered lists.

:::{hint}

```
\begin{itemize}
\item Apples
\item Cherries
\item Oranges
\item Peaches
\item Watermelon
\end{itemize}
```
---

This code results in:

- Apples
- Cherries
- Oranges
- Peaches
- Watermelon

:::

Use the \begin{enumerate}...\end{enumerate} environment to create numbered lists.

### Packages and Accessible PDFs

The steps for creating an accessible PDF begin when you initiate a new project.
Add the text below to enable tagging essential for an accessible PDF.

\DocumentMetadata{tagging=on,
    tagging-setup={math/setup=mathml-SE},
    pdfstandard=ua-2,
    lang=en-US
}

Read more:
- Information from Overleaf on *Creating accessible PDFs in LaTeX*: https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs
- More indepth documentation from the LaTeX Tagging Project: https://latex3.github.io/tagging-project/documentation/usage-instructions

Instructions for accessibility requirements related to images or figures follow below.