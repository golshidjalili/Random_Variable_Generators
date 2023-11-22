from RVGs import rvg_poisson, rvg_exponential, rvg_triangular


# Poisson
alpha = 0.5
rvg_poisson(alpha=alpha)

# Exponential
parameter = 2
rvg_exponential(parameter=parameter)

# Triangular
minimum = 5
most_likely = 6
maximum = 7
rvg_triangular(
    minimum=minimum,
    most_likely=most_likely,
    maximum=maximum
)
