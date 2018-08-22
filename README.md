# Prettify JSON

Скрипт преобразует исходное представление файла в формате JSON и выводит данные в удобном для чтения виде.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**

Для примера можно взять данные с портала [devman](https://devman.org/fshare/1502828617/1/) и сохранить в директории проекта под любым именем (например, `data.json`).

**Запуск на Linux**

```bash

$ python pprint_json.py data.json

# Скрипт выведет преобразованный json
{
    "type": "Feature",
    "properties": {
        "Attributes": {
            "TypeService": "реализация продовольственных товаров",
            "PublicPhone": [
                {
                    "PublicPhone": "(926) 281-82-60"
                }
            ],
            "OperatingCompany": null,
            "IsNetObject": "нет",
            "ClarificationOfWorkingHours": null,
            "District": "район Орехово-Борисово Северное",
            "AdmArea": "Южный административный округ",
            "global_id": 171714979,
            "Name": "Разливные напитки",
            "Address": "Борисовский проезд, дом 40А",
        },
        "RowId": "4af7d0bb-be94-40fa-aaaa-b32ebdddc967",
        "VersionNumber": 1,
        "ReleaseNumber": 2,
        "DatasetId": 1854
    },
}

```
Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
