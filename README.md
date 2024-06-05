# API proyecto AyP 2223-1

## Equipos

Deberá hacer una petición GET al url [https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
  {
    "name": "str",
    "flag": "str",
    "fifa_code": "str",
    "group": "str",
    "id": "str"
  },
```

## Estadios y Restaurantes

Deberá hacer una petición GET al url [https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
{
    "id": "int",
    "name": "str",
    "capacity": ["int", "int"],
    "location": "str",
    "restaurants": [
      {
        "name": "str",
        "products": [
          {
            "name": "str",
            "price": "int",
            "type": "str"
          },
        ]
      }
    ]
  },
```

## Partidos

Deberá hacer una petición GET al url [https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
  {
    "home_team": "str",
    "away_team": "str",
    "date": "str",
    "stadium_id": "int",
    "id": "str"
  },
```
