################################################################################
# Shortkeys and Stuff
################################################################################
# Sage arbeitet via dynamische typisierung.
[Strg]+[O]      # Add line
[Strg]+[M]      # Enter
[Alt]+[Enter]   # Execute

sage: notebook(reset=True) # Reset password for sage admin
sage: %colors Linux|LightBG|NoColor # Changes the the color theme
sage: version()
sage: whos
sage: reset()



################################################################################
# RECURSION: Reconstructing the function 'factorial()'
################################################################################
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)
fact_rec(5)



################################################################################
# RECURSION: Reconstructing the function 'sum()'
################################################################################
def sum_rec(l2):
    if len(l2) == 0:
        raise ValueError("Empty list given!")
    elif len(l2) == 1:
        return l2[0]
    else:
        return l2[0] + sum_rec(l2[1:])
l1 = [1,2,3,4]
sum_rec(l1)




################################################################################
# Sage1 Aufgabe7: Primzahlen
################################################################################
t = cputime(0)
start = 100000
end = 1000000
num_of_primes = 0
list_of_primes = []
for pointer in range(start,end):
    if is_prime(pointer) == true:
        num_of_primes += 1
        list_of_primes.append(pointer)
print "Number of primes: ", num_of_primes
print "Computation time: ", cputime(t)

Number of primes:  68906
Computation time:  1.324



################################################################################
# Sage1 Aufgabe7: Primzahlen
################################################################################
t = cputime(0)
start = 100000
end = 1000000
pointer = start
num_of_primes = 0
list_of_primes = []
while pointer < end:
    if is_prime(pointer) == true:
        num_of_primes += 1
        list_of_primes.append(pointer)
    pointer +=1
print "Number of primes: ", num_of_primes
print "Computation time: ", cputime(t)

Number of primes:  68906
Computation time:  0.752



################################################################################
# Sage1 Aufgabe7: Primzahlen
################################################################################
t = cputime(0)
start = 100000
end = 1000000
pointer = next_prime(start)
num_of_primes = 0
list_of_primes = []
while pointer < end:
    num_of_primes += 1
    list_of_primes.append(pointer)
    pointer = next_prime(pointer)
print "Number of primes: ", num_of_primes
print "Computation time: ", cputime(t)

Number of primes:  68906
Computation time:  0.26



################################################################################
# Sage1 Aufgabe7: Primzahlen
################################################################################
t = cputime(0)
list_of_primes = prime_range(100000,1000000)
number_of_primes = len(list_of_primes)
print "Number of primes: ", num_of_primes
print "Computation time: ", cputime(t)

Number of primes:  68906
Computation time:  0.012



################################################################################
# Sage1 Aufgabe7: Primzahlen
################################################################################
list_of_primes = prime_range(100000,1000000)
list_of_twins = []
i = 0
while i < len(list_of_primes)-1:
    if list_of_primes[i+1] == list_of_primes[i]+2:
        q = list_of_primes[i]
        p = list_of_primes[i+1]
        list_of_twins.append((q,p))
    i += 1
print "Number of twins: ", len(list_of_twins)



################################################################################
# Sage1 Aufgabe8: Fließkommazahlen1
################################################################################
x = var('x')
x = -12
list = []
while x >= -16:
    f1 = sqrt(1+10^x) - sqrt(1-10^x)
    f2 = (2*10^x) / (sqrt(1+10^x) + sqrt(1-10^x))
    list.append((f1,f2))
    x -= 1
i = 0
while i < len(list):
    print "f1: ", list[i][0].n(160)
    print "f2: ", list[i][1].n(160)
    i += 1



################################################################################
# Sage1 Aufgabe9: Fließkommazahlen2
################################################################################
xi = pi + e + 1000000
extra = 10  # extra Nachkommastellen um Rundungsfehler zu vermeiden
n = 13787   # n'te Nachkommastelle
v = len(str(int(xi)))   # v...Vorkommastellen
print str(xi.numerical_approx(digits=n+extra+v))[-extra]



