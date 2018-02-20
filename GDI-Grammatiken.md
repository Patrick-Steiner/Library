
--------------------------------------------------------------------------------
# THEORIE: RegEx - RegularExpression  
--------------------------------------------------------------------------------

Alphabet:  
`Σ` = {a,b,c} ... Das Alphabet wird durch eine Menge erlaubter Zeichen definiert  

Operatoren:  
`.`    Ein beliebiges Zeichen (aus Σ)  
`[a-z]` Eines der Zeichen aus {a, b} (Zeichenmenge)  
`(ab)` Fasst die Sequenz „ab“ zu einer Gruppe zusammen (Gruppierung)  
`a|bc` Entweder „a“ oder „bc“ (Alternation)  
`+`    Das vorige Zeichen kommt 1–∞ mal vor (mindestens einmal)  
`*`    Das vorige Zeichen kommt 0–∞ mal vor (beliebig oft)  
`?`    Das vorige Zeichen kommt 0–1 mal vor (optional)  




--------------------------------------------------------------------------------
# UEBUNG: Zeichenkette matchen  
--------------------------------------------------------------------------------
Gegeben ist ein reguläre Ausdruck und sechs Wörter.  
Es ist zu bestimmen ob die Wörter vom RegEx gematcht werden.  

Syntaxelemente:  `.*+?(|)[-]`  
Alphabet:  `Σ = {0-9,&,e,x}`  
RegEx:  `((5|e)+x)*&?((x*2)+|0?([a-z]+|[1-9]+))`  

    Wort          Match  
    5x073         Ja  
    ex&&1         Nein  
    e5x&012345    Ja  
    5x&x2x22xx2   Ja  
    55&0?fiofiwh  Nein  
    5xexxx2       Ja  




--------------------------------------------------------------------------------
# UEBUNG: URL matchen
--------------------------------------------------------------------------------

Syntaxelemente:  `.*+?(|)[-]{}^$`  
Alphabet:  `Σ = {0-9,a-z,&,=,?,/}`  
Erstelle eine RegEx mit folgenden Eigenschaften:  

Die URL beginnt mit http:// oder https://.  
`https?:\/\/`  
Der Domain-Name besteht aus mindestens 2 Teilen, welche durch Punkte getrennt sind.  
Jeder Teil besteht aus mindestens einem Zeichen, welche Zahlen und Kleinbuchstaben sein können.  
Die Top-Level-Domain, soll mit at, ch oder de enden.  
`([a-z0-9]+\.)+(at|(de|ch))`  
Nach der Domain folgt optional der Pfad, welcher nur aus Kleinbuchstaben besteht.  
Dieser beginnt mit einem Slash. Danach können beliegig viele Unterpfade stehen.  
`(\/[a-z]+)*`  
Am Ende des Pfads kann ein / folgen, jedoch ist ein leerer Pfad mit // nicht erlaubt.  
`\/?`  
Am Ende können beliebig viele Parameter an die URL angehängt werden, mit folgendem Format:  
Mindestens ein Kleinbuchstaben, gefolgt von einem Gleichzeichen, beliebig viele Kleinbuchstaben.  
Der erste Paramter wird von der Domain durch ein Fragezeichen getrennt.  
`(\?[a-z]+=[a-z]*`  
Alle folgenden Parameter werden voneinander durch & getrennt.  
Nach dem letzten Parameter folgt kein &.  
`(&[a-z]+=[a-z]*)*)?`  

## Match:  
    http://a1.at  
    http://orf.at/  
    https://tc.tu.at/main  
    http://www.derstandard.at/kultur/  
    https://wikipedia.at/wiki/regex/  
    http://duckduckgo.at/?q=regex  
    https://gdi.ist.tu.at?user=student  
    http://gdi.ist.tu.at/login?course=gdi&role=student  
    http://tu.at?emptyparam=  

## No match:  
    ε (Leerstring)  
    http  
    http://  
    http://www  
    http://.at  
    http://orf.at//  
    https://de.wikipedia.org  
    http://tu.at/?  
    http://gdi.ist.tu.at/?user=student&  
    http://?user=student  
    https://tu.at?user  

