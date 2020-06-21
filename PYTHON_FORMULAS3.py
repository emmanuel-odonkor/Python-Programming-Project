def areaofrectangle(length,breadth):
	L = length
	B = breadth
	a = L * B
	print("THE AREA OF A THE RACTANGLE WITH LENGTH OF",L,"AND BREADTH OF",B,"IS",round(a,4))

def perimeterofrectangle(length,breadth):
	L = length
	B = breadth
	P = (2 * L) + (2 * B)
	print("THE PERIMETER OF THE RECTANGLE WJTH LENGTH",L,"AND BREADTH",B,"IS",round(P,4))

#AREA OF TRIANGLE
def areaoftriangle(base,height):
	B = base
	H = height
	A = (1/2 * B )* H
	print("THE AREA OF THE TRIANGLE WITH A BASE OF",B,"AND A HEIGHT OF",H,"IS",round(A,4))


#AREA OF A NON TRIANGLE
def areaofnontriangle(SIDEA,SIDEB,ANGLE):
	import math
	A = SIDEA
	B = SIDEB
	a = ANGLE
	a1 = a * (math.pi/180)
	T = (1/2 * A * B) * math.sin(a1)
	print("THE AREA OF THE TRIANGLE WITH THE GIVEN SIDE A OF",A,"SIDE B",B,"AND AN ANGLE OF",a,"IS",round(T,4))

#COSINERULE(HAVING THE ANGLE AND TWO SIDES)
def cosinerule(SIDEA,SIDEB,ANGLE):
	import math
	A = SIDEA
	B = SIDEB
	a = ANGLE
	a1 = a * (math.pi/180)
	C = math.sqrt((A**2 + B**2) - 2*(A*B)*math.cos(a1))
	print("THE LENGHT OF THE PART TO BE IDENTIFIED HAVING THE ANGLE OF",a,"ONE SIDE AS",A,"AND ANOTHER SIDE AS",B,"IS",round(C,3))

#SINRULE ( FINDING MISSING ANGLE)
def sinruleangle(OPPOSITESIDEOFANGLE,OTHERANGLE,OTHERANGLESIDE):
	import math
	OS = OPPOSITESIDEOFANGLE
	A2 = OTHERANGLE
	OSS = OTHERANGLESIDE
	A3 = A2 * (math.pi/180)
	A = math.asin((OS * math.sin(A3) )/ OSS)
	A1 = A * (180/math.pi)
	print("THE HIDDEN ANGLE IDENTIFIED USING THE SIN RULE WITH OPPOSITE SIDE OF",OS,"OTHER ANGLE OF",A2,"AND OTHER ANGLE SIDE OF",OSS,"IS",round(A1,4))


#COSINE ANGLE (FINDING THE ANGLE)
def cosangle(adjacent,hypothenuse):
	import math
	A = adjacent
	H = hypothenuse
	COS =math.acos(A/H)
	COS1 = COS * (180/math.pi)
	print("THE COSINE ANGLE FOR A TRIANGLE WITH AN ADJACENT OF",A,"AND A HYPOTHENUSE OF",H,"IS",round(COS1,4))


#SINE ANGLE
def sinangle(OPPOSITE, HYPOTHENUSE):
	import math
	O = OPPOSITE
	H = HYPOTHENUSE
	A = math.asin( O / H )
	A1 = A * ( 180 / math.pi)
	print("THE SINE ANGLE FOR A TRIANGLE WITH AN OPPOSITE OF",O,"AND A HYPOTHENUSE OF",H,"IS",round(A1,4))


#TANGENT ANGLE
def tanangle(OPPOSITE,ADJACENT):
	import math
	O = OPPOSITE
	A = ADJACENT
	A1 = math.atan( O / A )
	A2 = A1 * (180 / math.pi)
	print("THE TANGENT ANGLE OF A TRIANGLE WITH AN OPPOSITE OF",O,"AND AN ADJACENT OF",A,"IS",round(A2,4))


#FINDING RADIAN OF A DEGREE
def findingradian(DEGREENUMBER):
	import math
	D = DEGREENUMBER
	S = D * math.pi / 180
	print("THE RADIAN REPRESENTATIVE OF",D,"DEGREES IS",round(S,3))


#FINDING DEGREE
def findingdegree(RADIAN):
	import math
	R = RADIAN
	D = R * (180 / math.pi)
	print("THE DEGREE FORMAT OF THE RADIAN",R,"IS",int(round(D,0)))


#FINDING GRADIENT
def gradient(Y2,Y1,X2,X1):
	A = Y2
	B = Y1
	C = X2
	D = X1
	G = (A - B) / (C - D)
	print("THE GRADIENT OR THE SLOPE OF THE LINE IS",round(G,4))


