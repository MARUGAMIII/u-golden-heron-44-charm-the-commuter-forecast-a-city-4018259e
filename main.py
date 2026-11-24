"""Charm the Commuter entry: one line of weather for a city that isn't.

Writes a single-line weather forecast (plain ASCII, 1-140 characters)
for an invented city to /output/entry.txt.
"""

FORECAST = "Wobbleton: scattered showers, a stiff breeze, and a 70% chance the 8:15 bus sees you sprinting, waves, and keeps going anyway."


def main():
    text = FORECAST.strip()
    # Gate self-check: mirror the sealed scorer (1-140 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
