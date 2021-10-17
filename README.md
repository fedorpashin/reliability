# reliability

[![build](https://github.com/fedorpashin/reliability/workflows/build/badge.svg)](https://github.com/fedorpashin/reliability/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0b2912a94e2a66ef70d9/maintainability)](https://codeclimate.com/github/fedorpashin/reliability/maintainability)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Managed By Self XDSD](https://self-xdsd.com/b/mbself.svg)](https://self-xdsd.com/p/fedorpashin/reliability?provider=github)

**reliability** is a Python package that provides reliability calculations for systems using statistical modeling.

## Example

```python
import reliability as rb

kit = rb.System(
    parts := tuple([
        rb.Part(1, 40e-6),
        rb.Part(2, 10e-6),
        rb.Part(3, 80e-6),
    ]),
    rb.Scheme({
        parts[0]: tuple([0, 1, 2]),
        parts[1]: tuple([3, 4]),
        parts[2]: tuple([5, 6, 7, 8, 9, 10]),
    }),
    (lambda x: ((x[0] and x[1] or x[2])
                and x[3] and x[4]
                and (x[5] and x[6] or x[7] and x[8] or x[9] and x[10])))
).min_possible_kit_for(
    0.999, 
    8760,
    0.99,
    {
        parts[0]: 3,
        parts[1]: 3,
        parts[2]: 12,
    }
)
```
