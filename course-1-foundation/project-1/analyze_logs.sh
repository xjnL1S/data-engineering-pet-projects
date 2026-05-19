#!/bin/bash

LOG_FILE="access.log"
REPORT_FILE="report.txt"

# Общее количество запросов
total_requests=$(wc -l < "$LOG_FILE")

# Количество уникальных IP-адресов
unique_ips=$(awk '{print $1}' "$LOG_FILE" | sort | uniq | wc -l)

# Количество запросов по методам
methods=$(awk '
{
    method=$6
    gsub(/"/, "", method)
    count[method]++
}
END {
    for (m in count)
        print m ":", count[m]
}' "$LOG_FILE")

# Самый популярный URL
popular_url=$(awk '
{
    url=$7
    count[url]++
}
END {
    max=0
    for (u in count) {
        if (count[u] > max) {
            max=count[u]
            result=u
        }
    }
    print max, result
}' "$LOG_FILE")

# Формирование отчета
{
    echo "Отчет по логам"
    echo "======================"
    echo "Общее количество запросов: $total_requests"
    echo "Количество уникальных IP-адресов: $unique_ips"
    echo
    echo "Количество запросов по методам:"
    echo "$methods"
    echo
    echo "Самый популярный URL: $popular_url"

} > "$REPORT_FILE"

echo "Отчет сохранен в $REPORT_FILE"