#FINDING AREA OF SQUARE
def squarearea(LENGTH):
	L = LENGTH
	A = L * L
	print("THE AREA OF THE SQUARE WITH GIVEN LENGTH OF",L,"IS",round(A,3))


#FINDING THE PERIMETER OF A SQUARE
def squareperimeter(LENGTH):
	L = LENGTH
	P = 4 * L
	print("THE PERIMETER OF A SQUARE WITH LENGTH OF",L,"IS",round(P,3))


#FINDING CIRCUMFERENCE
def circumference(RADIUS):
	import math
	R = RADIUS
	C = 2 * math.pi * R
	print("THE CIRCUMFERENCE OF THE CIRCLE WITH RADIUS OF",R,"IS",round(C,3))


#FINDING AREA OF CIRCLE
def areaofcircle(RADIUS):
	import math
	R = RADIUS
	A = math.pi * R**2
	print("THE AREA OF A CIRCLE WITH A RADIUS OF",R,"IS",round(A,3))



#FINDING ARCLENGTH
def arclength(RADIUS,DEGREE):
	import math
	R = RADIUS
	D = DEGREE
	D1 = D * (math.pi / 180)
	A = R * D1
	print("THE ARCLENGTH OF A CIRCLE WITH A RADIUS OF",R,"AND AN ANGLE OF",D,"IS",round(A,3))


#FINDING AREA OF TRAPEZIUM
def areaoftrapezium(SIDEA,SIDEB,HEIGHT):
	A = SIDEA
	B = SIDEB
	H = HEIGHT
	T = 1/2 * (A + B) * H
	print("THE ARA OF A TRAPEZIUM WITH SIDES",A,"AND",B,"AND A HEIGTH OF",H,"IS",round(T,3))


#FINDING THE ROOTS OF A QUADRATIC EQUATION
def quadraticroots(SIDEA,SIDEB,SIDEC):
	import math
	A = SIDEA
	B = SIDEB
	C = SIDEC
	squareroot = B*B-4*A*C
	if squareroot < 0:
		print("THERE ARE NO ROOTS")
	else:
		root = math.sqrt(B*B-4*A*C)
		F1 = (-B+root)/(2*A)
		F2 = (-B-root)/(2*A)
		print("THE ROOTS OF X FOR THE GIVEN SIDES OF",A,"AND",B,"AND",C,"ARE",round(F1,3),"AND",round(F2,3))


#SCIENCE
#FINDING FORCE
def force(MASS,ACCELERATION):
	M = MASS
	A = ACCELERATION
	F = M * A
	print("THE FORCE OF AN OBECT WIRH A MASS OF",M,"AND AN ACCELERATION OF",A,"IS",round(F,3))

	
#FINDING KINECTIC ENERGY
def kineticenergy(MASS,VELOCITY):
	M = MASS
	V = VELOCITY
	K =( 1/2 * M) * V**2
	print("THE KINETIC ENERGY OF THE OBJECT WITH A MASS OF",M,"AND A VELOCITY OF",V,"IS",round(K,3))



#FINDING PRESSURE
def pressure(FORCE,AREA):
	F = FORCE
	A = AREA
	P = F / A
	print("THE PRESSURE OF AN OBJECT WITH A FORCE OF",F,"AND AN AREA OF",A,"IS",round(P,3))

#FINDING DENSITY
def density(MASS,VOLUME):
	M = MASS
	V = VOLUME
	D = M / V
	print("THE DENSITY OF THE OBJECT WITH A MASS OF",M,"AND A VOLUME OF",V,"IS",round(D,3))


#FINDING WORKDONE
def work(FORCE,DISTANCE):
	F = FORCE
	D = DISTANCE
	W = F * D
	print("THE WORKDONE BY AN OBJECT WITH A FORCE OF",F,"AND A DISTANCE OF",D,"IS",round(W,3))


#FINDING HYDROGEN IONS IN A MOLE
def hydrogenions(MOLES):
	M = MOLES
	A = 6.02*10**23
	H = M * A
	print("THE NUMBER OF HYDROGEN IONS IN",M,"MOLES IS",H)


#FINDING THE EFFICIENCY OF A MACHINE
def efficiencyofmachine(WORKOUTPUT,WORKINPUT):
	WO = WORKOUTPUT
	WI = WORKINPUT
	E = (WO / WI) * (100/100)
	print("THE EFFICIENCY OF A MACHINE WITH A WORKOUTPUT OF",WO,"AND A WORKINPUT OF",WI,"IS",round(E,3),"%")


