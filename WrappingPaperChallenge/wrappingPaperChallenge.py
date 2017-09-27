from sys import stdin
    
wrapping = 0
ribbon = 0

# Main program execution
with open("input.txt") as f:
    for line in f:
        dim = line.split("x")
        d1 = int(dim[0])
        d2 = int(dim[1])
        d3 = int(dim[2])

        sd1 = min(d1, d2, d3)
        sd2 = 0
        if (sd1 == d1):
            sd2 = min(d2, d3)
        elif (sd1 == d2):
            sd2 = min(d1, d3)
        else:
            sd2 = min(d1, d2)

        ribbon = ribbon + (2*sd1) + (2*sd2) + (d1*d2*d3)
        
        s1 = int(d1)*int(d2)
        s2 = int(d2)*int(d3)
        s3 = int(d1)*int(d3)
        s4 = min(s1, s2, s3)
        area = (2*s1) + (2*s2) + (2*s3)
        wrapping = wrapping + area + s4
        
        

