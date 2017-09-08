# normalizer

The normalizer is a python script that can read in a CSV from stdin and normalize the data emitting a CSV on stdout.

The data expected and transformation that will occur is outlined below.

### Transformation Table

| Header | Raw Data | Transformation | Formatted Data |
| --- | --- | --- | --- |
| Timestamp | 4/1/11 11:00:00 AM |
| Address | 123 4th St, Anywhere, AA |
| ZIP | 94121 |
| FullName | Mary|
| FooDuration | 1:23:32.123 |
| BarDuration | 1:32:33.123 |
| TotalDuration | zzsasdfa |
| Notes | I like Emoji! 🍏🍎😍 |
