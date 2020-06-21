from PYTHON_FORMULAS3 import *
def main():
	print("HELLO AND WELCOME TO SPARTAN CORPORATION OF ADVANCED SCIENTIFIC AND MATHMATICAL CALCULATIONS.THE PROGRAM FEATURES THE FORMULAS LISTED BELOW,BASIC\n")
	print()
	print("FORMULAS TO KEEP IN MEMORY AS WELL AS SOME CONVERSION RATES IN THE TABLES BELOW TO AID YOU IN YOUR CALCULATIONS.TO BEGIN CALCULATIONS ENTER(YES) OR\n")
	print()
	print("TO QUIT, ENTER (NO).ONCE AGAIN YOU ARE WELCOME AND GOOD LUCK\n")
	print()
	print("TAKE NOTE ALSO OF SOME DIFFERENCES IN THE SYNTAX OF MATHEMATICS AND OF THE PYTHON PROGRAM")
	print()
	
	NOTE=(["MATHEMATICS SYNTAX","PROGRAM SYNTAX"],
              ["2 RAISED TO THE POWER 2","2**2"])
	for y in NOTE:
		print(":",y[0]," "*(30-len(y[0])),":",
		      y[1]," "*(30-len(y[1])),":")
	print()
	a = input("DO YOU WANT TO BEGIN SOME CALCULATIONS: ")
	print()
	b = "YES"
	c = "NO"
	E = "EFFICIENCY OF MACHINE"
	F = "FORCE"
	D = "DENSITY"
	W = "WORKDONE"
	H = "HYDROGENIONS"
	P = "PRESSURE"
	K = "KINETIC ENERGY"
	Q = "QUADRATIC EQUATION"
	R = "RADIAN"
	DE ="DEGREE"
	AOT = "AREA OF TRIANGLE"
	AONT = "AREA OF NON-TRIANGLE"
	COSINERULE = "COSINERULE"
	SINERULE = "SINERULE"
	COS ="COSINE ANGLE"
	SIN = "SINE ANGLE"
	TAN = "TANGENT ANGLE"
	AOR = "AREA OF RECTANGLE"
	POR = "PERIMETER OF RECTANGLE"
	GRADIENT = "GRADIENT"
	SQUAREAREA = "SQUAREAREA"
	SQUAREPERIMETER = "SQUAREPERIMETER"
	CIRCUMFERENCE = "CIRCUMFERENCE"
	AOC = "AREA OF CIRCLE"
	ARCLENGTH = "ARCLENGTH"
	AOT = "AREA OF TRAPEZIUM"
	ACCELERATION = "ACCLERATION"
	VELOCITY = "VELOCITY"
	SPEED = "SPEED"
	MA = "MECHANICAL ADVANTAGE"
	EPE = "ELASTIC POTENTIAL ENERGY"
	GPE = "GRAVITATIONAL POTENTIAL ENERGY"
	EE = "ELECTRICAL ENERGY"
	VOL = "VOLTAGE"
	CURR = "CURRENT"
	MC = "MOLAR CONCENTRATION"
	VE = "VERTEX"
	PARRA = "AREA OF PARALLELOGRAM"
	PERIT = "PERIMETER OF TRAPEZIUM"
	PERIP = "PERIMETER OF PARALLELOGRAM"
	MO = "MOMENTUM"
	WAV = "WAVESPEED"
	NO = "STOP"
	
	if a.upper()== c:
		d = input("ARE YOU SURE YOU WANT TO QUIT: ")
		if d.upper() == b:
			print("THE PROGRAM HAS QUITTED")	
	elif a.upper() == b:
		conversiontable()
		n = 20000000000000000000000
		for s in range(n):
			s = input("WHAT DO YOU WANT TO CALCULATE: ")
			
			if s.upper() == E:
				print("INPUT efficiencyofmachine(enter workoutput,enterworkinput)")
				a = input("ENTER YOUR CALCULATION: ")
				return eval(a)
				print(s)
			elif s.upper() == F:
				print("INPUT force(enter mass, enter accleration)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == W:
				print("INPUT work(enter force, enter distance)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == H:
				print("INPUT hydrogenions(number of moles)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == P:
				print("INPUT pressure(enter force, enter area)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == K:
				print("INPUT kineticenergy(enter mass,enter velocity)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == Q:
				print("INPUT quadraticroots(enter the a,enter the b,enter the c)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == R:
				print("INPUT findingradian(enter the degree number)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper()== DE:
				print("INPUT findingdegree(enter the radian number)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == AOT:
				print("INPUT areaoftriangle(enter base, enter height)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == AONT:
				print("INPUT areaofnontriangle(enter sideA, entersideB,enter angle)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == AOR:
				print("INPUT areaofrectangle(enter the length,enter the breadth)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == POR:
				print("INPUT perimeterofrectangle(enter the length,enter the breadth)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == COSINERULE:
				print("INPUT cosinerule(ENTER SIDE A,ENTER SIDE B,ENTER THE ANGLE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == SINERULE:
				print("INPUT sinruleangle(ENTER ANGLE TO BE FOUND,ENTER OPPOSITE SIDE OF ANGLE TO BE FOUND,ENTER OTHER ANGLE,ENTER OTHERANGLE SIDE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == COS:
				print("INPUT cosangle(ENTER THE ADJACENT,ENTER THE HYPOTHENUSE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == SIN:
				print("INPUT sinangle(ENTER THE OPPOSITE,ENTER THE HYPOTHENUSE)")
				a = input("ENTER THE CALCULATIONl: ")
				return eval(a)
			elif s.upper() == TAN:
				print("INPUT tanangle(ENTER THE OPPOSITE,ENTER THE ADJACENT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == GRADIENT:
				print("INPUT gradient(ENTER Y2,ENTER Y1,ENTER X2,ENTER X1)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == SQUAREAREA:
				print("INPUT squarearea(ENTER THE LENGTH)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == SQUAREPERIMETER:
				print("INPUT squareperimeter(ENTER THE LENGTH)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == CIRCUMFERENCE:
				print("INPUT circumference(ENTER THE RADIUS)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == AOC:
				print("INPUT areaofcircle(ENTER THE RADIUS)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == ARCLENGTH:
				print("INPUT arclength(ENTER THE RADIUS,ENTER THE RADIAN)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == AOT:
				print("INPUT areaoftrapezium(ENTER THE SIDE A,ENTER SIDE B,ENTER THE HEIGHT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == ACCELERATION:
				print("INPUT accleration(ENTER THE VELOCITY,ENTER THE TIME)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == VELOCITY:
				print("INPUT velocity(ENTER THE DISPLACEMENT, ENTER THE TIME)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == SPEED:
				print("INPUT speed(ENTER THE DISTANCE,ENTER THE TIME)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == MA:
				print("INPUT mechanicaladvantage(ENTER THE LOAD,ENTER THE EFFORT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == EPE:
				print("INPUT elasticpotentialenergy(SPRING CONSTANT,ENTER THE LENGTH OF THE EXTENTION)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == GPE:
				print("INPUT gravitationalpotentialenergy(ENTER THE MASS,ENTER THE ACCELERATION,ENTER THE HEIGHT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == EE:
				print("INPUT electricalenergy(ENTER THE CURRENT,ENTER THE TIME,ENTER THE VOLTAGE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == MC:
				print("INPUT molarconcentration(ENTER THE NUMBER OF MOLES,ENTER THE NUMBER OF LITRES)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == VOL:
				print("INPUT voltage(ENTER THE CURRENT,ENTER THE RESISTANCE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == CURR:
				print("INPUT current(ENTER THE VOLTAGE,ENTER THE RESISTANCE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == VE:
				print("INPUT vertex(ENTER THE MIDDLETERM,ENTER THE CO-EFFICIENT OF X,ENTER THE CONSTANT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == PERIT:
				print("INPUT perimeteroftrapezium(ENTER SIDE A, ENTER SIDE B, ENTER SIDE C, ENTER SIDE D)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == PARRA:
				print("INPUT areaofparallelogram(ENTER BASE, ENTER THE HEIGHT)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == PERIP:
				print("INPUT perimeterofparallelogram(ENTER THE SIDE A, ENTER THE BASE)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == MO:
				print("INPUT momentum(ENTER THE MASS,ENTER THE VELOCITY)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			elif s.upper() == WAV:
				print("INPUT wavespeed(ENTER THE FREQUENCY, ENTER THE WAVELENGTH)")
				a = input("ENTER THE CALCULATION: ")
				return eval(a)
			#elif s.upper() == D:
                                #print("INPUT density(ENTER THE MASS, ENTER THE VOLUME)")
                                #print("INPUT density(ENTER THE MASS, ENTER THE VOLUME)")
                                #a = input("ENTER THE CALCULATION: ")
                               # return eval(a)
			
		
main()