#FINDING SPEED
def speed(DISTANCE,TIME):
	D = DISTANCE
	T = TIME
	S = D / T
	print("THE SPEED OF AN OBJECT WITH A DISTANCE OF",D,"AND A TIME OF",T,"IS",round(S,4))


#FINDING ACCLERATION
def acceleration(VELOCITY,TIME):
	V = VELOCITY
	T = TIME
	A = V / T
	print("THE ACCELERATION OF AN OBJECT WITH A VELOCITY OF",V,"AND A TIME OF",T,"IS",round(A,4))


#FINDING VELOCITY
def velocity(DISPLACEMENT,TIME):
	D = DISPLACEMENT
	T = TIME
	V = D / T
	print("THE VELOCITY OF AN OBJECT WITH A DISPLACEMENT OF",D,"AND A TIME OF",T,"IS",round(V,4))


#FINDING MECHANICAL ADVANTAGE
def mechanicaladvantage(LOAD,EFFORT):
	L = LOAD
	E = EFFORT
	MA = L / E
	print("THE MECHANICAL ADVANTAGE OF AN OBJECT WITH LOAD OF",L,"AND AN EFFORT OF",E,"IS",round(MA,4))



#FINDING ELASTIC POTENTIAL ENERGY
def elasticpotentialenergy(SPRINGCONSTANT,LENGTHOFEXTENTION):
	S = SPRINGCONSTANT
	L = LENGTHOFEXTENTION
	EPE = (1/2) * S * L**2
	print("THE ELASTIC POTENTIAL ENERGY OF THE OBJECT IS",round(EPE,3))


#FINDING POWER
def power(WORK,TIME):
	W = WORK
	T = TIME
	P = W / T
	print("THE POWER OF AN OBJECT WITH A  WORK OF",W,"AND A TIME OF",T,"IS",round(P,4))


#FINDING GRAVITATIONAL POTENTIAL ENERGY
def gravitationalpotentialenergy(MASS,ACCELERATION,HEIGHT):
	M = MASS
	A = ACCELERATION
	H = HEIGHT
	GPE = M * A * H
	print("THE GRAVITATIONAL POTENTIAL ENERGY OF THE OBJECT IS",round(GPE,4))


def electricalenergy(CURRENT,TIME,VOLTAGE):
	C = CURRENT
	T = TIME
	V = VOLTAGE
	EE = C * T * V
	print("THE ELECTRICAL ENERGY OF THE AT A GIVEN TIME OF",T,"MINUTES WITH A CURRENT OF",C,"AND A VOLTAGE OF",V,"IS",round(EE,4))


def voltage(CURRENT,RESISTANCE):
	C = CURRENT
	R = RESISTANCE
	V = C * R
	print("THE VOLTAGE NF AN APLLIANCE WITH AN ELECTRIC CURRENT OF",C,"AND A RESISTANCE OF",R,"IS",round(V,4),"volts")

def current(VOLTAGE,RESISTANCE):
	V = VOLTAGE
	R = RESISTANCE
	C = V / R
	print("THE CURRENT WITH A VOLTAGE OF",V,"AND A RESISTANCE OF",R,"IS",round(C,4))


def molarconcentration(MOLES,LITRES):
	M = MOLES
	L = LITRES
	C = M / L
	print("THE MOLAR CONCENTRATION OF A SUBSTANCE WITH",M,"NUMBER OF MOLES AND ",L,"NUMBER OF LITRES IS",round(C,4),"mol/L")


def areaofparallelogram(BASE,HEIGHT):
	B = BASE
	H = HEIGHT
	A = B * H
	print("THE AREA OF THE PARALLELOGRAM WITH A BASE OF",B,"AND A HEIGHT OF",H,"IS",round(A,4))


def perimeterofparallelogram(SIDEA,BASE):
	A = SIDEA
	B = BASE
	P = (2*A + A*B)
	print("THE PERIMETER OF THE PARALLELOGRAM WTH ONE SIDE OF",A,"AND A BASE OF",B,"IS",round(P,4))


def vertex(MIDDLETERM,COEFFICIENTOFX,CONSTANT):
	M = MIDDLETERM
	C = COEFFICIENTOFX
	CO = CONSTANT
	V = -M / (2*C)
	print("THE X CO-ORDINATE OF THE VERTEX IS",round(V,3))
	V2 = (C*(V)**2)+M*(V)+CO
	print("THE Y CO-ORDINATE OF THE VERTEX IS",round(V2,3))
	V3 =round(V,2),round(V2,2)
	return V3


