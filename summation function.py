A=int(input(" enter summation starting limit: "))
B=int(input(" enter summation ending limit: "))
function=0

fx_string_storer=input(" enter function you want: ")
# hume function ko pehle 0 ke equal rakhna padta hai and for later is function ke aage+= formula karna padta hai because ye formula me limit lagi hui ko add karte hua chalta hai 

# hume automatic formula banane ke liye pehle usse input string me lo
# phir second second variable ke andar eval dalke (me pehle wala variable dalo)
# ye string ko formula me badal deta hai 


# x hi lagana hoga loop me because code puchega x ki value konsi hai loop bolega 2 phir code usse x wale formula me put kardega 
for x in range(A,B +1):
# normally loop me last wali value code exclude karke result deta ye +1 karne se code ko pata chalta ek value extra karna isse fayda ye hota ki limit ka khyaal nahi rakhna padta     
    fx_real_formula =eval(fx_string_storer)
    function+= fx_real_formula
    print ("function",function)


    