################################################################################
# Sage2 Aufgabe10: Gleichung1
################################################################################
y = var('y')
eq1 = y^8 - 6*y^7 - 14*y^6 + 138*y^5 - 116*y^4 - 546*y^3 + 1326*y^2 - 3042*y + 4563
print "Symbolic process solve():\n", solve(eq1,y)
print "Symbolic process .solve(f,args,to_poly_solve=True):\n", sage.symbolic.relation.solve(eq1, y, to_poly_solve=True)
print "Symbolic process factor():\n", factor(eq1,y)
print "Numerical process roots():\n", eq1.roots(ring=RR)
print "Numerical process find_root():\n", find_root(eq1,-10,10) # finds first occuring root



################################################################################
# Sage2 Aufgabe10: Gleichung2
################################################################################
y = var('y')
eq2 = y^5 + y - 2
print "Symbolic process solve():\n", solve(eq2,y)
print "Symbolic process .solve(f,args,to_poly_solve=True):\n", sage.symbolic.relation.solve(eq2, y, to_poly_solve=True)
print "Symbolic process factor():\n", factor(eq2,y)
print "Numerical process roots():\n", eq2.roots(ring=RR)
print "Numerical process find_root():\n", find_root(eq2,-10,10) # finds first occuring root



################################################################################
# Sage2 Aufgabe11: Gleichungssystem
################################################################################
y = var('y')
eq1 = x*y^2 - 5*y + 4*x - 3
eq2 = x*y - 2*x + 2
solution = solve([eq1,eq2],x,y)
print "Symbolic result:\n", solution
print "Numeric result:"
print solution[0][0].rhs().n(digits=5)
print solution[0][1].rhs().n(digits=5)
print solution[1][0].rhs().n(digits=5)
print solution[1][1].rhs().n(digits=5)



################################################################################
# Sage2 Aufgabe12: CURVE_SKETCHING
################################################################################
#
f(x) = ln(1 + x^2) - exp(-x) + x*sin(x) - ln(sqrt(1234567%777))
df(x) = diff(f(x))
ddf(x) = diff(df(x))
#
lb = -3  # lower boundary
ub = 9   # upper boundary
def find_all_roots(func,lb,ub):
    epsilon = 0.1
    list_of_roots = []
    pointer = lb
    while pointer < ub:
        try:
            list_of_roots.append(find_root(func,pointer,pointer+epsilon))
        except(RuntimeError):
            pass
        pointer += epsilon
    return list_of_roots
#
nullstellen_x = find_all_roots(f(x),lb,ub)
nullstellen_y = [f(i) for i in nullstellen_x]
nullstellen   = [[nullstellen_x[i],nullstellen_y[i]] for i in range(len(nullstellen_x))]
ns = point(nullstellen, size=50, color="red")
#
extrempunkte_x = find_all_roots(df(x),lb,ub)
extrempunkte_y = [f(i) for i in extrempunkte_x]
extrempunkte   = [[extrempunkte_x[i],extrempunkte_y[i]] for i in range(len(extrempunkte_x))]
ep = point(extrempunkte, size=50, color="orange")
#
wendepunkte_x = find_all_roots(ddf(x),lb,ub)
wendepunkte_y = [f(i) for i in wendepunkte_x]
wendepunkte   = [[wendepunkte_x[i],wendepunkte_y[i]] for i in range(len(wendepunkte_x))]
wp = point(wendepunkte,  size=50, color="black")
#
minima = []
maxima = []
i = 0
while i < len(extrempunkte):
    if ddf(extrempunkte_x[i]) > 0:
        minima.append(extrempunkte[i])
    else:
        maxima.append(extrempunkte[i])
    i += 1
mi = point(minima, size=50, color="blue")
ma = point(maxima, size=50, color="green")
#
g1 = plot(f(x), xmin=lb, xmax=ub, color="black")
g2 = g1 + ns + wp + ep + mi + ma
g2.show()



################################################################################
# Sage3 Aufgabe13: Rekursives ermitteln der catalanschen Zahlen
################################################################################
# cₙ = cₖ*cₙ₋ₖ₋₁
@cached_function
def catalan(n):
    if n == 0:
        return 1
    else:
        c = 0
        for k in range(n):
            c += catalan(k)*catalan(n-1-k)
        return c
sage: catalan(5)
42



################################################################################
# Sage3 Aufgabe14: Rekursives ermitteln der Chebyshev-Polynome
################################################################################
# Tₙ(x) = 2xTₙ₋₁(x) - Tₙ₋₂(x)
def T(n):
    if n < 1:
        return 1
    elif n == 1:
        return x
    else:
        t = 2*x*T(n-1)-T(n-2)
        return t.expand()

