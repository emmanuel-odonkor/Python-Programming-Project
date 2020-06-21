def conversiontable():
    print("THE FOLLOWING IS A COMBINATION OF BOTH SCIENCE AND MATHS FORMULAS AND CONVERSION CHARTS TO HELP YOU IN YOUR CONVERSION CALCULATION AND NORMAL CALCULATIONS")
    print("MATHS AND SCIENCE CONVERSION CHART")
    equations=(["MATHEMATICAL CONCEPTS","FORMULAS","SCIENCE CONCEPTS","FORMULAS"],
               ["AREA OF A RECTANGLE","LENGTH * BREADTH","FORCE","MASS*ACCELERATION DUE TO GRAVITY"],
               ["PERIMETER OF A RECTANGLE","(2*LENGTH)+(2*BREADTH)","DENSITY","MASS / VOLUME"],
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

conversiontable()
