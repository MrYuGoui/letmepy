from math import *

a = 6378245
ee = 0.00669342162296594323


def inMercator(lon, lat):
    '''
    绝对坐标转墨卡托投影
    :param lon:经度
    :param lat:纬度
    :return:横纵坐标
    '''
    x = lon * 20037508.34 / 180
    y = (log(tan((90 + lat) * pi / 360)) / (pi / 180)) * 20037508.34 / 180
    return (x, y)


def deMercator(x, y):
    '''
    墨卡托投影转绝对坐标
    :param x:横坐标
    :param y:纵坐标
    :return:经纬度
    '''
    lon = x * 180 / 20037508.34
    lat = 180 / pi * (2 * atan(exp(y * 180 / 20037508.34 * pi / 180)) - pi / 2)
    return (round(lon,10), round(lat,10))


def WGS84_to_GCJ02(lon, lat):
    '''
    WGS84转GCJ02
    :param lon:WGS精度
    :param lat:WGS纬度
    :return:GCJ经纬度
    '''
    dLon = transformlon(lon - 105, lat - 35)
    dLat = transformlat(lon - 105, lat - 35)
    radLat = lat / 180 * pi
    magic = 1 - ee * sin(radLat) * sin(radLat)
    sqrtMagic = sqrt(magic)
    dLat = (dLat * 180) / ((a * (1 - ee)) / (magic * sqrtMagic) * pi)
    dLon = (dLon * 180) / (a / sqrtMagic * cos(radLat) * pi)
    mgLon = lon + dLon
    mgLat = lat + dLat
    return (round(mgLon,10), round(mgLat,10))


def GCJ02_to_WGS84(lon, lat):
    '''
    GCJ02转WGS84
    :param lon:GCJ经度
    :param lat:GCJ纬度
    :return:WGS经纬度
    '''
    dlat = transformlat(lon - 105.0, lat - 35.0)
    dlon = transformlon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlon = (dlon * 180.0) / (a / sqrtmagic * cos(radlat) * pi)
    mglon = lon + dlon
    mglat = lat + dlat
    return round(lon * 2 - mglon,10), round(lat * 2 - mglat,10)

def transformlat(lon, lat):
    '''

    :param lon:
    :param lat:
    :return:
    '''
    ret = -100 + 2 * lon + 3 * lat + 0.2 * lat * lat + 0.1 * lon * lat + 0.2 * sqrt(fabs(lon))
    ret += (20 * sin(6 * lon * pi) + 20 * sin(2 * lon * pi)) * 2 / 3
    ret += (20 * sin(lat * pi) + 40 * sin(lat / 3 * pi)) * 2 / 3
    ret += (160 * sin(lat / 12 * pi) + 320 * sin(lat * pi / 30)) * 2 / 3
    return ret


def transformlon(lon, lat):
    '''

    :param lon:
    :param lat:
    :return:
    '''
    ret = 300 + lon + 2 * lat + 0.1 * lon * lon + 0.1 * lon * lat + 0.1 * sqrt(fabs(lon))
    ret += (20 * sin(6 * lon * pi) + 20 * sin(2 * lon * pi)) * 2 / 3
    ret += (20 * sin(lon * pi) + 40 * sin(lon / 3 * pi)) * 2 / 3
    ret += (150 * sin(lon / 12 * pi) + 300 * sin(lon / 30 * pi)) * 2 / 3
    return ret


def GCJ02_to_BD09(lon, lat):
    '''
    GCJ02转BD09
    :param lon:GCJ经度
    :param lat:GCJ纬度
    :return:BD经纬度
    '''
    # http://api.map.baidu.com/geoconv/v1/?coords=120.670870,28.017590&from=3&to=5&ak=aeNTgUpayl9YDZkewEXRqQ5TsLP02ckt
    x_pi = pi * 3000.0 / 180.0
    z = sqrt(lon * lon + lat * lat) + 0.00002 * sin(lat * x_pi)
    theta = atan2(lat, lon) + 0.000003 * cos(lon * x_pi)
    bd_lon = z * cos(theta) + 0.0065
    bd_lat = z * sin(theta) + 0.006
    return (round(bd_lon,10), round(bd_lat,10))


def BD09_to_GCJ02(lon, lat):
    '''
    BD09转GCJ02
    :param lon:BD经度
    :param lat:BD纬度
    :return:GCJ经纬度
    '''
    x_pi = pi * 3000.0 / 180.0
    x = lon - 0.0065
    y = lat - 0.006
    z = sqrt(x * x + y * y) - 0.00002 * sin(y * x_pi)
    theta = atan2(y, x) - 0.000003 * cos(x * x_pi)
    gg_lon = z * cos(theta)
    gg_lat = z * sin(theta)
    return (round(gg_lon,10), round(gg_lat,10))