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

```{image} ./images/template.png
:alt: two panel view of Overleaf platform
:width: 500px
:align: center
```

### Structure of a document

| Term | Description | Example |
|-|-|-|
| Command | Control sequence which performs an action | `\newpage`|
| Preamble | Block of commands that define the type of document you are writing,  the language you are writing in, the packages you would like to use. Comes before `\begin{document}`| `\documentclass{article}`|
| Package | Enable you to create bibliographies, insert images and figures, and write formulas. | `\usepackage{amsmath}` |
| Environment | Block of code with specific behavior depending on its type | `\begin{}` & `\end{}` |
| Body | Content of document enclosed inside an environment | `\begin{document}` |

:::{note}
- Comments: Use % to create a comment. Nothing on the line after the % will be typeset.
- Restricted Characters: Certain symbols require a backslash to appear, like $, &, #, and %.
:::

### Basic Commands
- *Bold*: \textbf{example}
- _Italics_ : \textit{example}
- {u}`Underline`: \underline{example}

Font typefaces:
Change font designations in preamble. More information about fonts and typefaces:
[https://v2.overleaf.com/learn/Font_typefaces](https://v2.overleaf.com/learn/Font_typefaces)

### Make Title
The simplest option for making a title is to use the `\maketitle` command which draws from the following declarations within the preamble:
`\author`
`\date`
`\thanks`
`\title`

### Lists
Use the `\begin{itemize}...\end{itemize}` environment to create unnumbered lists.

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

Use the `\begin{enumerate}...\end{enumerate}` environment to create numbered lists.

### Accessible PDFs

Take steps to create an accessible PDF when you initiate a new project. The main considerations:
- *Tagging* assists screen readers, differentiating elements like headers, body text, figures, and equations.
- *Descriptions* are required for particular content elements.
  - *Images*: provide alternative or alt-text for images and figures. More information follows below.
  - *Tables*: add `\tagpdfsetup` to describe table structure before the `\tabular` environment.

In this section, we introduce the text below to enable *tagging* essential for an accessible PDF. More content-specific information follows in later sections.

```
\DocumentMetadata{tagging=on,
    tagging-setup={math/setup=mathml-SE},
    pdfstandard=ua-2,
    lang=en-US
}
```

Read more:
- [Information from Overleaf on *Creating accessible PDFs in LaTeX*:] (https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs)
- [More in-depth documentation from the LaTeX Tagging Project:] (https://latex3.github.io/tagging-project/documentation/usage-instructions)


### Exercise

::::{hint} Exercise 1: Basic LaTeX Commands

_Objective: Practice several basic LaTeX commands in a new project._

1. Open a new project in [Overleaf](https://www.overleaf.com/edu/berkeley). 
2. Create Title 
- After `\title`, add "VOLT LaTeX Basics Assignment" 
- After `\author`, add your name 
- Confirm that the date is correct or edit if needed
- Display **Title** using command `\maketitle` inserted after `\begin{document}`
3. Add a new section labeled "Practice" using the `\section*` command. 
4. Add a new section labeled "California Road Trip Destinations"
5. Make a numbered list of four items, for example: 
  Yosemite \
  Big Sur \
  Lake Tahoe \
  Death Valley 

:::{hint}
*Commands needed:* `\section*{}`, `\begin{enumerate}...\end{enumerate}`.
:::

:::{note} Questions?
:class: dropdown
Compare your LaTeX code to the solutions document at  [https://www.overleaf.com/read/djdcymcpxcxq](https://www.overleaf.com/read/djdcymcpxcxq) to troubleshoot. 
:::
::::

## Mathematics and Equations

### Simple Operators, Subscripts, Superscripts & More

To render simple equations, you also need to know syntax and commands for operators, relations, subscripts, superscripts, and fractions.

#### Operators & Relations:
+, -, =, >, < work as expected. Here are some other commands:

| Command | Display | 
| :---: | :---: | 
| `\times` | $\times$ | 
| `\div` | $\div$ | 
| `\geq` | $\geq$ |
| `\neq` | $\neq$ |
| `\pm` | $\pm$ |
| `\leq` | $\leq$ |
| `\cdot` | $\cdot$ | 
| `\approx` | $\approx$ |

### Basic Math
To display math inline with text, place formula or symbol in between $:

`$x + y = z$` renders inline: $x + y = z$ 

Display mode `\[ x + y = z \]` or `$$ x + y = z $$` will center the equation on its own line: \
$$x + y = z$$

 
**Subscript:** use the underscore (_) / **Superscript**: use the carret (^)  

If the subscript or superscript includes more than one character, enclose it in curly brackets--otherwise the command applies only to the first character. 

**Example:** `$x^n+1$` gives $x^n+1$ but `$x^{n+1}$` gives $x^{n+1}$  

**Fractions:**  

To display a fraction, use the command `\frac` followed by the numerator and denominator in curly brackets.

**Example:** `\frac{1}{x}` gives $\frac{1}{x}$

### Next Steps: Greek Letters, Integrals & More

#### Greek Letters

Many equations and formulas use Greek letters. The command is simple - just the backslash and the name of the letter. Capitalize the command to get the capital letter. Here are some examples:  

| Command | Display | Command | Display | Command | Display |
| --- | --- | --- | --- | --- | --- |
| `\alpha` | $\alpha$ | `\lambda` | $\lambda$ | `\rho` | $\rho$ |
| `\beta` | $\beta$ | `\Lambda` | $\Lambda$ | `\sigma` | $\sigma$ |
| `\Gamma` | $\Gamma$ | `\mu` | $\mu$ | `\\hi` | $\Phi$ |
| `\delta` | $\delta$ | `\pi` | $\pi$ | `\omega` | $\omega$ | 
| `\Delta` | $\Delta$ ||| `\Omega` | $\Omega$ |

Greek letters that are the same in English are an exception, for example, use A for Alpha, B for Beta, Z for Zeta. For more commands, see the Overleaf [list of Greek letters](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols#Greek_letters).

:::{seealso} More help with Greek letters and Symbols
Apart from hand-coding Greek letters and other symbols, Berkeley's premium subscription allows us to take advantage of the [Overleaf Symbol Palette](https://www.overleaf.com/blog/new-feature-find-symbols-quicker-with-our-new-symbol-palette-for-premium). The Symbol Palette helps you quickly find commonly used symbols, and will also tell you which packages you need to use them.  
:::

### Limits & Integrals

There are also commands for common operations that take upper and lower bounds: 

**Limits:**

```
\[
lim_{x \to \infty} f(x) 
\]
``` 
results in 

:::{math}
:enumerated: false
lim_{x \to \infty} f(x)
:::

**Integrals:**

```
\[  
\int_{a}^{b} x^2 dx 
\]  
```

results in  
:::{math}
:enumerated: false
\int_{a}^{b} x^2 dx
:::

### More Advanced: Math Packages

### *amsmath* & *amssymb* Packages

LaTeX has many packages that you can use to extend its capabilities. The *amsmath* and *amssymb* packages provide you with additional symbols and commands for structuring equations.

To include them, add these commands to the preamble of your LaTeX document: 
`\usepackage{amsmath}` \
`\usepackage{amssymb}` 

### *amsmath*: Equations Environment

Use the `\begin{equation}...\end{equation}` command to include a numbered equation in display mode. 

```
\begin{equation}
\frac{\partial Q}{\partial t} = \frac{\partial s}{\partial t}
\end{equation}
```
results in
:::{math}
:enumerated: false
\frac{\partial Q}{\partial t} = \frac{\partial s}{\partial t} 
:::

:::{note} 
Use `\begin{equation*}` for unnumbered equations.
:::

### Exercise

::::{hint} Exercise 2: Mathematical Equations
_Objective: Experiment with mathematical notations in LaTeX._ 

1. Add the following paragraph under that section using "inline" math commands: 

"We know the initial pressure $P_0 = 7.00 \times 10^5 Pa$, the initial temperature $ T_0 = 18.0 ^{\circ}C$, and the final temperature $T_f = 35.0 ^{\circ}C$." 

2. Recreate this text in your document:  
A quadratic equation is an equation of the form $ax^2 + bx + c = 0$ and such equations can be solved using the quadratic formula:

:::{math}
:enumerated: false
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
:::

:::{hint}
Commands needed: `\frac{}{}`, `\pm`, `\sqrt{}`, `\[...\]` or `$...$` \
Degree can be represented several ways such as `$^\circ$` or `\degree` (requires the `\usepackage{gensymb}`). \ Subscripts and superscripts are written using the symbols _ and ^. 
:::
::::

::::{note} **Additional challenges**
:class: dropdown

Recreate this equation in your document: 
:::{math}
:enumerated: false
i\hbar\frac{\partial}{\partial t}\psi = \hat{H}\psi 
:::

:::{hint}
- Commands needed: `\partial`, `\psi`, `\hbar`, `\hat{H}` 
- Packages needed: `\usepackage{amsmath}`, `\usepackage{amssymb}` 
- Environment needed: `\begin{equation*} ... \end{equation*}`  
:::

Recreate this equation in your document: 
:::{math}
:enumerated: false
\frac{d\sigma}{d\lambda}= \left|\frac{2\mu}{\hbar^2}\int_{0}^{\infty}\frac{sin(\Delta kr)}{\Delta kr}V(r)r^2dr\right|^2
:::
    
:::{hint} 
- Commands needed: `\infty`, `\sigma`, `\lambda`, `\mu`, `\Delta`, `\left|`, `\right|` 
- Environment needed: `\begin{equation*} ... \end{equation*}` 
:::
::::


## Creating Bibliographies in LaTeX

_Objective: Learn the basic commands to create and edit in-text citations and bibliographies_

### Getting started with a `.bib` file
In order to include in-text citations and a bibliography, the document needs to refer to a .bib file.
There are three ways to include a `.bib` file in a project in Overleaf.

1. Upload your own `.bib` file that you create or export from a citation manager.
2. Link to a URL (`.bib`).
3. Sync your Overleaf account with Zotero.

If you are working in a traditional LaTeX editor, locate the `.bib` file in the directory.

What does a citation in a `.bib` file look like?

```bibtex
@article{drachen2016sharing,
  title = {Sharing data increases citations},
  author={Drachen, Thean and Ellegaard, Ole and Larsen,
  Asger and Dorch, S{\o}ren},
  journal={Liber Quarterly},
  volume={26},
  number={2},
  year={2016},
  url={https://doi.org/10.18352/lq.10149},
}

@misc{fsci2021,
  author={Teplitzky, Samantha, and Tranfield, Wynn},
  title={Introduction to Open and Reproducible Practices in 
  {Earth Sciences}},
  maintitle={Case Studies in the {Earth Sciences: Current} 
  Approaches to publishing, data and computation},
  eventtitle={{Force 11 Scholary Communication Institute (FSCI)}},
  venue={Virtual},
  eventdate={2021-07-27/2021-08-03},
}
```

KEY: The **citation key** is the internal label inside the `\cite{} command used to call in a citation or reference a source. \
Example: `drachen2016sharing` or `fsci2021`

To cite Drachen 2016 within your text, type `\cite{drachen2016sharing}`

### Bibliography Packages

We will use the **biblatex** package to generate in-text citations and bibliographies. **Biblatex** is a flexible package for generating citations.

When adding a bibligraphy, you will need to add commands to the preamble. 

Commands required for the **preamble**:

`\usepackage[backend=biber,style=apa]{biblatex}`

- The above syntax calls in the biblatex package.
- `backend=biber` defines *Biber* as the interface between the .bib data file and the LaTeX document. 
- `style=apa` sets your citation rules to APA style (this can be swapped for `ieee`, `mla`, `nature`, etc.). 

`\addbibresource{example.bib}`

The above command calls in the .bib file, which has the citation information for in-text citations and the bibliography. 

In an article or book chapter, the command \printbibliography inserts the bibliography, which will contain citations referenced in the text. 

Find more information [visit the Overleaf page on bibliography management](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX).

### In-text citations

| Command | Description |
| --- | --- |
| `\cite{}` | bare citation command (according to style) |
|`\parencite{}` | parenthetical citation |
|`\citeauthor{}`| prints author name(s) |
|`\textcite{}`| prints authors followed by a citation label enclosed in ()|
|`\nocite{*}`| prints publication in bibliography without a citation |
|`\citeyear{}`| prints only the year field |

#### Examples
| Command	|	Result |
| --- | --- |
| `\cite{knyazeva_duplex_2013}`	| Knyazeva and Pohl 2013 |
| `\parencite{singh_2013}` | (Singh et al. 2013) |
| `\citeauthor{campbell_how_2011}` |	Campbell and Cabrera |
| `\textcite{elsabbagh_microstructure_2014}`| Elsabbagh, Hamouda, and Taha (2014) |

### Exercise

:::{hint} Exercise 3: Adding a Bibliography

_Objective: Learn to create, edit or upload a `.bib` file, use basic citation commands, and display a bibliography._

*Step 1: Create a `.bib` file and add references*

1. Create a new file within your Overleaf project (click on the *New file* paper icon in the upper left) and name it references.bib

```{image} ./images/references.png
:alt: Overleaf document menu highlighting create new file
:width: 400px
:align: center
```
2. Search for these three articles and books in Google Scholar and locate their *BibTeX* formatted citations by clicking on the quotations marks and then selecting **BibTeX**.
   - 10.1126/science.1214319
   - Hydraulic power system analysis
   - 10.1103/PhysRevB.100.094418
   
```{image} ./images/scholar_bibtex.png
:alt: Google Scholar cite menu screenshot
:width: 400px
:align: center
``` 

3. Paste each citation completely within your .bib file. (No preamble code is needed).

*Step 2: Displaying the bibliography*

- To display bibliography in author-year style convention, add package and style command to preamble: 
```
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}
```
- And use these commands within document: 

`\printbibliography`
`\nocite{*}` 

*Step 3: Practicing citation commands*

Try using citation commands to recreate the sentence below: 

"In the example provided, Weber et al. 2012 describes the experiment, but Akers, Gassman, and Smith contradict these conclusions." 

Commands needed: `\cite{}`, `\citeauthor{}`

For additional examples and more information, please visit Overleaf's page on [bibliography management in LaTeX](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)

:::

## Figures

### Uploading a figure

Incorporating images and figures into your Overleaf project is best accomplished by creating your figures, particularly graphs and plots, outside of Overleaf and then importing them into Overleaf.

Click on the "upload" icon and navigate to the location of your figure.

```{image} ./images/tables_figure.png
:alt: Overleaf menu to upload images
:width: 400px
:align: center
``` 

#### Image Placement
Images and figures require a graphics package. Include `\usepackage{graphicx}` in the preamble of your document.

Within the text, place the image using the command `\includegraphics{filename.jpg}`.

#### Image Description and Alt text
Additional specifiers can be added to resize image and to add descriptive text.

1. Express size a proportion of linewidth: `width=0.25\linewidth`
2. Add description: `alt={image of cat typing on computer}`
3. Put it all together: `\includegraphics[width=0.25\linewidth,alt={image of cat typing on computer}]{filename.jpg}

#### Figure Placement

Use the following specifiers to adjust the placement of your figures.

| Specifier | Description |
| --- |--- |
|h|Place the float here: approximately, not exactly, at the same point it occurs in the source text|
|t|Position at the top of the page|
|b|Position at the bottom of the page|
|p|Put on a special page for floats only|
|!|Override internal parameters LaTeX uses for determining \"good\" float positions|
|H|Places the float at precisely the location in the LaTeX code. Requires the float package. This is somewhat equivalent to h!|

### Exercise

:::{hint} Exercise 4: Uploading an Image or Figure
_Objective: Learn to upload and position figures in Overleaf._

**Upload a figure**

- To upload image, choose an image of your own, or find file at: \
[https://github.com/EPS-Libraries-Berkeley/LaTeX/blob/master/keyboard_cat.png](https://github.com/EPS-Libraries-Berkeley/LaTeX/blob/master/keyboard_cat.png)
- Download keyboard_cat.png or image of your choice, and upload file to the Overleaf project.
- Place image with these commands:
  - Add to preamble: `\usepackage{graphicx}`
  - Add to main document: `\includegraphics[width=0.4\linewidth,alt={photo of cat from above with left paw near keyboard}]{keyboard_cat}`

```{image} ./images/keyboard_cat.png
:alt: cat with paw near keyboard
:width: 400px
:align: center
```

**Designate figure position**
Use b, t, h to see within the figure environment to determine or override placement. You might need to add additional text in the document to see how the figure placement varies.

```
\begin{figure}[b]
\centering
\includegraphics[width=0.6\linewidth]{keyboard_cat}
\end{figure}
```

:::

Compare your LaTeX code to the solutions at:  [https://www.overleaf.com/read/hsjrcdzkndvd](https://www.overleaf.com/read/hsjrcdzkndvd) to troubleshoot. 
 