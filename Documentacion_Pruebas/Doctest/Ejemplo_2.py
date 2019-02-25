def palindromo(palabra=""):
    """
    Crea un array auxiliar, inserta el original en el auxiliar empezando por el final, con esto el auxiliar tendra el original pero "dado la vuelta", comprueba si original y auxiliar son iguales, si lo son, entonces es palindromo.
    Tmb puedes pasar de crear un nuevo array, compara posicion 0 con posicion n-1, 1 con n-2, 2 con n-3 ....  siendo n el numero total de caracteres, si todos son iguales entonces palindromo
    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("Ana")
    True

    >>> palindromo("Atar a la rata")
    True
    """

    if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
