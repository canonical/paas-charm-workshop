# Create your views here.
from django.http import JsonResponse


def fibonacci(request, n):
    """Return the first n numbers of the Fibonacci sequence."""
    n = int(n)
    if n < 0:
        return JsonResponse({"error": "Invalid input"}, status=400)

    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return JsonResponse({"fibonacci": fib_sequence})