sage: T(0)
....: T(1)
....: T(2)
....: T(3)
....: T(4)
....:
1
x
2*x^2 - 1
4*x^3 - 3*x
8*x^4 - 8*x^2 + 1



################################################################################
# Sage3 Aufgabe14: Trigonometrie in der Ebene
################################################################################
def umkreis(A,B,C):
    # Pruefung auf echtes Dreieck
    if (A[0]==B[0]) & (B[0]==C[0]):
        # EG.: A[0,1], B[0,2], C[0,3]
        return "Kein echtes Dreieck!"
    elif (A[1]==B[1]) & (B[1]==C[1]):
        # EG.: A[1,0], B[2,0], C[3,0]
        return "Kein echtes Dreieck!"
    elif (A == B) | (B == C) | (C == A):
        # EG.: A[0,0], B[0,0]
        return "Kein echtes Dreieck!"
    else:

        # Variablen zu Vektoren konvertieren
        A = vector(A)
        B = vector(B)
        C = vector(C)

        # Vektoren ermitteln
        AB = B-A
        BC = C-B
        CA = A-C

        # Mittelsenkrechten ermitteln
        MAB = A+(AB/2)
        MBC = B+(BC/2)
        MCA = C+(CA/2)

        # Vektoren um 90 Grad drehen
        NAB = vector([-AB[1],AB[0]])
        NBC = vector([-BC[1],BC[0]])
        NCA = vector([-CA[1],CA[0]])

        # Gedrehte Vektoren auf Mittelsenkrechte auflegen,
        # sprich parallel im Raum verschieben
        VNAB = vector([MAB[0]+NAB[0], MAB[1]+NAB[1]])
        VNBC = vector([MBC[0]+NBC[0], MBC[1]+NBC[1]])
        VNCA = vector([MCA[0]+NCA[0], MCA[1]+NCA[1]])

        # Lineares Gleichungssystem der Geraden aufstellen
        var('s','t')
        equation1 = VNAB + t * (MAB-VNAB)
        equation2 = VNBC + s * (MBC-VNBC)
        equations = list(equation1-equation2)
        results = solve(equations,[s,t])
        # Substitution - Werte einsetzen um Schnittpunkt zu erhalten
        intersection = equation1.subs(results[0])

        # Umkreisradius ermitteln
        radius = sqrt((intersection[0]-A[0])^2 + (intersection[1]-A[1])^2)

        # Graph zeichnen
        frame = line([A,B,C,A])
        center = point(intersection,color='red',size=50)
        bisection1 = line([MAB,intersection],color='green')
        bisection2 = line([MBC,intersection],color='green')
        bisection3 = line([MCA,intersection],color='green')
        outer_circle = circle(intersection,radius,color='red')
        g = frame + center + bisection1 + bisection2 + bisection3 + outer_circle
        g.show()

# Echtes Dreieck:
A = [0,0]
B = [0,5]
C = [5,1]
umkreis(A,B,C)

# Echtes Dreieck:
A = [1,6]
B = [4,1]
C = [7,6]
umkreis(A,B,C)

# Kein echtes Dreieck:
A = [0,0]
B = [0,0]
C = [0,0]
umkreis(A,B,C)

# Kein echtes Dreieck:
A = [1,0]
B = [2,0]
C = [3,0]
umkreis(A,B,C)

# Kein echtes Dreieck:
A = [1,1]
B = [1,1]
C = [2,2]
umkreis(A,B,C)



################################################################################
# Sage3 Aufgabe17: Recursive powerset generator
################################################################################
#
# Potenzmenge = Powerset
# | xyz |  Liste  |  Liste  |
# | 000 | [-,-,-] | []      |
# | 001 | [-,-,z] | [z]     |
# | 010 | [-,y,-] | [y]     |
# | 011 | [-,y,z] | [y,z]   |
# | 100 | [x,-,-] | [x]     |
# | 101 | [x,-,z] | [x,z]   |
# | 110 | [x,y,-] | [x,y]   |
# | 111 | [x,y,z] | [x,y,z] |
#
def powerset (set):
    if len(set) == 0:
        yield []
    else:
        for subset in powerset(set[1:]):
            yield [set[0]]+subset
            yield subset
