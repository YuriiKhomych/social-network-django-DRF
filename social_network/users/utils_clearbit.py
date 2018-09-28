import clearbit

clearbit.key = 'KEY'


def get_data(email):
    try:
        response = clearbit.Enrichment.find(email=email, stream=True)
        data = {}
        if response:
            if response['person'] is not None:
                data['first_name'] = response['person']['name']['givenName']
                data['last_name'] = response['person']['name']['familyName']
            if response['company'] is not None:
                data['company'] = response['company']['name']
        return data
    except:
        return
