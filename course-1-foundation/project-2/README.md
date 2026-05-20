# Store Purchases Analytics with Python

This project analyzes store purchase data using Python.

The script `main.py` reads purchase information from `purchases.json` and generates a report with:

- Total revenue
- List of items grouped by category
- Purchases above a specified minimum price
- Average price by category
- Category with the highest number of sold items

## Project Files

```text
main.py
README.md
```

## Input Data

Purchase data is stored in `purchases.json`.

Example:

```json
[
    {
        "item": "apple",
        "category": "fruit",
        "price": 1.2,
        "quantity": 10
    },
    {
        "item": "banana",
        "category": "fruit",
        "price": 0.5,
        "quantity": 5
    },
    {
        "item": "milk",
        "category": "dairy",
        "price": 1.5,
        "quantity": 2
    },
    {
        "item": "bread",
        "category": "bakery",
        "price": 2.0,
        "quantity": 3
    }
]
```

Fields:

- `item` — product name
- `category` — product category
- `price` — price per item
- `quantity` — number of purchased items

## Run

Run the script:

```bash
python main.py
```

## Expected Output

The script prints an analytics report.

Example:

```text
Total revenue: 21.0

Items by category:
{'fruit': ['apple', 'banana'],
'dairy': ['milk'],
'bakery': ['bread']}

Purchases with price >= 1.0:
[
{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10},
{'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2},
{'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}
]

Average price by category:
{'fruit': 0.85,
'dairy': 1.5,
'bakery': 2.0}

Most frequent category:
fruit
```