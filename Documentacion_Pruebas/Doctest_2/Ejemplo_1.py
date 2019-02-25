def doblar(lista):
    """
    Doblar número sólo números pares por compresión de listas

    >>> l = [1, 2, 3, 4, 5]
    >>> doblar(l)
    [4, 8]

    >>> l = []
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 4, 8, 12, 16]
    """
    return [n*2 for n in lista if n%2==0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

