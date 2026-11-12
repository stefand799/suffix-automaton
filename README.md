# Suffix Automaton

**Author:** Stefan D.  
**Date of Discovery:** November 2026  
**Repository:** [stefand799/suffix-automaton](https://github.com/stefand799/suffix-automaton)

---

A minimal Python implementation of a discrete suffix-addition automaton, tracking the 37-step limit cycle starting from seed `9618`.

## Rule

The automaton operates as an iterative feedback system:

$$N_{t+1} = F(N_t)$$

Where $F(N)$ is the sum of each unique integer suffix value of $N$, automatically deduplicating leading-zero variants (e.g., `"05"` and `"5"` both evaluate to `5` and are counted once).

## Usage

Run the simulation script to verify the sequence and cycle periodicity:

```bash
python automaton.py