import collections

#Named tuples
Location = collections.namedtuple('Location','city state country')

def main():
    # show the header
    show_header()

    # Get the location request
    location_text = input('Where do you want the weather report(e.g. Portland, US)? ')
    print(f"You selected {location_text}")

    # Convert plaintext over to data we can use
    loc = convert_plaintext_location(location_text)
    print(loc)

    # Get the report from the API

    # Report the weather


def show_header():
    print('---------------------------')
    print('      WEATHER CLIENT')
    print('---------------------------')
    print()


def convert_plaintext_location(location_text):
    if not location_text or not location_text.strip():
        return None
    location_text = location_text.lower().strip()
    parts = location_text.split(',')

    city = ""
    state = ""
    country = "US"
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None
    # print(f"City={city}, State={state}, Country={country}")
    # return city, state, country
    # t2 = Location(city,state,country)
    # print(f"city = {t2.city}  state = {t2.state} country = {t2.country}")
    return Location(city,state,country)



if __name__ == '__main__':
    main()
