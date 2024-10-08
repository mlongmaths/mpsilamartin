import matplotlib.pyplot as plt
from numpy import array,linspace
from scipy.integrate import odeint

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a]
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list
    
def F(X,t):
    y,yp,ypp = X
    yppp = (5-9*(t**2)*ypp-18*t*yp-6*y)/t**3
    return array([yp,ypp,yppp])

   
def plot_solutions(nom_de_fichier,b,n):
    X0 = array([2,0,0])
    t_list,X_list_euler = euler(F,1,b,X0,(b-1)/n)
    y_list_euler = [X[0] for X in X_list_euler]
    X_list_odeint = odeint(F,X0,t_list)
    y_list_odeint = [X[0] for X in X_list_odeint]
    plt.clf()
    plt.plot(t_list,y_list_euler,label="Méthode d'Euler")
    plt.plot(x_list_odeint,y_list_odeint,label="Odeint")
    plt.title("$t^3y'''+9t^2y''+18ty+6y=5$, $y(0)=2$, $y'(0)=y''(0)=0$, ${}$ segments".format(n))
    plt.legend(loc=0)
    plt.ylim(1.84,2.1)
    plt.savefig(nom_de_fichier)
    
if __name__ == '__main__':
    plot_solutions('exo_8_0_2_3.png',2,10)
