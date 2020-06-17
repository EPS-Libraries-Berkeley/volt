# Basics

### What is LaTeX?

LaTeX is a typesetting system that allows you to focus on your content instead of formatting - formatting is done separately from entry.

You tell LaTeX “what it is” not “how it looks."

### LaTeX using Overleaf

* Create documents via a cloud-based account
* Source code or rich text format
* Collaborating and sharing documents
* Versioning and track changes
* Templates for a variety of documents and publishers
* Link with other tools in your research workflow
* Pro account with your berkeley.edu address


#image of side by side document goes here

### Structure of a document

| Term | Description | Example |
|-|-|-|
| Command | Control sequence which performs an action | \newpage|
| Preamble | Block of commands that define the type of document you are writing,  the language you are writing in, the packages you would like to use. Comes before \begin{document}| \documentclass{article}|
| Package | Enable you to create bibliographies, insert images and figures, and write formulas. | \usepackage{amsmath} |
| Environment | Block of code with specific behavior depending on its type | \begin{} & \end{} |
| Body | Content of document enclosed inside an environment | \begin{document} |

### *Note*: 

* Comments: 
Use % to create a comment. Nothing on the line after the % will be typeset.

* Restricted Characters: 
Certain symbols require a backslash to appear, like $, &, #, and %.


### Basic Commands

* **Bold**: \textbf{example}
* *Italics*: \textit{example}
* Underline: \underline{example}

Font typefaces: Change in preamble. More information:
https://v2.overleaf.com/learn/Font_typefaces


### Make Title

1. The simplest option is to use the \maketitle command which draws from the following declarations within the preamble:  
\author  
\date  
\thanks  
\title    
  
2. OR use the  
\begin{titlepage}  
...  
\end{titlepage}  
environment. 

The titlepage environment creates a title page, i.e. a page with no printed page number or heading. It also causes the following page to be numbered page one. 
Formatting is left to you, but commands like \centering, \vspace, and \vfill are helpful.

### Basic Math

\require{verb}

To display math inline with text, place formula or symbol in between $:

\verb|$x + y = z$|

$x + y = z$

#Display mode \mathtt{\[ x + y = z \]}, will center the equation on its own line:
#\[ x + y = z \]


### *EXERCISE 1*

*Objective:  
Practice several basic LaTeX commands in a new project.*


1. Open new project in Overleaf
2. Create title page  
    1. Add [title page] to make preamble command \documentclass[titlepage]{article}
    2.  After \title, add "class LaTeX assignment"
    3.  After \author, add your name
    4.  Confirm that the date is correct or edit if needed
    5.  Create **Title Page** using command \maketitle inserted after \begin{document}
3. Add a new section labeled "Practice" using the \section* command.
4. Add the following paragraph under that section using "inline" math commands:

Commands needed: 
#add commands

