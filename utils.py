from time import perf_counter
import settings

def heightPrct(percentage):
    return (settings.HEIGHT / 100) * percentage

def widthPrct(percentage):
    return (settings.WIDTH / 100) * percentage
    