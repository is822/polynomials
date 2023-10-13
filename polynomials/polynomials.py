class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def deg(self):
        return len(self.coefficients)-1
    
    def __str__(self):
        coefs = self.coefficients
        terms = []

        #Degree 0 and 1 terms have conventionally have different representation
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.deg()>0 and coefs[1]:
            terms.append(f"{coefs[1]}x")

        #Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]
        
        #Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

