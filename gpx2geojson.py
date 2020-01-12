import gpxpy
from umapgeojson import ATMFeature, AEDFeature, HospitalFeature, FreeWiFiFeature, SSWHFeature, SSFeature, BenchFeature, VMFeature, VMADFeature, ToiletFeature
import geojson
import sys
import os

def getFeatures( gpx ):
    # gpxファイルに定義されたウエイポイントnameから必要な地物のみgeojsonオブジェクトに変換
    features = []
    for waypoint in gpx.waypoints:
        if waypoint.name == 'atm' or waypoint.name == 'ATM':
            atm = ATMFeature(waypoint.longitude, waypoint.latitude)
            features.append(atm.getGeoJSON())
        if waypoint.name == 'aed' or waypoint.name == 'AED':
            aed = AEDFeature(waypoint.longitude, waypoint.latitude)
            features.append(aed.getGeoJSON())
        if waypoint.name == '病院':
            hospital = HospitalFeature(waypoint.longitude, waypoint.latitude)
            features.append(hospital.getGeoJSON())
        if waypoint.name == 'freewifi' or waypoint.name == 'FreeWiFi':
            wifi = FreeWiFiFeature(waypoint.longitude, waypoint.latitude)
            features.append(wifi.getGeoJSON())
        if waypoint.name == '災害時帰宅支援ステーション':
            sswh = SSWHFeature(waypoint.longitude, waypoint.latitude)
            features.append(sswh.getGeoJSON())
        if waypoint.name == 'セーフティステーション':
            ss = SSFeature(waypoint.longitude, waypoint.latitude)
            features.append(ss.getGeoJSON())
        if waypoint.name == 'ベンチ':
            bench = BenchFeature(waypoint.longitude, waypoint.latitude)
            features.append(bench.getGeoJSON())
        if waypoint.name == '自販機':
            vm = VMFeature(waypoint.longitude, waypoint.latitude)
            features.append(vm.getGeoJSON())
        if waypoint.name == '災害対応自販機':
            vmad = VMADFeature(waypoint.longitude, waypoint.latitude)
            features.append(vmad.getGeoJSON())
        if waypoint.name == 'トイレ':
            toilet = ToiletFeature(waypoint.longitude, waypoint.latitude)
            features.append(toilet.getGeoJSON())
    return features

def getOutputFilename(filename):
    # 出力ファイル名は拡張子.gpxを.geojsonにしたもの
    fname=filename.replace('.gpx','.geojson')
    if os.path.isfile(fname):
        # 既に同名のファイルが存在する場合は'_'を追加
        newname=fname.replace('.geojson','_.gpx')
        fname = getOutputFilename(newname)
    return fname

if __name__=='__main__':
    args = sys.argv
    if 2 != len(args):
        print('Usage: python %s gpx_filename' % args[0])
        print('transport gpx file to geojson for umap')
        print('output file name : (gpx_filename).geojson')
        quit()
    
    if not os.path.isfile(args[1]):
        print('Error: gpx file %s not found' % argx[1])
        quit()
    
    # gpxファイルの読み込み
    with open(args[1], 'r', encoding='utf-8') as infile:
        gpx = gpxpy.parse(infile)
    
    # 読み込んだgpxファイルをgeojsonオブジェクトに変換
    features = getFeatures(gpx)
    feature_collection=geojson.FeatureCollection(features)

    # geojsonオブジェクトをファイルに出力
    output_filename = getOutputFilename(args[1])
    with open(output_filename, 'w') as outfile:
        geojson.dump(feature_collection, outfile, indent=2)
