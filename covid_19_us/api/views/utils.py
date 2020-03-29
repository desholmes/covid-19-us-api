import pandas as pd
from django.core.cache import caches


def url_to_key(url):
    key = url.replace('https://raw.githubusercontent.com/', '')
    return key.replace('/', '_')


def get_df_from_url(url):
    cache_key = url_to_key(url)
    cached_df = caches['default'].get(cache_key)

    if cached_df is None:
        df = pd.read_csv(url)
        df = df.fillna(-1)
        caches['default'].set(cache_key, df, 3600)  # 1hr
        cached_df = df

    return cached_df


def get_states_from_df(df):
    states = {}
    i = 0
    for index, row in df.iterrows():
        states[i] = State(date=row["date"],
                          state=row["state"],
                          fips=row["fips"],
                          cases=row["cases"],
                          deaths=row["deaths"])
        i += 1
    return states


def get_states_by_date(date_str, df):
    states_by_date = df[df.date.eq(date_str)]
    if len(states_by_date) == 0:
        raise ValueError
    return get_states_from_df(states_by_date)


def get_counties_from_df(df):
    counties = {}
    i = 0
    for index, row in df.iterrows():
        counties[i] = County(date=row["date"],
                             county=row["county"],
                             state=row["state"],
                             fips=row["fips"],
                             cases=row["cases"],
                             deaths=row["deaths"])
        i += 1
    return counties


def get_counties_by_date(date_str, df):
    counties_by_date = df[df.date.eq(date_str)]
    if len(counties_by_date) == 0:
        raise ValueError
    return get_counties_from_df(counties_by_date)


class State(object):
    def __init__(self, **kwargs):
        for field in ('date', 'state', 'fips', 'cases', 'deaths'):
            setattr(self, field, kwargs.get(field, None))


class County(object):
    def __init__(self, **kwargs):
        for field in ('date', 'county', 'state', 'fips', 'cases', 'deaths'):
            setattr(self, field, kwargs.get(field, None))
