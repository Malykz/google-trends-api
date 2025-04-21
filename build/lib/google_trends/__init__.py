from .GoogleTrends import GoogleTrends

def fetch(geo) :
    return GoogleTrends(geo).result