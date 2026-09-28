# LaTeX for Dissertations

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
- Sync with other tools in your research workflow
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


### Document Metadata
#### Generic Document Metadata + Titling
The simplest option for making a title is to use the `\maketitle` command which draws from the following metadata declarations within the preamble: \
`\author` \
`\date` \
`\thanks` \
`\title` 

#### Thesis and Dissertation Document Metadata
The UC Berkeley Accessible Thesis Template also includes a section for metadata under the `\hypersetup` block in the preamble listed as: \
`pdftitle = {Thesis Title},` \
`pdfauthor = {Bear, Oski},` \
`pdflang=en-US`

### Basic Commands
- *Bold*: \textbf{example}
- _Italics_ : \textit{example}

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

Take steps to create an accessible PDF when you initiate any new project. 

1. Enable basic *tagging* essential for an accessible PDF in the document's metadata. *Tagging* assists screen readers, differentiating elements like headers, body text, figures, and equations.

```
\DocumentMetadata{tagging=on,
    tagging-setup={math/setup=mathml-SE},
    pdfstandard=ua-2,
    lang=en-US
}
```

2. **Descriptions** or alternative text are required for particular content elements:
- **Images**: provide alternative or alt-text for images and figures. 
- **Tables**: add `\tagpdfsetup` to describe table structure before the `\tabular` environment.
3.  **Artifacts for decorative content**: Mark purely decorative or duplicative graphics so assistive technology skips them.
4. Following the export and download of your PDF, **verify the tag structure** in Adobe Acrobat.

:::{important} UC Berkeley's Accessible Thesis Template
Created in 2026 by Chrystal Chern (UCB PhD '24) and Claudio Perez (UCB PhD '26), and adapted from the UC Berkeley thesis template maintained by Professor Paul Vojta, the **UC Berkeley Accessible Thesis Template** complies with current WCAG 2.1 AA Accessibility requirements, and preserves the Graduate Division's required formatting and layout while supporting LaTeX PDF tagging. 