def perimeteroftrapezium(SIDEA,SIDEB,SIDEC,SIDED):
	A = SIDEA
	B = SIDEB
	C = SIDEC
	D = SIDED
	P = A + B + C + D
	print("THE PERIMETER OF THE TRAPEZIUM IS",round(P,4))



def momentum(mass,velocity):
	m = mass
	v = velocity
	M = m * v
	print("THE MOMENTUM OF AN OBJECT WITH A MASS OF",m,"and a velocity of",v,"is",round(M,4),"m/s")

def wavespeed(frequency,wavelength):
	f = frequency
	w = wavelength
	W = f * w
	print("THE WAVESPEED OF THE OBJECT WITH A FREQUENCY OF",f,"AND A WAVELENGTH OF",w,"IS",round(W,4),"m/s")



def conversiontable():
    print("THE FOLLOWING IS A COMBINATION OF BOTH SCIENCE AND MATHS FORMULAS AND CONVERSION CHARTS TO HELP YOU IN YOUR CONVERSION CALCULATION AND NORMAL CALCULATIONS")
    print("MATHS AND SCIENCE CONVERSION CHART")
    equations=(["MATHEMATICAL CONCEPTS","FORMULAS","SCIENCE CONCEPTS","FORMULAS"],
               ["AREA OF RECTANGLE","LENGTH * BREADTH","FORCE","MASS*ACCELERATION DUE TO GRAVITY"],
               ["PERIMETER OF RECTANGLE","(2*LENGTH)+(2*BREADTH)","DENSITY","MASS / VOLUME"],
               ["RADIAN","DEGREE NUMBER*(PI/180)","WORKDONE","FORCE*DISTANCE"],
               ["QUADRATIC EQUATION","-B+-SQRT((B**2)-4*A*C)/)2*A)","KINETIC ENERGY","1/2 *(MASS * VELOCITY**2)"],
               ["AREA OF TRIANGLE","(1/2)* BASE* HEIGTH","HYDROGENIONS","NUMBER OF MOLES * 6.02 * 10**23"],
               ["AREA OF NON-TRIANGLE","(1/2) * SIDE A * SIDE B *SIN(ANGLE)","EFFICIENCY OF MACHINE","(WORKOUTPUT / WORKINPUT)* 100%"],
               ["DEGREE","RADIAN*(180/PI)","PRESSURE","FORCE / AREA"],
               ["GRADIENT","(Y2-Y1) / (X2 - X1)","SPEED","DISTANCE / TIME"],
               ["COSINERULE","C = A**2+B**2-2(A*C)*COS(ANGLE)","ACCELERATION","VELOCITY / TIME"],
               ["SINERULE","(SINANGLE/ANGLESIDE)=(SINOTHERANGLE)/OTHERANGLESIDE)","VELOCITY","DISPLACEMENT / TIME"],
               ["COSINE ANGLE","ADJACENT / HYPOTHENUSE","MECHANICAL ADVANTAGE","LOAD / EFFORT"],
               ["SINE ANGLE","OPPOSITE / HYPOTHENUSE","ELASTICPOTENTIALENERGY","(1/2)*SPRING CONSTANT*(LENGTH OF EXTENTION)"],
               ["TANGENT ANGLE","OPPOSITE / ADJACENT","GRAVITATIONALPOTENTIALENERGY","MASS*ACCELERATION*HEIGTH"],
               ["SQUAREAREA","2 * LENGTH","ELECTRICAL ENERGY","CURRENT*TIME*VOLTAGE"],
               ["SQUAREPERIMETER","4 * LENGTH","MOLAR CONCENTRATION","NUMBER OF MOLES/NUMBER OF LITRES"],
               ["CIRCUMFERENCE","2 * PI * RADIUS","VOLTAGE","CURRENT * RESISTANCE"],
               ["AREA OF CIRCLE","PI * RADIUS**2","CURRENT","VOLTAGE / RESISTANCE"],
               ["ARCLENGTH","RADIUS * RADIAN","MOMENTUM","MASS * VELOCITY"],
               ["AREA OF TRAPEZIUM","(1/2) * SIDE A + SIDE B * HEIGTH","WAVESPEED","FREQUENCY * VELOCITY"],
               ["PERIMETER OF TRAPEZIUM","SIDE A + SIDE B + SIDE C + SIDE D"," YET TO BE INSERTED","YET TO BE INSERTED"],
               ["AREA OF PARALLELOGRAM","BASE * HEIGHT","YET TO BE INSERTED","YET TO BE INSERTED"],
               ["PERIMETER OF PARALLELOGRAM","(2 * SIDE A)+ (2 * BASE)","YET TO BE INSERTED","YET TO BE INSERTED"],
               ["VERTEX","-B / 2*A(FOR X),DIVIDE THROUGH BY X(FOR Y)","YET TO BE INSERTED","YET TO BE INSERTED"],
               ["AREA OF A TRAPEZOID","1/2*(BASE1+BASE2)*HEIGHT","YET TO BE INSERTED","YET TO BE INSERTED"])
 
    names =(["CONVERSION","CONVERSIONS 1","CONVERSION","CONVERSION 2"],
            ["CELCIUS TO FAHRENHEIT","C * 9/5 + 32","FAHRENHEIT TO CELCIUS","(F -32)*5/9"],
            ["KILOMETERS TO METERS","KILOMETER*1000","METERS TO KILOMETERS","METERS/1000"],
            ["LITRES TO MILLILITRES","LITRES*1000","MILLILITRES TO LITRES","MILLILITRES/1000"],
            ["GALLON TO QUARTS","GALLON*4","QUARTS TO GALLON","QUARTS/4"],
            ["KILOGRAM TO GRAMS","KILOGRAM*1000","GRAMS TO KILOGRAM","GRAMS/1000"],
            ["GRAMS TO MILLIGRAMS","GRAMS*1000","MILLIGRAMS TO GRAMS","MILLIGRAMS/1000"],
            ["FOOT TO INCHES","FOOT*12","INCHES TO FOOT","INCHES/12"],
            ["METERS TO CENTIMETERS","METERS*100","CENTIMETERS TO METERS","CENTIMETERS/100"],
            ["MILES TO METERS","MILES*160934","METERS TO MILES","METERS/160934"])

   
    formulas=(["LIST OF FUNCTIONS","FORMULA SYNTAX"],
              ["LINEAR FUNCTION","Y = MX + C"],
              ["QUADRATIC FUNCTION","Y = AX**2+BX+C"],
              ["EXPONENTIAL FUNCTION(ANNUAL GROWTH)","Y=AB**T"],
              ["EXPONENTIAL FUNCTION(COMPOUND INTREST)","A=P(1+R/M)**MT"],
              ["EXPONENTIAL FUNCTION(COMPOUND CONTINIOUS)","A=Pe**rt"],
              ["LOGARITHM PROPERTY 1","LOG(AB)=LOGA + LOGB"],
              ["LOGARITHM PROPERTY 2","LOG(A/B)=LOGA - LOGB"],
              ["LOGARITHM PROPERTY 3","LOG(A)**2 = 2LOG(A)"],
              ["POWER FUNCTION","Y = KX**P"],
              ["DIFFERENCE OF TWO SQUARES","(A**2-B**2)=(A-B)(A+B)"],
              ["EQUATION OF LINE","Y-Y1=M(X-X1)"],
              ["TRANSFORMATION FUNCTION","Af(B(X-H))+K"],
              ["SINUSOIDAL FUNCTION(SIN FUNCTION)","Asin(B(X-H))+K"],
              ["SINUSOIDAL FUNCTION(COS FUNCTION)","Acos(B(X-H))+K"],
              ["INVERSE FUNCTION OF(Y=2X)","X=Y/2"],
              ["COMPOSITE FUNCTION(H(X),F(X))","H(F(X))"])

    notifications=(["COMMON NOTIFICATIONS IN MATHEMATICS"],
                   ["DISTANCE = MATH.SQRT((X2-X1)**2+(Y2+Y1)**2))"],
                   ["MIDPOINT = (X1-X2)/2,(Y1+Y2)/2)"])
    for i in equations:
        print(":",i[0]," "*(25-len(i[0])),":",
              i[1]," "*(45-len(i[1])),":",
              i[2]," "*(28-len(i[2])),":",
              i[3]," "*(45-len(i[3])),":")

    print()
    print()

    
    for i in names:
        print(":",i[0]," "*(22-len(i[0])),":",
              i[1]," "*(22-len(i[1])),":",
              i[2]," "*(22-len(i[2])),":",
              i[3]," "*(22-len(i[3])),":")
    print()
    print()
        
    print("THERE ARE ALSO FCUNCTION FORMULAS YOU NEED TO TAKE NOTE AS WELL")
    print("LIST OF FUNCTIONS AND THEIR RESPECTIVE FORMULAS")
    for s in formulas:
        print("|",s[0]," "*(44-len(s[0])),"|",
              s[1]," "*(25-len(s[1])),"|")

    print()
    print()

    print("NOTIFICATIONS IN MATHEMATICS")
    for a in notifications:
        print("|",a[0]," "*(47-len(a[0])),"|")












	
