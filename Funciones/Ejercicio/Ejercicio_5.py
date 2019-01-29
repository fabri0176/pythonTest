def recortar(num_recortar, lim_inf, lim_sup):
   if num_recortar < lim_inf:
       return lim_inf
   elif num_recortar > lim_sup:
       return  lim_sup
   else:
       return num_recortar


print(recortar(15,0,10))