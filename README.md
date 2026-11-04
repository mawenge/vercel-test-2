# vercel-test-2

Small Python text-statistics library used as a second target repository for a
Vercel eve software factory POC. Standard library only; tests use `unittest`.

```bash
python -m unittest discover -s tests -v
python -m textkit some_file.txt
```

Contains known rough edges on purpose (see the issues) so the factory has real
work to do.
