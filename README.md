# Random Variable Generator
## Introduction
In order to simulate many real-world problems, after fitting a probability distribution to a sequence of numbers, there is a need to artificially generate variables (called pseudo-random variables) that come from that specific distribution.
## Poisson
Poisson distribution is a famous discrete probability distribution mostly used to fit
data of number of arrivals of customers in a system (e.g., number of customers who
arrive in a bank in one hour). This distribution is defined by a parameter called rate
of arrival (𝛼). Here are the steps to generate Poisson random variables:
Step 1: Set 𝑛 = 0 and 𝑝 = 1
Step 2: Generate a random (uniform) number 𝑅௡ାଵ;
 Set 𝑝 = 𝑝 ∗ 𝑅௡ାଵ
Step 3: If 𝑝 < 𝑒
ିఈ, then print n, otherwise increase n by one and return to step 2. 