## Erstellte RegEx:  
`^https?:\/\/([a-z0-9]+\.)+(at|(de|ch))(\/[a-z]+)*\/?(\?[a-z]+=[a-z]*(&[a-z]+=[a-z]*)*)?$`  
Kontrolle auf [regex101.com](https://regex101.com/)  




--------------------------------------------------------------------------------
# UEBUNG: Zeichenkette matchen  
--------------------------------------------------------------------------------
Gesucht ist eine RegEx die keine zwei aufeinanderfolgenden Buchstaben matcht.  

## Match:  
    a  
    ab  
    aba  
    abab  
    ε  

## No match:  
    aa  
    abaa  
    abba  
    aababa  

## Erstellte RegEx:  
`^(a?(ba)*|b?(ab)*)$`  
Kontrolle auf [regex101.com](https://regex101.com/)  




--------------------------------------------------------------------------------
# UEBUNG: Telefonnummern  
--------------------------------------------------------------------------------
Erstelle eine RegEx um österreichische Telefonnummern  
aus Wien (Vorwahl 1) und Graz (Vorwahl 316) zu validieren:  

## Match:  
    +433161234  
    011519245  
    00433161  

## No match:  
    +432234  
    0664111213  
    043316456  

## Erstellte RegEx:  
`^(\+43|0|0043)(1|316)[0-9]+$`  
Kontrolle auf [regex101.com](https://regex101.com/)  




--------------------------------------------------------------------------------
# UEBUNG: Email-Adressen  
--------------------------------------------------------------------------------
Erstelle eine RegEx um Email-Adressen zu validieren:  

## Match:  
    firstname.lastname@example.com  
    f.l@example.com  
    f.lastname@example.com  
    firstname.l@example.com  
    F.Lastname@example.com  
    Firstname.L@example.com  
    f.s.t.f.f.s.s.e.n@example.com  

## No match:  
    firstname.lastname@example.co  
    firstname..lastname@example.com  
    f.l@example.uk  
    .lastname@example.com  
    f.l@otherhost.com  
    firstname.@example.com  
    firstName.lastName@example.com  

## Erstellte RegEx:  
`^([A-Z]|[a-z])[a-z]*(\.([A-Z]|[a-z])[a-z]*)*@example\.(com|de|at)$`  
Kontrolle auf [regex101.com](https://regex101.com/)  




--------------------------------------------------------------------------------
# UEBUNG: IPv4-Adressen  
--------------------------------------------------------------------------------
Erstelle eine RegEx um IPv4-Adressen zu validieren:  

## Match:  
    255.255.255.255/0  
    192.168.178.1/32  
    132.254.111.10  
    26.10.2.10/24  
    001.001.001.001  
    000.000.000.000  
    1.1.1.1  
    0.0.0.0  

## No match:  
    99.255.0.127/99  
    99.255.0.127/9a  
    10.10.10.10.10  
    10.10.10.256  
    255.255.255.255/33  
    1...1  
    1.2.3  
    1.2.3.4.5  
    192.168.178.1/33  
    c.123.123.123  
    192.168.178.1/c  

## Erstellte RegEx:  
`^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])(\/((3[0-2])|([0-2]?[0-9])))?$`  
Kontrolle auf [regex101.com](https://regex101.com/)  




--------------------------------------------------------------------------------
# THEORIE: Formale Grammatik G  
--------------------------------------------------------------------------------

`G = (V, Σ, P, S)` ... 4-Tupel  
`V` ... endliches Vokabular  
`Σ` ... Alphabet  
`P` ... Produktionsregeln  
`S` ... Startsymbol  

- Formale Grammatiken erzeugen Wiederholungen über Rekursion.  
- Das Erzeugen von Strings startet stets mit dem Startsymbol `S`.  
- Produktionsregeln `P` erlauben es schrittweise Zeichen aus `V` zu ersetzen.  
- Wir unterscheiden Terminalsymbole `Σ` und Nonterminalsymbole `V\Σ`.  
- Terminalsymbole sind jene Symbole, die in der endgültigen Zeichenkette vorkommen.  
- Für Nonterminalsymbole sind Regeln in `P` definiert, wie man sie ersetzen kann.  
- Die Ersetzungen erfolgen so lange bis nur mehr Terminalsymbole enthalten sind.  




--------------------------------------------------------------------------------
# UEBUNG: Klammern  
--------------------------------------------------------------------------------
Gesucht ist eine Kontextfreie Grammatik, die folgende Eigenschaften erfüllt:  
- Anzahl der offenen Klammern entspricht der Anzahl der schließenden Klammern.  
- Ein Klammerpaar kann das Symbol 'x' einmal enthalten, muss aber nicht.  
- Die gesamte Zeichenkette muss geklammert sein.  
- Klammerpaare müssen mit einem Semicolon getrennt werden.  

## Match:  
    {}  
    {x}  
    {{{x}}}  
    {{x};{{x}}}  
    {{};{{}}}  
    {{};{};{}}  
    {{};{x};{{};{x}}}  

## No match:  
    ;  
    x  
    {xx}  
    {{}{}}  
    {}};{{}  
    {{};{};}  
    {};{}  
    ;{}  
    ε  

## Lösungsansatz:  

**Terminale:**  
`T = {{,x,},;}`  

**Nichtterminale:**  
`N = {S,A,B,C,D}`  

**Produktionsregeln:**  
`S → {A}`  
`A → ε | x | B`  
`B → {C | {D`  
`C → ε} | x} | B}`  
`D → ε};B | x};B`  

**Herleitungen:**  
`S → {A} → {ε} → {}`  
`S → {A} → {x}`  
`S → {A} → {B} → {{CE} → {{BE} → {{{CEE} → {{{xEE} → {{{x}}}`  
`S → {A} → {B} → {{D} → {{x};B} → {{x};{C} → {{x};{B}} → {{x};{{C}} → {{x};{{x}}}`  
`S → {A} → {B} → {{D} → {{ε};B} → {{};{C} → {{};{B}} → {{};{{C}} → {{};{{ε}}} → {{};{{}}}`  
`S → {A} → {B} → {{D} → {{ε};B} → {{ε};{D} → {{ε};{ε};B} → {{ε};{ε};{C} → {{ε};{ε};{ε}} → {{};{};{}}`  
`S → {A} → {B} → {{ε};B} → {{ε};{D} → {{ε};{x};B} → {{ε};{x};{C} → {{ε};{x};{B}} →
{{ε};{x};{{D}} → {{ε};{x};{{ε};B}} → {{ε};{x};{{ε};{C}} → {{ε};{x};{{ε};{x}}} → {{};{x};{{};{x}}}`  

**Kontextfreie_Grammatik:**  
`G = (N,T,P,S)`  

`G = ({S,A,B,C,D}, {{,x,},;}, {S → {A}, A → ε | x | B, B → {C | {D, C → ε} | x} | B}, D → ε};B | x};B}, S)`  




--------------------------------------------------------------------------------
# UEBUNG: Buchstaben  
--------------------------------------------------------------------------------
Gesucht sind die Produktionsregeln für eine kontextfreie Grammatik,  
die folgende Form aufweisen:  uvw²ⁿxy³ⁿz  

## Match:  
uvxz              (n = 0)  
uvwwxyyyz         (n = 1)  
uvwwwwxyyyyyyz    (n = 2)  

## Lösung:  

Terminale:  
`T = {u,v,w,x,y,z}`  

Nichtterminale:  
`N = {S,A}`  

Produktionsregeln:  
`S → uvAz`  
`A → wwAyyy | x`  

Herleitungen:  
`S → uvAz → uvxz`  
`S → uvAz → uvwwAyyyz → uvwwxyyyz`  
`S → uvAz → uvwwAyyyz → uvwwwwAyyyyyyz → uvwwwwxyyyyyyz`  

Kontextfreie_Grammatik:  
`G = (N,T,P,S)`  
`G = ({S,A},{u,v,w,x,y,z},{S → uvAz, A → wwAyyy | x},S)`  




--------------------------------------------------------------------------------
# UEBUNG: RegEx vs kontextfreie Grammatik  
--------------------------------------------------------------------------------

1) Ausdruck:  aˣ⁻³ bʸ c⁵ᶻ  
Vereinfacht:  aˣbʸcᶻ  

Da von der Basis "a" der Exponent "x-3" ist, muss `x >= 3` sein.

Bsp.1: x=3, y=0, z=0:  
Herleitung 1:  a³⁻³ b⁰ c⁵ˣ⁰ == a⁰b⁰c⁰ = 1 == ε (Empty String)  

Bsp.2: x=4, y=1, z=1:  
Herleitung 2:  a⁴⁻³ b¹ c⁵*¹ == a¹b¹c⁵ = abccccc  

2) RegEx:  

    a*b*(ccccc)*  
    Entscheidbar in regulärer Grammatik: Ja  

3) Kontextfreie Grammatik:  

    A → aA|aB|ε  
    B → bB|bC|ε  
    C → ccccccC|ε  

    `V` = {A,B,C}  
    `Σ` = {a,b,c}  
    `P` = {A → aA|aB|ε, B → bB|bC|ε, C → cC|ε}  
    `S` = A  

    `G` = (V, Σ, P, S)  
    `G` = ({A,B,C}, {a,b,c}, {A → aA|aB|ε, B → bB|bC|ε, C → cC|ε}, A)  
    Entscheidbar in kontextfreier Grammatik: Ja  



## Welche Grammatik kann welchen Ausdruck entscheiden?  

    Gegebene Ausdrücke Entscheidbar in  | aⁿ | aⁿbⁿ | aⁿbⁿcⁿ |  
    Reguläre_Grammatik (RegEx)          | Ja | Nein |  Nein  |
    Kontextfreie_Grammatik              | Ja |  Ja  |  Nein  |
    Kontextsensitive_Grammatik          | Ja |  Ja  |   Ja   |



--------------------------------------------------------------------------------
# UEBUNG: RegEx vs kontextfreie Grammatik  
--------------------------------------------------------------------------------

Gegebene Sprache S:
`a²⁺³ˣ b⁵ˣ⁻⁷⁺²ʸ a⁶ʸ⁻⁸`

Gefragt: Wie groß müssen Variablen x und y mindestens gewählt werden?  
  Aus dem 3. Term (a⁶ʸ⁻⁸) erkennt man dass "6y >= 8" sein muss.
  Daraus folgt dass "y>=2" ist, da "6*2=12" und "12-8=4" ergibt.
  Somit ist ein positiver Exponent gewährleistet.  
  Aus dem 2. Term (b⁵ˣ⁻⁷⁺²ʸ) erkennt man dass "5x+2y >= 7" sein muss.
  Da aus dem 3. Term bereits bekannt ist dass "y>=2" ist, muss "x>=1" sein,
  da "5*1 + 2*2 = 5+4 = 9 > 7" ergibt,
  Somit ist wieder ein positiver Exponent gewährleistet.  

Sprache:
`a²⁺³ˣ b⁵ˣ⁻⁷⁺²ʸ a⁶ʸ⁻⁸`  

Potenzen aufteilen:
`a² a³ˣ b⁵ˣ b⁻⁷ b²ʸ a⁶ʸ a⁻⁸`  

Konstanten entfernen:
`a³ˣ b⁵ˣ b²ʸ a⁶ʸ`  (= a³ˣb⁵ˣ⁺²ʸa⁶ʸ)  

Terminale:
`T = {a,b}`  

Nichtterminale:
`N = {S,X,Y}`  

Produktionsregeln P:  
`S → XY|ε`         (= a³ˣb⁵ˣ⁺²ʸa⁶ʸ)  
`X → aaaXbbbbb|ε`  (= a³ˣb⁵ˣ)  
`Y → bbYaaaaaa|ε`  (= b²ʸa⁶ʸ)  

Wort Herleitung für x=1 und y=1 (a³*¹b⁵*¹⁺²*¹a⁶*¹ = a³b⁷a⁶):  
`S → (XY)`  
`  → ((aaaXbbbbb)(bbYaaaaaa))`  
`  → ((aaa(ε)bbbbb)(bb(ε)aaaaaa))`  
`  → aaabbbbbbbaaaaaa` (= a³b⁷a⁶)  

Wort Herleitung für x=2 und y=2 (a³*²b⁵*²⁺²*²a⁶*² = a⁶b¹⁴a¹²):  
`S → (XY)`  
`  → ((aaaXbbbbb)(bbYaaaaaa))`  
`  → ((aaa(aaaXbbbbb)bbbbb)(bb(bbYaaaaaa)aaaaaa))`  
`  → ((aaa(aaa(ε)bbbbb)bbbbb)(bb(bb(ε)aaaaaa)aaaaaa))`  
`  → aaaaaabbbbbbbbbbbbbbaaaaaaaaaaaa` (= a⁶b¹⁴a¹²)  

Grammatik G:
`G = (N, T, P, S) = ({S,X,Y},{a,b},{S → XY|ε, X → aaaXbbbbb|ε, Y → bbYaaaaaa|ε},S)`  




--------------------------------------------------------------------------------
# UEBUNG: Grammatik Bestimmen  
--------------------------------------------------------------------------------
1.Symbol = Entscheidbar in regulärer Grammatik: j|n  
2.Symbol = Entscheidbar in kontextfreier Grammatik: j|n  



## 1.Aufgabe:  

nn  |  aˣ⁻² b³ˣ⁻² a⁴ˣ⁻²  

nj  |  aˣ b²ˣ⁺ʸ b³ˣ⁺³ʸ⁺ᶻ  

jj  |  a²ˣ⁻² b³ʸ⁻² c⁴ᶻ⁻²  

nj  |  aˣ⁺²ᶻ bʸ c³ˣ⁺²ʸ⁺ᶻ  



## 2.Aufgabe:  

nn  |  bˣ⁻⁴ a³ˣ⁻² b⁵ˣ⁻²  

nj  |  bˣ a⁶ˣ⁺ʸ a²ˣ⁺²ʸ⁺ᶻ  

jj  |  bˣ⁻³ a⁴ʸ c⁵ᶻ  

nj  |  bˣ⁺³ᶻ aʸ c²ˣ⁺³ʸ⁺ᶻ  



## 3.Aufgabe:  

nj  |  a²ˣ⁺⁵ᶻ bʸ c³ˣ⁺²ʸ⁺ᶻ  

nj  |  aˣ b²ˣ⁺⁴ʸ b³ˣ⁺³ʸ⁺ᶻ⁻⁶  

nn  |  aˣ⁻⁷ b⁵ˣ⁻² a⁴ˣ⁻²  

jj  |  a⁸⁺ˣ⁻⁵ b²ʸ⁺¹ c³ᶻ  



## 4.Aufgabe:  

nj  |  bˣ a²ˣ⁺ʸ aˣ⁺²ʸ⁺ᶻ  

jj  |  bˣ⁻³ aʸ c¹¹ᶻ  

nj  |  b³ˣ⁺³ᶻ aʸ cˣ⁺³ʸ⁺ᶻ  

nn  |  bˣ a⁵ˣ⁻² b⁵ˣ⁻²  



## 5.Aufgabe:  

nn  |  aᶻ bˣʸ aʸ⁺ᶻ  

nn  |  a²ˣ⁺ʸ b³ʸ⁺⁴ᶻ a⁵ᶻ⁺²ʸ  

jj  |  a⁹ˣ⁺ˣ⁺⁵ c³ʸ⁺⁴ʸ b⁵ᶻ⁺²ᶻ  

nj  |  aᶻ bˣ⁺ʸ aʸ⁺ᶻ  



## 6.Aufgabe:  

nn  |  a²ˣ⁺ʸ b³ʸ⁺⁴ᶻ a⁵ᶻ⁺²ʸ  

nn  |  aᶻ bˣʸ aʸ⁺ᶻ  

nj  |  aᶻ bˣ⁺ʸ aʸ⁺ᶻ  

jj  |  a⁸ˣ⁺ˣ⁻⁵ b²ʸ⁺³ʸ c³ᶻ⁺ᶻ  



## 7.Aufgabe:  

jj  |  bˣ⁻³aʸc⁶ᶻ  

nj  |  b³ˣ⁺ᶻaʸcˣ⁺³ʸ⁺²ᶻ  

nn  |  a²ˣ⁻²b³ˣ⁻²aˣ⁻³  

nj  |  aˣb²ˣ⁺ʸb³ˣ⁺³ʸ⁺ᶻ  




--------------------------------------------------------------------------------
# UEBUNG: RegEx Analyse  
--------------------------------------------------------------------------------
[RegEx_Comparison](https://bakkot.github.io/dfa-lib/regeq.html)

Gegeben: `((a+(ab+|b+)(a?|a*)+)|(bb?(b|b?)(a?|a)(b|b+)b*))+`  
Vereinfacht: `((a+b+a*)|(bb?b?a?b+b*))+`  
Alphabet = {a,b}  
Match?:  

    n  |  cabbad  
    j  |  bbbb  
    n  |  aa  
    j  |  abababab  
    n  |  aabbbabbbcab  
    n  |  baba  
    n  |  aaaa  
    j  |  bb  
    j  |  ababbb  
    n  |  ba  
    j  |  bbabbbaba  


Gegeben: `((cd)*(cd)?(cd)*cd+|cd+d*d*ccdd)+|(dd*c*dc(dd)?|(dcd)?(dc)+(dc)*((cd)+(cd)*)?)*`  
Vereinfacht: `(cd+(ccdd)?)+|(d+c*dc(dd)?|(dcd)?(dc)+(cd)*)*`  
Alphabet = {c,d}  
Match?:  

    n  |  cddc  
    j  |  cdcdddcdddd  
    j  |  dccd  


Gegeben: `((.a(a*|b*)b+.)+|(b(b|b?).(a+|a)+(b|b+)b*)+)+`  
Vereinfacht: `(.a+b+.|bb?.a+b+)+`  
Alphabet = {a,b,c,d}  
Match?:  

    n  |  cabbad  
    j  |  dabd  
    j  |  babcdaaaaabbbbbbbd  
    j  |  babababb  
    n  |  babaabababbbababa  
    j  |  aabbbabbbcab  
    j  |  baabbabbababb  
    j  |  bcaaaabbbbdaaaaaabbbbbbbc  