Find the template hosted on Overleaf at: 
[https://www.overleaf.com/latex/templates/uc-berkeley-thesis-template-accessible/zmfmywbvmshw](https://www.overleaf.com/latex/templates/uc-berkeley-thesis-template-accessible/zmfmywbvmshw)

The syntax below is used in the Dissertation Template to create an accessible PDF from your dissertation manuscript:

```
\DocumentMetadata{
  lang         = en-US,
  pdfstandard  = ua-2,
  pdfstandard  = a-4,
  tagging-setup = {
    modules = {phase-III, title, table, firstaid, names, toc, sec},
    table/tagging       = presentation,
    table/header-rows   = {1},
  }
}
```

Find more information about formatting your dissertation from the UC Berkeley Graduate Division at: 

[https://grad.berkeley.edu/academics/degree-progress/dissertation/#formatting-your-manuscript](https://grad.berkeley.edu/academics/degree-progress/dissertation/#formatting-your-manuscript)

:::

Read more about accessibility:
- Information from Overleaf on *Creating accessible PDFs in LaTeX*:[https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs] (https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs)
- More in-depth documentation from the LaTeX Tagging Project: [https://latex3.github.io/tagging-project/documentation/usage-instructions](https://latex3.github.io/tagging-project/documentation/usage-instructions)


### Exercise 1

::::{hint} Exercise 1: Basic LaTeX Commands

_Objective: Practice several basic LaTeX commands in a new project._

1. Open a new project in [Overleaf](https://www.overleaf.com/edu/berkeley). 
2. Add syntax required to recreate an [accessible PDF](https://eps-libraries-berkeley.github.io/volt/latex-workshop/#accessible-pdfs) on **line 1** of the main.tex file
3. Create Title 
- After `\title`, add "VOLT LaTeX Basics Assignment" 
- After `\author`, add your name 
- Confirm that the date is correct or edit if needed
- Display **Title** using command `\maketitle` inserted after `\begin{document}`
4. Add a new section labeled "Practice" using the `\section*` command. 
5. Add a new section labeled "California Road Trip Destinations"
6. Make a numbered list of four items, for example: 
  Yosemite \
  Big Sur \
  Lake Tahoe \
  Death Valley 

:::{hint}
*Commands needed:* `\section*{}`, `\begin{enumerate}...\end{enumerate}`.
:::

:::{note} Questions?
:class: dropdown
Compare your LaTeX code to the solutions document at  [https://www.overleaf.com/read/hfbmjwstnbwh#f2e2e9](https://www.overleaf.com/read/hfbmjwstnbwh#f2e2e9) to troubleshoot. 
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

:::{seealso} Help with Greek letters and Symbols
For Greek letter commands, see the Overleaf [list of Greek letters](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols#Greek_letters).

Apart from hand-coding Greek letters and other symbols, Berkeley's premium subscription allows us to take advantage of the [Overleaf Symbol Palette](https://www.overleaf.com/blog/new-feature-find-symbols-quicker-with-our-new-symbol-palette-for-premium). The Symbol Palette helps you quickly find commonly used symbols, and will also tell you which packages you need to use them.  
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

### Exercise 2

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
Commands needed: `\qty`, `\degree C`, `\frac{}{}`, `\pm`, `\sqrt{}`, `\[...\]` or `$...$` \

In LaTeX, there is often more than one way to typeset a concept. For example, **degree** can be represented several ways such as `^\circ` or `\degree`. Compatability with accessibility packages requires the `\usepackage{siunitx}` and the joint commands: `\qty{number}{\degree C}`.

Subscripts and superscripts are written using the symbols _ and ^. 
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

## Tables
Basic tables can be created with a combination of the commands below, and the utilization of appropriate tagging. 

:::{note}
To comply with PDF-tagging, the header row of the table is declared to `LaTeX`'s PDF-tagging code through `table/header-rows={1}` in `setup.tex` in the Thesis Template, so it is tagged as a real table header (`<TH>`) rather than hidden as an artifact.
:::

| Basic Commands | Description |
| --- | --- |
| `l, r, c` | column alignment |
| \`&` | ampersand separates columns |
| `\\` | double backslash begins new row |
| `\hline` or `\toprule` `\bottomrule`| horizontal line |
| `\|` | vertical line | 
| `table` | table environment: creates the "wrapper" that treats the table as a floating object |
|`tabular`| tabular environment: creates the actual grid of data |

### Example: Two column table

::::{grid} 1 1 2 2

:::{card}
:header: Table syntax

```python
\usepackage{tabularx}
....
\begin{table}
\caption{Inventory}
\begin{tabular}{lc}
Item & Quantity 
\hline
Widget & 1 \\
Gadget & 2 \\
Cable & 3 \\
\end{tabular}
\end{table}
```
:::

:::{card}
:header: Table example
:::{table} Inventory
:label: table
:align: center

| Item | Quantity |
| --- | --- |
| Widget | 1 |
| Gadget | 2 |
| Cable | 3 |

:::
::::

### Exercise 3

::::{hint} Exercise 3: Create a table

_Objective: Create a two column table._

1. Using the 2026 [Golden State Valkyries](https://stats.wnba.com/team/1611661331/players-traditional/?sort=PTS&dir=1) roster create a table showing the top 5 scorers.
2. Like the example below, create two columns with the headers: player and total points.
3. Include a caption for the table

| Player | Total Points |
| --- | --- |
| Williams | 560 |
| Burton | 536 |
| Salaun | 509 |

:::{hint}
*Commands needed:* `&`, `\\`, `\caption`, `\begin{table}...\end{table}`, `\begin{tabular}...\end{tabular}`
:::
::::

## Figures and Images

### Uploading a figure or images

Incorporating images and figures into your Overleaf project is best accomplished by creating your figures, particularly graphs and plots, outside of Overleaf and then importing them into Overleaf.

Click on the "upload" icon and navigate to the location of your figure.

```{image} ./images/tables_figure.png
:alt: Overleaf menu to upload images
:width: 400px
:align: center
``` 

#### Image Placement
*Most documents*: Uploading images and figures requires a graphics package. 

1. Include `\usepackage{graphicx}` in the preamble of your document.
2. Within the text, place the image using the command `\includegraphics{filename.jpg}`.

:::{note}
*UC Berkeley Thesis Template*: In addition to the `\includegraphics` command, the template uses the `\begin{figure}... \end{figure}` to act as a floating container that assists with document layout as well as referring to the figure within the document.
:::

#### Image Description and Alt text
Additional specifiers can be added to resize image and to add descriptive text.

1. Express size a proportion of linewidth: `width=0.25\linewidth`
2. Add description: `alt={image of cat typing on computer}`
3. Put it all together: `\includegraphics[width=0.25\linewidth,alt={image of cat typing on computer}]{filename.jpg}`

OR

4. Use the `figure` environment:
```
\begin{figure}
\centering
\includegraphics[width=0.5\linewidth,
  alt={photo of cat from above with left paw near keyboard.}]{keyboard_cat.png}
\caption{Cat sitting at keyboard.}
\label{fig:keyboard_cat}
\end{figure}
```

### Exercise 4

:::{hint} Exercise 4: Uploading an Image or Figure
_Objective: Learn to upload figures in Overleaf._

**Upload a figure**

- To upload image, choose an image of your own, or find file at: \
[https://github.com/EPS-Libraries-Berkeley/LaTeX/blob/master/keyboard_cat.png](https://github.com/EPS-Libraries-Berkeley/LaTeX/blob/master/keyboard_cat.png)
- Download keyboard_cat.png or image of your choice, and upload file to the Overleaf project.
- Place image with these commands:
  - Add to preamble: `\usepackage{graphicx}`
  - Add to the figure to main document with commands shown above.

```{image} ./images/keyboard_cat.png
:alt: cat with paw near keyboard
:width: 400px
:align: center
```
:::

:::{seealso} Figure Placement
:class: dropdown

**Designate figure position**
Use b, t, h to see within the figure environment to determine or override placement. You might need to add additional text in the document to see how the figure placement varies.

Use the following specifiers to adjust the placement of your figures.

| Specifier | Description |
| --- |--- |
|h|Place the float here: approximately, not exactly, at the same point it occurs in the source text|
|t|Position at the top of the page|
|b|Position at the bottom of the page|
|p|Put on a special page for floats only|
|!|Override internal parameters LaTeX uses for determining \"good\" float positions|
|H|Places the float at precisely the location in the LaTeX code. Requires the float package. This is somewhat equivalent to h!|

```
\begin{figure}[b]
\centering
\caption{Gratuitous cat picture to demonstrate image commands}
\includegraphics[width=0.4\linewidth,alt={photo of cat from above with left paw near keyboard}]{keyboard_cat}
\end{figure}
```
:::


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

**Key**: The **citation key** is the internal label inside the `\cite{}` command used to call in a citation or reference a source.

**Example:** To cite Drachen 2016 within your text, type `\cite{drachen2016sharing}`

### Bibliography Packages

We will use the **biblatex** package to generate in-text citations and bibliographies. **Biblatex** is a flexible package for generating citations.

When adding a bibligraphy, you will need to add commands to the preamble. 

Commands required for the **preamble**:

`\usepackage[backend=biber,style=apa]{biblatex}` calls in the biblatex package.
- `backend=biber` defines *Biber* as the interface between the .bib data file and the LaTeX document. 
- `style=apa` sets your citation rules to APA style (this can be swapped for `ieee`, `mla`, `nature`, etc.). 

`\addbibresource{example.bib}` calls in the .bib file, which has the citation information for in-text citations and the bibliography. 

`\printbibliography` inserts the bibliography, which will contain citations referenced in the text. 

:::{note}
*UC Berkeley Thesis Template*: These elements are all present but come together differently due the template's more complex structure.
:::

Find more information [visit the Overleaf page on bibliography management](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX).

### In-text citations

| Command | Description | Example |
| --- | --- | --- |
| `\cite{}` | bare citation command (according to style) | Knyazeva and Pohl 2013 |
|`\parencite{}` | parenthetical citation | (Singh et al. 2013) |
|`\citeauthor{}`| prints author name(s) | Campbell and Cabrera |
|`\textcite{}`| prints authors followed by a citation label enclosed in ()| Elsabbagh, Hamouda, and Taha (2014) |
|`\nocite{*}`| prints publication in bibliography without a citation | |

### Exercise 5

:::{hint} Exercise 5: Adding a Bibliography

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



Compare your LaTeX code to the solutions at:  [https://www.overleaf.com/read/hfbmjwstnbwh#f2e2e9](https://www.overleaf.com/read/hfbmjwstnbwh#f2e2e9) to troubleshoot. 
 