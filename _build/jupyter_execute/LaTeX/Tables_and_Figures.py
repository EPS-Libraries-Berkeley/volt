# Tables and Figures

*Objective: Learn the basic commands to create and edit tables.*

## Create basic table

Use the tabularx package to create a simple table of the US Women’s Soccer Team’s 2019 World Cup Starting Roster: https://www.ussoccer.com/players

Begin with a header row and two columns.
* Your two column headers will be: Position and Last Name – Left align the text of the left column
* Center the text of the right column
* Add vertical and horizontal lines

Add a caption “2019 Team Roster” and center the table.  
Note: Using the \caption{} command will add the phrase “Table 1” in front of caption.

Use package needed: tabularx

Commands needed:  
& = column separator  
\\ = begin new row  
l, r, c = column alignment  

| Position | Last Name |
|-|-|
| GK | Naeher |
| D | Sauerbrunn |
| D | Dahlkemper |
| D | O’Hara |
| D | Dunn |
| M | Mewis |
| M | Ertz |


