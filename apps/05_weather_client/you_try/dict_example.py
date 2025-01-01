def main():
    # d = {
    #     'city':'Portland',
    #     'state':'ME',
    #     'details':['Cold','Warm','Snowy']
    # }
    # # print(d['country'])
    # print(d.get('country','US'))
    # d['country'] = 'AU'
    # print(d.get('country','US'))
    # print(d)
    w = {
        "weather": {
            "description": "clear sky",
            "category": "Clear"
        },
        "wind": {
            "speed": 5.6,
            "deg": 55
        },
        "units": "metric",
        "forecast": {
            "temp": 24.11,
            "feels_like": 23.57,
            "pressure": 1014,
            "humidity": 38,
            "low": 24.11,
            "high": 24.11
        },
        "location": {
            "city": "Portland",
            "state": "OR",
            "country": "US"
        },
        "rate_limiting": {
            "unique_lookups_remaining": 49,
            "lookup_reset_window": "1 hour"
        }
    }

    print(w.get('forecast').get('temp'))


if __name__ == '__main__':
    main()
