def scrape_table(table):
    rows = []
    header = []
    for item in table.find_all('th'):
        field_name = item.text.strip()
        if field_name:
            header.append(field_name)
    for item in table.find_all('tr'):
        index = 0
        row = {}
        for td in item.find_all('td'):
            field_value = td.text.strip()
            row[header[index]] = field_value
            index += 1
        if row:
            rows.append(row)

    print(f'{len(rows)} items scrapped')

    return rows
