--------------------------------------------------------------------------------
### GDI 8.Vorlesung Videoaufzeichnung ##########################################
--------------------------------------------------------------------------------

R...Ritter  = Knights say allways the truth.  
S...Schurke = Knaves are allways lying.  




--------------------------------------------------------------------------------
You meet two people A and B.  
- A says "I am a knave or B is a knight."  
- What are A and B?  

    | A B | A=S | B=R | A=S or B=R | Kann A sagen? |  
    | R R |  0  |  1  |     1      |       1       |<<  
    | R S |  0  |  0  |     0      |       0       |  
    | S R |  1  |  1  |     1      |       0       |  
    | S S |  1  |  0  |     1      |       0       |  

- What are A and B?  




--------------------------------------------------------------------------------
1.Trio: (Three is a crowd-pleaser)  
- A and B say the following:  
  - A: All of us are knaves.  
  - B: Exactly one of us is a knave.  
- Can be determined what B is?  
- Can be determined what C is?  

    | A B C |
    | S R R |
    | S S R |

- Can be determined what B is? No he is either a knight or a knave.
- Can be determined what C is? Yes he is a knight.




--------------------------------------------------------------------------------
2.Trio:  
- We have 3 inhabitants A,B and C.  
- A and B make following statements:  
  - A: B is a knave.  
  - B: A and C are of the same type.  
- What is C?  


    | # | A B C | A:B=S | B:A=C |Kann A sagen?|Kann B sagen?|  
    | 1 | R R R |   0   |   1   |      0      |      1      |  
    | 2 | R R S |   0   |   0   |      0      |      0      |  
    | 3 | R S R |   1   |   1   |      1      |      0      |  
    | 4 | R S S |   1   |   0   |      1      |      1      |<<  
    | 5 | S R R |   0   |   0   |      1      |      0      |  
    | 6 | S R S |   0   |   1   |      1      |      1      |<<  
    | 7 | S S R |   1   |   0   |      0      |      1      |  
    | 8 | S S S |   1   |   1   |      0      |      0      |  

- In row 4 and 6 A and B are able to make the statements.  
- What is C? In both statements is C a Knave.  




--------------------------------------------------------------------------------
3.Duo:
- Two people A and B resting under a Tree.
- We ask one "Is either of you a knight?" (OR-Question)
- After the response we know the true answer to the question.
- What is A?
- What is B?


    | # | A B | A=R OR B=R |Kann A sagen?|  
    | 1 | R R |      1     |      1      |  
    | 2 | R S |      1     |      1      |  
    | 3 | S R |      1     |      0      |<<  
    | 4 | S S |      0     |      1      |  

- Because of the statement: "After the response we know the true answer to the
  question." and there is only one different answer in line 3, we know that
  A is a knave and B is a Knight.




  --------------------------------------------------------------------------------
4.Trio: (The final trio)
- Three people A, B and C.
- A says: "B and C are the same type.".
- Someone asks C: "Are A and B of the same type?".
- What does C answer?


    | # | A B C | A:B=C | Kann A sagen? | A=B?C | C says: |  
    | 1 | R R R |   1   |       1       |   1   |    1    |  
    | 2 | R R S |   0   |       0       |   1   |    0    |  
    | 3 | R S R |   0   |       0       |   0   |    0    |  
    | 4 | R S S |   1   |       1       |   0   |    1    |  
    | 5 | S R R |   1   |       0       |   0   |    0    |  
    | 6 | S R S |   0   |       1       |   0   |    1    |  
    | 7 | S S R |   0   |       1       |   1   |    1    |  
    | 8 | S S S |   1   |       0       |   1   |    0    |  

- What does C answer? There is no unique yes or no to the answer, it depends on
  the participants. As we can see above C says 4 times yes and 4 times no.




--------------------------------------------------------------------------------
5.Solo (Not test substance)
- One person.
- You remember the person's first name was either Edwin or Edward.
- You ask him about hist first name.
- He answers Edward.
- What is his first name?


    | A | A=Edwin  | A:Edward |Kann A sagen?|  
    | R |    1     |    0     |      0      |  
    | S |    1     |    1     |      1      |  

- What is his first name? This is a joke.
  If he is a knight he says the truth otherwise he is a knave.
