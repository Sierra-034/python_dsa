
def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selection_sort(lyst):
    i = 0
    while i < len(lyst) - 1:    # Do n - 1 searches
        min_index = i           # for the smallest
        j = i + 1
        while j < len(lyst):    # Start a search
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:      # Exchange if needed
            swap(lyst, i, min_index)
        i += 1


# Evaluar detenidamente el posible error de desplazamiento en 1
def bubble_sort(lyst):
    n = len(lyst)
    while n > 1:                        # Do n - 1 bubbles
        i = 1                           # Start each bubble
        while i < n:
            if lyst[i] < lyst[i - 1]:   # Exchange if needed
                swap(lyst, i, i - 1)
            i += 1
        n -= 1 


def insertion_sort(lyst):
    i = 1
    while i < len(lyst):
        key = lyst[i]
        j = i - 1
        while j > 0 and key < lyst[j]:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = key
