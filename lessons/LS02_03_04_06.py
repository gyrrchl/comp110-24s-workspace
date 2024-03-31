def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    """defining this."""
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n