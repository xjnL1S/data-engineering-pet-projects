import json

def total_revenue(purchases_list: list[dict]) -> float:
    total = 0
    for item in purchases_list:
        total += item["price"] * item["quantity"]
    return total

def items_by_category(purchases_list: list[dict]) -> dict:
    categories = {}
    for item in purchases_list:
        if item["category"] not in categories:
            categories[item["category"]] = []
        if item["item"] not in categories[item["category"]]:
            categories[item["category"]].append(item["item"])
    return categories

def expensive_purchases(purchases_list: list[dict], min_price: float) -> list[dict]:
    pricey_purchases = []
    for item in purchases_list:
        if item["price"] >= min_price:
            pricey_purchases.append(item)
    return pricey_purchases

def average_price_by_category(purchases_list: list[dict]) -> dict:
    categories = {}
    for item in purchases_list:
        if item["category"] not in categories:
            categories[item["category"]] = []
        categories[item["category"]].append(item["price"])
    avg_price = {}
    for category in categories:
        avg_price[category] = sum(categories[category]) / len(categories[category])
    return avg_price

def most_frequent_category(purchases_list: list[dict]) -> str:
    categories = {}
    for item in purchases_list:
        if item["category"] not in categories:
            categories[item["category"]] = 0
        categories[item["category"]] += item["quantity"]
    return max(categories, key=categories.get)

if __name__ == "__main__":
    with open("purchases.json", "r", encoding="utf-8") as f:
        purchases = json.load(f)
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Товары дороже {(minimum_price := 1.0)}: {expensive_purchases(purchases, minimum_price)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")