# Error Log for Technical Questions

<span style="font-size: 1.5em;"><b>__Subtitle__</b></span>

Created:  26 May 2025

## Syntax Errors
---
- `self.variable` not in `__init__` method of class
- Incorrect syntax for error throw
	- `raise ValueError("message")`
- Incorrect import of default dict
	- `from collections import defaultdict`
- `abs()` referenced as a part of math package
- Validating non-null inputs with `if not x` leading to 0s being picked up

## Logic Errors
---
- 

## Missed Optimisations
---
- Wrote lengthy code to avoid O(n) by going for O(obstacles) (in [this](https://www.hackerrank.com/challenges/queens-attack-2/problem) question) but there could actually be $n^2$ obstacles 😐
